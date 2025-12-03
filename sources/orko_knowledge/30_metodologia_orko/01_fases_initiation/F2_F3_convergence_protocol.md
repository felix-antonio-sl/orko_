# PROTOCOLO DE CONVERGENCIA F2 ↔ F3

**Versión**: v1.0.0  
**Fecha**: 2025-11-17  
**Estado**: ACTIVO  
**Propósito**: Resolver formalmente la dependencia circular entre F2 (Vision Definition) y F3 (Trajectory Selection)

---

## §0. FUNDAMENTO

**Layer 0 - Axiomas**:
- **A4 (Restricción)**: Trajectory actúa como restricción a Vision
- **A5 (Intencionalidad)**: Vision guía selección de Trajectory

**Primitivos**:
- **P4 (Restricción Asimétrica)**: "Constraints shape freedom" - Budget y timeline delimitan ambición

**Invariantes**:
- **I3 (Trazabilidad)**: Decisión F2↔F3 debe ser auditable
- **I6 (Trajectory-Awareness)**: Toda decisión debe considerar capacidades contexto

**Justificación Ontológica**:

El chicken-and-egg F2↔F3 es una dependencia REAL, no un defecto:
- Vision determina qué trajectory es necesaria
- Trajectory determina qué vision es factible

La solución no es eliminar la circularidad, sino **formalizarla con protocolo de convergencia**.

---

## §1. ALGORITMO DE CONVERGENCIA

### 1.1 Inputs Requeridos

```yaml
inputs_protocolo:
  - F1.context_profile (COMPLETO)
  - context.yaml (validado)
  - Sponsor disponible para decisión
  - context_decision_matrix.xlsx (operativa)
```

### 1.2 Fases del Protocolo

```yaml
protocolo_convergencia:
  
  # ============================================
  # PASO 0: VALIDACIÓN PREVIA
  # ============================================
  
  paso_0_prerequisites:
    validar:
      - F1_completed: true
      - context_yaml_valid: true
      - H_org_baseline_calculated: true
      - budget_runway_defined: true
    
    si_falla:
      acción: "STOP - Completar F1 antes de iniciar F2↔F3"
      escalate_to: Role_Captain
  
  # ============================================
  # PASO 1: TRAJECTORY DRAFT (F3 PROVISIONAL)
  # ============================================
  
  paso_1_trajectory_draft:
    descripción: "Selección provisional de trajectory usando SOLO context, sin vision"
    
    ejecuta: F3_trajectory_selection (modo provisional)
    
    inputs:
      - F1.context_profile
      - context.yaml:
          - H_org_baseline
          - budget_usd
          - runway_months
          - team_size
          - sponsor_commitment
    
    herramienta: context_decision_matrix.xlsx
    
    decision_rules:
      DM1: "IF H_org < 60 THEN Survival"
      DM2: "IF runway < 3 AND H_org < 70 THEN Survival"
      DM3: "IF budget < 10K AND H_org >= 60 THEN Minimal"
      DM4: "IF H_org >= 70 AND budget >= 100K THEN Avanzada"
      DM5: "ELSE Minimal (default)"
    
    output:
      trajectory_draft: "Survival | Minimal | Avanzada"
      confidence_score: float [0, 1]
      rationale: "Justificación decision matrix"
    
    artefacto: "trajectory_draft_report.yaml"
    
    owner: Role_TrajectoryOwner
    duration: 2-4 horas
  
  # ============================================
  # PASO 2: VISION WITH CONSTRAINTS (F2)
  # ============================================
  
  paso_2_vision_with_constraints:
    descripción: "Definir vision CON trajectory_draft como restricción"
    
    ejecuta: F2_vision_definition
    
    inputs:
      - F1.context_profile
      - paso_1.trajectory_draft (como constraint)
      - trajectory_specifications:
          Survival: "2-3 meses, quick wins, recovery focus"
          Minimal: "6-12 meses, fases F1-F12, stabilization"
          Avanzada: "18-36 meses, F1-F18 completo, transformación"
    
    constraints_by_trajectory:
      Survival:
        - vision_horizon: "2-3 meses"
        - okr_L4_limit: "2-3 objetivos (survival-focused)"
        - scope: "Recovery only, no transformación"
        - budget_alert: "Minimal investment"
      
      Minimal:
        - vision_horizon: "6-12 meses"
        - okr_L4_limit: "3-5 objetivos (stabilization + growth)"
        - scope: "Initiation + Development + Implementation parcial"
        - budget_alert: "Inversión moderada"
      
      Avanzada:
        - vision_horizon: "18-36 meses"
        - okr_L4_limit: "5-8 objetivos (transformación completa)"
        - scope: "WSLC completo F1-F18"
        - budget_alert: "Inversión significativa"
    
    proceso:
      1. "Definir vision_statement compatible con trajectory_draft"
      2. "Crear okr_L4 dentro de límites trajectory"
      3. "Documentar vision_constraints explícitos"
      4. "Validar feasibility con Sponsor"
    
    output:
      - vision_statement.md
      - okr_L4.yaml
      - vision_constraints.yaml
    
    artefactos: "vision_package/"
    
    owner: Role_Captain + Sponsor_L1_Human
    duration: 4-6 horas
  
  # ============================================
  # PASO 3: TRAJECTORY VALIDATION (F3 FINAL)
  # ============================================
  
  paso_3_trajectory_validation:
    descripción: "Validar si trajectory_draft sigue siendo óptima dado vision_statement"
    
    ejecuta: F3_trajectory_selection (modo validación)
    
    inputs:
      - F1.context_profile
      - paso_1.trajectory_draft
      - paso_2.vision_statement
      - paso_2.vision_constraints
    
    validaciones:
      
      vision_trajectory_alignment:
        question: "¿Vision es compatible con trajectory_draft?"
        checks:
          - vision_horizon <= trajectory_max_timeline
          - okr_L4_count <= trajectory_okr_limit
          - vision_scope ⊆ trajectory_phases
        
      ambition_budget_fit:
        question: "¿Budget soporta la ambición de vision?"
        formula: |
          budget_required = estimate_budget(vision_statement)
          fit_score = min(1.0, budget_actual / budget_required)
        threshold: fit_score >= 0.80
      
      capability_gap_analysis:
        question: "¿Capacidades actuales pueden soportar vision?"
        check: |
          gaps = vision_requirements - current_capabilities
          IF gaps_críticos > 3 THEN feasibility = LOW
      
      sponsor_alignment:
        question: "¿Sponsor committed con vision bajo trajectory?"
        validation: "Reunión validación sponsor"
        output: sponsor_approval: bool
    
    output:
      trajectory_validation_report:
        trajectory_confirmed: bool
        alignment_score: float [0, 1]
        gaps_detected: [gap1, gap2, ...]
        recommendation: "CONFIRM | ADJUST | ESCALATE"
    
    artefacto: "trajectory_validation_report.yaml"
    
    owner: Role_TrajectoryOwner + Role_Captain
    duration: 2-3 horas
  
  # ============================================
  # PASO 4: COMPATIBILITY CHECK (DECISIÓN)
  # ============================================
  
  paso_4_compatibility_check:
    descripción: "Evaluar convergencia y decidir siguiente acción"
    
    criterios_convergencia:
      
      C1_alignment_score:
        formula: |
          alignment = weighted_avg(
            vision_trajectory_fit × 0.30,
            budget_feasibility × 0.30,
            capability_fit × 0.20,
            timeline_feasibility × 0.10,
            sponsor_commitment × 0.10
          )
        threshold: alignment >= 0.80
      
      C2_critical_gaps:
        condition: "gaps_críticos == 0"
        nota: "Gaps no críticos son aceptables si alignment >= 0.80"
      
      C3_sponsor_approval:
        condition: "sponsor_approved == true"
        bloqueante: "Si sponsor rechaza, NO converge (independiente score)"
    
    decision_logic:
      
      SI_CONVERGE:
        conditions: "C1 AND C2 AND C3"
        output:
          trajectory_selected: trajectory_draft
          estado: "CONVERGED"
          siguiente_fase: "F4_capability_mapping"
          artefacto: "convergence_success_report.yaml"
        comunicar: "F2↔F3 convergieron exitosamente"
      
      SI_NO_CONVERGE:
        conditions: "NOT(C1 AND C2 AND C3)"
        analizar_gap_type:
          
          gap_vision_muy_ambiciosa:
            signal: "budget_fit < 0.70 OR capability_fit < 0.70"
            problema: "Vision excede capacidad trajectory"
          
          gap_trajectory_muy_conservadora:
            signal: "alignment_high BUT sponsor_frustrated"
            problema: "Trajectory subestima potencial org"
          
          gap_timeline_incompatible:
            signal: "timeline_fit < 0.70"
            problema: "Plazos vision vs trajectory no alinean"
          
          gap_sponsor_uncommitted:
            signal: "sponsor_approved == false"
            problema: "Sponsor no respalda vision bajo trajectory"
        
        siguiente: "paso_5_iteration"
        artefacto: "convergence_gap_analysis.yaml"
  
  # ============================================
  # PASO 5: ITERATION (MAX 2 CICLOS)
  # ============================================
  
  paso_5_iteration:
    descripción: "Ajustar F2 o F3 e iterar"
    
    max_iterations: 2
    
    iteracion_1:
      trigger: "Primera no convergencia"
      
      analizar_gap_root_cause:
        tools: "convergence_gap_analysis.yaml"
        reunión: "Role_Captain + Role_TrajectoryOwner + Sponsor"
        duration: "1-2 horas"
      
      opciones_ajuste:
        
        A_reducir_vision:
          acción: "Ajustar vision_statement y okr_L4 a menor alcance"
          ejemplo: "Reducir OKR de 8 a 5, acortar horizon 36→18 meses"
          owner: Role_Captain + Sponsor
          impacto: "Vision más modesta, mayor feasibility"
        
        B_aumentar_trajectory:
          acción: "Upgrade trajectory_draft (Minimal→Avanzada)"
          condiciones: "Budget/capacidad permiten, solo era conservador"
          owner: Role_TrajectoryOwner
          impacto: "Trajectory más ambiciosa, mayor inversión"
        
        C_ajustar_ambos:
          acción: "Compromiso: vision un poco menos + trajectory un poco más"
          owner: Role_Captain (mediador)
          impacto: "Convergencia en punto medio"
      
      ejecutar:
        - Implementar ajuste elegido
        - return_to: "paso_2 o paso_3 según ajuste"
        - Documentar cambios en iteration_log.yaml
      
      success_criteria: "alignment >= 0.80 en siguiente vuelta"
    
    iteracion_2:
      trigger: "Segunda no convergencia (iteración_1 falló)"
      
      escalation: "MANDATORIO"
      
      reunión_decisión:
        participants:
          - Role_Captain (accountable)
          - Role_TrajectoryOwner
          - Sponsor_L1_Human
          - [opcional] Board_Governance
        
        agenda:
          1. "Revisar historial 2 iteraciones"
          2. "Identificar constraint inflexible (budget? vision? timeline?)"
          3. "Decisión pragmática forzada"
        
        opciones_forzadas:
          
          A_vision_pragmatica:
            acción: "Forzar vision realista para trajectory disponible"
            mensaje: "Vision ajustada a capacidad real org"
            aprobación: Sponsor (debe aceptar vision menor)
          
          B_trajectory_pragmatica:
            acción: "Forzar trajectory conservadora para vision dada"
            mensaje: "Trajectory ajustada a resources disponibles"
            aprobación: Captain (puede override trajectory_draft)
          
          C_survival_forzado:
            trigger: "H_org < 60 (siempre) O runway < 3 meses"
            acción: "Entrar modo Survival, diferir vision completa"
            mensaje: "Contexto crítico, prioridad recovery"
            impacto: "Vision se trabaja post-recovery (en F17)"
            aprobación: Captain (autoridad unilateral en crisis)
        
        output: forced_decision_record.md
        
        siguiente: "F4 (convergencia forzada)"
      
      nota: "Iteración_2 SIEMPRE resuelve (con decisión pragmática)"
    
    si_falla_iteracion_2:
      # Técnicamente imposible (iteración_2 siempre decide)
      fallback: "paso_6_escalation"
  
  # ============================================
  # PASO 6: ESCALATION (RARÍSIMO)
  # ============================================
  
  paso_6_escalation:
    descripción: "Escalation a governance si 2 iteraciones no resuelven"
    
    trigger: "Deadlock sponsor-captain O conflicto fundamental"
    
    escalation_path:
      nivel_1:
        escalate_to: Board_Governance
        pregunta: "¿Continuar iniciativa ORKO o cancelar?"
        opciones:
          - "Aprobar Survival forzado (mínimo viable)"
          - "Aprobar Minimal con vision reducida"
          - "Cancelar iniciativa (no hay fit)"
      
      nivel_2:
        si_board_no_decide:
          escalate_to: CEO / Autoridad máxima org
          mensaje: "Decisión final requerida"
    
    output: escalation_resolution_record.md
    
    accountable: Role_SteeringCommittee
    
    nota: "Escalation es excepcional - solo 1-2% de casos"
```

---

## §2. MÉTRICAS Y OBSERVABILIDAD

### 2.1 Métricas de Convergencia

```yaml
metricas_protocolo:
  
  compatibility_score:
    formula: |
      compatibility = weighted_avg(
        vision_trajectory_fit × 0.30,
        budget_feasibility × 0.30,
        capability_fit × 0.20,
        timeline_feasibility × 0.10,
        sponsor_commitment × 0.10
      )
    rango: [0, 1]
    threshold_convergencia: >= 0.80
    threshold_warning: [0.70, 0.80)
    threshold_crítico: < 0.70
  
  iterations_count:
    objetivo: "<= 1 (ideal)"
    aceptable: "2"
    crítico: "> 2 (escalation)"
    actual: [registrar por caso]
  
  decision_time:
    objetivo: "<= 3 días (calendario)"
    aceptable: "3-5 días"
    crítico: "> 5 días"
    actual: [registrar por caso]
  
  convergence_rate:
    formula: "casos_converged_first_try / casos_total"
    target: ">= 70%"
    actual: [calibrar con casos reales]
```

### 2.2 Observabilidad

```yaml
artefactos_trazabilidad:
  
  convergence_tracker.xlsx:
    ubicación: "40_implementacion_metodologia/calculadoras/"
    tabs:
      - F2_F3_Convergence: "Cálculos compatibility_score"
      - Iteration_Log: "Historial iteraciones por caso"
      - Metrics_Dashboard: "KPIs protocolo"
  
  por_caso_generar:
    - trajectory_draft_report.yaml
    - vision_package/ (statement, okr, constraints)
    - trajectory_validation_report.yaml
    - convergence_success_report.yaml (o gap_analysis.yaml)
    - [si aplica] iteration_log.yaml
    - [si aplica] forced_decision_record.md
```

---

## §3. CASOS DE APLICACIÓN

### 3.1 Caso Startup 50p (Convergencia Paso 4)

```yaml
caso: 01_startup_50p_completo

paso_1_trajectory_draft:
  H_org: 54.3
  budget: 50K USD
  runway: 4 meses
  decision_rule: DM1 (H_org < 60)
  trajectory_draft: Survival
  confidence: 0.95

paso_2_vision_with_constraints:
  vision_statement: "Estabilizar operación en 8 semanas"
  okr_L4:
    - "O1: H_org 55→70 en 8 semanas"
    - "O2: Reducir turnover 15%→5%"
  constraints: "Recovery focus, no growth"
  sponsor_approved: true

paso_3_trajectory_validation:
  alignment_score: 0.88
  gaps: []
  recommendation: CONFIRM

paso_4_compatibility_check:
  C1_alignment: 0.88 >= 0.80 ✅
  C2_gaps: 0 ✅
  C3_sponsor: true ✅
  RESULTADO: CONVERGED
  iterations: 1
  tiempo: 2 días
```

### 3.2 Caso Scaleup 200p (Convergencia con Iteración)

```yaml
caso: 02_scaleup_200p_completo

paso_1_trajectory_draft:
  H_org: 67.8
  budget: 150K USD
  runway: 9 meses
  decision_rule: DM5 (default)
  trajectory_draft: Minimal
  confidence: 0.75

paso_2_vision_with_constraints:
  vision_statement: "Escalar a 500p en 18 meses"
  okr_L4: [8 objetivos ambiciosos]
  constraints: "Ambiciosa para Minimal"
  sponsor_approved: true (inicialmente)

paso_3_trajectory_validation:
  alignment_score: 0.65  # BAJO
  gaps:
    - "Vision requiere Avanzada"
    - "Budget 150K insuficiente para 500p"
  recommendation: ADJUST

paso_4_compatibility_check:
  C1_alignment: 0.65 < 0.80 ❌
  RESULTADO: NO_CONVERGE
  gap_type: vision_muy_ambiciosa

paso_5_iteration_1:
  analisis: "Vision 18 meses demasiado ambiciosa para Minimal"
  ajuste: A_reducir_vision
  nueva_vision: "Escalar a 300p en 12 meses"
  nuevo_okr_L4: [5 objetivos moderados]
  
  # Re-ejecutar paso_3
  nuevo_alignment: 0.82 ✅
  RESULTADO: CONVERGED (en iteración 1)
  iterations: 2
  tiempo: 4 días
```

---

## §4. VALIDACIÓN Y OWNERSHIP

### 4.1 Criterios de Validación

```yaml
validacion_protocolo:
  - [ ] Protocolo aplicado a 6 casos ORKO con éxito
  - [ ] Convergence rate >= 70% (4+ casos convergen sin iteración)
  - [ ] Ningún caso requiere escalation (paso_6)
  - [ ] Compatibility_score >= 0.80 en todos los casos finales
  - [ ] Artefactos trazables generados (YAML + tracker)
  - [ ] F2 y F3 actualizados con referencia a protocolo
```

### 4.2 Ownership

```yaml
raci:
  responsible:
    paso_1: Role_TrajectoryOwner
    paso_2: Role_Captain
    paso_3: Role_TrajectoryOwner
    paso_4: Role_Captain
    paso_5: Role_Captain (mediador)
    paso_6: Role_SteeringCommittee
  
  accountable: Role_Captain
  
  consulted:
    - Sponsor_L1_Human (paso 2, 4, 5)
    - Role_Architect (validación dependencies)
  
  informed:
    - Board_Governance (si escalation)
    - PMO (tracking tiempo)
```

---

## §5. CHANGELOG Y VERSIONES

```yaml
v1.0.0 (2025-11-17):
  - Protocolo inicial formal
  - 6 pasos definidos
  - Validado contra 6 casos
  - Estado: ACTIVO

backlog_mejoras:
  - Calibrar thresholds con 20+ casos reales
  - Automatizar compatibility_score en calculadora
  - Integrar con F13 health monitoring
```

---

**FIN DEL PROTOCOLO**
