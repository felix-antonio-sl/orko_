# F4 – Capability Mapping

## §0 FUNDAMENTO

```yaml
fase_id: F4
nombre_canonico: "Capability Mapping"
vocabulos_referencia:
  wslc_phase: "VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F4"
  axiomas:
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A1_Organizacion"
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A3_Flujo"
  primitivos:
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P1_Capacidad"
  invariantes:
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I4_Clasificacion_Contextual"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I5_HAIC"
  dominios:
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D1_Arquitectura"
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D2_Percepcion"
relacion_kernel:
  depende_de:
    - "F1"
    - "F3"
  prepara_a:
    - "F5"
    - "F7"
    - "F9"
trayectorias_soportadas:
  - "Minimal"
  - "Avanzada"
  - "Survival"
referencias_formales:
  - "SPEC_ARQUITECTURA_DEFINITIVA.§1.3.Expansion_Layer_1_Development.F4_Capability_Mapping"
  - "PLAN_ETAPA_2_EXPANSION.SPRINT_3.FASE_1"
```

## §1 INTERFAZ

```yaml
inputs:
  - id: "F1.context_profile_36_params"
    fuente: "F1"
  - id: "F3.trajectory_selected"
    fuente: "F3"
  - id: "F2.vision_statement"
    fuente: "F2"
outputs:
  - id: "p1_inventory"
    archivo: "capacity_inventory.yaml"
    descripcion: "Inventario basado en P1_Capacidad (C1_Capacidad)"
  - id: "skills_matrix"
    archivo: "skills_matrix.xlsx"
    descripcion: "Matriz opcional de habilidades ligada a entries de p1_inventory"
  - id: "capacity_gaps"
    archivo: "capacity_gaps.yaml"
    descripcion: "Lista de gaps de P1_Capacidad alineados a trajectory_selected"
dependencies:
  reads_from:
    - "F1"
    - "F2"
    - "F3"
  writes_to:
    - "F5"
    - "F7"
    - "F9"
    - "F10"
```

