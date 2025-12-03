
# F16_learning_loops

## §0. FUNDAMENTO

**Layer 0:** `A1`, `A3`, `A5`, `P5`, `I3`, `I6`, `I8`  
**Layer 1:** `D1`, `D2`, `D4`, `E6`, `E7`  
**Layer 2:** `TF1`, `TF2`

F16 se encarga de cerrar loops de aprendizaje entre:

- Resultados medidos por `F13` (`H_org`, `eta_org`, `ROI_Habilitacion`).  
- Decisiones de trayectoria (`F3`, `03_decision_matrix.md`).  
- Ejecución de playbooks de transformación (`P05`–`P08`) y recovery (`P01`–`P04`).  
- Governance y roles definidos en `01_team_structure_raci.md`.

Su propósito es reforzar:

- `I3` – Trazabilidad: cada cambio relevante en `H_org`/`eta_org` debe ser rastreable a playbooks, decisiones y contextos.  
- `I6` – Trajectory-awareness: los loops de aprendizaje deben informar explícitamente decisiones de cambio/mantenimiento de trayectoria (`Survival`, `Minimal`, `Avanzada`).  
- `I8` – Consistencia temporal: los ciclos de aprendizaje deben considerar ventanas de tiempo coherentes con health gates G1–G4.

---

## §1. INTERFAZ

### Inputs

```yaml
inputs:
  - id: "metrics_snapshot"
    source: "F13"
    description: "Snapshot periódico de H_org, eta_org, ROI_Habilitacion por dominio/trayectoria."
  - id: "health_gates_state"
    source: "G1–G4 (02_health_gates.md)"
    description: "Estado actual de G1–G4 (activados/no activados, notas de umbral)."
  - id: "decision_matrix_context"
    source: "09_trayectorias/03_decision_matrix.md"
    description: "Contexto de trayectoria (Survival/Minimal/Avanzada) y factores de decisión (runway, complejidad, budget)."
  - id: "playbooks_outputs_P05_P08"
    source: "P05_bounded_autonomy_m6, P06_pilot_transformation, P07_scale_transformation, P08_optimization_sustain"
    description: "Reports y planes resultantes de P05–P08 (autonomy/scale/optimization)."
  - id: "governance_decisions"
    source: "12_roles_governance/01_team_structure_raci.md"
    description: "Decisiones clave tomadas en respuesta a G1–G4 y a outputs de playbooks."
```

### Outputs

```yaml
outputs:
  - id: "learning_loops_log"
    description: "Registro estructurado de hipótesis, experimentos (P05–P08), resultados y decisiones de trayectoria."
    consumers: ["F3", "F13", "F17", "E4_governance"]
  - id: "playbook_improvement_backlog"
    description: "Backlog de mejoras para playbooks P01–P08 basadas en evidencias recogidas en F16."
    consumers: ["E3_playbooks", "F17"]
  - id: "trajectory_adjustment_recommendations"
    description: "Recomendaciones para mantener/cambiar trayectoria (Survival/Minimal/Avanzada) apoyadas en G1–G4 y decision_matrix."
    consumers: ["F3", "F17", "E4_governance"]
```

### Notas sobre integración P05–P08 ↔ F16 ↔ G1–G4

- **P05 (Bounded Autonomy M6):** sus outputs sobre diseño de autonomía se registran en `learning_loops_log` como hipótesis de mejora de `eta_org`/`ROI_Habilitacion`. F16 observa si los cambios se reflejan en métricas y, si no, genera ítems en `playbook_improvement_backlog`.
- **P06 (Pilot Transformation):** sus experimentos piloto se usan como casos de prueba controlados; F16 compara métricas pre/post piloto y, si el impacto es positivo, alimenta `trajectory_adjustment_recommendations` y prepara insumos para P07.
- **P07 (Scale Transformation):** F16 monitoriza el efecto de la escala sobre `H_org`/`eta_org`/`ROI_Habilitacion`; cualquier degradación posterior genera loops adicionales (posible reactivación de P01/P02/P11 o reajuste de trayectoria en función de G1–G4).
- **P08 (Optimization Sustain):** los planes de optimización y sus resultados se consideran parte del ciclo continuo; F16 usa sus outputs para detectar drift y decidir si se requieren nuevos ciclos o cambios de trayectoria según `03_decision_matrix.md`.

