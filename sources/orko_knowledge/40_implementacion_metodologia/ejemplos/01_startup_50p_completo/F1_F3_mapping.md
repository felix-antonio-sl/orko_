# F1/F3 Mapping – 01_startup_50p_completo

## Propósito

Este documento mapea explícitamente cómo los artefactos `context.yaml` y `trajectory.md` del caso **01_startup_50p_completo** instancian los contratos de interfaz de las fases **F1 (Context Assessment)** y **F3 (Trajectory Selection)** según lo documentado en:
- `30_metodologia_orko/01_fases_initiation/F1_context_assessment.md`
- `30_metodologia_orko/01_fases_initiation/F3_trajectory_selection.md`

Versión: P0-COMPLETE (ORKO v1.0.0)

---

## §1 MAPEO F1 (Context Assessment)

### 1.1 Inputs F1 → Fuentes en este caso

Según F1 §1 INTERFAZ, los inputs son:

| Input F1 | Fuente en 01_startup | Notas |
|----------|---------------------|-------|
| `stakeholder_interviews` | **Implícito** (no documentado explícitamente en repo) | Se asume que el perfil en `context.yaml` deriva de entrevistas con founders/líderes |
| `org_documentation` | **Implícito** (organigramas, tech stack description) | `tech_stack_maturity: mid` sugiere mapeo preliminar; no hay artefacto formal en caso |
| `regulatory_context` | `context.yaml::regulatory_context` | "Contexto regulatorio estándar para SaaS B2B, con foco en privacidad y seguridad básica" |

**Gap P0:** Los inputs externos de F1 no están materializados como archivos separados en este caso (ej. `stakeholder_interviews.md`, `tech_inventory.yaml`). El perfil `context.yaml` se trata como **output consolidado** de F1, asumiendo que los inputs ya fueron procesados.

### 1.2 Outputs F1 → Artefactos en este caso

| Output F1 | Artefacto en 01_startup | Mapeo de campos |
|-----------|------------------------|-----------------|
| `context_profile_36_params` | `context.yaml` | **Mapeo parcial:** `context.yaml` tiene 15 campos estructurados; se asume que los 36 parámetros completos de F1 incluyen estos 15 + información adicional no explicitada en este caso (ej. runway en meses, presupuesto IT anual, % deuda técnica, métricas baseline de TF1/TF2/TF3). **Schema:** se esperaría `T01_context_assessment.yaml` (no presente en repo actualmente). |
| `h_org_baseline` | **No explícito** en `context.yaml` | Gap: H_org baseline debería calcularse usando `health_score_calculator.xlsx` a partir de datos de TF1/TF2/TF3. En este caso, se infiere que H_org está en banda **G3** (bueno pero con eficiencia baja) dado que `default_trajectory = Minimal` y `hypergrowth_flags.contratacion_rapida = true` (señal de stress en flujos). |
| `context_classification` | **Implícito** en `tipo_contexto: startup`, `maturity_level: startup_early`, `crisis_flags: false` | Clasificación: **G3 (H_org bueno, eficiencia baja)**. No hay banda explícita en YAML; se deriva de la lógica de `trajectory.md` que usa `DM3_G3_Minimal_Optimización`. |
| `regulatory_constraints` | `context.yaml::regulatory_context` | "Contexto regulatorio estándar... privacidad y seguridad básica" → se mapea a restricciones de compliance en F8. No hay archivo `regulatory_constraints.yaml` separado. |
| `tech_debt_inventory` | **No presente** | Gap: inventario de deuda técnica debería existir como output de F1 para alimentar F4/F5. En este caso, `tech_stack_maturity: mid` sugiere nivel moderado de deuda pero sin detalle. |

**Resumen F1:** `context.yaml` actúa como **proxy comprimido** del output `context_profile_36_params` de F1, pero sin la estructura formal de schema T01 ni la evidencia explícita de H_org baseline calculado.

---

## §2 MAPEO F3 (Trajectory Selection)

### 2.1 Inputs F3 → Fuentes en este caso

| Input F3 | Fuente en 01_startup | Mapeo |
|----------|---------------------|-------|
| `F1.context_profile_36_params` | `context.yaml` | Ver §1.2 arriba |
| `F1.h_org_baseline` | **Inferido** de `context.yaml` + `trajectory.md` | H_org estimado en banda G3 (ver §1.2) |
| `F1.context_classification` | `context.yaml::tipo_contexto`, `maturity_level`, `crisis_flags`, `hypergrowth_flags` | Clasificación: startup early-stage con hypergrowth en contratación, sin crisis activa |
| `F1.regulatory_constraints` | `context.yaml::regulatory_context` | SaaS B2B estándar |
| `stakeholder_risk_tolerance` | **Implícito** en `risk_profile` | "Alta incertidumbre de producto/mercado con runway limitado" → tolerancia media-alta al riesgo operativo, pero baja al riesgo financiero (runway limitado) |
| `budget_commitment` | **No explícito** | Gap: presupuesto comprometido para ciclo de transformación no está documentado. Se infiere que es **limitado** (típico de Series A) |
| `timeline_constraints` | **No explícito** | Gap: runway en meses no está en `context.yaml`. Se asume 12–18 meses por contexto Series A. |

**Gap P0:** Inputs externos de F3 (`stakeholder_risk_tolerance`, `budget_commitment`, `timeline_constraints`) no están materializados explícitamente. La decisión de trayectoria en `trajectory.md` se basa en inferencias razonables del contexto.

### 2.2 Outputs F3 → Artefactos en este caso

| Output F3 | Artefacto en 01_startup | Mapeo |
|-----------|------------------------|-------|
| `trajectory_selected` | `context.yaml::default_trajectory` + `trajectory.md` §1 | **Minimal** (explícito en ambos archivos) |
| `timeline_commitment` | **Implícito** en `trajectory.md` §1 | "Minimal" → horizonte 6–12 meses según `09_trayectorias/01_minimal_6_12_meses.md` |
| `budget_allocation` | **No presente** | Gap: no hay archivo `budget_allocation.yaml`. Se esperaría asignación por fase/playbook según trayectoria. |
| `phase_sequence` | **Implícito** en `trajectory.md` §2 | Se mencionan F13, F17, F4, F5 como fases activas; secuencia completa no está documentada explícitamente |
| `playbook_preselection` | `trajectory.md` §2 | **P01, P03, P09, P10, P11** mencionados según G1–G4; P02, P04, P15 reservados para Survival |
| `trajectory_decision_rationale` | `trajectory.md` §1–§2 | **Presente:** justificación basada en DM2/DM3, necesidad de optimización sin inversión de Avanzada |

**Resumen F3:** `trajectory.md` materializa la mayoría de los outputs de F3, especialmente `trajectory_selected` y `trajectory_decision_rationale`. Faltan artefactos formales de `budget_allocation` y `phase_sequence` completa.

---

## §3 CONEXIÓN CON CONTEXT_DECISION_MATRIX

### 3.1 Reglas de decisión aplicadas (según F3 §1 INTERFAZ)

El archivo `trajectory.md` §1 documenta explícitamente la aplicación de reglas DM de `09_trayectorias/03_decision_matrix.md`:

| Regla DM (F3) | Aplicación en 01_startup | Evidencia |
|---------------|-------------------------|-----------|
| **DM1_H_org_critical** | **No aplica** en baseline | `crisis_flags: false`; H_org estimado en G3, no G1 |
| **DM2_runway_short** | **Contexto de riesgo** | "runway limitado" en `risk_profile` señala posible activación futura de DM2 si H_org cae a G2 |
| **DM3_budget_minimal** | **Sí aplica** | Budget inferido como limitado (Series A); H_org >= G2 → selección de **Minimal** coherente con DM3 |
| **DM4_ambition_high** | **No aplica** | No cumple condiciones de G4 + budget avanzada + timeline >= 18 meses |
| **DM5_regulatory_heavy** | **No aplica** | Regulatory context estándar, no alto |

**Conclusión:** La decisión `trajectory_selected = Minimal` es **consistente** con DM3 (budget minimal + H_org >= G2) y con el contexto de startup early-stage.

### 3.2 Uso de `context_decision_matrix.xlsx`

**Gap P0:** El caso no incluye evidencia de uso explícito de `context_decision_matrix.xlsx` (calculadora). Se asume que:
1. Los parámetros de `context.yaml` alimentarían la matriz (tipo_contexto, maturity_level, funding_stage, risk_profile, crisis_flags, hypergrowth_flags)
2. La matriz calcularía H_org estimado y aplicaría reglas DM1–DM5
3. El output sería `trajectory_selected = Minimal`, consistente con lo documentado

**Pendiente (backlog post-1.0.0):** Implementar la calculadora según `CALCULADORAS_P0_SPEC.md` y aplicarla a este caso para validar coherencia.

---

## §4 CONEXIÓN CON HEALTH GATES G1–G4

El archivo `trajectory.md` §2 documenta cómo las decisiones F3/F17 se rigen por health gates:

| Health Gate | Banda H_org | Uso en 01_startup |
|-------------|-------------|-------------------|
| **G1 (Crítico)** | H_org < 60 | **Reservado para crisis:** si aparece, fuerza paso temporal a Survival (DM1) con P01/P02/P04/P15 |
| **G2 (Bajo/Riesgo)** | 60 ≤ H_org < 70 | **Monitoreo activo:** DM2 activa ajustes defensivos (P09 Drift Detection + P01 focalizado) |
| **G3 (Bueno/Eficiencia baja)** | 70 ≤ H_org < 85 | **Estado actual inferido:** DM3 activa ciclos de optimización (P10/P11/P03) |
| **G4 (Ready for Avanzada)** | H_org >= 85 | **Horizonte futuro:** poco frecuente en startup 50p; activaría transición a Avanzada (DM4) |

**Evidencia:** `trajectory.md` §2 detalla explícitamente las decisiones F17 (Adaptation) según cada gate, alineado con `02_health_gates.md` y con el contrato F3 §1 INTERFAZ.

---

## §5 GAPS Y PRÓXIMOS PASOS (P0)

### 5.1 Gaps detectados

1. **Inputs externos de F1 no materializados:** `stakeholder_interviews`, `org_documentation` asumidos implícitos
2. **H_org baseline no calculado explícitamente:** se infiere de contexto, pero no hay output formal de `health_score_calculator.xlsx`
3. **Schema T01 ausente:** `context.yaml` no sigue schema formal de 36 parámetros
4. **Inputs externos de F3 no explícitos:** `budget_commitment`, `timeline_constraints` inferidos
5. **Artefactos faltantes de F3:** `budget_allocation.yaml`, `phase_sequence` completa
6. **Calculadora no aplicada:** `context_decision_matrix.xlsx` no usada explícitamente en este caso

### 5.2 Fortalezas del caso actual

1. **Trayectoria explícita y justificada:** `trajectory.md` materializa bien `trajectory_decision_rationale`
2. **Conexión clara con DM y G1–G4:** se referencian reglas de decisión y health gates de forma coherente
3. **Playbook preselection documentada:** P01/P03/P09/P10/P11 explícitos según escenarios G1–G4
4. **Adaptación F17 descrita:** mecanismo de cambio de trayectoria según health gates está documentado

### 5.3 Acciones recomendadas (backlog post-1.0.0)

1. **Enriquecer `context.yaml` a 36 parámetros** usando schema T01 cuando esté definido
2. **Calcular H_org baseline** usando `health_score_calculator.xlsx` según spec de sq2
3. **Crear `budget_allocation.yaml`** con asignación por fase/playbook según Minimal
4. **Aplicar `context_decision_matrix.xlsx`** y documentar resultado en este caso
5. **Generar `phase_sequence.md`** con orden explícito de ejecución F4–F18 según Minimal

---

## §6 CONCLUSIÓN

El caso **01_startup_50p_completo** instancia razonablemente los contratos F1/F3 a nivel conceptual:
- `context.yaml` actúa como proxy de `F1.context_profile_36_params`
- `trajectory.md` materializa `F3.trajectory_selected` y `trajectory_decision_rationale`
- La decisión Minimal es coherente con DM3 y con el contexto startup early-stage
- La conexión con G1–G4 está bien documentada para decisiones F17

Sin embargo, faltan artefactos formales (H_org calculado, budget_allocation, uso explícito de calculadoras) que deberían completarse en iteraciones post-1.0.0 para cerrar el loop F1→context_decision_matrix→F3→trajectory.

---

**Versión:** P0-COMPLETE  
**Autor:** sq1/E1  
**Fecha:** 2025-11-18
