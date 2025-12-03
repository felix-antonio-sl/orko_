# F17 – Adaptation

## §0 FUNDAMENTO

```yaml
fase_id: F17
nombre_canonico: "Adaptation"
vocabulos_referencia:
  wslc_phase: "VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F17"
  axiomas:
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A5_Cambio"
  primitivos:
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P4_Limite"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P5_Proposito"
  invariantes:
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I8_Adaptacion_Contextual"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I3_Trazabilidad"
  dominios:
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D3_Decision"
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D2_Percepcion"
  metricas_canonicas:
    - "VOCABULARIO_CONTROLADO.layer_1.metricas_canonicas.H_org"
relacion_kernel:
  depende_de:
    - "F16"
    - "F13"
  prepara_a:
    - "F18"
trayectorias_soportadas:
  - "Minimal"
  - "Avanzada"
estado_fundamento: "STABLE"
notas_fundamento: |
  F17 formaliza la adaptación (policy/ADR) ante drift o shock contextual. Entregables: adaptation_policy.yaml, ADRs, decision_log.
  Integración con learning_loops (F16) y health gates (F13). Es responsable la junta de gobernanza.
referencias_formales:
  - "30_metodologia_orko/16_evolucion_metodologia/01_feedback_loops_metodologia.md"
```

---

## §1 INTERFAZ

```yaml
inputs:
  - id: "learnings"
    source: "F16.learnings"
    required: true
    description: "Learnings capturados de operación y post-mortems"
  
  - id: "health_trends"
    source: "F13.health_trends"
    required: true
    description: "Tendencias H_org, eta_org, ROI_Habilitacion"
  
  - id: "gate_history"
    source: "F13.gate_history"
    required: true
    description: "Historial de health gates G1-G4 activados"

outputs:
  - id: "trajectory_adjustment"
    artifact: "trajectory_adjustment.md"
    consumers: ["F3", "F18"]
    description: "Ajuste de trayectoria basado en learnings"
    location: "artefactos/f17/"
  
  - id: "adaptation_plan"
    artifact: "adaptation_plan.yaml"
    consumers: ["F7", "F9", "F18"]
    description: "Plan de adaptación con decisiones ADR"
    location: "artefactos/f17/"
  
  - id: "okr_refinement"
    artifact: "okr_refinement.yaml"
    consumers: ["F7"]
    description: "Refinamiento de OKRs basado en feedback operación"
    location: "artefactos/f17/"

dependencies:
  reads_from: ["F13", "F16"]
  writes_to: ["F3", "F7", "F18"]
  triggers: ["P03", "P05", "P06", "P13", "P15"]

acceptance_criteria:
  - criterion: "Adaptation_plan incluye mínimo 1 ADR formal"
    verification: "count(ADRs) >= 1"
    responsible: "Role_Captain"
  
  - criterion: "Trajectory_adjustment justificado con datos F13"
    verification: "trajectory_change_rationale incluye H_org_trends"
    responsible: "Role_TrajectoryOwner"
  
  - criterion: "OKR_refinement aprobado por Sponsor_L1_Human"
    verification: "sponsor_approval == true"
    responsible: "Sponsor_L1_Human"
    bloqueante: true

templates:
  - T12_adr_template.md
```

---

## §2 DESCRIPCIÓN EJECUTIVA

F17 formaliza decisiones de adaptación organizacional basadas en learnings (F16) y health trends (F13), incluyendo ajustes de trayectoria, OKRs y políticas.

**Actividades principales**:
1. Revisar learnings de F16 y health_trends de F13
2. Identificar necesidad de adaptación (cambio trajectory, OKRs, políticas)
3. Documentar decisiones con ADRs
4. Crear adaptation_plan con acciones concretas
5. Triggerar playbooks transformacionales

**Duración estimada**: 1-2 días

**Owner**: Role_Captain + Role_SteeringCommittee
