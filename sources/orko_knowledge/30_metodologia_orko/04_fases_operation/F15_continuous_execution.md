# F15 – Continuous Execution

## §0 FUNDAMENTO

```yaml
fase_id: F15
nombre_canonico: "Continuous Execution"
vocabulos_referencia:
  wslc_phase: "VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F15"
  axiomas:
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A1_Organizacion"
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A2_Capacidad"
  primitivos:
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P1_Capacidad"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P2_Flujo"
  invariantes:
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I6_Trajectory_Awareness"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I5_HAIC"
  dominios:
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D4_Operacion"
  metricas_canonicas:
    - "VOCABULARIO_CONTROLADO.layer_1.metricas_canonicas.eta_org"
relacion_kernel:
  depende_de:
    - "F13"
    - "F14"
    - "F11"
  prepara_a:
    - "F16"
trayectorias_soportadas:
  - "Minimal"
  - "Avanzada"
estado_fundamento: "STABLE"
notas_fundamento: |
  F15 regula la operación continua (runbooks, SLOs, cadence). Entregables: runbook_catalog.md, SLO_definitions.yaml, cadence_policy.md.
  Trazabilidad: cada runbook ligado a E7 y a playbooks con ADRs.
referencias_formales:
  - "SPEC_ARQUITECTURA_DEFINITIVA.§1.4.Continuous_Execution"
```

---

## §1 INTERFAZ

```yaml
inputs:
  - id: "quick_wins_backlog"
    source: "F10.quick_wins_backlog"
    required: true
    description: "Backlog de quick wins a ejecutar continuamente"

  - id: "deployment_status"
    source: "F11.deployment_status"
    required: true
    description: "Estado actual de deployments en producción"

  - id: "state_transition_log"
    source: "F12.state_transition_log"
    required: true
    description: "Log de transiciones E6_current → E6_target"

  - id: "drift_alerts"
    source: "F13.drift_alerts"
    required: false
    description: "Alertas de drift para ajustar ejecución"

outputs:
  - id: "execution_log"
    artifact: "execution_log.md"
    consumers: ["F16", "F17"]
    description: "Registro continuo de ejecución de tareas y sprints"
    location: "artefactos/f15/"

  - id: "cadence_adjustments"
    artifact: "cadence_adjustments.yaml"
    consumers: ["F13", "F16"]
    description: "Ajustes a cadencia operacional (sprints, reviews, deploys)"
    location: "artefactos/f15/"

  - id: "sprint_reports"
    artifact: "sprint_reports/"
    consumers: ["F16", "F17"]
    description: "Reportes periódicos de sprints ejecutados"
    location: "artefactos/f15/sprint_reports/"

dependencies:
  reads_from: ["F10", "F11", "F12", "F13"]
  writes_to: ["F16", "F17"]
  triggers: ["P15"]

acceptance_criteria:
  - criterion: "Execution_log actualizado semanalmente (mínimo)"
    verification: "timestamp last_update <= 7 días"
    responsible: "Role_Delivery_Lead"
    bloqueante: false

  - criterion: "Cadence_adjustments documentados cuando eta_org < threshold"
    verification: "IF eta_org < 0.70 THEN cadence_adjustment != null"
    responsible: "Role_HealthOwner"

  - criterion: "Sprint_reports incluyen métricas DORA (si Avanzada)"
    verification: "deployment_frequency, lead_time, MTTR, change_failure_rate"
    responsible: "Role_Delivery_Lead"

templates:
  - T08_weekly_checkin.md
  - T09_retrospective.md
  - T15_dora_dashboard.json
```

---

## §2 DESCRIPCIÓN EJECUTIVA

F15 gestiona la ejecución operacional continua del sistema de trabajo, ajustando cadencia, priorización y deployment según feedback de F13 (health monitoring).

**Actividades principales**:
1. Ejecutar backlog de F10/F11/F12 en cadencia regular
2. Monitorear eta_org (eficiencia organizacional)
3. Ajustar sprint length/deploy frequency según contexto
4. Documentar execution_log y sprint_reports
5. Triggerar P15 (hypergrowth cadence) si aplica

**Herramientas**:
- XanPan board (T11_xanpan_board.png)
- Weekly check-in template (T08)
- Retrospective template (T09)
- DORA dashboard (T15, si Avanzada)

**Duración estimada**: Continuo (revisión semanal/quincenal)

**Owner**: Role_Delivery_Lead + equipos ejecución

**Nota**: F15 NO existe en trajectory Survival (solo recovery)
