# INTEGRACIÓN ENTRE TEJIDOS

**Objetivo:** Patterns de composición TF1 ↔ TF2 ↔ TF3 con trazabilidad end-to-end

---

## §1. PRINCIPIOS DE INTEGRACIÓN

```yaml
P1_Loose_Coupling:
  "Tejidos integran via contratos (interfaces), no implementación"
  Mechanism: UUID references, API contracts, event-driven
  
P2_High_Cohesion:
  "Cada tejido contiene funcionalidad completa de su dominio"
  Anti-Pattern: Lógica TF1 dispersa en TF2, TF3
  
P3_Explicit_Dependencies:
  "Dependencias declaradas en contracts (used_by, consumes, produces)"
  Benefit: Lineage completo, impact analysis
  
P4_Event_Driven:
  "Tejidos reaccionan a eventos, no polling"
  Pattern: Pub/Sub, message queues, webhooks
  
P5_Idempotency:
  "Operaciones cross-tejido re-ejecutables sin efectos duplicados"
  Mechanism: Idempotency keys, upserts, transaction IDs
```

---

## §2. PATTERNS DE INTEGRACIÓN

### §2.1 TF1 → TF2: Capacidades Ejecutan Flujos

```yaml
Pattern: Capacity_Assignment
  
  Description:
    "Cada step en Flow requiere Capacity que lo ejecute"
    
  Contract_Link:
    Flow.steps[i].capacity_id → Capacity.id
    
  Validation:
    - Capacity.lifecycle.current_state = Active
    - Capacity.capacity_type compatible con step complexity
    - Capacity.availability > 0 (no idle indefinidamente)
    
  Runtime:
    1. Flow orchestrator query Capacity availability
    2. If available: Assign step to Capacity
    3. Capacity executes, returns result
    4. Flow continues to next step
    
  Error_Handling:
    - If Capacity unavailable: Retry con backoff OR escalate HITL
    - If Capacity fails: Circuit breaker, compensation
    
Example_ETL:
  Flow: "ETL_Daily"
  Steps:
    - Extract: capacity="cap-db-connector" (C0)
    - Transform: capacity="cap-dbt-runner" (C0)
    - Load: capacity="cap-warehouse-writer" (C0)
```

### §2.2 TF2 ← TF3: Información Trigger Flujos

```yaml
Pattern: Event_Triggered_Flow
  
  Description:
    "Cambios en Information assets trigger Flow executions"
    
  Triggers:
    - New_File: S3 event → Flow(process_file)
    - Threshold_Exceeded: Metric > limit → Flow(alert_ops)
    - Freshness_SLA_Miss: Data stale → Flow(refresh_pipeline)
    - Quality_Degradation: Quality < 90 → Flow(investigate_root_cause)
    
  Implementation:
    Event_Source: TF3 (CloudWatch, Kafka, custom events)
    Event_Consumer: TF2 orchestrator (Airflow, Temporal)
    
  E7_Logging_Obligatorio:
    - trigger_context: JSON con event payload (e.g., {file_path, size, timestamp})
    - FlowExecution.id: UUID único de la ejecución
    - trigger: "Event_Driven"
    - Almacenamiento: TF2.FlowAsset.execution_history.executions
    - Trazabilidad: Permite auditar "qué evento disparó qué ejecución"
    
Example_ML_Retraining:
  Trigger: TF3.drift_detected = true
  Flow: "Retrain_Churn_Model"
  Steps:
    1. Extract_Training_Data (TF3.Foundation)
    2. Retrain_Model (TF1.Algorithmic_Capacity)
    3. Evaluate_Performance (TF2.validation)
    4. Deploy_If_Better (TF1.model_serving)
```

### §2.3 TF2 → TF3: Flujos Producen Información

```yaml
Pattern: Flow_Produces_Information
  
  Description:
    "Flow execution generates/transforms Information assets"
    
  Contract_Link:
    Flow.produces_information → [InformationAsset_IDs]
    
  Lineage:
    InformationAsset.lineage.produced_by_flow → Flow.id
    InformationAsset.lineage.parent_assets → Input InformationAssets
    
Example_Feature_Engineering:
  Flow: "Generate_Features_Daily"
  Consumes: ["info-raw-transactions", "info-customer-master"]
  Steps:
    1. Join_Data (capacity: SQL engine)
    2. Aggregate_Features (capacity: Spark)
    3. Validate_Quality (capacity: Great Expectations)
  Produces: "info-feature-store-daily"
  
  Lineage_Trace:
    info-raw-transactions → Flow(Generate_Features) → info-feature-store-daily
    info-customer-master → Flow(Generate_Features) → info-feature-store-daily
```

### §2.4 TF1 ← TF3: Información Alimenta Capacidades

```yaml
Pattern: Data_Feeds_Capacity
  
  Description:
    "Information assets son inputs para Capacities (training, context)"
    
  Use_Cases:
    
    ML_Training:
      TF3.Foundation (training dataset)
        → TF1.Algorithmic_Capacity (trained model)
      
      Steps:
        1. TF3: Prepare training data (Bronze → Silver → Gold)
        2. TF1: Train model on TF3.Gold dataset
        3. TF1: Deploy model as Capacity
        4. TF2: Use Capacity in prediction flows
        
    RAG_Context:
      TF3.Semantic (knowledge base)
        → TF1.Algorithmic_Capacity (LLM agent with RAG)
      
      Steps:
        1. TF3: Index documents (chunking, embedding)
        2. TF2: Query flow receives user question
        3. TF3: Retrieve relevant chunks (hybrid search)
        4. TF1: LLM agent generates answer with context
        5. TF2: Return answer with citations
        
Example_Churn_Prediction:
  Information: "info-customer-features-gold"
    - Schema: [customer_id, tenure, monthly_charges, ...]
    - Quality: 98% complete, 99% accurate
    
  Capacity: "cap-churn-model"
    - Type: Algorithmic, C1_Decidir
    - Training: Trained on info-customer-features-gold
    - Performance: 89% accuracy, 87% precision
    
  Flow: "Predict_Churn_Daily"
    - Step1: Load features (TF3)
    - Step2: Predict (TF1.cap-churn-model)
    - Step3: Save predictions (TF3)
```

### §2.5 Ciclo Completo: TF3 → TF1 → TF2 → TF3

```yaml
Pattern: ML_Lifecycle_Loop
  
  Description:
    "Ciclo completo ML: Data → Model → Inference → Feedback → Retrain"
    
  Phases:
    
    Phase_1_Training:
      TF3.Foundation: Prepare training data
        ↓
      TF2.Flow: Orchestrate training pipeline
        ↓
      TF1.Capacity: Train ML model
        ↓
      TF1.Capacity: Deploy model as serving endpoint
      
    Phase_2_Inference:
      TF3.Foundation: New data arrives
        ↓
      TF2.Flow: Feature engineering pipeline
        ↓
      TF3.Foundation: Features ready
        ↓
      TF2.Flow: Prediction pipeline
        ↓
      TF1.Capacity: Model inference
        ↓
      TF3.Foundation: Store predictions
      
    Phase_3_Monitoring:
      TF3.Analytics: Monitor model performance
        ↓
      TF1.Trajectory: Drift detection
        ↓
      IF drift_detected:
        ↓
      TF2.Flow: Trigger retraining (back to Phase_1)
      
Example_Fraud_Detection:
  1. TF3: Historical transactions (Bronze → Silver → Gold)
  2. TF2: Training flow orchestrates
  3. TF1: Fraud model trained, deployed
  4. TF3: New transaction arrives
  5. TF2: Feature eng flow prepares features
  6. TF1: Model predicts fraud_score
  7. TF2: If score > 0.90 → Flag for review (HITL)
  8. TF3: Store prediction + human feedback
  9. TF1: Trajectory monitors accuracy
  10. IF accuracy drops → TF2: Retrain flow triggered
```

---

## §3. CASOS DE USO END-TO-END

### §3.1 RAG Pipeline Completo

```yaml
Use_Case: "Customer Support Chatbot con RAG"

Componentes:
  TF3.Semantic:
    - info-support-docs (knowledge base)
    - Indexed: Vector + BM25
    - Vigencia: Reviewed cada 90 días
    
  TF1.Capacity:
    - cap-embedding-model (text-embedding-ada-002)
    - cap-llm-agent (gpt-4-turbo with RAG)
    
  TF2.Flow:
    - flow-rag-qa (orchestration)

Flow_Steps:
  1. User_Query:
     Input: "How do I reset my password?"
     
  2. Embed_Query (TF1):
     Capacity: cap-embedding-model
     Output: [0.123, -0.456, ...] (vector)
     
  3. Retrieve_Context (TF3):
     Query: Hybrid search (BM25 + vector)
     Top-K: 5 chunks
     Assets: info-support-docs
     Output: [
       {chunk: "Password reset: Go to Settings...", score: 0.92},
       {chunk: "If locked out, contact admin...", score: 0.85},
       ...
     ]
     
  4. Generate_Answer (TF1):
     Capacity: cap-llm-agent
     Prompt: System + User_Query + Retrieved_Context
     Guardrails:
       - Citations required
       - Faithfulness check
       - Max cost $0.10
     Output: {
       answer: "To reset password, go to Settings > Security...",
       citations: ["doc-123#section-4", "doc-456#section-2"]
     }
     
  5. HITL_Check (TF2):
     Condition: confidence < 0.75
     Action: Escalate to human agent
     
  6. Log_Interaction (TF3):
     Store: Query, answer, citations, feedback
     Purpose: Trajectory learning, knowledge gap detection
     
Trazabilidad:
  User_Query
    → TF2.flow-rag-qa
    → TF1.cap-embedding-model (embed query)
    → TF3.info-support-docs (retrieve chunks)
    → TF1.cap-llm-agent (generate answer)
    → TF3.info-interactions-log (store feedback)
    → TF1.Trajectory (improve over time)

E7_Execution_Tracking:
  FlowExecution.id: "exec-rag-20250111-001"
  trigger: "Manual" (user query)
  trigger_context: {user_id: "usr-123", query: "How do I reset...", timestamp: "..."}
  status: "Completed"
  outputs_produced: ["info-interactions-log#entry-456"]
  metrics: {cycle_time: 2.3s, llm_cost: $0.04, confidence: 0.87}
```

### §3.2 Automated Deployment Pipeline

```yaml
Use_Case: "CI/CD con Quality Gates y Rollback"

Componentes:
  TF2.Flow: flow-cicd-pipeline
  TF1.Capacities:
    - cap-build-runner (C0)
    - cap-test-suite (C0)
    - cap-security-scanner (C1)
    - cap-deploy-agent (C0)
  TF3.Information:
    - info-code-repo (source)
    - info-test-results (analytics)
    - info-deployment-logs (audit)

Flow_Steps:
  1. Trigger:
     Event: Git push to main
     Source: TF3.info-code-repo
     E7: trigger="Event_Driven", trigger_context={commit_sha: "abc123", author: "dev@...",...}
     
  2. Build (TF1):
     Capacity: cap-build-runner
     Input: Source code
     Output: Docker image
     Timeout: 300s
     
  3. Test (TF1):
     Capacity: cap-test-suite
     Input: Docker image
     Output: Test results (pass/fail, coverage %)
     Quality_Gate: coverage > 80% AND all_tests_pass
     
  4. Security_Scan (TF1):
     Capacity: cap-security-scanner (ML-based CVE detection)
     Input: Docker image
     Output: Vulnerabilities (critical, high, medium, low)
     Quality_Gate: critical_vulns = 0
     
  5. HITL_Approval (TF2):
     Condition: production deployment
     Human: Engineering Manager
     Timeout: 4 hours
     
  6. Deploy (TF1):
     Capacity: cap-deploy-agent
     Strategy: Blue-green (zero downtime)
     Rollback_Trigger: error_rate > 5% within 5 min
     
  7. Monitor (TF3):
     Metrics: Latency, error_rate, throughput
     Alert: If degradation → Auto-rollback (TF2 compensation)
     
  8. Log (TF3):
     Store: Deployment event, approver, results
     Purpose: Audit, DORA metrics
     
Compensation (si falla):
  - Step 6 fails: Rollback to previous blue env
  - Error_rate spike: Auto-rollback within 60s
  - Quality_gate fail: Block deployment, notify team

Trazabilidad:
  Git_Commit
    → TF2.flow-cicd
    → TF1.cap-build-runner (build)
    → TF1.cap-test-suite (test)
    → TF1.cap-security-scanner (scan)
    → HITL_Approval (human)
    → TF1.cap-deploy-agent (deploy)
    → TF3.info-deployment-logs (audit)
```

### §3.3 Multi-Agent Research Synthesis

```yaml
Use_Case: "AI Research Team genera reporte ejecutivo"

Componentes:
  TF1.Capacities:
    - cap-manager-agent (C2, coordinator)
    - cap-research-agent (C1, web search + RAG)
    - cap-writer-agent (C1, content generation)
    - cap-critic-agent (C1, quality review)
    
  TF2.Flow: flow-multi-agent-research
    Pattern: Hierarchical orchestration
    
  TF3.Information:
    - info-web-search-results (semantic)
    - info-internal-knowledge (semantic)
    - info-draft-report (output)

Flow_Steps:
  1. Manager_Decompose (TF1):
     Capacity: cap-manager-agent
     Input: "Research AI trends in fintech"
     Output: Sub-tasks [
       "Search recent papers",
       "Query internal case studies",
       "Synthesize findings"
     ]
     
  2. Parallel_Research (TF2):
     Step_2a: Research_Web (TF1.cap-research-agent)
       - Tool: Web search API
       - Output: TF3.info-web-search-results
       - Budget: $3, Timeout: 180s
       
     Step_2b: Research_Internal (TF1.cap-research-agent)
       - Tool: RAG on TF3.info-internal-knowledge
       - Output: Retrieved chunks
       - Budget: $2, Timeout: 120s
       
  3. Writer_Draft (TF1):
     Capacity: cap-writer-agent
     Input: Research results (Step 2a + 2b)
     Output: TF3.info-draft-report (v1)
     Guardrails: Min 1000 words, citations required
     
  4. Critic_Review (TF1):
     Capacity: cap-critic-agent
     Input: TF3.info-draft-report (v1)
     Criteria: [Clarity, Completeness, Citations, Structure]
     Output: Feedback + Pass/Fail
     
  5. Refinement_Loop (TF2):
     IF critic_pass = false:
       Manager asks Writer to revise (max 3 iterations)
     ELSE:
       Proceed to Step 6
       
  6. HITL_Final_Review (TF2):
     Human: Domain Expert (TF1.Capacity.Humano, C3)
     Input: TF3.info-draft-report (final)
     Actions: Approve | Request Changes | Reject
     
  7. Publish (TF3):
     IF approved:
       Store: TF3.info-executive-reports
       Notify: Stakeholders via email (TF2.notification-flow)
       
Bounded_Autonomy:
  - Manager: M5 (co-execute with human oversight)
  - Workers: M4 (auto-execute, escalate if confidence < 0.70)
  - Critic: M3 (human invokes, agent reviews)
  - Final approval: Always human (I5_HAIC)
  
Guardrails_Total:
  - Max_Budget: $15 (all agents combined)
  - Max_Iterations: 3 (refinement loop)
  - Max_Time: 30 minutes
  - Required_Citations: ≥5 sources
  
Trazabilidad:
  User_Request
    → TF1.cap-manager-agent (decompose)
    → TF1.cap-research-agent (gather info from TF3)
    → TF1.cap-writer-agent (generate draft)
    → TF1.cap-critic-agent (review quality)
    → TF2.refinement-loop (iterate if needed)
    → HITL.domain-expert (final approval)
    → TF3.info-executive-reports (publish)
```

---

## §4. MATRIZ DE INTEGRACIÓN

```yaml
Integration_Matrix:
  
  TF1 → TF2:
    Pattern: Capacity assignment to Flow steps
    Frequency: Every flow execution (high)
    Mechanism: UUID reference Flow.step.capacity_id → Capacity.id
    
  TF2 → TF1:
    Pattern: Flow utilization metrics update Capacity
    Frequency: Post-execution (high)
    Mechanism: Callback Capacity.trajectory.total_executions++
    
  TF1 ← TF3:
    Pattern: Information feeds Capacity (training, context)
    Frequency: Training (low), RAG query (high)
    Mechanism: Capacity reads InformationAsset via TF3 APIs
    
  TF3 → TF1:
    Pattern: Information asset changes trigger Capacity updates
    Frequency: Medium (drift detection, retraining)
    Mechanism: Events InformationAsset.quality_degraded → Capacity.retrain
    
  TF2 ← TF3:
    Pattern: Information events trigger Flows
    Frequency: High (event-driven pipelines)
    Mechanism: Events (S3, Kafka) → Flow.trigger
    
  TF3 ← TF2:
    Pattern: Flows produce Information
    Frequency: Very high (every pipeline)
    Mechanism: Flow writes InformationAsset, updates lineage
    
Cross-Cutting:
  Security (P4):
    - Access control on ALL interactions
    - Audit logs for cross-tejido calls
    
  Purpose (P5):
    - OKR linkage propagates across tejidos
    - H_org aggregates metrics from TF1, TF2, TF3
```

---

## §5. ANTI-PATTERNS INTEGRACIÓN

```yaml
AP_INT_01_Tight_Coupling:
  Problem: "TF2 Flow hardcodes TF1 Capacity implementation details"
  Fix: "Interact via contracts, not internals"
  
AP_INT_02_Circular_Dependencies:
  Problem: "TF1 depends on TF2, TF2 depends on TF1 → deadlock"
  Fix: "Event-driven decoupling, async communication"
  
AP_INT_03_No_Lineage:
  Problem: "Information flows between tejidos sin trazabilidad"
  Fix: "Always update lineage: produced_by_flow, consumed_by"
  
AP_INT_04_Synchronous_Blocking:
  Problem: "TF2 Flow waits synchronously for TF1 Capacity (slow)"
  Fix: "Async patterns: callbacks, promises, pub/sub"
  
AP_INT_05_No_Compensation:
  Problem: "TF2 Flow falla mid-execution, no rollback"
  Fix: "Saga pattern, compensation steps defined"
  
AP_INT_06_Unbounded_Costs:
  Problem: "Cross-tejido calls sin budget limits"
  Fix: "Guardrails on ALL integrations (P4.Límite)"
```

---

## §6. GOVERNANCE INTEGRACIÓN

```yaml
Change_Management:
  Contract_Versioning:
    - Breaking changes: Major version bump (v1 → v2)
    - Backwards compatible: Minor version (v1.0 → v1.1)
    - Deprecation: 90 days notice, migration guide
    
  Impact_Analysis:
    Tool: Lineage graph (TF3.governance.lineage)
    Query: "Which Flows use this Capacity?"
    Output: List<Flow_IDs> → Notify owners before change
    
  Testing:
    Integration_Tests: Test cross-tejido interactions
    Contract_Tests: Validate schemas (Pact, OpenAPI)
    End-to-End_Tests: Full use case flows
    
Monitoring:
  Cross-Fabric_Observability:
    Traces: Distributed tracing (Jaeger, Tempo)
    Metrics: Latency, error_rate per integration point
    Alerts: SLA violations on cross-tejido calls
    
  SLA_Enforcement:
    TF1 → TF2: Capacity response_time < 5s (P95)
    TF2 ← TF3: Event delivery latency < 1s
    TF3 → TF1: Data freshness < 1h (for RAG)
```

---

**Status:** ✅ Integration patterns documentados con casos de uso end-to-end
