# FMU reserve follow-up: HOLD

A real permissively licensed historical defect was found, but it does not establish the proposed stateful-generation advantage. No FMU was executed; no library was loaded; no compiler/build/test was run. Only source/API text and ZIP member metadata were inspected. Downloaded issue archives were read in memory and not unpacked onto disk.

## Exact historical case

[Reference-FMUs issue635](https://github.com/modelica/Reference-FMUs/issues/635) reports BouncingBall FMI2 co-simulation serialization working within one process and failing across processes. [Issue652](https://github.com/modelica/Reference-FMUs/issues/652) additionally records frozen outputs after restore. [PR653](https://github.com/modelica/Reference-FMUs/pull/653) fixes both via merge `690a33972c939cdbd58b3cf6c3e55b2c1f3c020b`; immediate parent is `8d050ef87a3a81dae665eb76d53b622d9186b7ff`.

Source diff: dynamically allocated continuous-state and event-indicator arrays become inline arrays in ModelInstance; restoration copies dimension counts, current/previous event indicators, continuous states and derivatives. The historical license is BSD-2-Clause. Sources, build definition, and exact diff are publicly available. CMake explicitly supports Apple x86_64 and FMI3 aarch64; FMI2 aarch64 is rejected. Thus native Apple-Silicon FMI2 execution is not established. Building FMI3 or using a verified x86 environment would be a separate explicit experiment, not an unnoticed platform substitution.

The issue already includes two `fmusim` invocations: save at time1.5 then restart from the serialized state in another process. Its continuation output is constant when it should evolve. The obvious fixed baseline—fresh-process checkpoint, then compare the continuation with the uninterrupted trajectory—should detect this. Merely checking equality at the restored boundary is too weak. This is a source-level inference supported by the published trace, not our reproduction result.

A fixed coverage suite spanning before/after initialization, a state event, multiple saved states, repeated restore and fresh process would cover the relevant interactions. No inspected defect requires a long, unexpected legal action chain. Therefore adding Hypothesis is not justified by this case. If future work claims only smaller reproductions, compare with generic delta debugging at equal FMI calls, including validity repair and cold-process costs. A shorter generated script alone is not labor/ROI evidence.

## Attachment licensing

FMPy304's `serialize_and_deserialize.zip` contains two Python scripts with no explicit license file. `test_serialization_model.zip` contains a Modelica source and FMU with a Linux64 binary, documentation and third-party license notices. It contains no generated C source or explicit whole-model/whole-FMU redistribution grant established by this inspection. CVODE, FMI and other library notices do not license the entire exported Dymola artifact. No binaries were executed. Metadata-only sanitized records are in `attachment-summary.json`; the original archives are not part of publication.

## Decision

**HOLD and leave this lane.** Rights-cleared source exists for a useful historical checkpoint regression, so absence of any real data is no longer the reason. The limiting fact is the competent simple baseline, plus no demonstrated economic/acceptance-report distinction. Building the old bug solely to show a failure would not resolve either. Prior screen remains unchanged; this addendum supersedes its suggestion that another FMU fixture hunt is the best next step.
