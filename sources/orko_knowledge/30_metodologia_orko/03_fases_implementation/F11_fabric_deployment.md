# F11 – Fabric Deployment

## §0 FUNDAMENTO

```yaml
fase_id: F11
nombre_canonico: "Fabric Deployment"
vocabulos_referencia:
  wslc_phase: "VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F11"
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
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I5_HAIC"
  dominios:
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D1_Arquitectura"
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D4_Operacion"
  tejidos:
    - "VOCABULARIO_CONTROLADO.layer_2.tejidos.TF1_Capacity"
    - "VOCABULARIO_CONTROLADO.layer_2.tejidos.TF2_Flow"
    - "VOCABULARIO_CONTROLADO.layer_2.tejidos.TF3_Information"
relacion_kernel:
  depende_de:
    - "F3"
    - "F4"
    - "F5"
    - "F6"
    - "F8"
    - "F9"
  prepara_a:
    - "F12"
    - "F13"
trayectorias_soportadas:
  - "Minimal"
  - "Avanzada"
referencias_formales:
  - "SPEC_ARQUITECTURA_DEFINITIVA.§1.3.Expansion_Layer_2_Implementation.F11_Fabric_Deployment"
  - "PLAN_ETAPA_2_EXPANSION.SPRINT_4.FASE_7"
```

## §1 INTERFAZ

```yaml
inputs:
  - id: "F3.trajectory_selected"
    fuente: "F3"
  - id: "F4.p1_inventory"
    fuente: "F4"
  - id: "F5.vsm_maps"
    fuente: "F5"
  - id: "F6.data_catalog"
    fuente: "F6"
  - id: "F8.limit_catalog"
    fuente: "F8"
  - id: "F9.e6_target"
    fuente: "F9"
outputs:
  - id: "fabric_deployment_plan"
    archivo: "02_tejidos_plans/fabric_deployment_plan.yaml"
    descripcion: "Plan de despliegue de TF1–TF3 por horizonte y modo (full/tool-agnostic/constrained)"
  - id: "tf1_capacity_plan"
    archivo: "02_tejidos_plans/tf1_capacity_plan.md"
    descripcion: "Lineamientos de despliegue para TF1_Capacity (si aplica)"
  - id: "tf2_flow_plan"
    archivo: "02_tejidos_plans/tf2_flow_plan.md"
    descripcion: "Lineamientos de despliegue para TF2_Flow (si aplica)"
  - id: "tf3_information_plan"
    archivo: "02_tejidos_plans/tf3_information_plan.md"
    descripcion: "Lineamientos de despliegue para TF3_Information (si aplica)"
  - id: "fabric_status"
    archivo: "02_tejidos_plans/fabric_status.yaml"
    descripcion: "Estado resumido de despliegue por tejido y horizonte"
dependencies:
  reads_from:
    - "F3"
    - "F4"
    - "F5"
    - "F6"
    - "F8"
    - "F9"
  writes_to:
    - "F12"
    - "F13"
```

