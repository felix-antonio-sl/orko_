# F8 – Limits Definition

## §0 FUNDAMENTO

```yaml
fase_id: F8
nombre_canonico: "Limits Definition"
vocabulos_referencia:
  wslc_phase: "VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F8"
  axiomas:
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A4_Limite"
  primitivos:
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P4_Limite"
  invariantes:
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I4_Clasificacion_Contextual"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I8_Adaptacion_Contextual"
  dominios:
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D3_Decision"
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D2_Percepcion"
relacion_kernel:
  depende_de:
    - "F1"
    - "F3"
  prepara_a:
    - "F6"
    - "F9"
    - "F10"
    - "F11"
trayectorias_soportadas:
  - "Minimal"
  - "Avanzada"
  - "Survival"
referencias_formales:
  - "SPEC_ARQUITECTURA_DEFINITIVA.§1.3.Expansion_Layer_1_Development.F8_Limits_Definition"
  - "PLAN_ETAPA_2_EXPANSION.SPRINT_3.FASE_3"
```

## §1 INTERFAZ

```yaml
inputs:
  - id: "F1.context_profile_36_params.constraints"
    fuente: "F1"
  - id: "F3.trajectory_selected"
    fuente: "F3"
  - id: "F3.budget_allocation"
    fuente: "F3"
  - id: "schemas.compliance_framework_instances"
    fuente: "compliance_framework_instances.yaml"
outputs:
  - id: "limit_catalog"
    archivo: "limit_catalog.yaml"
    descripcion: "Catálogo clasificado de límites (P4_Limite) que aplica a fases WSLC"
  - id: "compliance_framework_refs"
    archivo: "compliance_framework_instances.yaml"
    descripcion: "Lista de instancias de compliance asociadas a cada límite"
  - id: "limit_phase_matrix"
    archivo: "limit_phase_matrix.md"
    descripcion: "Matriz límite → fases/playbooks afectados"
dependencies:
  reads_from:
    - "F1"
    - "F3"
    - "schemas.compliance_framework_instances"
  writes_to:
    - "F6"
    - "F9"
    - "F10"
    - "F11"
```

