# Prospective environment repair — original attempt retained

The original protocol/source packet was published in commit355bc51 before the first run. Its unchanged `run-screen.py` first attempt stopped at process startup with `Exception occurred in preexec_fn`. `results/summary.json` records HOLD_CONTROL_OR_RESOURCE and zero workloads. No geometry control, native kernel call, path generation, or performance observation ran. A separate resource-limit diagnostic confirmed macOS15.0/Python rejects setting RLIMIT_AS to2GiB with `ValueError: current limit exceeds maximum limit`; resource-support-diagnostic.json preserves the exact result.

The original protocol, runner, source freeze and failure files remain unchanged. This amendment applies only to a prospective second attempt with `run-screen-portable.py` and `results-resource-repair/`.

## Resource enforcement replacement

Remove the rejected RLIMIT_AS pre-execution call. Start each study child in an owned new process group. While it runs, sample `/bin/ps -axo pid=,pgid=,rss=` and sum RSS for that owned group, including its descendants. Only aggregate figures for the study group are recorded. Target polling interval is50ms plus the time needed to obtain a process snapshot. Between samples use a timed child wait, so an already completed child returns immediately rather than adding a fixed50ms sleep. Terminate the owned group with SIGKILL if its observed aggregate RSS exceeds2GiB, its registered wall deadline expires, or the memory monitor fails. Retain output, exit status, wall time, sampled maximum and sample count. A short-lived process can finish between samples; cumulative endpoint ru_maxrss remains recorded and checked against the same2GiB threshold.

This is sampled RSS monitoring plus an endpoint rejection rule. It is explicitly **not an instantaneous hard virtual-memory bound**, and an unsampled transient group sum could exceed the threshold. Polling/process launch overhead is charged to the same registered phase budgets. Native kernel/replay CPU timing remains inside the unchanged native driver. No claimed whole-job savings will use polling overhead.

The two native binaries, input geometries/settings, native source, trace instrumentation, successful output/tag equality, topology/visibility controls, geometry limits, native clocks, prospective selection and all headroom thresholds are unchanged. The old negative result is an environment/control failure, not evidence for or against CAM usefulness.

The repaired runner reads `resource-repair-freeze.json`, which pins the entire original41-file freeze plus this amendment, the new runner and resource diagnostic. Its first evaluation still requires parent publication of this amendment and freeze. Exact next command, only after publication:

`python3 work/round7-c/run-screen-portable.py --out results-resource-repair`
