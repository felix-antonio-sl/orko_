# F10 – Quick Wins

## §0 FUNDAMENTO

```yaml
fase_id: F10
nombre_canonico: "Quick Wins"
vocabulos_referencia:
  wslc_phase: "VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F10"
  axiomas:
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A1_Organizacion"
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A3_Flujo"
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A5_Cambio"
  primitivos:
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P1_Capacidad"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P2_Flujo"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P3_Informacion"
  invariantes:
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I1_Minimalidad"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I7_Emergencia_Complejidad"
  dominios:
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D4_Operacion"
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D3_Decision"
relacion_kernel:
  depende_de:
    - "F3"
    - "F4"
    - "F8"
  prepara_a:
    - "F13"
    - "F12"
trayectorias_soportadas:
  - "Minimal"
  - "Avanzada"
  - "Survival"
referencias_formales:
  - "SPEC_ARQUITECTURA_DEFINITIVA.§1.3.Expansion_Layer_2_Implementation.F10_Quick_Wins"
  - "PLAN_ETAPA_2_EXPANSION.SPRINT_4.FASE_6"
```

## §1 INTERFAZ

```yaml
inputs:
  - id: "F4.capacity_gaps"
    fuente: "F4"
  - id: "F4.p1_inventory"
    fuente: "F4"
  - id: "F5.vsm_maps"
    fuente: "F5"
  - id: "F5.handoff_ratio"
    fuente: "F5"
  - id: "F8.limit_catalog"
    fuente: "F8"
  - id: "F9.e6_target"
    fuente: "F9"
  - id: "F13.h_org_dashboard_live"
    fuente: "F13"
outputs:
  - id: "quick_wins_backlog"
    archivo: "quick_wins_backlog.yaml"
    descripcion: "Lista priorizada de quick wins con esfuerzo e impacto estimado"
  - id: "quick_wins_execution_log"
    archivo: "quick_wins_execution_log.md"
    descripcion: "Registro de ejecucion de quick wins"
  - id: "quick_wins_impact"
    archivo: "quick_wins_impact.yaml"
    descripcion: "Impacto observado en H_org y artefactos relacionados tras quick wins"
  - id: "h_org_improvement_plan"
    archivo: "h_org_improvement_plan.md"
    descripcion: "Plan de mejora de H_org basado en quick wins priorizados"
dependencies:
  reads_from:
    - "F3"
    - "F4"
    - "F5"
    - "F8"
    - "F9"
    - "F13"
  writes_to:
    - "F13"
    - "F12"
```

