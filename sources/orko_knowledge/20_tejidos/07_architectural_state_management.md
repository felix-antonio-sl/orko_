# E6: ARCHITECTURAL STATE MANAGEMENT

**Primitivo Base:** Meta-arquitectónico (cruza todos primitivos)  
**Status:** Concern Transversal (como Security, Purpose)  
**Layer:** Arquitectura (Layer 1)

---

## §1. CONCEPTO Y ALCANCE

### §1.1 Definición

```yaml
E6_ArchitecturalState:
  Concepto: "Snapshot completo del sistema en momento dado"
  
  Propósito:
    - Arquitectura evolutiva: Current → Target planning
    - Change management: Transiciones controladas
    - Compliance: Snapshots auditables históricos
    - Rollback: Capacidad volver a estado previo
    - Impact analysis: Diff entre estados
    
  Trazabilidad:
    Layer_1_Arquitectura: E6 (entidad compuesta)
    Cruza: TF1 (capacities), TF2 (flows), TF3 (information)
    Relaciona: Todos primitivos P1-P5, Purpose, Limits
```

### §1.2 Tipos de Estado

```yaml
State_Types:
  
  Current:
    Descripción: "Estado actual del sistema"
    Effective_date: NOW()
    Valid_until: null (siempre vigente)
    Uso: Observabilidad, baseline para planning
    
  Target:
    Descripción: "Estado objetivo futuro"
    Effective_date: Future date
    Valid_until: null (hasta lograrse)
    Uso: North star architecture, roadmap endpoint
    
  Intermediate:
    Descripción: "Hito en ruta Current → Target"
    Effective_date: Milestones dates
    Parent_target_id: UUID(Target state)
    Uso: Roadmap steps, change management incremental
    
  Historical:
    Descripción: "Snapshot pasado (audit trail)"
    Effective_date: Past date
    Valid_until: Superseded date
    Uso: Compliance, rollback, forensics
```

---

## §2. SCHEMA E6 (Entidad Compuesta)

```yaml
ArchitecturalState:
  # Core
  id: UUID
  name: String(1..255)  # e.g., "Q1-2025 Target", "Pre-Migration Baseline"
  description: String
  
  # Clasificación temporal
  state_type: {Current | Target | Intermediate | Historical}
  effective_date: Date
  valid_until: Date | null
  
  # Snapshot arquitectónico
  snapshot:
    # Capacities (TF1)
    capacities: List<{
      capacity_id: UUID,
      name: String,
      capacity_type: {C0 | C1 | C2 | C3},
      substrate: {Humano | Algorítmico | Mecánico | Mixto},
      lifecycle_state: LifecycleState,
      configuration: JSON  # Key config params
    }>
    
    # Flows (TF2)
    flows: List<{
      flow_id: UUID,
      name: String,
      cognitive_level: {C0 | C1 | C2 | Mixed},
      status: FlowStatus,
      configuration: JSON  # Key config params
    }>
    
    # Information Assets (TF3)
    information_summary:
      total_assets: Integer
      by_subdomain: {
        foundation: Integer,
        analytics: Integer,
        semantic: Integer
      }
      storage_size_gb: Float
      quality_score_avg: Float
      
    # Purposes (P5)
    purposes: List<{
      purpose_id: UUID,
      objective: String,
      status: PurposeStatus,
      hierarchy_position: Path,
      progress_pct: Float
    }>
    
    # Limits (P4 / Security)
    limits: List<{
      limit_id: UUID,
      limit_type: LimitType,
      active: Boolean,
      compliance_rate: Float
    }>
    
  # Metadata del snapshot
  snapshot_metadata:
    captured_at: Timestamp
    captured_by: UUID(Capacity.Humano)
    consistency_validated: Boolean
    validation_errors: List<String> | null
    validation_report_url: String | null
    
  # Relación con otros estados
  evolution:
    previous_state_id: UUID | null  # Estado previo
    next_state_id: UUID | null      # Próximo estado planeado
    parent_target_id: UUID | null   # Si es Intermediate, su Target
    
  # Métricas del estado
  metrics:
    # Composition
    total_capacities: Integer
    active_capacities: Integer
    total_flows: Integer
    active_flows: Integer
    total_information_assets: Integer
    total_okrs: Integer
    
    # Health (aggregated from TF1, TF2, TF3)
    health_score: Float[0..100]
    tf1_score: Float[0..100]
    tf2_score: Float[0..100]
    tf3_score: Float[0..100]
    security_score: Float[0..100]
    
    # Convergence (if Target or Intermediate)
    convergence_pct: Float[0..100] | null  # Progress toward target
    
  # Tags & Classification
  tags: List<String>
  criticality: {Low | Medium | High | Critical}
  
  # Ownership
  owner_capacity_id: UUID(Capacity.Humano)
  status: {Draft | Approved | Active | Superseded | Archived}

Invariantes:
  INV_E6.1: state_type = Current → valid_until IS NULL
  INV_E6.2: state_type = Target → effective_date > NOW()
  INV_E6.3: state_type = Intermediate → parent_target_id NOT NULL
  INV_E6.4: Snapshot satisface invariantes I1-I8 del sistema
  INV_E6.5: Evolution forma DAG (no ciclos en transiciones)
  INV_E6.6: ∀ capacity_id, flow_id en snapshot → existen en sistema
```

---

## §3. OPERACIONES CORE

### §3.1 Capture Current State

```yaml
Operation: capture_current_state()
  
  Description: "Captura snapshot estado actual sistema"
  
  Algorithm:
    1. Query TF1.list_all_capacities()
       - Include: lifecycle_state, key config
       - Filter: Active + Deprecated (exclude Retired)
       
    2. Query TF2.list_all_flows()
       - Include: status, cognitive_level, key config
       - Filter: Active + Paused (exclude Retired)
       
    3. Query TF3.catalog_summary()
       - Count by subdomain
       - Calculate quality_score_avg
       - Sum storage_size
       
    4. Query Purpose.list_all_okrs()
       - Include: hierarchy, progress
       
    5. Query Security.list_active_limits()
       - Include: compliance_rate
       
    6. Calculate metrics:
       - Aggregate TF1_Score, TF2_Score, TF3_Score
       - Compute health_score = weighted_avg(TF scores)
       
    7. Validate consistency:
       - Check all IDs exist
       - Validate I1-I8 compliance
       
    8. Create ArchitecturalState:
       - state_type = Current
       - effective_date = NOW()
       - snapshot = aggregated data
       
  Output: UUID(ArchitecturalState)
  
  Use_Cases:
    - Baseline before major change
    - Audit snapshot (monthly, quarterly)
    - Input for target state planning
```

### §3.2 Define Target State

```yaml
Operation: define_target_state(target_date, changes)
  
  Description: "Define estado objetivo futuro del sistema"
  
  Input:
    target_date: Date (3-12 months futuro típico)
    changes: {
      capacities_to_add: List<CapacitySpec>,
      capacities_to_remove: List<UUID>,
      flows_to_add: List<FlowSpec>,
      flows_to_modify: List<{flow_id, changes}>,
      okrs_target: List<{okr_id, target_progress}>,
      quality_targets: {tf1_score, tf2_score, tf3_score}
    }
    
  Algorithm:
    1. Start from current state snapshot
    
    2. Apply changes:
       - Add new capacities to snapshot
       - Remove deprecated capacities
       - Add/modify flows
       - Update OKR targets
       
    3. Validate target state:
       - Check dependencies (flows use existing capacities)
       - Validate I1-I8 compliance
       - Check feasibility (resources, timeline)
       
    4. Calculate target metrics:
       - Projected health_score
       - Projected TF scores
       
    5. Create ArchitecturalState:
       - state_type = Target
       - effective_date = target_date
       - snapshot = projected state
       - evolution.previous_state_id = current_state_id
       
  Output: UUID(ArchitecturalState)
  
  Use_Cases:
    - Quarterly architecture planning
    - Strategic roadmap (12-24 months)
    - Investment justification (current vs target value)
```

### §3.3 Plan Intermediate States

```yaml
Operation: plan_intermediate_states(current_id, target_id, milestones)
  
  Description: "Planifica estados intermedios en ruta Current → Target"
  
  Input:
    current_id: UUID(ArchitecturalState, type=Current)
    target_id: UUID(ArchitecturalState, type=Target)
    milestones: List<{date, name, priorities}>
    
  Algorithm:
    1. Calculate delta:
       delta = diff(current.snapshot, target.snapshot)
       
    2. Prioritize changes:
       - Critical dependencies first
       - High-value, low-effort early
       - Risky changes with buffers
       
    3. Distribute changes across milestones:
       FOR EACH milestone:
         - Assign subset of changes
         - Ensure dependencies met
         - Balance workload
         
    4. Create intermediate states:
       FOR EACH milestone:
         - state_type = Intermediate
         - effective_date = milestone.date
         - parent_target_id = target_id
         - snapshot = cumulative changes
         - calculate convergence_pct
         
    5. Link evolution chain:
       current → intermediate_1 → ... → intermediate_n → target
       
  Output: List<UUID(ArchitecturalState)>
  
  Use_Cases:
    - Agile roadmap (sprints, quarters)
    - Change management (phased rollout)
    - Risk mitigation (incremental validation)
```

### §3.4 Calculate Convergence

```yaml
Operation: calculate_convergence(current_id, target_id)
  
  Description: "Mide qué tan cerca estamos del target state"
  
  Algorithm:
    1. Load states:
       current = get_state(current_id)
       target = get_state(target_id)
       
    2. Calculate component convergence:
       
       capacities_conv = (
         capacities_implemented / capacities_planned
       ) × 100
       
       flows_conv = (
         flows_implemented / flows_planned
       ) × 100
       
       quality_conv = AVG(
         current.tf1_score / target.tf1_score,
         current.tf2_score / target.tf2_score,
         current.tf3_score / target.tf3_score
       ) × 100
       
       okr_conv = AVG(
         okr.current_progress / okr.target_progress
       ) × 100
       
    3. Aggregate convergence:
       convergence_pct = weighted_avg(
         capacities_conv × 30%,
         flows_conv × 30%,
         quality_conv × 25%,
         okr_conv × 15%
       )
       
  Output: Float[0..100]
  
  Interpretation:
    0-25%: Early stage, major work ahead
    25-50%: Progressing, foundation laid
    50-75%: Advancing, most components in place
    75-90%: Near completion, polishing
    90-100%: Target achieved
```

### §3.5 Transition to State

```yaml
Operation: transition_to_state(state_id)
  
  Description: "Ejecuta transición a estado (Intermediate o Target)"
  
  Input:
    state_id: UUID(ArchitecturalState, type=Intermediate|Target)
    
  Algorithm:
    1. Load target state
    
    2. Calculate required changes:
       delta = diff(current_state, target_state)
       
    3. Generate change plan:
       plan = {
         capacities_to_deploy: [...],
         flows_to_activate: [...],
         configurations_to_update: [...],
         validations_to_run: [...]
       }
       
    4. Execute changes (orchestrated):
       FOR EACH change IN plan:
         - Execute change (TF1, TF2, or TF3 operation)
         - Validate result
         - Record outcome
         - IF failure: Rollback, alert, escalate
         
    5. Validate new state:
       - Capture actual state
       - Compare vs expected (target_state)
       - Calculate convergence
       
    6. Update state lifecycle:
       - IF convergence > 95%:
           target_state.status = Active
           Create new Current state snapshot
       - ELSE:
           Log discrepancies
           Plan remediation
           
  Output: {
    success: Boolean,
    convergence_achieved: Float,
    changes_applied: Integer,
    changes_failed: Integer,
    issues: List<String>
  }
  
  Use_Cases:
    - Milestone deployment
    - Quarterly architecture refresh
    - Post-change validation
```

---

## §4. INTEGRACIÓN CON TEJIDOS

### §4.1 TF1 Capacity

```yaml
E6 → TF1:
  capture_state():
    TF1.list_all_capacities() → E6.snapshot.capacities
    
  define_target():
    New capacities specs → E6.snapshot.capacities (projected)
    
  transition_to_state():
    E6.delta.capacities_to_add → TF1.deploy_capacity()
    E6.delta.capacities_to_remove → TF1.deprecate_capacity()

TF1 → E6:
  Capacity lifecycle changes trigger:
    - Recalculate E6.Current convergence
    - Update E6.metrics.active_capacities
```

### §4.2 TF2 Flow

```yaml
E6 → TF2:
  capture_state():
    TF2.list_all_flows() → E6.snapshot.flows
    
  transition_to_state():
    E6.delta.flows_to_activate → TF2.activate_flow()
    E6.delta.flows_to_pause → TF2.pause_flow()

TF2 → E6:
  Flow status changes trigger:
    - Update E6.Current snapshot
    - Recalculate convergence if Target exists
```

### §4.3 TF3 Information

```yaml
E6 → TF3:
  capture_state():
    TF3.catalog_summary() → E6.snapshot.information_summary
    
  Quality targets:
    E6.Target.quality_score_avg → TF3 quality improvement OKRs

TF3 → E6:
  Quality score changes:
    - Update E6.Current.metrics.tf3_score
    - Contribute to E6.convergence calculation
```

---

## §5. USE CASES

### Use Case 1: Quarterly Architecture Planning

```yaml
Scenario: "Q1 planning: Define target architecture para Q2"

Steps:
  1. capture_current_state()
     Output: state_q1_baseline
     
  2. Architect workshop:
     - Review current state (health_score, gaps)
     - Define Q2 goals (OKRs)
     - List required changes (new capacities, flows)
     
  3. define_target_state(
       target_date = "2025-06-30",
       changes = {
         capacities_to_add: [llm_agent_prod, analytics_ml_model],
         flows_to_add: [multi_agent_research, ml_retraining_pipeline],
         quality_targets: {tf2_score: 85, tf3_score: 80}
       }
     )
     Output: state_q2_target
     
  4. plan_intermediate_states(
       current = state_q1_baseline,
       target = state_q2_target,
       milestones = [
         {date: "2025-04-30", name: "Sprint 3 End"},
         {date: "2025-05-31", name: "Sprint 6 End"}
       ]
     )
     Output: [state_q2_sprint3, state_q2_sprint6]
     
  5. Track progress:
     Weekly: calculate_convergence(current, target)
     Dashboard: Convergence trend, blockers

Result: Transparent roadmap con hitos validables
```

### Use Case 2: Major Migration Rollback

```yaml
Scenario: "Migration to new platform failed, rollback required"

Steps:
  1. Pre-migration:
     state_pre_migration = capture_current_state()
     (Captured automatically before change)
     
  2. Migration executed:
     transition_to_state(state_post_migration_target)
     Result: Partial success, critical issues
     
  3. Rollback decision:
     Architect approves rollback to pre_migration state
     
  4. Execute rollback:
     transition_to_state(state_pre_migration)
     
     Algorithm:
       - Compare current vs pre_migration
       - Revert capacity configurations
       - Reactivate old flows
       - Rollback data migrations (TF3)
       
  5. Validate rollback:
     state_post_rollback = capture_current_state()
     convergence = calculate_convergence(
       state_post_rollback,
       state_pre_migration
     )
     Expected: convergence > 95%

Result: System restored to known-good state
```

### Use Case 3: Compliance Audit

```yaml
Scenario: "SOC2 audit requires architectural snapshots"

Steps:
  1. Historical snapshots:
     Query: get_states_by_date_range(
       start = "2024-01-01",
       end = "2024-12-31",
       type = Current
     )
     Output: 12 monthly snapshots
     
  2. Evidence generation:
     FOR EACH snapshot:
       - Export snapshot.capacities (who had access)
       - Export snapshot.limits (what controls active)
       - Export security_score history
       
  3. Compliance validation:
     Check: security_score ≥ 80 for all months
     Check: limits.compliance_rate ≥ 95%
     Check: snapshot_metadata.consistency_validated = true
     
  4. Audit report:
     - Timeline visualization (snapshots over time)
     - Security posture evolution
     - Change history (state transitions)

Result: Complete audit trail with evidence
```

---

## §6. MÉTRICAS E6

```yaml
E6_Health_Metrics:
  
  Snapshot_Quality:
    consistency_validated: Boolean
    validation_errors_count: Integer
    completeness_pct: (Fields_populated / Total_fields) × 100
    
  Evolution_Quality:
    convergence_pct: Float[0..100]  # If Target/Intermediate
    convergence_velocity: Δconvergence / Δtime  # Points per week
    planned_vs_actual_delta: Diff(planned_state, actual_state)
    
  Usage_Metrics:
    snapshots_per_quarter: Integer
    avg_time_to_target: Duration (historical)
    rollback_frequency: Count / total_transitions
    
Alerts:
  - Convergence_Stalled: velocity < threshold for 4 weeks
  - Target_At_Risk: convergence < 50% AND < 30 days to deadline
  - Validation_Failures: consistency_validated = false
  - Drift_Detected: actual diverges > 20% from expected
```

---

## §7. STORAGE & TOOLING

```yaml
Storage:
  Primary: Database (PostgreSQL, DynamoDB)
    - ArchitecturalState records
    - Indexed by: type, effective_date, status
    
  Snapshots: Object storage (S3, GCS)
    - Full JSON snapshots
    - Compression: gzip
    - Retention: 7 years (compliance)
    
  Lineage: Graph database (Neo4j optional)
    - State evolution DAG
    - Query: path(current → target)

Tooling:
  CLI:
    - `orko state capture`
    - `orko state define-target --date 2025-Q2`
    - `orko state convergence --current <id> --target <id>`
    
  UI:
    - State timeline visualization
    - Diff viewer (state A vs B)
    - Convergence dashboard
    - Roadmap Gantt chart
    
  API:
    - REST: `/api/v1/architectural-states`
    - GraphQL: Flexible state queries
```

---

**Status:** ✅ E6 especificado como concern transversal con integración completa TF1-TF3
