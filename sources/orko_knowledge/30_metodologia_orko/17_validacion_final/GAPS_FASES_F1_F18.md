# GAPS CRÍTICOS – FASES F1-F18

**Versión**: v1.0.0 FINAL  
**Fecha**: 2025-11-18 (Actualizado post-remediación)

---

## ✅ ESTADO REMEDIACIÓN

```yaml
GAPS_P0_RESUELTOS: 3/3 (100%)
  ✅ GAP-F1: Protocolo convergencia F2↔F3 creado (738 líneas)
  ✅ GAP-F2: §1 INTERFAZ en 7 fases (F2,F7,F9,F14,F15,F17,F18)
  ✅ GAP-F8: Kernel F1/F3/F13 actualizados a STABLE

GAPS_PENDIENTES_BACKLOG_v1.1: 5
  ⏸️ GAP-F3: Fórmula H_org F1 vs F13 (P1)
  ⏸️ GAP-F4: Esquemas TF1/TF2/TF3 (P1)
  ⏸️ GAP-F5: §2 DESCRIPCIÓN F2/F7/F9 (P2)
  ⏸️ GAP-F6: §0 FUNDAMENTO 7 fases (P2)
  ⏸️ GAP-F7: Lifecycle TF1-TF3 (P2)

Estado_§0_FUNDAMENTO_Post_Remediación:
  STABLE: 11 fases (61%) ✅
  Pendiente: 7 fases (39%) → Backlog v1.1
```

---

## RESUMEN EJECUTIVO ORIGINAL

```yaml
Total_Gaps: 8
Severidad:
  P0_CRÍTICA: 3 → RESUELTOS 3/3 ✅
  P1_ALTA: 2 → Backlog v1.1
  P2_MEDIA: 3 → Backlog v1.1

Fases_Afectadas: 12/18 (67%)
Estado_§0_FUNDAMENTO:
  PASSED: 8 fases
  CONDITIONAL: 10 fases
```

---

## ~~GAP-F1: CIRCULARIDAD F2 ↔ F3 NO RESUELTA FORMALMENTE~~ ✅ **RESUELTO**

### Descripción del Problema Original

Existe una dependencia circular entre F2 (Vision Definition) y F3 (Trajectory Selection) que no tiene protocolo de resolución formal documentado.

### ✅ REMEDIACIÓN APLICADA

**Archivo creado**: `/01_fases_initiation/F2_F3_convergence_protocol.md` (738 líneas)

- 6 pasos formales de convergencia
- 2 casos ejemplo validados (startup, scaleup)
- Métricas de convergencia (delta_vision, delta_trajectory)
- Escalation paths y criterios terminación

### Evidencia Detallada

```yaml
# F2_vision_definition.md
inputs:
  - F1.context_profile
  - F3.trajectory_selected  # ← Depende de F3

outputs:
  - vision_statement
  - okr_L4
  - vision_constraints

# F3_trajectory_selection.md
inputs:
  - F1.context_profile
  - F2.vision_statement  # ← Implícito, no documentado

prepara_a: ["F2"]  # ← Menciona que prepara a F2

# README Initiation
"F2 y F3 pueden requerir iteración para converger"
# ← Menciona iteración pero SIN algoritmo
```

### Problema Raíz

1. **Chicken-and-egg**: F2 necesita saber la trayectoria para constraintar la visión, pero F3 necesita la visión para seleccionar trayectoria
2. **Sin algoritmo convergencia**: No existe protocolo formal de cómo iterar
3. **Sin criterios terminación**: No se especifica cuándo declarar convergencia
4. **Sin escalation path**: No se define qué hacer si no converge

### Impacto

🔴 **CRÍTICO (P0)** - Bloquea ejecución Initiation

**Impacto operacional**:

- Casos reales NO pueden ejecutar F2-F3 consistentemente
- Equipos hacen "guessing" de orden de ejecución
- Resultados no reproducibles entre implementaciones
- Violación I3 (Trazabilidad) en kernel crítico

**Impacto en casos existentes**:

```yaml
01_startup_50p_completo:
  problema: "¿Cómo se decidió trajectory antes de vision?"
  workaround_actual: "Asume trajectory primero, ajusta vision después"
  
02_scaleup_200p_completo:
  problema: "Vision ambiciosa conflicta con budget Minimal"
  workaround_actual: "Iteración manual no documentada"
```

### Remediación Detallada

**Paso 1: Crear protocolo formal**

Artefacto: `/01_fases_initiation/F2_F3_convergence_protocol.md`

```yaml
## §0. FUNDAMENTO

**Layer 0**: A5 (Intencionalidad), A4 (Restricción)
**Invariantes**: I3 (Trazabilidad), I6 (Trajectory-Awareness)
**Justificación**: Resolver circularidad F2↔F3 de forma determinista

## §1. PROTOCOLO DE CONVERGENCIA

### Algoritmo Iterativo

```yaml
protocolo_convergencia:
  
  paso_0_inputs:
    - F1.context_profile completado
    - context.yaml validado
  
  paso_1_trajectory_draft:
    ejecuta: F3_provisional
    input: F1.context_profile
    herramienta: context_decision_matrix.xlsx
    output: trajectory_draft (Survival|Minimal|Avanzada)
    criterio: "Usar SOLO context, sin vision"
    
  paso_2_vision_with_constraints:
    ejecuta: F2
    inputs:
      - F1.context_profile
      - F3.trajectory_draft (como constraint)
    output: 
      - vision_statement.md
      - okr_L4.yaml
      - vision_constraints.yaml
    criterio: "Vision debe ser compatible con trajectory_draft"
    
  paso_3_trajectory_validation:
    ejecuta: F3_final
    inputs:
      - F1.context_profile
      - F2.vision_statement
      - F2.vision_constraints
    acción: "Validar si trajectory_draft sigue siendo óptima"
    output: trajectory_validation_report
    
  paso_4_compatibility_check:
    criterio_convergencia:
      - compatibility_score >= 0.80
      - budget_feasible = true
      - timeline_feasible = true
      - sponsor_approved = true
    
    si_converge:
      output: trajectory_selected = trajectory_draft
      estado: CONVERGED
      siguiente: F4
      
    si_no_converge:
      analizar_gap:
        - vision_demasiado_ambiciosa_para_budget
        - trajectory_demasiado_conservadora_para_vision
        - timeline_incompatible
      siguiente: paso_5_iteration
  
  paso_5_iteration:
    max_iterations: 2
    
    iteracion_1:
      acción: "Ajustar F2.vision_constraints o F3.trajectory_draft"
      owner: Role_TrajectoryOwner + Role_Captain
      return_to: paso_2
      
    iteracion_2:
      acción: "Forzar decisión pragmática"
      owner: Role_Captain
      return_to: paso_2
      
    si_falla_iteracion_2:
      siguiente: paso_6_escalation
  
  paso_6_escalation:
    trigger: "No convergencia después 2 iteraciones"
    owner: Role_Captain
    opciones:
      A_ajustar_vision:
        acción: "Reducir alcance vision_statement"
        impacto: "Vision más modesta"
      B_forzar_trajectory:
        acción: "Seleccionar trajectory pragmática"
        impacto: "Gap vision-trajectory documentado"
      C_survival_forzado:
        trigger: "H_org < 60"
        acción: "Entrar modo Survival, diferir vision"
        impacto: "Vision se trabaja post-recovery"
    
    output: escalation_decision_record.md
    accountable: Role_SteeringCommittee
```

### Métricas de Convergencia

```yaml
metricas:
  compatibility_score:
    formula: |
      score = weighted_avg(
        budget_fit × 0.35,
        timeline_fit × 0.30,
        capability_fit × 0.20,
        risk_fit × 0.15
      )
    threshold: >= 0.80
  
  iterations_count:
    objetivo: <= 2
    actual: [registrar por caso]
  
  decision_time:
    objetivo: <= 5 días
    actual: [registrar por caso]
```

```

**Paso 2: Actualizar F2 y F3**

Actualizar inputs en ambas fases para referenciar protocolo:

```yaml
# F2 §1 INTERFAZ (actualizar)
inputs:
  - F1.context_profile
  - F3.trajectory_draft (paso 1 de convergence_protocol)
  
protocol_ref: "01_fases_initiation/F2_F3_convergence_protocol.md"

# F3 §1 INTERFAZ (actualizar)
inputs:
  - F1.context_profile
  - F2.vision_statement (paso 2 de convergence_protocol, opcional iteración)
  
protocol_ref: "01_fases_initiation/F2_F3_convergence_protocol.md"
```

**Paso 3: Crear calculadora convergencia**

Poblar `/40_implementacion_metodologia/calculadoras/convergence_tracker.xlsx` con:

- Tab "F2_F3_Convergence"
- Campos: compatibility_score, iterations, gaps
- Fórmulas automáticas

**Paso 4: Validar en casos**

Aplicar protocolo retrospectivamente a los 6 casos:

```yaml
01_startup_50p:
  trajectory_draft: Minimal (por context: budget 50K, H_org 55)
  vision_constraints: "Growth rápido pero budget limitado"
  compatibility_score: 0.85 ✅
  iterations: 1
  
02_scaleup_200p:
  trajectory_draft: Minimal (por context: H_org 65)
  vision_ambiciosa: "Escalar a 500p en 18 meses"
  compatibility_score_inicial: 0.65 ❌
  iteracion_1: "Reducir alcance vision a 12 meses"
  compatibility_score_final: 0.82 ✅
  iterations: 2
```

### Criterios de Validación

```yaml
validacion_gap_resuelto:
  - [ ] Protocolo F2_F3_convergence_protocol.md creado
  - [ ] §1 INTERFAZ actualizado en F2 y F3
  - [ ] convergence_tracker.xlsx poblada
  - [ ] Protocolo aplicado a 6 casos con éxito
  - [ ] dependency_closure_script.py PASSED
  - [ ] No más referencias a "iteración" sin protocolo
```

### Esfuerzo Estimado

- **Crear protocolo**: 3 horas
- **Actualizar F2/F3**: 1 hora
- **Validar casos**: 2 horas
- **Total**: 6 horas (0.75 días)

### Owner

- **Responsible**: Role_PlaybooksLead
- **Accountable**: Role_Captain
- **Consulted**: Role_TrajectoryOwner

---

## ~~GAP-F2: §1 INTERFAZ AUSENTE O INCOMPLETO EN 7 FASES~~ ✅ **RESUELTO**

### ✅ REMEDIACIÓN APLICADA

**7 fases completadas con §1 INTERFAZ formal**:

- F2: Vision Definition
- F7: Purpose Cascade  
- F9: Target State Design
- F14: Incident Response
- F15: Continuous Execution
- F17: Adaptation
- F18: Convergence Check

**Contenido agregado**: inputs, outputs, dependencies, acceptance_criteria, protocol_ref, templates, tools

### Descripción del Problema Original

Siete fases (39% del total) carecen de §1 INTERFAZ formal o tienen sección truncada/incompleta, violando el contrato de documentación ORKO.

### Evidencia Detallada

```yaml
Fases_Sin_§1_Completo:
  
  F2_Vision_Definition:
    archivo: "02_fases_development/F2_vision_definition.md"
    estado: "TRUNCADO (termina línea 75 abruptamente)"
    tiene_§0: ✅
    tiene_§1: ❌ (parcial)
    
  F7_Purpose_Cascade:
    archivo: "02_fases_development/F7_purpose_cascade.md"
    estado: "AUSENTE (solo §0)"
    tiene_§0: ✅
    tiene_§1: ❌
    
  F9_Target_State_Design:
    archivo: "02_fases_development/F9_target_state_design.md"
    estado: "AUSENTE"
    tiene_§0: ✅
    tiene_§1: ❌
    
  F14_Incident_Response:
    archivo: "04_fases_operation/F14_incident_response.md"
    estado: "AUSENTE"
    tiene_§0: ❌ (también falta)
    tiene_§1: ❌
    
  F15_Continuous_Execution:
    archivo: "04_fases_operation/F15_continuous_execution.md"
    estado: "AUSENTE"
    tiene_§0: ❌
    tiene_§1: ❌
    
  F17_Adaptation:
    archivo: "05_fases_evolution/F17_adaptation.md"
    estado: "AUSENTE"
    tiene_§0: ❌
    tiene_§1: ❌
    
  F18_Convergence_Check:
    archivo: "05_fases_evolution/F18_convergence_check.md"
    estado: "AUSENTE"
    tiene_§0: ❌
    tiene_§1: ❌

Comparación_Fases_Completas:
  
  F4_Capability_Mapping:
    tiene_§0: ✅
    tiene_§1: ✅ (inputs, outputs, dependencies)
    líneas_§1: 25
    
  F5_Flow_Design:
    tiene_§0: ✅
    tiene_§1: ✅
    líneas_§1: 28
```

### Problema Raíz

1. **Contratos no verificables**: Sin §1, no se pueden validar inputs/outputs
2. **Dependency graph roto**: DEPENDENCY_GRAPH.yaml referencia fases sin interfaz formal
3. **Auditoría VG4 incompleta**: No se puede verificar I3/I4 sin contratos
4. **Casos no validables**: Imposible verificar que casos usan fases correctamente

### Impacto

🔴 **CRÍTICO (P0)** - Bloquea validación formal metodología

**Impacto por invariante**:

```yaml
I3_Trazabilidad:
  estado: CONDITIONAL
  razón: "Sin §1, no se puede trazar inputs→outputs"
  
I4_Contratos:
  estado: CONDITIONAL
  razón: "Interfaces no formalizadas"
  
I8_Consistencia_Temporal:
  estado: CONDITIONAL
  razón: "F15/F17/F18 sin §1, evolución no verificable"
```

**Impacto en dependency_closure_script.py**:

```yaml
script_actual:
  valida: "Estructura YAML DEPENDENCY_GRAPH"
  no_valida: "Existencia de §1 en archivos referenciados"
  
si_ejecuta_check_profundo:
  F2: ⚠️  MISSING_INTERFACE
  F7: ⚠️  MISSING_INTERFACE
  F9: ⚠️  MISSING_INTERFACE
  F14-F18: ⚠️  MISSING_INTERFACE (5 fases)
```

### Remediación Detallada

**Template §1 INTERFAZ Estándar**

```yaml
## §1. INTERFAZ

### Inputs

```yaml
inputs:
  - id: "input_1_canonical_id"
    source: "Fx.output_y"
    schema_ref: "VOCABULARIO_CONTROLADO.layer_z.entity_w"
    required: true|false
    description: "Descripción breve del input"
    example: "context.yaml con org_structure poblado"
```

### Outputs

```yaml
outputs:
  - id: "output_1_canonical_id"
    artifact: "artifact_name.yaml|.md|.xlsx"
    schema_ref: "contracts/schemas/artifact_schema.yaml" # si existe
    consumers: ["Fa", "Fb", "Playbook_Px"]
    description: "Descripción del output"
    location: "artefactos/fase_X/"
```

### Dependencies

```yaml
dependencies:
  reads_from: ["F1", "F3"]  # Fases previas
  writes_to: ["F5", "F9"]   # Fases posteriores
  triggers: ["P01", "P02"]  # Playbooks que puede triggerar (si aplica)
  triggered_by: ["F13"]     # Fases que lo triggerea (si aplica)
```

### Acceptance Criteria

```yaml
acceptance:
  - criterion: "Output artifact valida contra schema"
    verification: "manual|automated"
    responsible: "Phase owner"
    
  - criterion: "Métricas H_org/eta_org/ROI_Habilitacion actualizadas (si aplica)"
    verification: "F13 dashboard"
    responsible: "Role_HealthOwner"
    
  - criterion: "Dependencias verificadas con fases previas"
    verification: "dependency_closure_script.py"
    responsible: "Role_Architect"
```

```

**Plan de completitud por fase**:

**F2 - Vision Definition**
```yaml
## §1. INTERFAZ

inputs:
  - id: "context_profile"
    source: "F1.context_assessment"
    schema_ref: "context_pattern_schema.yaml"
    required: true
    
  - id: "trajectory_draft"
    source: "F3.trajectory_provisional"
    schema_ref: "trayectorias/*.md"
    required: true
    note: "Ver F2_F3_convergence_protocol.md"

outputs:
  - id: "vision_statement"
    artifact: "vision_statement.md"
    consumers: ["F3", "F7", "F9"]
    template: "T02_vision_statement.md"
    
  - id: "okr_L4"
    artifact: "okr_L4.yaml"
    consumers: ["F7", "F13"]
    schema: "okr_schema.yaml"
    
  - id: "vision_constraints"
    artifact: "vision_constraints.yaml"
    consumers: ["F3"]
    description: "Constraints derivados de vision para validar trajectory"

dependencies:
  reads_from: ["F1", "F3"]
  writes_to: ["F3", "F7", "F9"]
```

**F7 - Purpose Cascade**

```yaml
inputs:
  - F2.vision_statement
  - F2.okr_L4
  - F3.trajectory_selected
  
outputs:
  - okr_cascade_L4_to_L1.yaml
  - purpose_policy.yaml
  - alignment_matrix.xlsx
  
dependencies:
  reads_from: ["F2", "F3"]
  writes_to: ["F5", "F6", "F9"]
```

**F9 - Target State Design**

```yaml
inputs:
  - F4.capacity_inventory
  - F5.flow_maps
  - F6.information_architecture
  - F7.okr_cascade
  - F8.limits_catalog
  - F3.trajectory_selected
  
outputs:
  - e6_target.yaml (E6_ArchitecturalState)
  - target_diagrams.drawio
  - target_schemas.yaml
  
dependencies:
  reads_from: ["F4", "F5", "F6", "F7", "F8"]
  writes_to: ["F10", "F11", "F12", "F18"]
```

**F14 - Incident Response**

```yaml
inputs:
  - F13.h_org_current
  - F13.playbook_triggers
  - F13.drift_alerts
  
outputs:
  - incident_report.md (template T10)
  - recovery_actions.yaml
  - post_mortem.md
  
dependencies:
  reads_from: ["F13"]
  writes_to: ["F16", "F17"]
  triggers: ["P01", "P02", "P04", "P09"]
```

**F15 - Continuous Execution**

```yaml
inputs:
  - F10.quick_wins_backlog
  - F11.deployment_status
  - F12.state_transition_log
  - F13.drift_alerts
  
outputs:
  - execution_log.md
  - cadence_adjustments.yaml
  - sprint_reports.md
  
dependencies:
  reads_from: ["F10", "F11", "F12", "F13"]
  writes_to: ["F16", "F17"]
  triggers: ["P15"]
```

**F17 - Adaptation**

```yaml
inputs:
  - F16.learnings
  - F13.health_trends
  - F13.gate_history (G1-G4)
  
outputs:
  - trajectory_adjustment.md
  - adaptation_plan.yaml
  - okr_refinement.yaml
  
dependencies:
  reads_from: ["F13", "F16"]
  writes_to: ["F3", "F7", "F18"]
  triggers: ["P03", "P05", "P06", "P13", "P15"]
```

**F18 - Convergence Check**

```yaml
inputs:
  - F9.e6_target
  - F12.e6_current
  - F13.h_org_trends
  
outputs:
  - convergence_report.md
  - convergence_score: float [0, 1]
  - gap_analysis.yaml
  
dependencies:
  reads_from: ["F9", "F12", "F13"]
  writes_to: ["F17"]
```

### Criterios de Validación

```yaml
validacion_por_fase:
  - [ ] §1 completo con 4 secciones (inputs, outputs, dependencies, acceptance)
  - [ ] Todos los inputs tienen source válido
  - [ ] Todos los outputs tienen consumers documentados
  - [ ] Dependencies alineadas con DEPENDENCY_GRAPH.yaml
  - [ ] Templates/schemas referenciados existen
  - [ ] Acceptance criteria específicos y medibles

validacion_global:
  - [ ] dependency_closure_script.py PASSED
  - [ ] No orphan outputs (todo output es input de alguien)
  - [ ] Ciclo WSLC completo cubierto F1→F18
  - [ ] Health gates G1-G4 enganchados a fases correctas
```

### Esfuerzo Estimado

```yaml
Por_Fase:
  - Redacción §1: 3 horas
  - Validación dependencies: 1 hora
  - Total por fase: 4 horas
  
Total_7_Fases:
  - 7 fases × 4h = 28 horas
  - Equivalente: 3.5 días (estimado 3 días con paralelización)
```

### Owner

- **Responsible**: Role_PlaybooksLead
- **Consulted**: Role_Architect (dependencies), Role_HealthOwner (métricas)

---

## GAP-F3: FÓRMULA H_org INCONSISTENTE F1 vs F13

**Problema**:

- F1 produce `h_org_baseline` sin fórmula
- F13 tiene fórmula explícita weighted_avg
- Métrica canónica con 2 definiciones

**Impacto**: 🟠 P1 - Baselines no comparables con current

**Remediación**: Unificar fórmula en VOCABULARIO_CONTROLADO.yaml, actualizar F1 §1, poblar health_score_calculator.xlsx

---

## GAP-F4: UMBRALES NUMÉRICOS AUSENTES EN F3

**Problema**: DM1-DM5 usan variables sin valores (`umbral_G1`, `umbral_minimal`)

**Impacto**: 🟠 P1 - F3 no ejecutable, context_decision_matrix.xlsx no operable

**Remediación**: Crear tabla canónica umbrales (H_org: <60 critical, budget: <10K survival, etc.)

---

## GAP-F5: E6 UBICACIÓN ONTOLÓGICA INCORRECTA

**Problema**: E6 en `/20_tejidos/` cuando debería estar en `/10_arquitectura_orko/`

**Impacto**: 🟡 P2 - Confusión ontológica (no bloquea operación)

**Remediación**: Mover a `10_arquitectura_orko/06_e6_architectural_state.md`, actualizar referencias

---

## GAP-F6: FASES CONDITIONAL EN DEPENDENCIAS CRÍTICAS

**Fases**: F16, F17, F18 sin §0 completo pero usadas activamente

**Impacto**: 🟡 P2 - Integridad arquitectónica comprometida

**Remediación**: Completar §0 FUNDAMENTO en F16-F18 o marcar dependencias como "soft"

---

## GAP-F7: MATRIZ [FASE × TRAYECTORIA] AUSENTE

**Problema**: Scope de fases por trayectoria disperso en docs

**Impacto**: 🟡 P2 - Usuarios no saben qué fases ejecutar

**Remediación**: Crear `00_trajectory_phase_matrix.yaml` con mapeo explícito

---

## ~~GAP-F8: §0 FUNDAMENTO INCOMPLETO EN 10 FASES~~ ✅ **PARCIALMENTE RESUELTO**

### ✅ REMEDIACIÓN APLICADA

**3 fases kernel actualizadas a STABLE**:

- F1: Context Assessment (justificación formal, casos validados, backlog v1.1)
- F3: Trajectory Selection (justificación formal, protocolo F2↔F3, backlog v1.1)
- F13: Health Monitoring (justificación formal, métricas tracking, backlog v1.1)

**Estado post-remediación**: 11/18 fases con §0 STABLE (61%)

**Fases CONDITIONAL restantes** → Backlog v1.1: F7, F9, F14-F18 (7 fases, 39%)

**Impacto**: 🟡 P2 para v1.0.0 (documentado), 🔴 P0 para v1.1.0

**Remediación por prioridad**:

- P0 v1.0.0: F1, F3, F13 (kernel crítico)
- P1 v1.1.0: F7, F9, F14, F15
- P2 v1.2.0: F16, F17, F18

---

## PRIORIZACIÓN v1.0.0

**BLOQUEANTES (P0)**:

1. GAP-F1: Protocolo F2↔F3
2. GAP-F2: §1 en 7 fases  
3. GAP-F8_kernel: §0 en F1/F3/F13

**RECOMENDADOS (P1)**:
4. GAP-F3: Fórmula H_org
5. GAP-F4: Umbrales F3

**BACKLOG v1.1 (P2)**:
6. GAP-F5: Mover E6
7. GAP-F6: §0 F16-F18
8. GAP-F7: Matriz fases×trayectoria
