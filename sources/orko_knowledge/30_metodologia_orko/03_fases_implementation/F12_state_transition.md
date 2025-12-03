# F12 – State Transition

## §0 FUNDAMENTO

```yaml
fase_id: F12
nombre_canonico: "State Transition"
vocabulos_referencia:
  wslc_phase: "VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F12"
  axiomas:
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A1_Organizacion"
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A5_Cambio"
  primitivos:
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P1_Capacidad"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P2_Flujo"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P3_Informacion"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P4_Limite"
  invariantes:
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I3_Trazabilidad"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I6_Trajectory_Awareness"
  dominios:
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D1_Arquitectura"
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D4_Operacion"
  entidades:
    - "VOCABULARIO_CONTROLADO.layer_1.entidades.E6_ArchitecturalState"
relacion_kernel:
  depende_de:
    - "F9"
    - "F11"
  prepara_a:
    - "F18"
    - "F13"
trayectorias_soportadas:
  - "Minimal"
  - "Avanzada"
referencias_formales:
  - "SPEC_ARQUITECTURA_DEFINITIVA.§1.3.Expansion_Layer_2_Implementation.F12_State_Transition"
  - "PLAN_ETAPA_2_EXPANSION.SPRINT_4.FASE_8"
```

## §1 INTERFAZ

```yaml
inputs:
  - id: "F1.h_org_baseline"
    fuente: "F1"
  - id: "F13.h_org_dashboard_live"
    fuente: "F13"
  - id: "F9.e6_target"
    fuente: "F9"
  - id: "F11.fabric_deployment_plan"
    fuente: "F11"
  - id: "F10.quick_wins_impact"
    fuente: "F10"
outputs:
  - id: "state_transition_plan"
    archivo: "02_tejidos_plans/state_transition_plan.yaml"
    descripcion: "Plan de transicion E6_current → E6_target con pasos, horizontes y deltas esperados en H_org"
  - id: "e6_intermediate"
    archivo: "02_tejidos_plans/e6_intermediate.yaml"
    descripcion: "Estados intermedios definidos en el plan de transicion"
  - id: "transition_validation"
    archivo: "02_tejidos_plans/transition_validation.md"
    descripcion: "Resumen de criterios y riesgos de la transicion"
  - id: "transition_status"
    archivo: "02_tejidos_plans/transition_status.yaml"
    descripcion: "Estado de avance de la transicion, consumido por F13"
dependencies:
  reads_from:
    - "F1"
    - "F9"
    - "F10"
    - "F11"
    - "F13"
  writes_to:
    - "F18"
    - "F13"
```

