# PARTE I: CONTRATOS CANÓNICOS

Especificación OPERABLE de Primitivos P1–P5

> **Etiquetado Genoma/Fenotipo**: Contratos especifican schemas abstractos (genoma) operacionalizables en múltiples tecnologías (fenotipo):
> - **[GENOMA]** Schemas YAML: Campos base, tipos, multiplicidades, invariantes lógicos
> - **[FENOTIPO]** Implementaciones: SQL/JSON específicos, índices, optimizaciones (ver Layer 2 Tejidos)
> - **[FENOTIPO]** Campos opcionales: Lifecycle details, archetype, metrics derivadas
>
> Ver ../00_fundamentos_teoricos/00_introduccion.md §0.1 para definición completa framework.

- [PARTE I: CONTRATOS CANÓNICOS](#parte-i-contratos-canónicos)
  - [§1. FUNDAMENTOS CONTRACTUALES](#1-fundamentos-contractuales)
  - [§2. CONTRATO C1: CAPACIDAD](#2-contrato-c1-capacidad)
  - [§3. CONTRATO C2: FLUJO](#3-contrato-c2-flujo)
  - [§4. CONTRATO C3: INFORMACIÓN](#4-contrato-c3-información)
  - [§5. CONTRATO C4: LÍMITE](#5-contrato-c4-límite)
  - [§6. CONTRATO C5: PROPÓSITO](#6-contrato-c5-propósito)
  - [§6B. CONTRATO E7: EJECUCIÓN DE FLUJO (G3)](#6b-contrato-e7-ejecución-de-flujo-g3)
  - [§6C. CONTRATO E6: ESTADO ARQUITECTÓNICO (G1)](#6c-contrato-e6-estado-arquitectónico-g1)
  - [§7. MATRIZ DE INTEROPERABILIDAD](#7-matriz-de-interoperabilidad)

## §1. FUNDAMENTOS CONTRACTUALES

**Definición:**
Contrato = Especificación OPERABLE de un primitivo.

**Propósito:**

1. Interoperabilidad entre dominios D1–D4.
2. Type safety (estados inválidos imposibles).
3. Implementabilidad directa (code/DB/UI).
4. Validación automática de invariantes I1–I8.

**Estructura_Canónica:**

- Schema: Campos + tipos + constraints.
- Propiedades_Derivadas: Calculadas desde campos.
- Invariantes: Reglas que DEBEN cumplirse.
- Interfaces: Operaciones por dominio (D1–D4).
- Validación: Función verificable.

## §2. CONTRATO C1: CAPACIDAD

```yaml
Schema:
  id: UUID [NOT NULL, UNIQUE, IMMUTABLE]
  name: String(1..255)
  
  # Clasificación Ontológica
  substrate: {Humano | Algorítmico | Mecánico | Mixto}
  capacity_type: {C0_Ejecutar | C1_Decidir | C2_Reflexionar | C3_Meta_Reflexionar}
  
  # Clasificación Contextual (I4)
  role: {Producción | Habilitación}
  role_context: String  # justificación de la clasificación
  
  # Arquetipo AOC (opcional)
  archetype:
    type: {α_Creador | β_Operador | γ_Conector | δ_Descubridor | ε_Validador} | null
    purity_pct: Float[0..1]  # % de actividades alineadas al arquetipo

  # Composición (si Mixto)
  composition:
    type: {Paralelo | Secuencial | Híbrido}
    component_ids: List<UUID>
    rule: String

  # Ownership (I5: HAIC)
  ownership:
    accountable_id: UUID  # Humano/Mixto únicamente
    delegated_from: UUID | null  # si Algorítmico
    delegation_mode: DelegationMode | null
      # Tipo abstracto representando nivel autonomía algorítmica
      # Valores: Ver I5_[FENOTIPO] en ../00_fundamentos_teoricos/03_invariantes.md §6
      # Espectro: M1_Monitorear → M6_Ejecutar (6 niveles autonomía progresiva)

  # Lifecycle (G11)
  lifecycle:
    current_state: {Planning | Development | Active | Idle | Deprecated | Sunset | Retired}
    state_history: List<{state, entered_at, exited_at, trigger, triggered_by}>
    metrics: {time_active, time_idle, utilization_avg, last_assignment}
    deprecation:
      deprecated_at: Timestamp
      reason: String
      sunset_plan:
        planned_date: Date
        handover_to: UUID
        knowledge_transfer_complete: Boolean
        dependents_notified: Boolean
    retirement:
      retired_at: Timestamp
      reason: String
      archived_documentation: String

  # Trazabilidad (I3)
  created_by: UUID
  created_at: Timestamp
  updated_at: Timestamp
  version: Integer

Invariantes:
  INV_C1: accountable_id.substrate ∈ {Humano, Mixto}
  INV_C2: substrate = Algorítmico → delegated_from NOT NULL
  INV_C3: substrate = Mixto → composition NOT NULL ∧ ∃ componente con substrate = Humano
  INV_C4: substrate = Mecánico → capacity_type = C0
  INV_C5: lifecycle.current_state = Sunset → irreversible
  INV_C6: archetype.type NOT NULL → archetype.purity_pct > 0.80
  INV_C7: incompatibilidades de arquetipo (α↔β, γ↔δ, γ↔ε, δ↔ε) → warning del sistema
  INV_C8: lifecycle.current_state = Retired → terminal (G11)
  
  INV_GOLDEN_RULE:
    description: "Autoridad y Accountability deben coincidir (Golden Rule Meyer)"
    rule: owner.accountability_scope == owner.authority_scope
    OR waiver_id EXISTS
    
    waiver:
      waiver_id: UUID
      rationale: String  # Por qué excepción necesaria
      sponsor: UUID      # Capacity_ID (Humano, C-level)
      expiry: Date       # Fecha revisión obligatoria
      risk_acceptance: String  # Qué puede salir mal y por qué se acepta
      
    enforcement: Preventivo (block en create/update si violado sin waiver)

Interfaces:
  D1_Arquitectura:
    - create(schema) → UUID
    - assign_to_unit(capacity_id, unit_id)
    - set_decision_rights(capacity_id, RACI)
    - calculate_span_of_control(capacity_id) → Integer
    
  D2_Percepción:
    - observe_utilization(capacity_id) → Float[0..1]
    - observe_health(capacity_id) → Metrics
    - detect_bottleneck(capacity_id) → Boolean
    
  D3_Decisión:
    - query_available(filters) → List<UUID>
    - allocate_to_initiative(capacity_id, initiative_id, effort_pct)
    - evaluate_capacity_gap(required, available) → Gap
    
  D4_Operación:
    - utilize(capacity_id, task) → Execution
    - report_output(capacity_id, output)
    - escalate_blocker(capacity_id, description)
```

NOTA ARQUITECTURAL CRÍTICA: Resolución Actor/Agente

```yaml
Decisión_Ontológica:
  "Actor y Agente NO son primitivos separados.
   Son VISTAS del primitivo único P1 (Capacidad)."

Fundamento:
  Derivación: teoría_orko.md §2.5 Parte II (líneas 422–571)
  Invariantes: I1 (Minimalidad) + I2 (Ortogonalidad)
  
Relación_Formal:
  Actor := Vista_Sustrato(Capacidad)
    Pregunta: ¿QUIÉN ejecuta?
    Clasificación: substrate ∈ {Humano, Algorítmico, Mecánico, Mixto}
    
  Agente := Vista_Cognitiva(Capacidad)
    Pregunta: ¿QUÉ nivel de decisión?
    Clasificación: capacity_type ∈ {C0, C1, C2, C3}
    Restricción: Agente ⟺ capacity_type ≥ C1

Implicaciones_Implementación:
  Base_Datos:
    - Tabla única: 'capacity'
    - NO crear 'actor' o 'agent' como tablas separadas
    
  Modelo_Código:
    - Clase base: Capacity
    - Propiedades: substrate + capacity_type
    - NO clases Actor o Agent como entidades
    
  API_Queries:
    - Filtro por sustrato: GET /capacities?substrate=Humano
    - Filtro por cognición: GET /capacities?capacity_type=C1
    - Agentes algorítmicos: GET /capacities?substrate=Algorítmico&capacity_type>=C1

Uso_Conversacional:
  Técnico: "Capacidad C1 algorítmica"
  Informal: "Actor humano" = Capacidad(substrate=Humano)
  Informal: "Agente IA" = Capacidad(substrate=Algorítmico, capacity_type≥C1)
  
Validación:
  ✓ Parsimonia: 1 primitivo vs 3 (navaja de Occam)
  ✓ Ortogonalidad: substrate ⟂ capacity_type (dimensiones independientes)
  ✓ Expresividad: Todos los casos son modelables
  ✓ Coherencia: Trazable al axioma A2
```

## §3. CONTRATO C2: FLUJO

```yaml
Schema:
  id: UUID
  name: String(1..255)
  
  # Clasificación (I4)
  type: {Producción | Habilitación}
  type_context: String
  
  # Estructura DAG
  steps: List<{
    step_id: UUID,
    name: String,
    sequence: Integer,
    capacity_required: {capacity_id, capacity_type_min, effort},
    input_info: List<UUID>,
    output_info: List<UUID>,
    automation_level: {Manual | Assisted | Semiautomático | Automático},
    is_handoff: Boolean
  }>

  dependencies: List<{
    from_step: UUID,
    to_step: UUID,
    type: {Sequential | Prerequisite | Optional}
  }>
  
  # Métricas
  metrics:
    cycle_time_target: Duration
    cycle_time_actual: Duration | null
    throughput_target: Float
    throughput_actual: Float | null
    flow_efficiency: Float[0..1] | null
    handoff_ratio: Float[0..1]  # objetivo < 0.20
  
  # Definición Formal de Handoff (G27)
  handoff_definition: |
    "Handoff = transición step_i → step_j donde:
     1) step_j depende de step_i (secuencia directa)
     2) team_id de step_i.capacity_required ≠ team_id de step_j.capacity_required
     
     Casos especiales:
     - Handoff intra-equipo NO cuenta (mismo team_id)
     - Cross-person dentro del mismo equipo NO es handoff
     - Cola asíncrona SÍ es handoff si es cross-team
     - Pasos en paralelo NO son handoff (sin dependencia)
     
     Cálculo de handoff_ratio:
       handoffs = Σ handoff(step_i, step_i+1) para todos los pares secuenciales
       transitions = COUNT(dependencies en el DAG)
       handoff_ratio = handoffs / transitions"
  
  # Ownership
  owner_capacity_id: UUID  # mínimo C2
  purpose_id: UUID  # todo flujo sirve a un propósito (A5)
  
  status: {Design | Active | Deprecated | Retired}
  created_by: UUID
  created_at: Timestamp

Invariantes:
  INV_F1: dependencies forman un DAG (sin ciclos)
  INV_F2: ∀ dep: from_step, to_step ∈ steps
  INV_F3: ∀ step: capacity_required.capacity_id existe
  INV_F4: purpose_id existe
  INV_F5: owner_capacity.capacity_type ≥ C2

Interfaces:
  D1_Arquitectura:
    - design_flow(schema) → UUID
    - assign_capacity_to_step(flow_id, step_id, capacity_id)
    - calculate_handoff_ratio(flow_id) → Float
    
  D2_Percepción:
    - observe_cycle_time(flow_id) → Duration
    - observe_bottlenecks(flow_id) → List<Step>
    - observe_flow_efficiency(flow_id) → Float[0..1]
    
  D3_Decisión:
    - prioritize_flow_optimization(criteria) → List<UUID>
    - allocate_capacity_to_flows(portfolio) → Allocation
    
  D4_Operación:
    - execute_flow(flow_id, input) → Output
    - report_completion(execution_id, metrics)
    - escalate_blocker_in_flow(flow_id, step_id, blocker)
```

> ACLARACIÓN: Interfaces por dominio
> Las interfaces propuestas son derivaciones lógicas (no están explícitas en la teoría), pero son consistentes con las responsabilidades de cada dominio definidas en §4–§7 Parte IV.

## §4. CONTRATO C3: INFORMACIÓN

```yaml
Schema:
  id: UUID
  name: String(1..255)
  
  # Tipo (unifica Dato + Señal + Estado)
  information_type: {Persistente | Transitoria | Agregada}
  
  # Contenido
  payload:
    schema: JSONSchema
    data: JSON
    encoding: String
    size_bytes: Integer
  
  # Lineage (I3: Trazabilidad)
  lineage:
    produced_by_flow: UUID | null
    produced_by_capacity: UUID | null
    parent_info_ids: List<UUID>  # DAG
    transformation: String | null
    origin: {Internal | External}
    source_ref: String | null  # URL, contrato o referencia de origen
  
  # Temporalidad
  temporal:
    created_at: Timestamp
    valid_from: Timestamp
    valid_until: Timestamp | null
    retention_policy: Duration | null
  
  # Semántica
  semantics:
    domain: String
    tags: List<String>
    sensitivity: {Public | Internal | Confidential | Secret}
  
  # Observable Mapping (16 categorías D2)
  observable_id: {EX1..EX8 | IN1..IN8} | null

  # Calidad
  quality:
    completeness: Float[0..1]
    accuracy: Float[0..1] | null
    timeliness: Float[0..1]
    consistency: Boolean
  
  status: {Active | Archived | Deprecated | Deleted}
  created_by: UUID

Observable_Units_Standard (G30):
  "Especificación de unidades canónicas para 16 observables, para asegurar comparabilidad"
  
  EX1_Demanda: "Pipeline_Value_USD (monthly active pipeline)"
  EX2_Competidores: "Competitor_Activity_Index [0..10]"
  EX3_Regulatorio: "Compliance_Deadlines_Count (próximos 90d)"
  EX4_Tecnológico: "Tech_Risk_Score [0..10]"
  EX5_Feedback: "NPS_Score [-100..100]"
  EX6_Disruptivo: "Disruption_Horizon_Index [0..10]"
  EX7_Social: "Brand_Sentiment_Score [-1..1]"
  EX8_Económico: "Economic_Conditions_Index [0..10]"
  
  IN1_Velocidad: "Lead_Time_Days (p50 commit→prod)"
  IN2_Salud: "eNPS_Score [-100..100]"
  IN3_Eficiencia: "Flow_Efficiency_Ratio [0..1]"
  IN4_Calidad: "Defect_Density o Change_Failure_Rate_%"
  IN5_Utilización: "Capacity_Utilization_Ratio [0..1]"
  IN6_Alineación: "Alignment_Score [0..1] vía Q15"
  IN7_Violaciones: "Severity_Score_Weighted (Σ weight×count)"
  IN8_Debt: "Tech_Debt_Ratio [0..1] (remediation/development cost)"

# Política de Lineage y Origen
Política_Lineage_Origen:
  origin: {Internal | External}
  rules:
    Internal:
      - produced_by_flow != null OR produced_by_capacity != null
    External:
      - produced_by_flow == null
      - source_ref != null  # URL, contrato o referencia de origen
  validator: |
    CHECK (
      (origin = 'Internal' AND (produced_by_flow IS NOT NULL OR produced_by_capacity IS NOT NULL))
      OR (origin = 'External' AND source_ref IS NOT NULL)
    )

Invariantes:
  INV_I1: information_type = Agregada → parent_info_ids.length > 1
  INV_I2: payload.data conforms_to payload.schema
  INV_I3: lineage forma un DAG (sin ciclos)
  INV_I4: sensitivity = Secret → retention_policy NOT NULL

Interfaces:
  D1_Arquitectura:
    - define_information_schema(schema) → UUID
    - set_retention_policy(info_id, policy)
    
  D2_Percepción:
    - capture_observable(observable_id, payload) → UUID
    - aggregate_information(parent_ids, transformation) → UUID
    - observe_freshness(info_id) → Duration
    - observe_quality(info_id) → QualityMetrics
    
  D3_Decisión:
    - query_information(filters) → List<UUID>
    - evaluate_decision_inputs(info_ids) → Sufficiency
    
  D4_Operación:
    - produce_information(flow_id, step_id, payload) → UUID
    - consume_information(capacity_id, info_id)
    - track_lineage(info_id) → DAG
```

## §5. CONTRATO C4: LÍMITE

```yaml
Schema:
  id: UUID
  name: String(1..255)
  
  # Tipo
  limit_type: {Físico | Regulatorio | Organizacional | Económico | Técnico}
  severity: {Info | Warning | Error | Critical}

  # Restricción
  constraint:
    target_entity_type: {Capacidad | Flujo | Información | Propósito}
    target_entity_ids: List<UUID>
    constraint_expression: String  # formal o lenguaje natural
    enforcement: {Preventivo | Detectivo | Correctivo}
    severity: {Info | Warning | Error | Critical}
  
  # Fuente
  source:
    origin: String  # Ley, policy interna, constraint físico
    authority: String  # quién impone
    justification: String
  
  # Compliance (G29: ponderado por severidad)
  compliance:
    violations_count: Integer  # DEPRECATED: usar violations_summary
    last_violation: Timestamp | null
    
    violations: List<{
      violation_id: UUID
      timestamp: Timestamp
      severity:
        level: {Minor | Moderate | Major | Critical}
        magnitude: Float
        magnitude_pct: Float
      impact:
        operational: {Low | Medium | High | Critical}
        financial: Currency
        reputational: {Low | Medium | High | Critical}
        legal_risk: {Low | Medium | High | Critical}
      context:
        detected_by: UUID
        affected_entities: List<{type, id}>
        duration: Duration
      remediation:
        status: {Open | In_Progress | Resolved | Accepted}
        plan: String
        responsible: UUID
        deadline: Date
        resolution_date: Date | null
    }>
    
    violations_summary:
      count_total: Integer
      count_by_severity: {minor: Integer, moderate: Integer, major: Integer, critical: Integer}
      severity_score: Float  # Minor×1 + Moderate×5 + Major×20 + Critical×100
    remediation_required: Boolean
  
  owner_capacity_id: UUID
  status: {Active | Deprecated | Retired}
  created_by: UUID
  created_at: Timestamp

Invariantes:
  INV_L1: ∀ target_id ∈ target_entity_ids → la entidad existe
  INV_L2: enforcement ≠ NULL
  INV_L3: limit_type = Regulatorio → source.authority NOT NULL
  INV_L4: severity = Critical → Preventivo ∈ enforcement

Interfaces:
  D1_Arquitectura:
    - define_limit(schema) → UUID
    - apply_limit_to_entities(limit_id, entity_ids)
    - evaluate_governance_coverage() → Coverage
    
  D2_Percepción:
    - detect_violation(limit_id) → Boolean
    - observe_compliance_rate(limit_id) → Float
    - track_violations(limit_id) → List<Violation>
    
  D3_Decisión:
    - validate_decision_against_limits(decision, limits) → Valid
    - request_exception(limit_id, justification) → Approval
    
  D4_Operación:
    - enforce_limit(limit_id, entity_id) → Enforcement
    - report_violation(limit_id, entity_id, details)
```

## §6. CONTRATO C5: PROPÓSITO

```yaml
Schema:
  id: UUID
  objective: String(1..500)  # cualitativo, inspirador
  
  # Métricas (Key Results con Achievement Criteria, G12)
  key_results: List<{
    kr_id: UUID,
    description: String,
    current_value: Float,
    target_value: Float,
    progress_pct: Float[0..100+],
    unit: String,
    achievement:
      type: {Threshold | Target | Range | Boolean}
      weighting: Float[0..1]
      scoring: {partial_credit: Boolean, overshoot_bonus: Boolean}
  }>  # 2–5 KRs típico, Σ weighting = 1.0
  
  # Jerarquía (G28: fórmula de alineamiento)
  hierarchy:
    parent_purpose_id: UUID | null
    child_purpose_ids: List<UUID>
    alignment_score: Float[0..1]
  
  alignment_score_formula: |
    "SI el propósito es HOJA (sin hijos):
       alignment = AVG(progress_kr_i para i en key_results)
       
     SI el propósito es PADRE (con hijos):
       alignment = Σ(w_i × p_i × c_i) / Σ w_i
       
       Donde:
         w_i = peso del KR relevante del child_i
         p_i = alignment_score de child_i (recursivo)
         c_i = contribution_factor(child_i → parent)
       
     Propiedades: recursiva, ponderada, acotada [0..1], monótona"
  
  # Temporal
  temporal:
    scope: {Individual | Team | Unit | Organization}
    horizon: {Inmediato | Táctico | Estratégico}
    start_date: Date
    end_date: Date
  
  # Ownership (I5)
  ownership:
    owner_capacity_id: UUID  # Humano/Mixto
    status: {Draft | Active | At_Risk | Completed | Abandoned}
  
  created_by: UUID
  created_at: Timestamp
  updated_at: Timestamp

Invariantes:
  INV_P1: parent_purpose_id ≠ null → el parent existe
  INV_P2: ∀ child: child.end_date ≤ this.end_date
  INV_P3: owner_capacity.substrate ∈ {Humano, Mixto}
  INV_P4: key_results.length ∈ [2..5]  # best practice
  INV_P5: hierarchy forma un árbol (sin ciclos)

Interfaces:
  D1_Arquitectura:
    - cascade_purpose(parent_id, child_schema) → UUID
    - validate_alignment(child_id, parent_id) → Alignment
    
  D2_Percepción:
    - observe_progress(purpose_id) → Float[0..100+]
    - detect_at_risk(purpose_id) → Boolean
    - calculate_alignment_score() → Float[0..1]
    
  D3_Decisión:
    - set_okr(schema) → UUID
    - prioritize_by_purpose(purpose_id, initiatives) → Prioritized
    - quarterly_okr_planning() → OKRTree
    
  D4_Operación:
    - update_progress(purpose_id, kr_id, new_value)
    - report_kr_achievement(purpose_id, kr_id, outcome)
```

## §6B. CONTRATO E7: EJECUCIÓN DE FLUJO (G3)

```yaml
Schema:
  id: UUID
  flow_id: UUID  # → Flujo
  
  # Temporal
  started_at: Timestamp
  ended_at: Timestamp | null
  duration: Duration | null  # ended_at - started_at
  
  # Contexto de ejecución
  executed_by_capacity_id: UUID  # → Capacidad
  trigger: {Manual | Scheduled | Event_Driven | Transition}
  trigger_context: JSON  # event payload, schedule config, etc.
  
  # Seguimiento de estado
  status: {In_Progress | Completed | Failed | Cancelled}
  current_step_id: UUID | null  # si In_Progress
  steps_completed: Integer
  steps_total: Integer
  
  # Outputs
  outputs_produced: List<{
    info_id: UUID  # → Información
    step_id: UUID
    produced_at: Timestamp
  }>
  
  # Errores (si Failed)
  failure:
    failed_at: Timestamp
    failed_step_id: UUID
    error_type: {Timeout | Validation | Infrastructure | Business_Logic}
    error_message: String
    stack_trace: String | null
    retry_count: Integer
  
  # Métricas DORA (G4)
  metrics:
    cycle_time: Duration        # ended_at - started_at
    wait_time: Duration         # tiempo esperando dependencias
    active_time: Duration       # tiempo de trabajo efectivo
    handoff_count: Integer
    rework: Boolean             # si es reintento de una falla previa

Invariantes:
  INV_E7.1: status = Completed → ended_at NOT NULL
  INV_E7.2: status = Failed → failure NOT NULL
  INV_E7.3: flow_id existe en Flujo
  INV_E7.4: executed_by_capacity_id.lifecycle.current_state = Active

Interfaces:
  D1_Arquitectura:
    - get_executions_by_flow(flow_id, date_range) → List<E7>
    - analyze_flow_performance(flow_id) → Stats
    
  D2_Percepción:
    - observe_execution_status(execution_id) → Status
    - detect_slow_execution(execution_id, threshold) → Boolean
    - track_cycle_time(flow_id, period) → Duration_p50
    
  D3_Decisión:
    - prioritize_failing_flows() → List<Flujo>
    
  D4_Operación:
    - start_execution(flow_id, trigger_context) → UUID
    - complete_execution(execution_id, outputs)
    - fail_execution(execution_id, error)
    - retry_execution(failed_execution_id) → UUID
```

## §6C. CONTRATO E6: ESTADO ARQUITECTÓNICO (G1)

```yaml
Schema:
  id: UUID
  name: String(1..255)
  
  # Clasificación temporal
  state_type: {Current | Target | Intermediate | Historical}
  effective_date: Date
  valid_until: Date | null
  
  # Snapshot arquitectónico
  snapshot:
    capacities: List<{
      capacity_id: UUID
      lifecycle_state: LifecycleState
      configuration: JSON
    }>
    
    flows: List<{
      flow_id: UUID
      status: FlowStatus
      configuration: JSON
    }>
    
    purposes: List<{
      purpose_id: UUID
      status: PurposeStatus
      hierarchy_position: Path
    }>
    
    limits: List<{
      limit_id: UUID
      active: Boolean
    }>
  
  # Metadata del snapshot
  snapshot_metadata:
    captured_at: Timestamp
    captured_by: UUID  # → Capacidad
    consistency_validated: Boolean
    validation_errors: List<String> | null
  
  # Relación con otros estados
  evolution:
    previous_state_id: UUID | null
    next_state_id: UUID | null
    parent_target_id: UUID | null  # si es estado intermedio
  
  # Métricas del estado
  metrics:
    total_capacities: Integer
    active_capacities: Integer
    total_flows: Integer
    active_flows: Integer
    health_score: Float[0..100]

Invariantes:
  INV_E6.1: state_type = Current → valid_until IS NULL (siempre vigente)
  INV_E6.2: state_type = Target → effective_date > NOW()
  INV_E6.3: el snapshot satisface INV_C1–C8, R1–R13 (consistencia)
  INV_E6.4: evolution forma un DAG (sin ciclos en transiciones de estado)

Interfaces:
  D1_Arquitectura:
    - capture_current_state() → UUID
    - define_target_state(target_date, schema) → UUID
    - plan_intermediate_states(from, to, milestones) → List<UUID>
    
  D2_Percepción:
    - observe_state_delta(state_a, state_b) → Delta
    - calculate_convergence(current, target) → Float[0..1]
    - detect_state_drift(expected, actual) → Drift
    
  D3_Decisión:
    - approve_target_state(state_id) → Approval
    - sequence_intermediates(states) → Timeline
    
  D4_Operación:
    - transition_to_state(state_id) → Execution
    - validate_state_consistency(state_id) → ValidationResult
```

## §7. MATRIZ DE INTEROPERABILIDAD

Resumen_Interfaces: 5 contratos × 4 dominios = 20 interfaces

Tabla:

|             | D1_Arquitectura | D2_Percepción | D3_Decisión | D4_Operación |
| ----------- | --------------- | ------------- | ----------- | ------------ |
| Capacidad   | 4 ops           | 3 ops         | 3 ops       | 3 ops        |
| Flujo       | 3 ops           | 3 ops         | 2 ops       | 3 ops        |
| Información | 2 ops           | 4 ops         | 2 ops       | 3 ops        |
| Límite      | 3 ops           | 3 ops         | 2 ops       | 2 ops        |
| Propósito   | 2 ops           | 3 ops         | 3 ops       | 2 ops        |

Total_Operaciones: 51 interfaces definidas

Propiedad_Cobertura:

- ✓ Todo primitivo tiene operaciones en los 4 dominios.
- ✓ Todo dominio opera sobre los 5 primitivos.
- ✓ Interoperabilidad completa garantizada.
