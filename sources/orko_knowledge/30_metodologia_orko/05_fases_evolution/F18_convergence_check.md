# F18 – Convergence Check

## §0 FUNDAMENTO

```yaml
fase_id: F18
nombre_canonico: "Convergence Check"
vocabulos_referencia:
  wslc_phase: "VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F18"
  axiomas:
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A1_Organizacion"
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A5_Cambio"
  primitivos:
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P1_Capacidad"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P2_Flujo"
  invariantes:
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I6_Trajectory_Awareness"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I7_Coherencia"
  dominios:
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D1_Arquitectura"
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D4_Operacion"
  metricas_canonicas:
    - "VOCABULARIO_CONTROLADO.layer_1.metricas_canonicas.H_org"
    - "VOCABULARIO_CONTROLADO.layer_1.metricas_canonicas.eta_org"
relacion_kernel:
  depende_de:
    - "F9"
    - "F13"
    - "F16"
  prepara_a:
    - "E3_governance"
trayectorias_soportadas:
  - "Minimal"
  - "Avanzada"
estado_fundamento: "STABLE"
notas_fundamento: |
  F18 revisa convergence_score, verifica cumplimiento de E6_target y produce informe de cierre/reevaluación.
  Outputs: convergence_report.md, lessons_learned.md, update_requests para playbooks.
referencias_formales:
  - "40_implementacion_metodologia/calculadoras/convergence_tracker.xlsx"
```

---

## §1 INTERFAZ

```yaml
inputs:
  - id: "e6_target"
    source: "F9.e6_target"
    schema_ref: "E6_ArchitecturalState"
    required: true
    description: "Estado arquitectónico objetivo definido"
  
  - id: "e6_current"
    source: "F12.e6_current"
    schema_ref: "E6_ArchitecturalState"
    required: true
    description: "Estado arquitectónico actual post-transiciones"
  
  - id: "h_org_trends"
    source: "F13.h_org_trends"
    required: true
    description: "Evolución H_org baseline → current"

outputs:
  - id: "convergence_report"
    artifact: "convergence_report.md"
    consumers: ["F17", "Role_SteeringCommittee"]
    description: "Reporte formal convergencia E6_current vs E6_target"
    location: "artefactos/f18/"
  
  - id: "convergence_score"
    type: "float"
    range: "[0, 1]"
    consumers: ["F17"]
    description: "Score numérico de convergencia"
  
  - id: "gap_analysis"
    artifact: "gap_analysis.yaml"
    consumers: ["F17"]
    description: "Gaps restantes current → target"
    location: "artefactos/f18/"

dependencies:
  reads_from: ["F9", "F12", "F13"]
  writes_to: ["F17"]

acceptance_criteria:
  - criterion: "Convergence_score calculado con fórmula formal"
    verification: "score = weighted_avg(arch_convergence, h_org_delta, okr_achievement)"
    responsible: "Role_Architect"
    bloqueante: true
  
  - criterion: "Convergence_report incluye recomendación: CONTINUE | ADAPT | CLOSE"
    verification: "recommendation field != null"
    responsible: "Role_Captain"
  
  - criterion: "Gap_analysis prioriza top-5 gaps restantes"
    verification: "count(gaps_prioritized) >= 5"
    responsible: "Role_Architect"

herramientas:
  - convergence_tracker.xlsx
```

---

## §2 DESCRIPCIÓN EJECUTIVA

F18 es el "checkpoint final" del ciclo WSLC que evalúa si la organización ha convergido hacia E6_target o requiere adaptación (vía F17).

**Actividades principales**:
1. Comparar E6_current (F12) vs E6_target (F9)
2. Calcular convergence_score con métricas arquitectónicas y H_org
3. Analizar gaps restantes (current → target)
4. Generar convergence_report con recomendación
5. Decidir: CONTINUE (seguir operando), ADAPT (volver a F17), CLOSE (mission accomplished)

**Fórmula convergence_score**:
```
score = weighted_avg(
  architectural_convergence × 0.40,
  h_org_improvement × 0.30,
  okr_achievement × 0.30
)

architectural_convergence = components_deployed / components_target
h_org_improvement = (h_org_current - h_org_baseline) / (h_org_target - h_org_baseline)
okr_achievement = okrs_met / okrs_total
```

**Duración estimada**: 4-8 horas (análisis + reporte)

**Owner**: Role_Architect + Role_Captain

**Nota**: F18 cierra el ciclo WSLC - solo existe en Minimal y Avanzada (Survival no tiene target formal)
