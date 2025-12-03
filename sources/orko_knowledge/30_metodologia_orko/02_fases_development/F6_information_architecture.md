# F6 – Information Architecture

## §0 FUNDAMENTO

```yaml
fase_id: F6
nombre_canonico: "Information Architecture"
vocabulos_referencia:
  wslc_phase: "VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F6"
  axiomas:
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A3_Flujo"
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A5_Cambio"
  primitivos:
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P3_Informacion"
  invariantes:
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I3_Trazabilidad"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I8_Adaptacion_Contextual"
  dominios:
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D1_Arquitectura"
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D2_Percepcion"
  tejidos:
    - "VOCABULARIO_CONTROLADO.layer_2.tejidos.TF3_Information"
relacion_kernel:
  depende_de:
    - "F1"
    - "F3"
  prepara_a:
    - "F9"
    - "F11"
trayectorias_soportadas:
  - "Minimal"
  - "Avanzada"
  - "Survival"
referencias_formales:
  - "SPEC_ARQUITECTURA_DEFINITIVA.§1.3.Expansion_Layer_1_Development.F6_Information_Architecture"
  - "PLAN_ETAPA_2_EXPANSION.SPRINT_3.FASE_5"
```

## §1 INTERFAZ

```yaml
inputs:
  - id: "F1.context_profile_36_params"
    fuente: "F1"
  - id: "F3.trajectory_selected"
    fuente: "F3"
  - id: "F7.okr_cascade"
    fuente: "F7"
  - id: "F8.p4_limit_catalog"
    fuente: "F8"
outputs:
  - id: "data_catalog"
    archivo: "critical_datasets.yaml"
    descripcion: "Catalogo de datasets clave (p3_catalog) consumido por F9 y F11"
  - id: "architecture_blueprint"
    archivo: "data_domain_model.md"
    descripcion: "Blueprint de dominios de informacion y relaciones clave"
  - id: "information_governance"
    archivo: "information_governance.md"
    descripcion: "Principios y roles de governance de informacion"
dependencies:
  reads_from:
    - "F1"
    - "F3"
    - "F7"
    - "F8"
  writes_to:
    - "F9"
    - "F11"
```

