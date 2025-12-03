# F3 – Trajectory Selection

## §0 FUNDAMENTO

```yaml
fase_id: F3
nombre_canonico: "Trajectory Selection"
vocabulos_referencia:
  wslc_phase: "VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F3"
  axiomas:
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A4_Contexto"
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A5_Cambio"
  primitivos:
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P4_Limite"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P5_Proposito"
  invariantes:
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I1_Continuidad_Operacional"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I3_Trazabilidad"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I4_Clasificacion_Contextual"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I8_Adaptacion_Contextual"
  dominios:
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D3_Decision"
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D4_Operacion"
  metricas_canonicas:
    - "VOCABULARIO_CONTROLADO.layer_1.metricas_canonicas.H_org"
relacion_kernel:
  es_kernel: true
  depende_de:
    - "F1"
  prepara_a:
    - "F2"
    - "F4"
    - "F5"
    - "F6"
    - "F7"
    - "F8"
    - "F9"
    - "F10"
    - "F11"
    - "F12"
    - "F17"
trayectorias_soportadas:
  - "Survival"
  - "Minimal"
  - "Avanzada"
estado_fundamento: "STABLE"
justificacion: |
  F3 es fase kernel de decisión estratégica que materializa A4_Contexto y A5_Cambio mediante 
  selección de trayectoria óptima basada en F1 (H_org, context_profile) y health gates G1-G4. 
  Usa matriz de decisión formalizada en 03_decision_matrix.md. Tiene dependencia circular con F2 
  resuelta por protocolo F2_F3_convergence_protocol.md. Validado en 3 casos con trayectorias distintas.
backlog_v1_1:
  - "Explicitar reglas de decisión DM1-DMx en decision_matrix.md"
  - "Calibrar thresholds G1-G4 con 10+ casos reales"
  - "Automatizar trajectory_recommendation en calculadora"
referencias_formales:
  - "SPEC_ARQUITECTURA_DEFINITIVA.§1.2.Kernel.F3_Trajectory_Selection"
  - "PLAN_ETAPA_1_KERNEL.SPRINT_1.FASE_2"
  - "validation_final_report.md.§2.3.F3_PASSED"
  - "30_metodologia_orko/09_trayectorias/03_decision_matrix.md"
```

**Propósito:**  
F3 (Trajectory Selection) es la fase de decisión estratégica que, a partir del contexto capturado en F1 (context_profile, H_org_baseline, regulatory_constraints), selecciona la trayectoria óptima de transformación entre: **Survival** (0–3 meses, H_org crítico), **Minimal** (6–12 meses, mejora incremental) o **Avanzada** (18–36 meses, transformación profunda). La decisión se rige por la matriz de decisión (`03_decision_matrix.md`) que considera H_org, presupuesto, runway, complejidad regulatoria y health gates G1–G4.

**Conexión con genoma:**  
- **A4_Contexto:** F3 materializa la dependencia contextual de las decisiones de cambio; la trayectoria seleccionada no es arbitraria sino derivada del perfil F1.
- **A5_Cambio:** F3 define el alcance y ritmo del cambio organizacional (qué fases ejecutar, en qué orden, con qué restricciones).
- **I1_Continuidad_Operacional:** las trayectorias están diseñadas para no romper operaciones críticas; Survival prioriza estabilización, Minimal equilibra mejora y riesgo, Avanzada asume capacidad de transformación profunda.
- **I3_Trazabilidad:** toda decisión de trayectoria queda registrada en `trajectory.md` con justificación explícita basada en F1 y G1–G4.
- **I4_Clasificacion_Contextual:** F3 usa la clasificación de contexto de F1 (ej. G1_critical → Survival forzado) para gobernar la selección.
- **I8_Adaptacion_Contextual:** F3 habilita cambios de trayectoria (F17) si el contexto evoluciona durante la ejecución.

## §1 INTERFAZ

```yaml
inputs:
  - id: "F1.context_profile_36_params"
    fuente: "F1"
  - id: "F1.h_org_baseline"
    fuente: "F1"
  - id: "F1.context_classification"
    fuente: "F1"
  - id: "F1.regulatory_constraints"
    fuente: "F1"
  - id: "stakeholder_risk_tolerance"
    fuente: "external"
    descripcion: "Nivel de tolerancia al riesgo de los stakeholders clave"
  - id: "budget_commitment"
    fuente: "external"
    descripcion: "Presupuesto comprometido para el ciclo de transformación"
  - id: "timeline_constraints"
    fuente: "external"
    descripcion: "Restricciones temporales (runway, deadlines regulatorios, eventos críticos)"
outputs:
  - id: "trajectory_selected"
    archivo: "trajectory.md"
    descripcion: "Trayectoria seleccionada (Survival/Minimal/Avanzada) con justificación explícita"
    valores_posibles: ["Survival", "Minimal", "Avanzada"]
  - id: "timeline_commitment"
    descripcion: "Compromiso temporal de la trayectoria (en meses)"
  - id: "budget_allocation"
    archivo: "budget_allocation.yaml"
    descripcion: "Asignación presupuestaria por fase/playbook según trayectoria"
  - id: "phase_sequence"
    descripcion: "Secuencia de fases F4–F18 a ejecutar según trayectoria (ej. Survival: F4,F10,F13; Minimal: F4,F5,F7,F10,F11,F13; Avanzada: F4–F18 completo)"
  - id: "playbook_preselection"
    descripcion: "Pre-selección de playbooks P01–P15 relevantes según trayectoria y G1–G4"
  - id: "trajectory_decision_rationale"
    archivo: "trajectory_decision_rationale.md"
    descripcion: "Narrativa de justificación de la decisión (por qué Survival/Minimal/Avanzada)"
dependencies:
  reads_from:
    - "F1"
  writes_to:
    - "F2"
    - "F4"
    - "F5"
    - "F6"
    - "F7"
    - "F8"
    - "F9"
    - "F10"
    - "F11"
    - "F12"
    - "F17"
artefactos_soporte:
  templates:
    - "assessment/trajectory_decision_worksheet.md"
  calculadoras:
    - "context_decision_matrix.xlsx"
    - "health_score_calculator.xlsx"
    - "budget_parametric_allocator.xlsx"
  documentos_referencia:
    - "30_metodologia_orko/09_trayectorias/01_minimal_6_12_meses.md"
    - "30_metodologia_orko/09_trayectorias/02_avanzada_18_36_meses.md"
    - "30_metodologia_orko/09_trayectorias/04_survival_0_10K.md"
    - "30_metodologia_orko/09_trayectorias/03_decision_matrix.md"
health_gates_relacionados:
  - "G1"
  - "G2"
  - "G3"
  - "G4"
playbooks_relacionados:
  - "P01_low_h_org_recovery"
  - "P05_bounded_autonomy_m6"
  - "P06_pilot_transformation"
  - "P07_scale_transformation"
reglas_decision:
  - id: "DM1_H_org_critical"
    condicion: "H_org < umbral_G1"
    resultado: "trajectory_selected = Survival (forzado)"
  - id: "DM2_runway_short"
    condicion: "runway < 3 meses AND H_org < umbral_G3"
    resultado: "trajectory_selected = Survival"
  - id: "DM3_budget_minimal"
    condicion: "budget < umbral_minimal AND H_org >= umbral_G2"
    resultado: "trajectory_selected = Minimal"
  - id: "DM4_ambition_high"
    condicion: "H_org >= umbral_G3 AND budget >= umbral_avanzada AND timeline >= 18 meses"
    resultado: "trajectory_selected = Avanzada"
  - id: "DM5_regulatory_heavy"
    condicion: "regulatory_constraints.nivel = alto AND sector = regulado"
    ajuste: "extender timeline y priorizar compliance playbooks (P04)"
```

**Notas de implementación (P0):**  
- Los casos `01_startup_50p_completo`, `06_gore_nuble_completo` ya tienen `trajectory.md` con decisión explícita (Minimal/Avanzada), pero sin documentación formal de cómo se aplicaron las reglas DM1–DM5.
- La conexión `F1.context` → `context_decision_matrix.xlsx` → `trajectory_selected` debe explicitarse en la aplicación a casos (pending M1.2 de CAP-P0-01).
- Las reglas DM1–DM5 son propuestas iniciales basadas en `03_decision_matrix.md`; requieren calibración con casos reales y definición de umbrales canónicos (pending backlog post-1.0.0).

