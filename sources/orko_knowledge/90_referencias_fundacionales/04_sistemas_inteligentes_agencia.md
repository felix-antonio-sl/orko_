# Sistemas Inteligentes y Agencia

**ID**: ORKO-REF-SIA-01  
**Versión**: 1.1.0  
**Última actualización**: 2025-01-13  
**Changelog 1.1.0**: Agregado §12 (Modelo Unificado Agencia Algorítmica, taxonomía 4 arquetipos)  
**Fuentes**: TSTI Axiomática, AIHC (Human-Centered AI)  

---

## §1. CICLO SADE (Situation Awareness-Decision-Execution)

### Estructura Tripartita

```
SADE := ⟨SENSE, DECIDE, EXECUTE⟩

SENSE := {L1_Detect, L2_Comprehend, L3_Project}
DECIDE := {M1_DirectControl, M2_RuleBased, M3_Associative, M4_KnowledgeBased}
EXECUTE := {E1_Action, E2_Specification, E3_Planning, E4_Orchestration}
```

### Fase 1: Situation Awareness (Endsley)

**L1. Detect**: Identificar/detectar nuevo fact o event

**L2. Comprehend**: Entender, interpretar, sintetizar (reconocer patterns/anomalies)

**L3. Project**: Predecir, forecast events futuros

### Fase 2: Decision-making (Rasmussen levels)

**M1. Direct Control Loops**: Información → acción directa (feedback loop algorítmico)

- Ex: Mantener temperatura en rango

**M2. Rule-Based**: Reconocer condiciones → mapear a acciones predefinidas

- Ex: IF temp > threshold THEN activate cooling

**M3. Associative Mapping**: Heurística experta, fuzzy similarity con patrones pasados

- Naturalística (NDM), instintiva, basada en experiencia

**M4. Knowledge-Based**: Análisis iterativo, investigación, planning, simulation

- Causal analysis, generación decision options, comparación outcomes

### Fase 3: Execution

**E1. Action**: Implementación directa

**E2. Specification**: Detalle de acciones a nivel operacional

**E3. Planning**: Secuencia, recursos, timing

**E4. Orchestration**: Coordinación multi-agente

---

## §2. SMARTNESS Y CAPACIDADES

### Capacidades (23 subcapacidades)

**C1. Procesamiento Información** (7 subcaps)

**C2. Acción en Mundo** (6 subcaps)

**C3. Regulación Interna** (5 subcaps)

**C4. Adquisición Conocimiento** (5 subcaps)

### Grados de Smartness

```
Grade: Cap → {0, 1, 2, 3, 4}

0: No_Inteligente
1: Ejecución_Scripted
2: Adaptación_Formulaica
3: Adaptación_Creativa
4: Invención_NoScripted
```

### Función de Smartness

```
Smartness(ws) := Σᵢ₌₁²³ wᵢ × Grade(capᵢ)

wᵢ = peso contextual de capacidad i
Σwᵢ = 1
```

**Teorema Anti-Binaridad**: Smartness es función continua en [0, 92]

**Corolario**: `∀gap: ∃cap_i: Incrementar(Grade(cap_i)) → Reducir(gap)`

---

## §3. MARCO AR (Agente-Responsabilidad)

### Tensor AR

```
AR: R × F → {NR, Bajo, Medio, Alto, Crítico}

R = 6 roles
F = 18 facetas
Dimensionalidad = 108 decisiones
```

### Mapeo Roles-SADE

```
ρ: R → 2^{SENSE,DECIDE,EXECUTE}

ρ(R1_Monitor) = {SENSE}
ρ(R2_ProveerInfo) = {SENSE, DECIDE}
ρ(R3_ProveerCapac) = {DECIDE, EXECUTE}
ρ(R4_Controlar) = {EXECUTE}
ρ(R5_Coproducir) = {SENSE, DECIDE, EXECUTE}
ρ(R6_Ejecutar) = {EXECUTE}
```

### Teorema Composición

```
∀CHS: Configuración ≡ Distribución_SADE ⊗ Tensor_AR
```

---

## §4. HCAI SOLUTION MAP

### Dimensión 1: Human-Centered AI Purpose

**AI Assistants**: Support users (natural language, recommendations, triggering)

**AI Augmentation Tools**: Packaged functionality augments abilities/capacity (interactive)

**AI Orchestration Agents**: Coordinate/supervise AI systems, set intervention points

**AI Automation Agents**: Run decoupled, provide cognitive functions (SADE completo)

### Dimensión 2: Human-Centered AI Cognition

**Sense**: Perceptual capabilities, monitor task-relevant state

- Ex: Fraud detection, churn risk recognition

**Decide**: Make decisions, rule-engines, problem solvers

- Ex: Complex problem-solving, decision options generation

**Act**: Trigger/execute actions, integrated with other systems

- Ex: Block transactions, generate personalized emails

---

## §5. CARACTERÍSTICAS HCAI

### Context Awareness

```
Kinds of Awareness:
- User awareness
- Task awareness
- Agent awareness
- Situational awareness
- Mission awareness
```

Representación: User history, time series, behavioral graphs, digital twins

### Human-Centeredness (Qualities)

**Design Objectives**: Empathy, Trust, Explainability, Transparency, Intervenability, Goal alignment

**Prominence by AI Type**:

- Assistants: Empathy, explainability
- Tools: Transparency, usability
- Orchestration: Control, intervention
- Automation: Trust, accountability

### Human Control (Levels)

**In-the-loop**: Human directly involved, uses AI for consultation

**On-the-loop**: Human provides supervision, monitors ongoing, can override

**Out-of-the-loop**: Human detached, meta-level management only

---

## §6. PATRONES DE INTERACCIÓN H-AA

### Modos de Engagement

```
Engagement := Balance(Iniciativa_H, Iniciativa_AA)

Patterns := {P1_Inform, P2_Command, P3_Guide, P4_Query,
             P5_Recommend, P6_Converse, P7_Negotiate,
             ..., P16_Accidental}
```

### Selección de Patrones

```
σ: (Fase_SADE, Rol_AA, Modo_Engagement) → 2^Patterns

σ(SENSE, R1_Monitor, _) ⊇ {P1_Inform}
σ(DECIDE, _, Mixed_Initiative) ⊇ {P6_Converse, P7_Negotiate}
σ(EXECUTE, R6_Ejecutar, _) ⊇ {P2_Command}
```

**Teorema Completitud**: Los 16 patrones cubren espacio completo interacciones H-AA

---

## §7. OBJETOS DE CONOCIMIENTO (KO)

### Taxonomía

```
KO := Conceptos ∪ Datos ∪ Interpretaciones ∪
      Generalizaciones ∪ Métodos

Conceptos := {Cosas, Actividades, Características, Métricas, Fenómenos}
Datos := {Facts, Datasets, Textos, Imágenes, Videos}
Interpretaciones := {Stories, Metáforas, Explicaciones, Modelos_Situacionales}
Generalizaciones := {Principios, Frameworks, Teorías, Axiomas}
Métodos := {Técnicas, Herramientas, Prácticas}
```

### Uso de KO

```
Uso_KO: (H ∪ AA) × KO → {Puede_Usar, No_Puede_Usar}

Uso_KO(H, Generalizaciones) = Puede_Usar
Uso_KO(AA_actual, Generalizaciones) = No_Puede_Usar
Uso_KO(AA_actual, Datos) = Puede_Usar
```

**Teorema Asimetría Cognitiva H-AA**: `∃ko: Uso_KO(H, ko) ≠ Uso_KO(AA, ko)`

**Oportunidad Smartness**: Incrementar `Uso_KO(AA, Generalizaciones)` → incrementa smartness en C4

---

## §8. EVALUACIÓN DE SISTEMAS INTELIGENTES

### Criterios Operacionales

```
E_op := {E1_Efficiency, E2_Effectiveness,
         E3_Reliability, E4_Resilience}
```

### Criterios Sociotécnicos

```
E_st := {E5_Equity, E6_Engagement, E7_Empathy,
         E8_Explainability, E9_Externalities}
```

### Función de Valor

```
Valor(ws) := f(e₁, e₂, ..., e₉ | Pesos, Constraints)

eᵢ: WS → [0, 1] (normalizado)
```

**Teorema Imposibilidad**: `∀ws: ∄configuración: ∀i: eᵢ(ws) = 1`

**Corolario**: Diseño efectivo requiere especificar pesos y constraints explícitos

---

## §9. INTEGRACIÓN SADE-SMARTNESS-AR

### Teorema Mapeo

```
∀fase ∈ SADE: ∃Cap_dominante ⊆ Cap:
  Performance(fase) ≈ f(Smartness(Cap_dominante))
```

**Construcción**:

- SENSE → C1 (Procesamiento Info) dominante
- DECIDE → C4 (Adquisición Conocimiento) + C3 (Regulación) dominante
- EXECUTE → C2 (Acción Mundo) dominante

### Ecuación Configuración CHS

```
Configuración(CHS) = Distribución_SADE(H, AA) ⊗
                     Tensor_AR(R × F) ⊗
                     Vector_Smartness(Cap)
```

---

## §10. DISEÑO PARA AUTONOMÍA

### Espectros Integrados

**Autonomía**:

```
Aumentación (RAG) → Agente ReAct → Plan-and-Execute
```

**Responsabilidad** (Marco AR):

```
Monitorear → Proveer → Controlar → Coproducir → Ejecutar
```

**Interacción**:

```
Máquina-en-bucle → Mixta → Humano-en-bucle → Autónomo supervisado
```

### Regla de Selección (SIGMA)

```
Modo_Interacción = f(Impacto, Irreversibilidad, Riesgo)

Alto riesgo → HITL obligatorio
Medio riesgo → On-the-loop + checkpoints
Bajo riesgo → Autónomo supervisado
```

---

## §11. BOUNDED AUTONOMY

### Definición

Autonomía siempre bounded:

- Human siempre puede engage/disengage
- Configuración/intervention interfaces obligatorias
- Meta-level control preservado

### Transiciones de Modo

```
Sistema debe ser flexible para soportar:
- Autonomous → Interactive (escalation)
- Interactive → Autonomous (delegation)

Triggered by:
- Complejidad situación
- Trust del humano
- Impacto decisión
```

---

## §12. MODELO UNIFICADO DE AGENCIA ALGORÍTMICA

### 12.1 Taxonomía Canónica AA

**Problema motivador**: Doc 01 define `AA` genérico, pero no especifica tipos ni protocolos governance diferenciados.

**Solución**: Taxonomía formal de 4 arquetipos AA ortogonales

```
AA := Conversational ∪ Decisional ∪ Mechanical ∪ Hybrid

Ortogonalidad: ∀i≠j: AA_i ∩ AA_j = ∅ (no overlap)
Completitud: ∀capacidad_algorítmica ∈ Sistema: ∃!AA_tipo
```

### 12.2 Arquetipo 1: Conversational AA

**Definición**:

```
Conversational_AA := {
  Interface: Natural language (texto/voz)
  Cognitive_Core: LLM + tool orchestration
  SADE: Full cycle (Sense-Decide-Execute)
  Smartness: C2-C3 (Adaptación creativa)
  Interaction: P6_Converse, P7_Negotiate (Doc §6)
}
```

**Ejemplos**: ChatGPT assistant, customer service bot, research analyst agent

**Governance Protocol**: **ADP/ALM** (Ref: Doc 10)

```yaml
agent_contract_id: AGENT-TYPE-DOMAIN-VERSION
agent.yaml: Declarative definition (roles, objectives, workflows, KB)
alm_phase: {Conception, KB_Curation, Programming, Testing, Maintenance}
guardrails: {input, output, operational, ethical}
kb_sync_protocol: {Manual, CI/CD, Drive_Sync}
```

**Capabilities dominantes** (Doc §2):

- C1.1: Natural language understanding
- C1.4: Contextual interpretation
- C4.1: Learning from examples
- C2.3: Generate coherent responses

**Bounded Autonomy** (6 dimensiones):

```
Financial: Token budget limits
Operational: HITL checkpoints on low confidence
Reputational: Brand guidelines compliance
Legal: Prohibition lists (PII, illegal content)
Temporal: Max session duration
Scope: Restricted tool catalog
```

### 12.3 Arquetipo 2: Decisional AA

**Definición**:

```
Decisional_AA := {
  Interface: Data inputs (structured/unstructured)
  Cognitive_Core: ML model (supervised/unsupervised/RL)
  SADE: Decide-Execute (Sense delegado a data pipeline)
  Smartness: C1-C2 (Ejecución scripted → Adaptación formulaica)
  Interaction: P5_Recommend, P4_Query
}
```

**Ejemplos**: Churn prediction model, fraud detection system, demand forecasting, recommendation engine

**Governance Protocol**: **MLOps** (extendido)

```yaml
model_contract_id: MODEL-TYPE-DOMAIN-VERSION
model_card: Declarative spec (use case, training data, performance, limitations)
mlops_phase: {Scoping, Data, Modeling, Deployment, Monitoring}
guardrails: {input_validation, output_bounds, drift_detection}
retraining_policy: {trigger_conditions, approval_gate}
```

**Capabilities dominantes**:

- C1.2: Pattern recognition
- C1.3: Classification/regression
- C4.2: Generalization from training data
- C3.2: Self-monitoring (drift detection)

**Bounded Autonomy**:

```
Financial: Inference cost budget
Operational: Confidence threshold for auto-decision
Reputational: Fairness constraints (demographic parity)
Legal: GDPR Article 22 (right to explanation)
Temporal: Max staleness training data
Scope: Feature space restrictions
```

### 12.4 Arquetipo 3: Mechanical AA

**Definición**:

```
Mechanical_AA := {
  Interface: UI/API automation (no ML)
  Cognitive_Core: Rule engine + workflow scripts
  SADE: Execute only (deterministic)
  Smartness: C0-C1 (No inteligente → Ejecución scripted)
  Interaction: P2_Command, P1_Inform
}
```

**Ejemplos**: RPA bot (attended/unattended), workflow engine (BPMN), task scheduler

**Governance Protocol**: **RPA/BPM Governance**

```yaml
automation_contract_id: RPA-TYPE-DOMAIN-VERSION
process_definition: BPMN 2.0 XML or RPA studio project
governance_phase: {Process_Mining, Design, Implementation, Monitoring, Optimization}
guardrails: {error_handling, retry_logic, fallback_to_human}
maintenance_policy: {update_frequency, regression_testing}
```

**Capabilities dominantes**:

- C2.1: Execute predefined actions
- C1.5: Data extraction (screen scraping)
- C3.1: Exception handling (basic)
- C4.0: No learning (requires manual update)

**Bounded Autonomy**:

```
Financial: Execution quota (runs/day)
Operational: HITL on exception queue
Reputational: Audit trail mandatory
Legal: Compliance with process standards
Temporal: Max execution time per run
Scope: Whitelisted applications only
```

### 12.5 Arquetipo 4: Hybrid AA

**Definición**:

```
Hybrid_AA := Composition(AA_i, AA_j, ...) where i≠j

Ejemplo canónico: Conversational + Decisional
  LLM agent orchestrates ML models as tools
  
Propiedad composicional:
  Smartness(Hybrid) = max{Smartness(AA_i)}
  SADE(Hybrid) = ∪ SADE(AA_i)
  Governance(Hybrid) = superset protocols
```

**Ejemplos**:

- Agentic RAG (LLM + vector search + reranking models)
- Intelligent RPA (RPA + ML classification for routing)
- AI-powered fraud investigator (Conversational + Decisional + Mechanical)

**Governance Protocol**: **Multi-Protocol Composition**

```yaml
hybrid_contract_id: HYBRID-TYPE-DOMAIN-VERSION
component_protocols:
  - protocol: ADP/ALM
    applies_to: conversational_layer
  - protocol: MLOps
    applies_to: ml_models_tool_catalog
  - protocol: BPM
    applies_to: workflow_orchestration
guardrails: Union of all component guardrails (strictest wins)
```

**Bounded Autonomy**: Intersection (most restrictive) of all component bounds

### 12.6 Decision Tree: Protocol Selection

```
¿AA interactúa en lenguaje natural?
  ├─ SÍ → Conversational_AA → ADP/ALM (Doc 10)
  └─ NO → ¿AA aprende de datos (ML)?
          ├─ SÍ → Decisional_AA → MLOps
          └─ NO → ¿AA ejecuta flujos/reglas deterministas?
                  ├─ SÍ → Mechanical_AA → RPA/BPM Governance
                  └─ NO → ¿Composición de múltiples tipos?
                          ├─ SÍ → Hybrid_AA → Multi-Protocol
                          └─ NO → Error: AA no clasificable (revisar definición)
```

### 12.7 Mapeo a Primitivos ORKO

**Primitivo P1 (Capacidad)**:

```yaml
Capacity:
  substrate: Algorítmico
  capacity_type: {C0, C1, C2, C3}  # Mapea a Smartness grades
  aa_archetype: {Conversational, Decisional, Mechanical, Hybrid}  ← NUEVO
  governance_protocol: {ADP/ALM, MLOps, RPA/BPM, Multi}  ← NUEVO
```

**Relación R13 (Delegación HAIC)**:

```yaml
R13_Extension_ADP_ALM:
  agent_contract_id: String
    Requerido: Si aa_archetype = Conversational
    
  model_contract_id: String  ← NUEVO
    Requerido: Si aa_archetype = Decisional
    
  automation_contract_id: String  ← NUEVO
    Requerido: Si aa_archetype = Mechanical
    
  hybrid_component_refs: URI[]  ← NUEVO
    Requerido: Si aa_archetype = Hybrid
```

### 12.8 Matriz de Governance Completa

| Arquetipo | Smartness | SADE | Protocol | Contrato Tipo | Ejemplo Tool |
|-----------|-----------|------|----------|---------------|--------------|
| **Conversational** | C2-C3 | S-D-E | ADP/ALM | agent.yaml | LangChain |
| **Decisional** | C1-C2 | D-E | MLOps | model_card.yaml | MLflow |
| **Mechanical** | C0-C1 | E | RPA/BPM | process.bpmn | UiPath, Camunda |
| **Hybrid** | max(components) | ∪(components) | Multi | hybrid.yaml | Custom orchestrator |

### 12.9 Invariantes de Agencia Unificada

**I-AA-1**: `∀AA: ∃!archetype ∈ {Conv, Deci, Mech, Hybrid}`

**I-AA-2**: `∀AA: governance_protocol = f(archetype)` (determinista)

**I-AA-3**: `∀Hybrid_AA: Smartness ≥ max{Smartness(component_i)}`

**I-AA-4**: `∀AA(substrate=Algorítmico): ∃Capacity(substrate=Humano, role=Accountable)` (HAIC preserved)

**I-AA-5**: `Bounded_Autonomy(AA) = min{Bounds_i} ∀i ∈ 6_dimensions` (strictest wins)

### 12.10 Integración con TF1 (Capacity Fabric)

**TF1 Schema extendido**:

```yaml
Capacity:
  id: string
  substrate: {Humano, Algorítmico, Mecánico, Mixto}
  
  # Si substrate = Algorítmico:
  aa_archetype: {Conversational, Decisional, Mechanical, Hybrid}
  governance_protocol_ref: URI  # apunta a agent.yaml, model_card.yaml, etc.
  smartness_grade: {C0, C1, C2, C3, C4}
  sade_phases: [Sense, Decide, Execute]  # subset según arquetipo
  bounded_autonomy:
    financial: {budget_limit, currency}
    operational: {hitl_checkpoints, confidence_thresholds}
    reputational: {brand_guidelines, compliance_refs}
    legal: {prohibition_lists, regulatory_refs}
    temporal: {max_session_duration, max_staleness}
    scope: {allowed_tools, feature_space}
```

---

**Aplicación en ORKO**: Esta extensión (§12) fundamenta formalmente la clasificación de capacidades algorítmicas en Layer 0-1, permitiendo que TF1 (Capacity Fabric) tenga especificación completa para cada tipo AA. Elimina ambigüedad en R13 (Delegación HAIC) sobre qué protocolo governance aplicar según tipo de agente algorítmico.
