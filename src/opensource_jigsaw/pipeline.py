import hashlib
import random
from datetime import UTC, datetime, timedelta
from pathlib import Path

from . import prompts
from .astra import Astra
from .gate import decide, idea_errors
from .github import GitHub, collect
from .models import Critique, Ideas, Judgment, Plan, Repository, Research, Result, Selection
from .storage import read, save


def catalog_from(path: Path) -> dict[str, Repository]:
    return {r.full_name: r for item in read(path) if (r := Repository.model_validate(item))}


def summarize(repo: Repository) -> dict:
    return repo.model_dump(mode="json", exclude={"queries", "retrieved_at", "forks"})


def discover(out: Path, astra: Astra, max_repos: int, per_query: int) -> dict[str, Repository]:
    save(out / "results.json", [])
    report(out, {}, [], complete=False)
    if (out / "plan.json").exists():
        plan = Plan.model_validate(read(out / "plan.json"))
    else:
        plan = astra.ask(
            prompts.PLAN,
            {
                "active_since": (datetime.now(UTC) - timedelta(days=730)).date().isoformat(),
            },
            Plan,
        )
        save(out / "plan.json", plan.model_dump())
    catalog = collect(GitHub(out / "github-cache"), plan, out, max_repos, per_query)
    report(out, catalog, [], complete=False)
    return catalog


def analyze(
    out: Path, astra: Astra, catalog: dict[str, Repository], candidates: int
) -> list[Result]:
    if len(catalog) < 2:
        raise ValueError("Need at least two repositories before analysis")
    if not 1 <= candidates <= 100:
        raise ValueError("candidates must be 1..100")
    save(out / "results.json", [])
    report(out, catalog, [], complete=False)
    repos = sorted(catalog.values(), key=lambda r: r.full_name)
    random.Random(42).shuffle(repos)
    selected = set()
    for start in range(0, len(repos), 80):
        batch = repos[start : start + 80]
        scout = astra.ask(prompts.SCOUT, {"repositories": [summarize(r) for r in batch]}, Selection)
        valid = {r.full_name for r in batch}
        if len(scout.repositories) > 12 or not set(scout.repositories) <= valid:
            raise ValueError("Astra scout returned too many or unknown repositories")
        selected.update(scout.repositories)
    pool = [r for r in repos if r.full_name in selected]
    save(out / "shortlist.json", [r.full_name for r in pool])
    ideas = []
    excluded = []
    signatures = set()
    # Each shortlist member appears in a mixed-field panel; later panels see prior hypotheses.
    for start in range(0, len(pool), 100):
        panel = pool[start : start + 100]
        proposed = astra.ask(
            prompts.PROPOSE.replace("LIMIT", str(min(8, candidates))),
            {
                "repositories": [summarize(r) for r in panel],
                "excluded_ideas": excluded,
            },
            Ideas,
        )
        panel_catalog = {r.full_name: r for r in panel}
        if len(proposed.ideas) > min(8, candidates):
            raise ValueError("Astra exceeded the proposal budget")
        for idea in proposed.ideas:
            signature = tuple(sorted(c.repository for c in idea.components))
            errors = idea_errors(idea, panel_catalog)
            if errors:
                raise ValueError(f"Invalid Astra proposal {idea.title}: {', '.join(errors)}")
            if signature not in signatures:
                signatures.add(signature)
                ideas.append(idea)
                excluded.append(idea.model_dump(mode="json"))
    # Candidates are hypotheses, not wins. Let a separate selection call choose research priority.
    if len(ideas) > candidates:
        ranked = astra.ask(
            "Select exactly LIMIT distinct idea titles for investigation. Favor exceptional "
            "cross-field synergy and concrete buyer pain. These are unvalidated hypotheses. "
            "Return titles in the repositories field, most promising first.".replace(
                "LIMIT", str(candidates)
            ),
            {"ideas": excluded},
            Selection,
        )
        by_title = {idea.title: idea for idea in ideas}
        if (
            len(set(ranked.repositories)) != candidates
            or not set(ranked.repositories) <= by_title.keys()
        ):
            raise ValueError("Astra returned an invalid candidate ranking")
        ideas = [by_title[title] for title in ranked.repositories]
    save(out / "proposals.json", [idea.model_dump(mode="json") for idea in ideas])
    results = []
    for number, idea in enumerate(ideas, 1):
        print(f"Investigating {number}/{len(ideas)}: {idea.title}", flush=True)
        payload = {
            "idea": idea.model_dump(mode="json"),
            "repositories": [summarize(catalog[c.repository]) for c in idea.components],
        }
        research = astra.ask(prompts.RESEARCH, payload, Research, web=True)
        payload["research"] = research.model_dump(mode="json")
        critique = astra.ask(prompts.CRITIQUE, payload, Critique, web=True)
        payload["critique"] = critique.model_dump(mode="json")
        judgment = astra.ask(prompts.JUDGE, payload, Judgment, web=True)
        result = Result(
            idea=idea,
            research=research,
            critique=critique,
            judgment=judgment,
            decision=decide(idea, research, critique, judgment, catalog),
        )
        results.append(result)
        identity = hashlib.sha256(idea.model_dump_json().encode()).hexdigest()[:16]
        save(out / "decisions" / f"{identity}.json", result.model_dump(mode="json"))
        save(out / "results.json", [r.model_dump(mode="json") for r in results])
        report(out, catalog, results, complete=False)
    report(out, catalog, results, complete=True)
    return results


def report(out: Path, catalog: dict[str, Repository], results: list[Result], *, complete: bool):
    accepted = [r for r in results if r.decision.accepted]
    fields = {f for repo in catalog.values() for f in repo.fields}
    summary = {
        "status": "complete" if complete else "partial",
        "repositories": len(catalog),
        "fields": len(fields),
        "evaluated": len(results),
        "accepted": len(accepted),
        "model": "gpt-6-astra",
        "updated_at": datetime.now(UTC).isoformat(),
    }
    save(out / "summary.json", summary)
    save(out / "accepted.json", [r.model_dump(mode="json") for r in accepted])
    lines = [
        "# Open Source Jigsaw",
        "",
        f"Status: **{summary['status']}**",
        "",
        f"{len(catalog)} repositories · {len(fields)} fields · {len(results)} evaluated "
        f"· **{len(accepted)} passed**",
        "",
        "A pass means worth a validation experiment, not proven profitability. "
        "Scores are model judgments; evidence remains open to human review.",
        "",
        "## Passed the bar",
        "",
    ]
    if not accepted:
        lines += ["No combinations cleared every gate. The bar was not lowered.", ""]
    for result in sorted(results, key=lambda r: (not r.decision.accepted, -r.decision.score)):
        if not result.decision.accepted and "## Rejected / watch" not in lines:
            lines += ["## Rejected / watch", ""]
        lines += [
            f"### {result.idea.title}",
            "",
            f"**{'PASS' if result.decision.accepted else 'NO PASS'} · "
            f"{result.decision.score}/100** · Astra: {result.judgment.verdict}",
            "",
            result.idea.thesis,
            "",
            f"Buyer: {result.idea.buyer}",
            "",
            "Components: "
            + ", ".join(
                f"[{c.repository}]({catalog[c.repository].url})" for c in result.idea.components
            ),
            "",
            result.judgment.rationale,
            "",
        ]
        if result.decision.reasons:
            lines += ["Gate failures:", ""] + [f"- {r}" for r in result.decision.reasons] + [""]
        lines += [f"Next experiment: {result.judgment.next_experiment}", "", "Sources:", ""]
        lines += [f"- [{e.title}]({e.url}): {e.finding}" for e in result.research.evidence] + [""]
    (out / "report.md").write_text("\n".join(lines) + "\n")
