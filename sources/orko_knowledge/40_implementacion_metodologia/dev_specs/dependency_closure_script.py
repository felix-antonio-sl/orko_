#!/usr/bin/env python3
"""Dependency closure checker for DEPENDENCY_GRAPH.yaml vs VOCABULARIO_CONTROLADO.yaml.

Checks:
- All referenced phases, playbooks, trayectorias and metrics exist in VOCAB.
- The phase dependency graph (writes_to edges) is a DAG (no cycles).
- Kernel phases (from kernel.phases) are not orphaned (have at least one consumer).

Usage:
  python dependency_closure_script.py [--vocab-path PATH] [--deps-path PATH] [--check-refs] [--check-dag] [--check-orphans]

By default, all checks run against the canonical paths for this repo.
"""

import argparse
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError as exc:  # pragma: no cover
    sys.stderr.write("[ERROR] PyYAML is required: pip install pyyaml\n")
    raise


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_VOCAB_PATH = ROOT / "40_implementacion_metodologia" / "dev_specs" / "VOCABULARIO_CONTROLADO.yaml"
DEFAULT_DEPS_PATH = ROOT / "40_implementacion_metodologia" / "dev_specs" / "DEPENDENCY_GRAPH.yaml"


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_vocab_index(vocab: dict) -> dict:
    layer1 = vocab.get("layer_1", {})
    layer3 = vocab.get("layer_3", {})

    phases = set(layer3.get("wslc_phases", {}).keys())
    playbooks = set(layer3.get("playbooks", {}).keys())
    trayectorias = set(layer3.get("trayectorias", {}).keys())

    metricas_block = layer1.get("metricas", {})
    metrics = set(metricas_block.keys())
    for mid, data in metricas_block.items():
        mid2 = str(data.get("id"))
        if mid2:
            metrics.add(mid2)

    return {
        "phases": phases,
        "playbooks": playbooks,
        "trayectorias": trayectorias,
        "metrics": metrics,
    }


def check_references(deps: dict, vocab_index: dict) -> list:
    errors: list[str] = []

    phases_vocab = vocab_index["phases"]
    playbooks_vocab = vocab_index["playbooks"]
    trayectorias_vocab = vocab_index["trayectorias"]
    metrics_vocab = vocab_index["metrics"]

    # Kernel phases
    kernel_phases = set(deps.get("kernel", {}).get("phases", []))
    for p in kernel_phases:
        if p not in phases_vocab:
            errors.append(f"[REF] kernel.phase '{p}' not defined in VOCAB.layer_3.wslc_phases")

    fases = deps.get("fases", {})

    # Phase nodes
    for phase_key, node in fases.items():
        pid = node.get("id")
        if pid != phase_key:
            errors.append(f"[REF] fases.{phase_key}.id='{pid}' mismatch")
        if phase_key not in phases_vocab:
            errors.append(f"[REF] phase node '{phase_key}' not present in VOCAB.layer_3.wslc_phases")

        # Layer 1 metrics
        for mid in node.get("layer_1", {}).get("metricas", []) or []:
            if mid not in metrics_vocab:
                errors.append(f"[REF] fases.{phase_key}.layer_1.metricas uses unknown metric '{mid}'")

        deps_block = node.get("dependencies", {})

        # reads_from.phase
        for rf in deps_block.get("reads_from", []) or []:
            p2 = rf.get("phase")
            if p2 and p2 not in phases_vocab:
                errors.append(f"[REF] fases.{phase_key}.dependencies.reads_from.phase '{p2}' not in VOCAB phases")

        # writes_to
        for p2 in deps_block.get("writes_to", []) or []:
            if p2 not in phases_vocab:
                errors.append(f"[REF] fases.{phase_key}.dependencies.writes_to '{p2}' not in VOCAB phases")

        # coordinates_with
        for p2 in deps_block.get("coordinates_with", []) or []:
            if p2 not in phases_vocab:
                errors.append(f"[REF] fases.{phase_key}.dependencies.coordinates_with '{p2}' not in VOCAB phases")

        # feedback_loops.phase
        for fb in deps_block.get("feedback_loops", []) or []:
            p2 = fb.get("phase")
            if p2 and p2 not in phases_vocab:
                errors.append(f"[REF] fases.{phase_key}.dependencies.feedback_loops.phase '{p2}' not in VOCAB phases")

    # Playbooks
    for pb_key, pb in deps.get("playbooks", {}).items():
        pid = pb.get("id")
        if pid != pb_key:
            errors.append(f"[REF] playbooks.{pb_key}.id='{pid}' mismatch")
        if pb_key not in playbooks_vocab:
            errors.append(f"[REF] playbooks node '{pb_key}' not in VOCAB.layer_3.playbooks")

        for trig in pb.get("triggered_by", []) or []:
            metric = trig.get("metric")
            if metric and metric not in metrics_vocab:
                errors.append(f"[REF] playbooks.{pb_key}.triggered_by.metric '{metric}' not in VOCAB metrics")
            phase = trig.get("source_phase")
            if phase and phase not in phases_vocab:
                errors.append(f"[REF] playbooks.{pb_key}.triggered_by.source_phase '{phase}' not in VOCAB phases")

        for phase in pb.get("acts_on_phases", []) or []:
            if phase not in phases_vocab:
                errors.append(f"[REF] playbooks.{pb_key}.acts_on_phases '{phase}' not in VOCAB phases")

    # Trayectorias
    for traj_key, traj in deps.get("trayectorias", {}).items():
        if traj_key not in trayectorias_vocab:
            errors.append(f"[REF] trayectoria node '{traj_key}' not in VOCAB.layer_3.trayectorias")

        for phase in traj.get("fases_core", []) or []:
            if phase not in phases_vocab:
                errors.append(f"[REF] trayectorias.{traj_key}.fases_core '{phase}' not in VOCAB phases")

        for phase in traj.get("fases_expansion", []) or []:
            if phase not in phases_vocab:
                errors.append(f"[REF] trayectorias.{traj_key}.fases_expansion '{phase}' not in VOCAB phases")

        for pb in traj.get("playbooks_clave", []) or []:
            if pb not in playbooks_vocab:
                errors.append(f"[REF] trayectorias.{traj_key}.playbooks_clave '{pb}' not in VOCAB playbooks")

    return errors


def build_phase_graph(deps: dict) -> dict:
    fases = deps.get("fases", {})
    graph: dict[str, set[str]] = {}

    for phase_key, node in fases.items():
        graph.setdefault(phase_key, set())
        deps_block = node.get("dependencies", {})
        for p2 in deps_block.get("writes_to", []) or []:
            graph.setdefault(phase_key, set()).add(p2)
            graph.setdefault(p2, set())

    return graph


def check_dag(graph: dict) -> list:
    errors: list[str] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def dfs(node: str, stack: list[str]):
        if node in visiting:
            cycle = " -> ".join(stack + [node])
            errors.append(f"[DAG] cycle detected: {cycle}")
            return
        if node in visited:
            return
        visiting.add(node)
        stack.append(node)
        for neigh in graph.get(node, ()):
            dfs(neigh, stack)
        stack.pop()
        visiting.remove(node)
        visited.add(node)

    for n in list(graph.keys()):
        if n not in visited:
            dfs(n, [])

    return errors


def check_orphans(deps: dict) -> list:
    errors: list[str] = []

    fases = deps.get("fases", {})
    kernel_phases = set(deps.get("kernel", {}).get("phases", []))

    # Build reverse index of phase consumers
    consumers: dict[str, set[str]] = {p: set() for p in fases.keys()}

    for phase_key, node in fases.items():
        deps_block = node.get("dependencies", {})
        for rf in deps_block.get("reads_from", []) or []:
            p2 = rf.get("phase")
            if p2:
                consumers.setdefault(p2, set()).add(phase_key)
        for p2 in deps_block.get("writes_to", []) or []:
            consumers.setdefault(p2, set()).add(phase_key)

    # From playbooks
    for pb_key, pb in deps.get("playbooks", {}).items():
        for phase in pb.get("acts_on_phases", []) or []:
            consumers.setdefault(phase, set()).add(f"PB:{pb_key}")

    # From trayectorias
    for traj_key, traj in deps.get("trayectorias", {}).items():
        for phase in (traj.get("fases_core", []) or []) + (traj.get("fases_expansion", []) or []):
            consumers.setdefault(phase, set()).add(f"TRJ:{traj_key}")

    for kp in sorted(kernel_phases):
        if not consumers.get(kp):
            errors.append(f"[ORPHAN] kernel phase '{kp}' has no consumers in fases/playbooks/trayectorias")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate DEPENDENCY_GRAPH.yaml against VOCABULARIO_CONTROLADO.yaml")
    parser.add_argument("--vocab-path", type=Path, default=DEFAULT_VOCAB_PATH)
    parser.add_argument("--deps-path", type=Path, default=DEFAULT_DEPS_PATH)
    parser.add_argument("--check-refs", action="store_true")
    parser.add_argument("--check-dag", action="store_true")
    parser.add_argument("--check-orphans", action="store_true")

    args = parser.parse_args(argv)

    if not (args.check_refs or args.check_dag or args.check_orphans):
        args.check_refs = args.check_dag = args.check_orphans = True

    vocab = load_yaml(args.vocab_path)
    deps = load_yaml(args.deps_path)

    vocab_index = build_vocab_index(vocab)
    all_errors: list[str] = []

    if args.check_refs:
        all_errors.extend(check_references(deps, vocab_index))

    if args.check_dag:
        graph = build_phase_graph(deps)
        all_errors.extend(check_dag(graph))

    if args.check_orphans:
        all_errors.extend(check_orphans(deps))

    if all_errors:
        sys.stderr.write("\n".join(all_errors) + "\n")
        sys.stderr.write(f"[SUMMARY] {len(all_errors)} error(s) detected.\n")
        return 1

    sys.stdout.write("[SUMMARY] All dependency checks passed.\n")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
