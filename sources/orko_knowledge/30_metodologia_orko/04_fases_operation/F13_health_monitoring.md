# F13 – Health Monitoring

## §0 FUNDAMENTO

```yaml
fase_id: F13
nombre_canonico: "Health Monitoring"
vocabulos_referencia:
  wslc_phase: "VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F13"
  axiomas:
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A1_Organizacion"
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A3_Flujo"
  primitivos:
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P1_Capacidad"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P2_Flujo"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P3_Informacion"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P4_Limite"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P5_Proposito"
  invariantes:
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I5_HAIC"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I7_Coherencia"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I8_Adaptacion_Contextual"
  dominios:
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D4_Operacion"
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D2_Percepcion"
  tejidos:
    - "VOCABULARIO_CONTROLADO.layer_2.tejidos.TF1_Capacity"
    - "VOCABULARIO_CONTROLADO.layer_2.tejidos.TF2_Flow"
    - "VOCABULARIO_CONTROLADO.layer_2.tejidos.TF3_Information"
  metricas_canonicas:
    - "VOCABULARIO_CONTROLADO.layer_1.metricas.H_org"
    - "VOCABULARIO_CONTROLADO.layer_1.metricas.eta_org"
    - "VOCABULARIO_CONTROLADO.layer_1.metricas.ROI_Habilitacion"
relacion_kernel:
  depende_de:
    - "F1"
    - "F4"
    - "F5"
    - "F6"
    - "F9"
    - "F10"
    - "F11"
    - "F12"
  prepara_a:
    - "F14"
    - "F17"
    - "F18"
trayectorias_soportadas:
  - "Minimal"
  - "Avanzada"
  - "Survival"
estado_fundamento: "STABLE"
justificacion: |
  F13 es fase continua de monitoreo que materializa A1_Organizacion y A3_Flujo mediante tracking 
  de métricas canónicas (H_org, eta_org, ROI_Habilitacion) derivadas de TF1/TF2/TF3. Implementa 
  health gates G1-G4 que triggerea playbooks y decisiones adaptativas (F14/F17). Garantiza I5_HAIC 
  con accountability humana explícita en dashboards. §1 INTERFAZ completo con observability tools.
backlog_v1_1:
  - "Automatizar drift detection E6_current vs E6_target"
  - "Integrar alerting con playbook triggers automáticos"
  - "Calibrar thresholds G1-G4 por industria/contexto"
referencias_formales:
  - "SPEC_ARQUITECTURA_DEFINITIVA.§1.4.Operation.F13_Health_Monitoring"
  - "30_metodologia_orko/13_metricas_validacion/02_health_gates.md"
  - "30_metodologia_orko/04_fases_operation/README.md"
```

## §1 INTERFAZ

```yaml
inputs:
  - id: "F1.h_org_baseline"
    fuente: "F1"
    descripcion: "Línea base de salud organizacional para comparación"
  - id: "F9.e6_target"
    fuente: "F9"
    descripcion: "Estado arquitectónico objetivo definido en Target State Design"
  - id: "F10.quick_wins_deployed"
    fuente: "F10"
    descripcion: "Lista de quick wins ejecutados y su impacto esperado"
  - id: "F11.fabric_deployment_status"
    fuente: "F11"
    descripcion: "Estado de despliegue de tejidos TF1/TF2/TF3"
  - id: "F12.state_transition_progress"
    fuente: "F12"
    descripcion: "Progreso de transición E6_current → E6_target"
  - id: "tf1_capacity_metrics"
    fuente: "TF1_Capacity"
    descripcion: "Señales de capacidad desde tejido TF1"
  - id: "tf2_flow_metrics"
    fuente: "TF2_Flow"
    descripcion: "Señales de flujo desde tejido TF2"
  - id: "tf3_information_metrics"
    fuente: "TF3_Information"
    descripcion: "Señales de información desde tejido TF3"
  - id: "health_score_calculator"
    fuente: "40_implementacion_metodologia/calculadoras/health_score_calculator.xlsx"
    descripcion: "Calculadora de H_org y componentes A/P/D scores"
outputs:
  - id: "h_org_current"
    descripcion: "Valor actual de salud organizacional (H_org) calculado"
    consumers:
      - "F14"
      - "F17"
      - "F18"
  - id: "health_gate_status"
    descripcion: "Estado actual de health gates (G1 | G2 | G3 | G4) según 02_health_gates.md"
    consumers:
      - "F14"
      - "F17"
  - id: "drift_signals"
    descripcion: "Señales de desviación entre E6_current y E6_target"
    consumers:
      - "F14"
      - "F17"
  - id: "dashboards_h_org"
    archivo: "health_dashboards.md"
    descripcion: "Dashboards de seguimiento de H_org, eta_org y ROI_Habilitacion"
    consumers:
      - "F15"
      - "F17"
  - id: "playbook_triggers"
    descripcion: "Lista de playbooks (P01–P15) disparados por condiciones de health gates"
    consumers:
      - "F14"
dependencies:
  reads_from:
    - "F1"
    - "F9"
    - "F10"
    - "F11"
    - "F12"
    - "TF1_Capacity"
    - "TF2_Flow"
    - "TF3_Information"
  writes_to:
    - "F14"
    - "F15"
    - "F17"
    - "F18"
```

