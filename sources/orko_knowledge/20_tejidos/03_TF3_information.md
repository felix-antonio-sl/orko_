# TF3: INFORMATION FABRIC

**Primitivo:** P3_Información | **Axioma:** A3_Existencia_Información  
**Dominios:** D2_Percepción, D4_Operación | **Tech:** Data, Analytics, Knowledge

> **📘 GENOMA/FENOTIPO EN TF3**:  
> - **[GENOMA]**: Schema InformationAsset (Foundation/Analytics/Semantic), invariantes (lineage obligatorio, encryption at rest, PII governance), patterns abstractos (lakehouse layers, data products, RAG retrieval)  
> - **[FENOTIPO]**: Plataformas específicas (Snowflake, Databricks, Airbyte), vectorstores (Pinecone, Weaviate), embedding models (OpenAI ada-002, Cohere), BI tools (Tableau, Looker)  
> 
> **Unificación Data+Analytics+Knowledge**: Evita silos; información fluye Bronze→Silver→Gold→Semantic sin boundaries artificiales.

---

## §1. DEFINICIÓN

```yaml
TF3_Information:
  Scope: Ciclo vida completo información organizacional
  Unifica: TF1_Data + TF3_Analytics + TF4_Knowledge (previo)
  
  Sub-Dominios:
    Foundation: Ingestion, Storage, Processing, Governance
    Analytics: BI, ML, predictive/prescriptive
    Semantic: RAG, knowledge graph, vector search
    
  Arquitectura: Lakehouse (Bronze → Silver → Gold → Semantic)
  
Trazabilidad:
  A3 (Información existe) → P3 (estructura información) → TF3 (operacionalización)
  
Justificación_Unificación:
  "Todos operan P3.Información. Tech stacks convergiendo (Lakehouse).
   RAG pipeline requiere los 3 sub-dominios → unificación necesaria"
```

---

## §2. ACTOR CONTRACT

```yaml
InformationAsset:
  # Core
  id: UUID
  name: String
  description: String
  
  # Clasificación P3
  information_type: {Persistente | Transitoria | Agregada}
  structure: {Structured | Semi_Structured | Unstructured}
  
  sub_domain: {Foundation | Analytics | Semantic}
  
  # Schema
  schema:
    format: {Parquet | JSON | CSV | Text | Image | Audio | Binary}
    schema_definition: JSON_Schema | null  # Si structured
    fields: List<Field> | null
      Field:
        name: String
        type: String
        nullable: Boolean
        description: String
        
  # Temporal Properties (P3)
  temporal:
    timestamp: Timestamp  # Cuándo generada
    validity_period_seconds: Integer | null  # null = infinito (persistente)
    expires_at: Timestamp | null
    freshness_sla_seconds: Integer | null  # Max age aceptable
    
  # Lineage (I3_Trazabilidad)
  lineage:
    origin: {Internal | External}  # ⚠️ NUEVO: Origen información
    produced_by_flow: UUID(Flow) | null  # TF2 que generó (Internal only)
    produced_by_capacity: UUID(Capacity) | null  # TF1 que produjo (Internal only)
    source_ref: String | null  # Referencia fuente externa (External only)
    parent_assets: List<UUID(InformationAsset)>  # Información origen (DAG, Internal)
    lineage_level: {Field | Table | Dataset}  # Granularidad tracking
    
  # Invariante de Origen (INV_TF3_Lineage):
  # - origin=Internal ⇒ produced_by_flow OR produced_by_capacity NOT NULL
  # - origin=External ⇒ produced_by_flow=NULL AND produced_by_capacity=NULL AND source_ref NOT NULL
    
  # Quality (Foundation)
  quality:
    completeness_pct: Float[0..1]  # % campos no-null
    accuracy_pct: Float[0..1]  # % valores correctos (vs ground truth)
    freshness: {Fresh | Stale | Expired}  # Basado en validity_period
    validity_pct: Float[0..1]  # % valores que pasan reglas validación
    uniqueness_pct: Float[0..1]  # % registros únicos (si aplica)
    consistency_score: Float[0..1]  # Consistencia cross-datasets
    
  # Governance (P4 transversal)
  governance:
    access_control:
      readers: List<UUID(Capacity)>
      writers: List<UUID(Capacity)>
      row_level_security: Boolean
      
    privacy:
      contains_pii: Boolean
      pii_fields: List<String> | null
      masking_rules: List<MaskingRule> | null
        MaskingRule:
          field: String
          method: {Hash | Redact | Tokenize | Encrypt}
          
    compliance:
      regulatory_tags: List<String>  # GDPR, HIPAA, etc.
      data_residency: String | null  # e.g., "EU", "US"
      retention_policy:
        retention_days: Integer | null  # null = indefinido
        deletion_method: {Hard_Delete | Soft_Delete | Archive}
        
    encryption:
      at_rest: Boolean
      at_transit: Boolean
      key_management: String | null  # KMS reference
      
  # Storage (Foundation)
  storage:
    location_uri: String  # s3://, gs://, /data/, postgres://
    size_bytes: Integer
    partition_key: String | null
    compression: {None | Gzip | Snappy | LZ4} | null
    
  # Analytics-Specific (si sub_domain=Analytics)
  analytics:
    metric_definition: String | null  # Business logic
    aggregation_logic: String | null  # SQL, formula
    compatible_dimensions: List<String> | null
    variance_tolerance_pct: Float | null  # % variación aceptable
    
    # Si ML model
    model_info:
      model_type: {Classification | Regression | Clustering | Ranking} | null
      algorithm: String | null
      features: List<String> | null
      target_variable: String | null
      performance_metrics: Map<String, Float> | null  # accuracy, f1, etc.
      training_dataset_id: UUID(InformationAsset) | null
      
  # Semantic-Specific (si sub_domain=Semantic)
  semantic:
    content_type: {Document | QA_Pair | Entity | Relationship}
    
    # Metadata semántica
    metadata:
      language: String  # ISO 639
      author: String | null
      created_date: Date
      last_modified: Date
      tags: List<String>
      categories: List<String>
      
    # Vigencia (Knowledge Management)
    vigencia:
      review_frequency_days: Integer  # Cada cuánto revisar
      last_review_date: Date | null
      next_review_date: Date | null
      status: {Current | Under_Review | Deprecated | Archived}
      reviewer_id: UUID(Capacity.Humano) | null
      
    # Indexing (RAG)
    indexing:
      vector_indexed: Boolean
      embedding_model: String | null  # e.g., "text-embedding-ada-002"
      vector_dimension: Integer | null
      vector_db_collection: String | null
      
      keyword_indexed: Boolean
      keyword_index_type: {BM25 | TF_IDF} | null
      
      graph_indexed: Boolean
      entities: List<Entity> | null
        Entity:
          name: String
          type: String
          confidence: Float[0..1]
          
    # RAG Configuration
    rag_config:
      chunk_strategy: {Fixed_Size | Semantic | Recursive} | null
      chunk_size: Integer | null
      chunk_overlap: Integer | null
      retrieval_k: Integer | null  # Top-k results
      reranking_enabled: Boolean
      citation_required: Boolean
      
  # Usage & Performance
  usage:
    access_count_30d: Integer
    query_count_30d: Integer
    last_accessed: Timestamp | null
    consumers: List<UUID(Capacity | Flow)>  # Quién usa
    
  # Integration
  serves_flows: List<UUID(Flow)>  # TF2 que consume
  feeds_capacities: List<UUID(Capacity)>  # TF1 que consume (e.g., ML models)
  
  # Purpose (P5)
  purpose:
    usage_role: {Producción | Habilitación} | null  # ⚠️ NUEVO (I4)
    linked_okrs: List<UUID(OKR)>
    business_value: String
    criticality: {Low | Medium | High | Critical}
    
  # Nota I4: usage_role puede ser null y derivarse del contexto:
  # - Producción: Datos operacionales, transaccionales, core business
  # - Habilitación: Metadatos, catálogos, configuración, soporte
    
  # Lifecycle
  lifecycle:
    current_state: {Planning | Ingestion | Processing | Active | Deprecated | Archived | Deleted}
    version: Integer
    
Invariantes:
  - INV_TF3_Lineage: origin=Internal ⇒ (produced_by_flow OR produced_by_capacity NOT NULL)
  - INV_TF3_Lineage: origin=External ⇒ (produced_by_flow=NULL AND produced_by_capacity=NULL AND source_ref NOT NULL)
  - information_type=Transitoria → validity_period_seconds NOT NULL
  - information_type=Agregada → parent_assets.length > 1
  - sub_domain=Semantic ∧ rag_config NOT NULL → indexing.vector_indexed=true
  - contains_pii=true → masking_rules NOT NULL
  - sub_domain=Analytics ∧ metric_definition NOT NULL → compatible_dimensions NOT NULL
```

---

## §3. ARQUITECTURA: LAKEHOUSE UNIFICADO

```yaml
Lakehouse_Pattern:
  "Unifica data lake (almacenamiento) + warehouse (analytics) + vector DB (semantic)"
  
  Bronze_Layer:  # Raw
    Scope: Ingestion sin transformación
    Format: Original (JSON, CSV, logs, docs)
    Quality: Sin validación
    Retention: 90-365 días
    Examples: API responses, sensor data, raw documents
    
  Silver_Layer:  # Cleaned
    Scope: Limpieza, validación, normalización
    Format: Parquet (structured), normalized JSON (semi)
    Quality: Validation rules aplicadas
    Retention: 1-3 años
    Examples: Validated transactions, cleaned logs, parsed documents
    Deduplication: true
    Schema_Enforcement: true
    
  Gold_Layer:  # Curated
    Scope: Business-ready, agregaciones
    Format: Parquet optimizado, semantic models
    Quality: High (completeness > 95%, accuracy > 98%)
    Retention: 3-7 años (o indefinido)
    Examples: Customer360, OKR dashboards, feature stores
    SLA: Freshness < 1 hora
    
  Semantic_Layer:  # Knowledge
    Scope: Información no-estructurada indexada
    Format: Text chunks + vector embeddings + knowledge graph
    Quality: Curation + review process
    Retention: Indefinido (con revisiones periódicas)
    Examples: Documentation, policies, FAQs, entity relationships
    Indexing: Hybrid (BM25 + vector)
    RAG_Ready: true

Data_Flow:
  Bronze → Silver: Cleaning, validation (TF2_Flow.ETL)
  Silver → Gold: Aggregation, business logic (TF2_Flow.Analytics)
  Raw_Docs → Semantic: Chunking, embedding, indexing (TF2_Flow.RAG_Pipeline)
  
  Cross-Layer:
    Gold → Semantic: Structured insights → Knowledge base
    Semantic → Analytics: Entity extraction → Feature engineering
```

---

## §4. SUB-DOMINIOS DETALLADOS

### Foundation (Structured/Semi-Structured)

```yaml
Capabilities:
  Ingestion:
    - Batch ETL [FENOTIPO] (Airbyte, Fivetran)
    - Streaming [FENOTIPO] (Kafka, Kinesis)
    - CDC [FENOTIPO] (Debezium, log-based)
    - APIs (REST, GraphQL)
    
  Storage:
    - OLTP [FENOTIPO]: PostgreSQL, MySQL (transactional)
    - OLAP [FENOTIPO]: Snowflake, BigQuery, Databricks (analytical)
    - Lake [FENOTIPO]: S3, GCS, Azure Blob (object storage)
    - Lakehouse [FENOTIPO]: Delta Lake, Iceberg, Hudi
    
  Processing:
    - ETL [FENOTIPO]: dbt, Spark, Dataflow
    - Orchestration [FENOTIPO]: Airflow, Dagster, Prefect
    
  Governance:
    - Catalog [FENOTIPO]: DataHub, Collibra, Alation
    - Lineage [FENOTIPO]: OpenLineage, dbt docs
    - Quality [FENOTIPO]: Great Expectations, Soda, Datafold
    
Métricas:
  - Data_Quality_Score: AVG(completeness, accuracy, freshness, validity)
  - Lineage_Coverage: % assets con lineage completo
  - SLA_Compliance: % pipelines meeting freshness SLA
```

### Analytics (Insights, ML)

```yaml
Capabilities:
  Descriptive:
    - Dashboards [FENOTIPO]: Tableau, Looker, PowerBI
    - Reports: Scheduled, parameterized
    - Ad-hoc: SQL editors, notebooks
    
  Diagnostic:
    - Root cause: Correlation, segmentation
    - Cohort analysis: Behavioral patterns
    - A/B testing: Statistical significance
    
  Predictive:
    - Forecasting [FENOTIPO]: Time-series (Prophet, ARIMA)
    - Classification: Churn, fraud detection
    - Anomaly detection: Outliers, drift
    
  Prescriptive:
    - Optimization: Linear programming
    - Recommendations: Collaborative filtering
    - Simulation: Monte Carlo, what-if
    
  MLOps:
    - Training [FENOTIPO]: MLflow, Kubeflow, SageMaker
    - Serving [FENOTIPO]: Seldon, KServe, BentoML
    - Feature Store [FENOTIPO]: Feast, Tecton
    - Monitoring [FENOTIPO]: Evidently, WhyLabs
    
Métricas:
  - Analytics_Coverage: % OKRs con dashboards
  - Model_Performance: AVG(accuracy, precision, recall)
  - Drift_Incidents: Count models con drift detectado
  - Adoption: Active users / total users
```

### Semantic (Unstructured, Knowledge)

```yaml
Capabilities:
  Capture:
    - Documents: PDF, Word, Markdown
    - Conversations: Slack, emails, meetings
    - Web: Scraping, APIs
    
  Curation:
    - Review: Human-in-loop quality check
    - Versioning: Track changes
    - Vigencia: Expiration tracking, review cycles
    
  Indexing:
    - Vector [FENOTIPO]: Embeddings (OpenAI, Cohere, local)
    - Keyword [FENOTIPO]: BM25, Elasticsearch
    - Graph [FENOTIPO]: Neo4j, entity relationships
    - Hybrid: Fusion BM25 + vector
    
  Retrieval:
    - Semantic search: Natural language queries
    - RAG: Retrieval-augmented generation
    - Q&A: Citations required
    - Recommendations: Similar content
    
  Delivery:
    - Chatbots: LLM-powered Q&A
    - Search UI: Web, mobile
    - Contextual help: Embedded in apps
    - APIs: Programmatic access
    
RAG_Pipeline_Pattern:
  Steps:
    1. Ingestion: Multi-format documents
    2. Chunking: Semantic boundaries [FENOTIPO] (RecursiveCharacterTextSplitter)
    3. Embedding: Vector representation [FENOTIPO] (e.g., ada-002)
    4. Indexing: Vector DB + BM25 [FENOTIPO] (Pinecone, Weaviate)
    5. Retrieval: Hybrid search (reranking)
    6. Generation: LLM with context + citations
    
  Quality_Gates:
    - Curation: Human review before indexing
    - Relevance: Retrieval precision > 0.80
    - Faithfulness: Generated answer matches retrieved context
    - Citation: Every claim has source link
    
Métricas:
  - Knowledge_Coverage: % processes con docs
  - Freshness: % docs reviewed < 180 days
  - RAG_Quality: Precision@K, NDCG
  - Adoption: Queries per week / employees
```

---

## §5. MÉTRICAS TF3

```yaml
TF3_Score = weighted_avg(
  TF3_Coverage      × 20%,  # % información catalogada
  TF3_Quality       × 30%,  # Data quality score
  TF3_Freshness     × 20%,  # % información fresh
  TF3_Governance    × 15%,  # Lineage, access control
  TF3_Adoption      × 15%   # Active users
)

Threshold: ≥ 70

Por Sub-Dominio:
  Foundation: Enfasis Quality, Freshness
  Analytics: Enfasis Adoption, Model Performance
  Semantic: Enfasis Freshness (vigencia), RAG Quality
  
Alerts:
  - Quality_Degradation: Score drop > 10%
  - Freshness_SLA_Miss: > 5% assets stale
  - Lineage_Gap: < 80% coverage
  - PII_Unmasked: PII detected sin masking
```

---

## §6. INTEGRACIÓN

```yaml
TF3 ← TF2: Flujos producen información
  Pattern: Flow produces Bronze → Silver → Gold
  Examples: ETL pipeline, ML training pipeline
  
TF3 → TF1: Información alimenta capacidades
  Pattern: 
    - Training datasets → ML models (TF1.algorithmic_specs)
    - RAG context → LLM agents (TF1.algorithmic_specs.model_info)
  
TF3 → TF2: Información trigger flujos
  Pattern: Data events (new file, threshold exceeded) → Flow execution
  
TF3 ↔ P4: Governance, security
  Access_Control: Row-level, column-level, dataset-level
  Privacy: PII detection, masking, encryption
  Compliance: Retention policies, audit trails
  
TF3 ↔ P5: Purpose alignment
  InformationAsset.linked_okrs → Business value
  Criticality determines: SLA, replication, backup
```

---

## §7. EJEMPLOS

### Foundation: Customer Data

```yaml
id: "info-001-customers-gold"
sub_domain: Foundation
information_type: Persistente
structure: Structured
schema:
  format: Parquet
  fields:
    - {customer_id, UUID, non_null}
    - {email, String, non_null}
    - {lifetime_value, Float, nullable}
quality:
  completeness_pct: 0.98
  accuracy_pct: 0.99
  freshness: Fresh
storage:
  location_uri: "s3://data-lake/gold/customers/"
  size_bytes: 524288000
governance:
  contains_pii: true
  pii_fields: [email, phone]
  masking_rules: [{email, Hash}]
```

### Analytics: ML Model

```yaml
id: "info-002-churn-model"
sub_domain: Analytics
information_type: Agregada
analytics:
  model_info:
    model_type: Classification
    algorithm: "XGBoost"
    features: [tenure, monthly_charges, support_tickets]
    target_variable: "churned"
    performance_metrics:
      accuracy: 0.89
      precision: 0.87
      recall: 0.85
      f1: 0.86
    training_dataset_id: "info-003-training-data"
lineage:
  parent_assets: ["info-003-training-data", "info-004-feature-store"]
```

### Semantic: Documentation

```yaml
id: "info-005-api-docs"
sub_domain: Semantic
information_type: Persistente
structure: Unstructured
semantic:
  content_type: Document
  metadata:
    language: "en"
    tags: [API, Developer, Integration]
  vigencia:
    review_frequency_days: 90
    last_review_date: "2025-01-01"
    status: Current
  indexing:
    vector_indexed: true
    embedding_model: "text-embedding-ada-002"
    vector_dimension: 1536
    keyword_indexed: true
    keyword_index_type: BM25
  rag_config:
    chunk_strategy: Recursive
    chunk_size: 1000
    chunk_overlap: 200
    citation_required: true
```

---

**Status:** ✅ Especificación completa con sub-dominios unificados (Foundation, Analytics, Semantic)
