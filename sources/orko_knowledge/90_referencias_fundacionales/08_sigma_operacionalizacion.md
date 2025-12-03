# SIGMA: Operacionalización Tecnológica

**ID**: ORKO-REF-SIGMA-01  
**Versión**: 1.1.0  
**Última actualización**: 2025-01-13  
**Changelog 1.1.0**: Refactorizado P7 (KM+RAG) con referencia explícita a Doc 09, elimina redundancia  
**Fuente**: SIGMA - Sistemas Inteligentes Gobernados por Métricas y Autonomía  
**Propósito**: Operacionalizar Layer 2 (Tejidos Tecnológicos) de ORKO

---

## §1. DEFINICIÓN Y ALCANCE

### Objetivo SIGMA

Alinear estrategia, datos, conocimiento, procesos y agentes IA en Sistema de Trabajo gobernado por:

- Contratos semánticos
- Guardrails
- SLO/SLA
- Operación observable end-to-end

### Fundamentos

1. Marco estratégico "Agentes Digitales" y espectro autonomía/rol
2. Ingeniería software empresarial (C4/ADR/CI-CD/observabilidad/seguridad/FinOps)
3. BPA con BPMN/EDA/RPA y CoE
4. Arquitectura datos orientada a productos (DaP) con policy-as-code, linaje
5. Gestión conocimiento con curation y RAG para respuestas citables

---

## §2. LOS 7 PRINCIPIOS RECTORES

**P1. Semántica Primero**: Todo artefacto opera bajo contratos

**P2. Gobernanza Embebida**: Guardrails desde diseño→operación (no after-the-fact)

**P3. Federación con Guardrails**: Dominios autónomos + estándares comunes + policy-as-code

**P4. Observabilidad Requisito**: Métricas, traces, linaje para auditar decisiones H y AA

**P5. HITL por Defecto en Riesgo**: Espectro autonomía progresivo (RAG → ReAct → Plan&Execute)

**P6. Automatiza Procesos (no solo tareas)**: BPMN/EDA orquestan; RPA último recurso

**P7. KM + RAG Confiable**: Knowledge curation + RAG con citaciones exactas

```yaml
Descripción: RAG responses require curated knowledge with exact citations
Protocolo: Aplicar STS/SFD/KHM (Ref: Doc 09 - Curation y Gestión Conocimiento)
Invariantes:
  - citation_policy: required_exact (SIGMA Invariante I-SIGMA-1)
  - fidelity_score: 1.0 (100% información preservada, STS Teorema Fidelidad)
  - density_score: >0.9 (STS Principio P4 - Zero Fat)
Métricas:
  - citation_exactness: ≥0.95
  - no_answer_correctness: precision/recall
  - corpus_coverage: %documentos con al menos 1 retrieval
Implementación: Ver Doc 09 para ciclo completo (Sourcing → Publishing → Maintenance)
```

---

## §3. CAPAS DEL SUPRADOMINIO

```
┌─────────────────────────────────────────────────────────────┐
│ Valor y Gobierno (Estrategia, Ética, Riesgo, CoE, FinOps)  │
├─────────────────────────────────────────────────────────────┤
│ Semántica Común (Ontologías, Glosario, Contratos)          │
├─────────────────────────────────────────────────────────────┤
│ TEJIDOS DE EJECUCIÓN:                                       │
│  - Conocimiento (Curation→Indexación→RAG→Citas)            │
│  - Datos (Lakehouse, Data Products, Linaje, DQ, SLOs)      │
│  - Procesos (BPMN/EDA, Sagas, HITL, RPA)                   │
│  - Agentes (LLMs, herramientas, espectro autonomía)        │
├─────────────────────────────────────────────────────────────┤
│ Plataforma Ingeniería (CI/CD, IaC, Observabilidad)         │
├─────────────────────────────────────────────────────────────┤
│ Integración (APIs, Bus Mensajes, MDM, Catálogos)           │
└─────────────────────────────────────────────────────────────┘
```

---

## §4. ONTOLOGÍA NÚCLEO

### Clases Principales

**SistemaDeTrabajo**: Contexto sociotécnico conteniendo Proceso, AgenteDigital, ActorHumano, ProductoDeDatos

**AgenteDigital**: LLM + herramientas

- Atributos: capabilities, guardrails, autonomía, rol, contratoAgente

**Proceso**: BPMN/EDA

- Atributos: flujo, tareas, SLA, HITL, compensaciones

**Tarea**: Automatizable

- Clase: API, UI/RPA, humana, agente
- Atributos: idempotencia, reintentos

**Evento**: EDA

- Atributos: esquema, contratoEvento, orden, exactly/at-least once

**ProductoDeDatos**:

- Atributos: contratoDatos, SLO, linaje, clasificación, métricas

**Documento y Chunk** (KM/RAG):

- Atributos: taxonomía, vigencia, ACL, citas exactas

**Contrato** (abstracta):

- Tipos: ContratoDeDatos, ContratoDeProceso, ContratoDeAgente, ContratoDeConocimiento

**Métrica/SLO/SLA y Guardrail**:

- Tipos guardrail: entrada, salida, operacional, ético

**Política** (policy-as-code), **Riesgo**, **Incidente**, **Linaje**

---

## §5. CONTRATOS CANÓNICOS

### Contrato de Datos (resumen)

```yaml
type: data_contract
product: billing_invoices
version: 2.1.0
semantics: {glossary_refs, rules}
slo: {freshness_p95_minutes: 30, availability_pct: 99.9}
quality: {checks: pk_unique, etc}
security: {classification: P1, pii: false}
lineage: [kafka → bronze → silver → gold]
changes: {policy: semver, deprecation_window_days: 120}
```

### Contrato de Proceso

```yaml
type: process_contract
process: invoice_approval
sla: {cycle_time_p95_minutes: 180, stp_target_pct: 80}
hitl: {queues: ["exceptions.approval"], escalation_rules}
saga: {compensations: [{action, on}]}
events: [{name, schema_ref, delivery}]
idempotency: {keys: ["invoice_id"]}
rpa_fallback: {enabled, guardrails}
```

### Contrato de Agente

```yaml
type: agent_contract
agent: pre_reviewer
autonomy_level: PLAN_AND_EXECUTE
role: COPRODUCIR
tools: [kb_search, erp_api, doc_parser]
rag_policy: {retrieval, citations}
guardrails: {input, output, ops}
quality_metrics: {faithfulness>=0.9, citation_exactness>=0.95}
hitl_checkpoints: ["score<0.85", "conflict_detected"]
```

### Contrato de Conocimiento

```yaml
type: knowledge_contract
collection: normativa_interna
authority: official_only
doc_units: [expediente, documento, seccion, articulo]
metadata_min: [id_doc, tipo, emisor, fecha, vigencia, hash, acl]
indexing: {lexical: bm25, vector: embeddings_v3, filters}
serving: {context_assembly, citation_policy: required_exact}
audit: {chain_of_custody: true, snapshots: true}
```

---

## §6. ESPECTROS INTEGRADOS

### Autonomía

```
Aumentación (RAG) → Agente ReAct → Plan-and-Execute
```

### Responsabilidad (Marco AR)

```
Monitorear → Proveer info/capacidades → Controlar →
Coproducir → Ejecutar
```

### Interacción

```
Máquina-en-el-bucle → Iniciativa mixta →
Humano-en-el-bucle → Autónomo supervisado
```

**Regla SIGMA**: Modo interacción = f(impacto, irreversibilidad, riesgo) del Proceso

---

## §7. ARQUITECTURA DE REFERENCIA

### Flujo E2E

1. **Descubrir**: Oportunidades por fricción (operacional, cognitiva, capacidad, variabilidad)

2. **Diseñar**: C4/ADRs, NFRs, go/no-go (deseabilidad/factibilidad/viabilidad)

3. **Construir**:
   - Datos: ingesta→bronze/silver/gold, DQ, contratos
   - Agentes: prompts/herramientas/orquestación
   - Procesos: BPMN/EDA, Sagas, HITL
   - UIs y conectores

4. **Probar**: offline+online, LLM-as-Judge, seguridad, e2e RAG con citation-exactness

5. **Desplegar/Operar**: CI/CD, IaC, K8s, observabilidad, linaje activo, SRE

6. **Mejorar**: Data flywheel, feedback, drift detection, canary

---

## §8. TEJIDOS ESPECÍFICOS

### Tejido de Procesos (BPMN/EDA/RPA)

- **Orquestación**: BPMN + Sagas (compensación, SLAs)
- **Coreografía**: EDA (desacoplamiento)
- **HITL**: Colas excepciones, escalamiento
- **Métricas**: STP%, cycle time
- **RPA**: Attended/unattended como fallback a legacy

### Tejido de Datos (DaP)

- **Lakehouse**: ACID, time-travel, bronze→silver→gold
- **DQ**: Declarativa, checks automáticos
- **Contratos y SLOs**: Publicados, monitoreados
- **Linaje**: As-designed + as-implemented, columna-a-columna
- **Evolución**: Backward-compatible, CDC log-based

### Tejido de Conocimiento (KM→RAG)

- **Curation**: Autoridad, vigencia, metadata mín-suficiente
- **Indexación**: Híbrida (BM25+vector), filtros vigencia/ACL
- **Reranking**: Por autoridad/entidades
- **Serving**: Ensamblado por secciones, citas obligatorias
- **Audit**: Chain of custody, snapshots

### Tejido de Agentes (IA en Producción)

- **Motor cognitivo** + herramientas + orquestación
- **Guardrails**: entrada/salida/ops/éticos
- **Evaluación**: Fidelidad, citation-exactness, latencia, coste
- **Observabilidad**: Traces, métricas, logs específicos

---

## §9. MÉTRICAS Y SLOS

### Por Proceso

- Cycle time p95
- STP % (Straight-Through Processing)
- Tasa error
- Backlog HITL
- MTTR excepciones

### Por Datos

- Frescura p95
- Latencia p95 (ingesta/transform/serving)
- Violaciones DQ/1k filas
- Costo/consulta
- Error budget

### Por IA (Agente/RAG)

- Fidelidad
- Citation-exactness
- No-answer correcto
- TTFT/TPOT (Time To First/Per Output Token)
- Coste/tarea
- Drift

### Por KM

- % respuestas con cita válida
- Cobertura corpus
- Lag ingestión
- Participación CoPs

---

## §10. ANTI-PATRONES

**AP1**: RPA como martillo universal (usar APIs/ETL cuando existan)

**AP2**: Automatizar procesos rotos sin process mining previo

**AP3**: Ignorar "longa cola" excepciones

**AP4**: Data dual-write y cambios big-bang esquema

**AP5**: Tópicos sin contrato

**AP6**: RAG sin curation/vigencia/ACL

**AP7**: Respuestas sin cita exacta

**AP8**: Observabilidad mínima

**AP9**: Falta ADRs/linaje activo

---

## §11. OPERACIONALIZACIÓN AVANZADA

### Patrones Clave

**Sagas + ReAct**:

```
Agente planifica → ejecuta pasos con tools →
confirma pre-commit → compensa on failure
```

**RAG con Policy-as-Code**:

```
Filtros vigencia/ACL en retrieval (ABAC/RLS) →
Citation-gate en output
```

**Linaje 2D**:

```
OpenLineage para tablas +
Trace para tool-calls de agentes
```

**FinOps**:

```
Showback/chargeback por dominio +
Presupuesto tokens/cómputo por agent_contract
```

---

## §12. ROADMAP IMPLEMENTACIÓN

### 90 días

- Charter SIGMA
- Templates contratos
- 1 proceso orquestado (Sagas/HITL)
- 2 data products (SLO + linaje)
- Curation mínima + RAG citables
- CI/CD + observabilidad base

### 180 días

- 3-5 agentes (ReAct/plan)
- Metric store
- ABAC/RLS E2E
- Error budgets por producto
- CoE BPA activo

### 365 días

- Dominios federados
- MDM entidad crítica
- Privacy by default
- Canary embeddings/reranking
- FinOps guardrails
- Deprecación sistemática

---

## §13. CHECKLIST ADOPCIÓN

1. ☐ Seleccionar flujo valor con fricción prioritaria + KPIs
2. ☐ Modelar contexto (C4 L1/L2), límites (DDD), eventos
3. ☐ Aplicar contratos unificados antes primer commit
4. ☐ Instrumentar observabilidad (OpenTelemetry) + linaje
5. ☐ Definir error budgets
6. ☐ Probar e2e con citation-exactness + no-answer correctos
7. ☐ Endurecer guardrails
8. ☐ Desplegar con canary + HITL por defecto
9. ☐ Revisar métricas/SLIs semanalmente

---

## §14. INVARIANTES CRÍTICOS SIGMA

**I-SIGMA-1**: Toda respuesta RAG debe tener ≥1 cita exacta con doc/folio/versión

**I-SIGMA-2**: Toda tarea compensable en Saga define acción inversa determinista

**I-SIGMA-3**: Todo producto datos P1 mantiene linaje columna-a-columna + SLO frescura publicado

**I-SIGMA-4**: Todo agente con autonomía PLAN_AND_EXECUTE tiene checkpoints HITL definidos

**I-SIGMA-5**: Todo contrato tiene política cambio (semver) + deprecation window

---

**Aplicación en ORKO**: SIGMA operacionaliza completamente Layer 2 (Tejidos Tecnológicos), proveyendo especificaciones ejecutables para TF1-TF7. Conecta teoría (Layer 0-1) con implementación (Layer 4) vía contratos semánticos.

**Mapeo a Tejidos ORKO**:

- TF1 (Data Fabric) = Tejido de Datos
- TF2 (Automation Fabric) = Tejido de Procesos
- TF4 (Knowledge Fabric) = Tejido de Conocimiento
- TF5 (Orchestration Fabric) = Tejido de Agentes
- TF6 (Security Fabric) = Guardrails + Policy-as-Code
- TF7 (UX/UI Fabric) = Interfaces HITL
- TF3 (Analytics Fabric) = Métricas + Observabilidad
