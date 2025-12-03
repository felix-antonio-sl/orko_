# F1 – Context Assessment

## §0 FUNDAMENTO

```yaml
fase_id: F1
nombre_canonico: "Context Assessment"
vocabulos_referencia:
  wslc_phase: "VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F1"
  axiomas:
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A1_Organizacion"
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A4_Contexto"
  primitivos:
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P1_Capacidad"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P2_Flujo"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P3_Informacion"
  invariantes:
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I1_Continuidad_Operacional"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I4_Clasificacion_Contextual"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I6_Metricas_Canonicas"
  dominios:
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D2_Percepcion"
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D3_Decision"
  metricas_canonicas:
    - "VOCABULARIO_CONTROLADO.layer_1.metricas_canonicas.H_org"
  tejidos:
    - "VOCABULARIO_CONTROLADO.layer_2.tejidos.TF1_Capacity"
    - "VOCABULARIO_CONTROLADO.layer_2.tejidos.TF2_Flow"
    - "VOCABULARIO_CONTROLADO.layer_2.tejidos.TF3_Information"
relacion_kernel:
  es_kernel: true
  depende_de: []
  prepara_a:
    - "F2"
    - "F3"
    - "F4"
    - "F5"
    - "F6"
    - "F7"
trayectorias_soportadas:
  - "Survival"
  - "Minimal"
  - "Avanzada"
estado_fundamento: "STABLE"
justificacion: |
  F1 es la fase de entrada del WSLC que materializa A1_Organizacion y A4_Contexto mediante 
  captura de estado organizacional (36 parámetros). Produce H_org baseline y clasificación 
  contextual (G1-G4) que gobiernan decisiones de F3. Validado en casos startup_50p, gore_nuble, 
  y unicornio_latam. Templates T01, calculadoras y §1 INTERFAZ completos.
backlog_v1_1:
  - "Profundizar conexión axioma A1 con TF1/TF2/TF3 lifecycles"
  - "Formalizar fórmula canónica H_org en health_score_calculator.xlsx"
referencias_formales:
  - "SPEC_ARQUITECTURA_DEFINITIVA.§1.2.Kernel.F1_Context_Assessment"
  - "PLAN_ETAPA_1_KERNEL.SPRINT_1.FASE_1"
  - "validation_final_report.md.§2.3.F1_PASSED"
```

**Propósito:**  
F1 (Context Assessment) es la fase de entrada del WSLC que captura el estado organizacional actual (E6_current) mediante un perfil de 36 parámetros contextuales alineados con los primitivos P1 (Capacidad), P2 (Flujo) y P3 (Información). Produce una baseline de H_org y permite clasificar el contexto según bandas de salud organizacional (health gates G1–G4), habilitando decisiones informadas de trayectoria en F3.

**Conexión con genoma:**  
- **A1_Organizacion:** F1 materializa la lectura del estado organizacional como sistema socio-técnico.
- **A4_Contexto:** F1 respeta que toda intervención depende del contexto específico (runway, presupuesto, riesgo regulatorio, madurez digital).
- **I1_Continuidad_Operacional:** la baseline H_org capturada en F1 se usa como referencia para garantizar que ninguna intervención rompa operaciones críticas.
- **I4_Clasificacion_Contextual:** F1 entrega la clasificación explícita del contexto que luego gobierna la selección de playbooks y trayectorias.
- **I6_Metricas_Canonicas:** F1 produce H_org baseline, métrica canónica de referencia para todo el WSLC.

## §1 INTERFAZ

```yaml
inputs:
  - id: "stakeholder_interviews"
    fuente: "external"
    descripcion: "Entrevistas estructuradas con stakeholders clave de la organización"
  - id: "org_documentation"
    fuente: "external"
    descripcion: "Documentación organizacional existente (organigramas, procesos, tech stack)"
  - id: "regulatory_context"
    fuente: "external"
    descripcion: "Marco regulatorio aplicable y nivel de cumplimiento actual"
outputs:
  - id: "context_profile_36_params"
    archivo: "context.yaml"
    descripcion: "Perfil contextual de 36 parámetros (estructura, madurez, presupuesto, runway, etc.)"
    schema: "T01_context_assessment.yaml"
  - id: "h_org_baseline"
    descripcion: "Health Score organizacional baseline (H_org) calculado a partir de TF1/TF2/TF3"
    metric_id: "H_org"
  - id: "context_classification"
    descripcion: "Clasificación del contexto en bandas (ej. G1_critical, G2_low, G3_moderate, G4_healthy)"
  - id: "regulatory_constraints"
    archivo: "regulatory_constraints.yaml"
    descripcion: "Lista de restricciones regulatorias que condicionan F3/F8"
  - id: "tech_debt_inventory"
    archivo: "tech_debt_inventory.yaml"
    descripcion: "Inventario preliminar de deuda técnica relevante para trayectorias"
dependencies:
  reads_from: []
  writes_to:
    - "F2"
    - "F3"
    - "F4"
    - "F5"
    - "F6"
    - "F7"
    - "F8"
    - "F13"
artefactos_soporte:
  templates:
    - "T01_context_assessment.yaml"
    - "assessment/organizational_maturity_checklist.md"
  calculadoras:
    - "context_decision_matrix.xlsx"
    - "health_score_calculator.xlsx"
health_gates_relacionados:
  - "G1"
  - "G2"
  - "G3"
  - "G4"
playbooks_relacionados:
  - "P01_low_h_org_recovery"
  - "P02_handoff_reduction"
  - "P03_okr_alignment"
```

**Notas de implementación (P0):**  
- El archivo `context.yaml` en casos (`01_startup_50p_completo`, `06_gore_nuble_completo`) ya contiene una estructura de parámetros consistente con F1, aunque sin documentación explícita de su origen en §0/§1.
- La conexión entre `context.yaml` → `context_decision_matrix.xlsx` → `trajectory_selected` debe explicitarse en la aplicación a casos (pending M1.2 de CAP-P0-01).
- H_org baseline aún no tiene fórmula canónica implementada en `health_score_calculator.xlsx`; eso queda en scope de sq2 bajo P0-COMPLETE.

