# F5 – Flow Design

## §0 FUNDAMENTO

```yaml
fase_id: F5
nombre_canonico: "Flow Design"
vocabulos_referencia:
  wslc_phase: "VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F5"
  axiomas:
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A3_Flujo"
  primitivos:
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P2_Flujo"
  invariantes:
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I2_Ortogonalidad"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I7_Emergencia_Complejidad"
  dominios:
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D1_Arquitectura"
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D4_Operacion"
relacion_kernel:
  depende_de:
    - "F1"
    - "F4"
  prepara_a:
    - "F9"
    - "F10"
    - "F11"
trayectorias_soportadas:
  - "Minimal"
  - "Avanzada"
  - "Survival"
referencias_formales:
  - "SPEC_ARQUITECTURA_DEFINITIVA.§1.3.Expansion_Layer_1_Development.F5_Flow_Design"
  - "PLAN_ETAPA_2_EXPANSION.SPRINT_3.FASE_2"
```

## §1 INTERFAZ

```yaml
inputs:
  - id: "F4.p1_inventory"
    fuente: "F4"
  - id: "F4.capacity_gaps"
    fuente: "F4"
  - id: "F1.context_profile_36_params"
    fuente: "F1"
  - id: "F3.trajectory_selected"
    fuente: "F3"
  - id: "F7.okr_cascade"
    fuente: "F7"
outputs:
  - id: "vsm_maps"
    descripcion: "Coleccion de mapas de flujo (Value Stream Mapping) para flujos criticos"
  - id: "handoff_ratio"
    descripcion: "Metricas de proporcion de handoffs por flujo, usadas por F9 y F13"
  - id: "flow_optimization"
    descripcion: "Conjunto de decisiones de optimizacion de flujo derivadas de vsm_maps"
dependencies:
  reads_from:
    - "F1"
    - "F3"
    - "F4"
    - "F7"
  writes_to:
    - "F9"
    - "F10"
    - "F11"
```

