# PARTE II: PRINCIPIOS DE DISEÑO

> **Etiquetado Genoma/Fenotipo**: Este documento contiene principios con diferente nivel de universalidad:
> - **[GENOMA]** PD1-PD30: Principios universales derivados de I1-I7 (obligatorios, no configurables)
> - **[FENOTIPO]** PD31-PD35: Arquetipos AOC (contextuales, best practices validadas desde Meyer)
> - **[GENOMA]** PD36-PD40: Parametrización contextual desde I8 (obligatorios, valores configurables)
> - **[FENOTIPO]** PD41-PD46: Métricas AOC/Kelly (fórmulas recomendadas, thresholds configurables)
> - **[FENOTIPO]** PD47-PD76: Guidelines operacionales G## (implementación específica)
>
> Ver ../00_fundamentos_teoricos/00_introduccion.md §0.1 para definición completa framework.

- [PARTE II: PRINCIPIOS DE DISEÑO](#parte-ii-principios-de-diseño)
  - [§1. FUNDAMENTOS](#1-fundamentos)
  - [§2. DESDE I1: MINIMALIDAD](#2-desde-i1-minimalidad)
  - [§3. DESDE I2: ORTOGONALIDAD](#3-desde-i2-ortogonalidad)
  - [§4. DESDE I3: TRAZABILIDAD](#4-desde-i3-trazabilidad)
  - [§5. DESDE I4: CLASIFICACIÓN CONTEXTUAL](#5-desde-i4-clasificación-contextual)
  - [§6. DESDE I5: HAIC (Human-AI Collaboration)](#6-desde-i5-haic-human-ai-collaboration)
  - [§7. DESDE I6: TRAJECTORY-AWARENESS](#7-desde-i6-trajectory-awareness)
  - [§8. DESDE I7: EMERGENCIA COMPLEJIDAD](#8-desde-i7-emergencia-complejidad)
  - [§9. MÉTRICAS OPERABLES (AOC + Kelly): PD41-PD46](#9-métricas-operables-aoc--kelly-pd41-pd46)
  - [§10. DESDE I8 (Parametrización Contextual): PD36-PD40](#10-desde-i8-parametrización-contextual-pd36-pd40)
  - [§11. DESDE GUIDELINES G## (Operacionalización): PD47-PD76](#11-desde-guidelines-g-operacionalización-pd47-pd76)
    - [Principios Definicionales (PD47-51, desde G26-G30)](#principios-definicionales-pd47-51-desde-g26-g30)
      - [PD47: Composition Acyclicity Transitive (desde G26)](#pd47-composition-acyclicity-transitive-desde-g26)
      - [PD48: Handoff Formal Definition (desde G27)](#pd48-handoff-formal-definition-desde-g27)
      - [PD49: Alignment Weighted Recursive (desde G28)](#pd49-alignment-weighted-recursive-desde-g28)
      - [PD50: Violation Severity Weighted (desde G29)](#pd50-violation-severity-weighted-desde-g29)
      - [PD51: Observable Standard Units (desde G30)](#pd51-observable-standard-units-desde-g30)
    - [Principios Lifecycle (PD52-54, desde G11-G24)](#principios-lifecycle-pd52-54-desde-g11-g24)
      - [PD52: Lifecycle Explicit Transitions (desde G11)](#pd52-lifecycle-explicit-transitions-desde-g11)
      - [PD53: Achievement Criteria Explicit (desde G12)](#pd53-achievement-criteria-explicit-desde-g12)
      - [PD54: Deprecation Phased Timeline (desde G24)](#pd54-deprecation-phased-timeline-desde-g24)
    - [Principios Estados y Transiciones (PD55-58, desde G1-G23)](#principios-estados-y-transiciones-pd55-58-desde-g1-g23)
      - [PD55: State Snapshot Consistency (desde G1)](#pd55-state-snapshot-consistency-desde-g1)
      - [PD56: Transition Executability (desde G23)](#pd56-transition-executability-desde-g23)
      - [PD57: Reachability Validation (desde G2)](#pd57-reachability-validation-desde-g2)
      - [PD58: Convergence Monitoring (desde G13)](#pd58-convergence-monitoring-desde-g13)
    - [Principios Execution \& DORA (PD59-63, desde G3-G7)](#principios-execution--dora-pd59-63-desde-g3-g7)
      - [PD59: Execution Instance Tracking (desde G3)](#pd59-execution-instance-tracking-desde-g3)
      - [PD60: DORA Metrics Mandatory (desde G4)](#pd60-dora-metrics-mandatory-desde-g4)
      - [PD61: Incident Flow Linkage (desde G5)](#pd61-incident-flow-linkage-desde-g5)
      - [PD62: Health Score Composite (desde G6)](#pd62-health-score-composite-desde-g6)
      - [PD63: Decision Audit Trail (desde G7)](#pd63-decision-audit-trail-desde-g7)
    - [Principios Governance \& Portfolio (PD64-68, desde G8-G15)](#principios-governance--portfolio-pd64-68-desde-g8-g15)
      - [PD64: Portfolio Value Maximization (desde G14)](#pd64-portfolio-value-maximization-desde-g14)
      - [PD65: Cross-Domain Health Balance (desde G15)](#pd65-cross-domain-health-balance-desde-g15)
      - [PD66: Governance Automation Progressive (desde G10)](#pd66-governance-automation-progressive-desde-g10)
      - [PD67: Pattern Catalog Mandatory (desde G8)](#pd67-pattern-catalog-mandatory-desde-g8)
      - [PD68: Anti-Pattern Detection Automated (desde G9)](#pd68-anti-pattern-detection-automated-desde-g9)
    - [Principios Vistas \& Optimización (PD69-72, desde G16-G19)](#principios-vistas--optimización-pd69-72-desde-g16-g19)
      - [PD69: Dashboard Real-Time Constraints (desde G16)](#pd69-dashboard-real-time-constraints-desde-g16)
      - [PD70: Artifact Templates Complete (desde G17)](#pd70-artifact-templates-complete-desde-g17)
      - [PD71: Metric Threshold Adaptive (desde G18)](#pd71-metric-threshold-adaptive-desde-g18)
      - [PD72: Integration Points Explicit (desde G19)](#pd72-integration-points-explicit-desde-g19)
    - [Principios Refinamientos Finales (PD73-76, desde G20-G25)](#principios-refinamientos-finales-pd73-76-desde-g20-g25)
      - [PD73: Query Performance Budgets (desde G20)](#pd73-query-performance-budgets-desde-g20)
      - [PD74: Validation Rules Complete (desde G21)](#pd74-validation-rules-complete-desde-g21)
      - [PD75: Migration Path Documented (desde G22)](#pd75-migration-path-documented-desde-g22)
      - [PD76: Pattern Success Metrics (desde G25)](#pd76-pattern-success-metrics-desde-g25)

## §1. FUNDAMENTOS

```yaml
Naturaleza_Principios:
  "Principio de Diseño = Regla operativa derivada de invariante teórico.
   Traduce verdad abstracta en criterio decisión aplicable."

Método_Derivación:
  Invariante (I) → Principio (PD) → Criterio Verificable
  
  Ejemplo:
    I1 (Minimalidad) → PD1 (Justificar Complejidad) → 
    "Nueva entidad requiere business case probando irreducibilidad"

Propiedad_Trazabilidad:
  ∀ PD: ∃ I | PD deriva de al menos un invariante

Propósito:
  Derivar reglas diseño arquitectónico desde invariantes sistema (Parte III)

Total_Principios: 76 (PD1-PD76)
  Distribución:
    - PD1-PD40: Desde Invariantes I1-I8 (40 principios universales)
    - PD41-PD46: Desde AOC+Kelly (6 métricas operacionales configurables)
    - PD47-PD76: Desde Guidelines G## (30 principios implementación específica)
```

## §2. DESDE I1: MINIMALIDAD

```yaml
Enunciado_I1: "Sistema usa mínimo número primitivos necesarios y suficientes"

PD1_Justificación_Entidad:
  "Toda nueva entidad (capacidad, flujo, información, límite, propósito) 
   debe justificar su existencia demostrando irreducibilidad."
   
  Criterio_Verificable:
    BEFORE create(entidad):
      justification = {
        why_not_reuse: "¿Por qué entidad existente no sirve?",
        why_not_compose: "¿Por qué composición existentes insuficiente?",
        expected_roi: "Beneficio > costo creación + mantenimiento"
      }
      IF NOT all(justification) THEN REJECT
      
  Aplicación:
    - Nueva capacidad → ¿Por qué no reusar/entrenar existente?
    - Nuevo flujo → ¿Por qué no adaptar flujo similar existente?
    - Nueva información → ¿Por qué no derivar de existente?
    
  Anti-Pattern_Combatido:
    Proliferación entidades (capability sprawl, flow duplication)

PD2_Composición_Antes_Creación:
  "Preferir composición de primitivos existentes sobre creación nuevos."
  
  Operadores_Composición:
    Capacidad: Team = ⊕(C1, C2, ..., Cn) [paralelo]
    Flujo: Pipeline = F1 ⊗ F2 ⊗ F3 [secuencial]
    Información: Report = ∪(I1, I2, ..., In) [agregación]
    
  Criterio:
    IF exists_composition(entidades_existentes) THAT satisfies_requirement
    THEN compose
    ELSE create_new
    
  Ejemplo:
    Requiere: "Capacidad ML + Human review"
    Solución: Mixto = ML_Model ⊕ Human_Reviewer
    NO crear: "ML_With_Review" como primitivo nuevo

PD3_Eliminación_Redundancia:
  "Detectar y eliminar entidades redundantes o subusadas."
  
  Métricas_Sunset:
    - Capacidad: utilization < 20% por 3 meses → candidato sunset
    - Flujo: executions < 10/mes → revisar necesidad
    - Información: access_count = 0 por 6 meses → archive
    - Límite: violations = 0 Y no preventivo → posible eliminar
    - Propósito: abandoned por 2 quarters → retire
    
  Proceso:
    1. Quarterly: Audit entidades subusadas
    2. Review: ¿Aún necesarias?
    3. Deprecate: Marcar deprecated con timeline
    4. Sunset: Eliminar tras período transición

PD4_Parsimonia_Propiedades:
  "Entidades solo tienen propiedades necesarias, no 'por si acaso'."
  
  Test:
    ∀ propiedad P en schema:
      - ¿Se usa en al menos 1 interfaz dominio?
      - ¿Es calculable desde otras propiedades? → derivada, no persistida
      - ¿Contribuye a invariante o decisión? → justificada
      
  Ejemplo_Negativo:
    Capacidad.favorite_color: String  # NO justificado → eliminar
    
  Ejemplo_Positivo:
    Capacidad.utilization → calculable desde assignments → derivada OK

PD5_Agregación_Lazy:
  "Información agregada se calcula on-demand, no pre-computada 
   salvo requisito performance demostrado."
   
  Razón:
    Pre-agregación = complejidad + riesgo inconsistencia
    
  Excepción:
    IF query_frequency > 100/día AND computation_cost > 1s
    THEN materialized_view justificado
```

## §3. DESDE I2: ORTOGONALIDAD

```yaml
Enunciado_I2: "Primitivos son mutuamente independientes sin overlap"

PD6_Separación_Concerns:
  "Cada entidad tiene responsabilidad única bien definida."
  
  Test_Ortogonalidad:
    ∀ entidad E1, E2 de diferente tipo:
      - Cambiar E1 NO requiere cambiar E2
      - E1.propiedades ∩ E2.propiedades = ∅
      
  Aplicación:
    - Capacidad define QUIÉN, Flujo define SECUENCIA
    - Límite RESTRINGE, Propósito DIRECCIONA
    - NO mezclar responsabilidades
    
  Violación_Ejemplo:
    Capacidad.target_okr → INCORRECTO
    (Propósito es responsabilidad de primitivo Propósito)
    
  Corrección:
    Propósito.owner_capacity_id → CORRECTO
    (Propósito referencia Capacidad, no al revés)

PD7_Relaciones_Explícitas:
  "Relaciones entre primitivos son explícitas, no embebidas."
  
  Patrón:
    Entidad_A {
      id: UUID,
      related_B_id: UUID  # Referencia explícita
    }
    
  Anti-Pattern:
    Entidad_A {
      id: UUID,
      embedded_B: Entidad_B  # Embebido rompe ortogonalidad
    }
    
  Excepción_Composición:
    Capacidad.composition.component_ids OK porque composición
    es propiedad intrínseca de Capacidad Mixta

PD8_Cambio_Local:
  "Modificar primitivo no propaga cambios forzados a otros."
  
  Implicación_Arquitectura:
    - Schema changes localizados
    - Versioning por entidad independiente
    - Migrations no acopladas
    
  Test:
    IF change(Primitivo_P) THEN 
      affected_entities SHOULD be only Entities_referencing_P
      NOT entities_of_different_primitive_type

PD9_Interfaces_Mínimas:
  "Interfaces entre primitivos/dominios son mínimas y bien definidas."
  
  Principio:
    Cada primitivo expone SOLO operaciones necesarias por dominio
    
  Matriz_Cobertura:
    51 operaciones total (ver §7 Parte I)
    Promedio: ~3 ops por (primitivo, dominio)
    
  Anti-Pattern:
    God_Interface con 20+ métodos mezclados → violar ortogonalidad
```

## §4. DESDE I3: TRAZABILIDAD

```yaml
Enunciado_I3: "Toda transformación, decisión y artefacto tiene 
               origen, responsable y justificación rastreables"

PD10_Metadata_Obligatoria:
  "Toda entidad incluye metadata creación/modificación."
  
  Campos_Obligatorios:
    created_by: UUID [Capacidad humana/mixta]
    created_at: Timestamp [inmutable]
    updated_at: Timestamp [actualiza cada cambio]
    version: Integer [incremental]
    
  Rationale:
    Accountability requiere saber quién/cuándo/por qué

PD11_Lineage_Completo:
  "Información registra cadena producción completa (DAG)."
  
  Implementación:
    lineage: {
      produced_by_flow: UUID | null,
      produced_by_capacity: UUID | null,
      parent_info_ids: List<UUID>,  # DAG ancestors
      transformation: String
    }
    
  Consulta_Típica:
    trace_lineage(info_id) → DAG completo hasta fuentes originales
    
  Aplicación_Regulatoria:
    GDPR Art.30: "Records of processing activities"
    → Lineage satisface requisito

PD12_Audit_Trail_Inmutable:
  "Eventos críticos se registran en log inmutable."
  
  Eventos_Auditables:
    - Cambios estructura (D1): reorg, nuevos roles
    - Decisiones estratégicas (D3): OKR setting, priorización
    - Violaciones límites (D2): compliance breaches
    - Delegación algorítmica (I5): cambio modo M1→M6
    
  Propiedad:
    Audit_log append-only, no editable
    Retention según compliance (7 años típico)

PD13_Decision_Records:
  "Decisiones arquitectónicas documentadas con ADR."
  
  Template_ADR:
    - Título: Decisión en forma statement
    - Contexto: Problema/oportunidad
    - Opciones: Alternativas consideradas
    - Decisión: Qué se decidió
    - Consecuencias: Tradeoffs aceptados
    - Status: Proposed | Accepted | Deprecated
    
  Scope:
    Type_1 decisions (irreversibles) → ADR obligatorio
    Type_2 decisions (reversibles) → ADR opcional
```

## §5. DESDE I4: CLASIFICACIÓN CONTEXTUAL

```yaml
Enunciado_I4: "Componente operativo tiene rol Producción o Habilitación 
               según contexto organizacional"

PD14_Test_Cliente_Externo:
  "Producción = output consumido directamente por cliente externo/pagador."
  
  Test_Operativo:
    IF destinatario.paga_por(output) OR destinatario.external
    THEN Producción
    ELSE Habilitación
    
  Ejemplo_Fintech:
    API_Pagos → Cliente usa directamente → Producción
    
  Ejemplo_Retail:
    API_Pagos → Solo backend interno → Habilitación

PD15_Test_Amplificación:
  "Habilitación = output amplifica capacidad de otros componentes internos."
  
  Test_Operativo:
    IF output → Capacidad_Interna AND mejora(velocidad | calidad | costo)
    THEN Habilitación
    
  Ejemplo:
    CI/CD → Desarrolladores deployan 10x más rápido → Habilitación
    Monitoring → SRE detecta issues más temprano → Habilitación

PD16_Documentar_Contexto:
  "Clasificación incluye justificación contextual explícita."
  
  Campo_Requerido:
    role_context: String [explicación por qué Prod/Habilitación]
    
  Ejemplo:
    Capacidad: Internal_API
    role: Habilitación
    role_context: "80% uso interno, 20% partners B2B. 
                   Dominante interno → Habilitación."

PD17_Reclasificación_Explícita:
  "Cambio contexto requiere reclasificación documentada."
  
  Trigger_Reclasificación:
    - Pivote negocio (tool interna → producto)
    - Cambio destinatario (interno → externo)
    - Adquisición/fusión (contexto org cambia)
    
  Proceso:
    1. Detect: Context shift
    2. Evaluate: Nuevo test Prod/Habilitación
    3. Reclassify: Update role + role_context
    4. Propagate: Ajustar métricas/governance según nuevo rol
    
  Implicación_Gobernanza:
    Producción → SLA estrictos, soporte 24/7, revenue tracking
    Habilitación → Efficiency focus, internal users, cost optimization
```

## §6. DESDE I5: HAIC (Human-AI Collaboration)

```yaml
Enunciado_I5: "Sistema es colaboración humano-AI TRANSVERSAL donde humanos
               establecen propósito, AI amplifica capacidades en TODOS dominios,
               y accountability permanece humana con override siempre disponible."

PD18_Accountability_Humana_Transversal:
  "Toda decisión/acción crítica en CUALQUIER dominio tiene humano accountable identificable."
  
  Implementación:
    ∀ entidad_crítica ∈ {D1_Tecnológico, D2_Informacional, D3_Organizacional, D4_Escalar}:
      ownership.accountable_capacity.substrate ∈ {Humano, Mixto}
      
  Entidades_Críticas_Cross_Domain:
    D1: Capacidad DevOps AI → delegated_from (engineer humano)
    D2: Capacidad Data AI → delegated_from (data steward humano)
    D3: Capacidad Coach AI → delegated_from (manager humano)
    D4: Capacidad Coordination AI → delegated_from (coordinator humano)
    
  Invariante_Sistema:
    NEVER: Algorítmico accountable de algorítmico EN NINGÚN DOMINIO
    ALWAYS: Human-in-the-loop para accountability TODOS DOMINIOS
    NEVER: TF7 como único lugar AI (HAIC es transversal)

PD19_Delegación_Explícita_Cross_Domain:
  "Capacidad algorítmica en CUALQUIER dominio solo opera con delegación explícita documentada."
  
  Campos_Obligatorios (si substrate=Algorítmico):
    ownership.delegated_from: UUID [humano delegador]
    ownership.delegation_mode: {M1..M6}
    ownership.domain: {D1, D2, D3, D4} [explícito]
    
  Modos_Delegación (aplicables TODOS dominios):
    M1_Monitorear: Observa, no actúa
    M2_Informar: Sugiere, humano decide
    M3_Habilitar: Humano invoca, algorítmico ejecuta
    M4_Controlar: Decide dentro reglas, humano excepciones
    M5_Coproducir: Colaboración mixta
    M6_Ejecutar: Autónomo, humano supervisa periódico
    
  Ejemplos_Transversalidad:
    D1: GitHub Copilot (M3 - habilitar code generation)
    D2: AI Data Analyst (M2 - informar insights)
    D3: AI Coach 1:1 (M2 - informar sugerencias)
    D4: Multi-site Coordinator AI (M4 - controlar scheduling)
    
  Regla_Progresión:
    Autonomía incrementa SOLO si trajectory prueba confiabilidad
    Aplica IGUAL en todos dominios (Ver PD22-PD25)

PD20_Override_Capability_Universal:
  "Humano puede intervenir/override decisión algorítmica siempre, EN CUALQUIER DOMINIO."
  
  Mecanismos_Requeridos (todos dominios):
    - Circuit_breaker: Pausar sistema algorítmico
    - Manual_override: Corregir decisión específica
    - Escalation_path: Cuándo/cómo escalar a humano
    
  Implementación_Por_Dominio:
    D1_Tecnológico:
      - Manual deploy capability (override AI CD)
      - Infrastructure freeze (pausar AI changes)
      
    D2_Informacional:
      - Human veto análisis AI
      - Ajuste thresholds anomaly detection
      
    D3_Organizacional:
      - Manager override AI coach suggestions
      - Human final say decisiones personas
      
    D4_Escalar:
      - Coordinator override AI scheduling
      - Escalation to regional leadership
    
  Implementación_UI:
    Dashboard algorítmico incluye botón "Override" prominente SIEMPRE
    Log override events para análisis posterior (trajectory I6)

PD21_Explainability_Transversal:
  "Capacidad algorítmica en CUALQUIER DOMINIO debe explicar decisiones a humano accountable."
  
  Nivel_Explicación_Por_Modo (universal):
    M1-M2: Explicación detallada (humano evalúa)
    M3-M4: Explicación sumaria (humano audita)
    M5-M6: Explicación on-demand (humano supervisa)
    
  Técnicas_Por_Dominio:
    D1_Tecnológico:
      - Code diff explanation (Copilot)
      - Infrastructure change reasoning (IaC AI)
      - Pipeline optimization rationale
      
    D2_Informacional:
      - Feature importance (ML models)
      - Anomaly detection reasoning
      - Data quality issue explanation
      
    D3_Organizacional:
      - Reasoning trace coaching advice (LLM chain-of-thought)
      - Decision support scenario explanation
      - Meeting summary derivation
      
    D4_Escalar:
      - Scheduling decision rationale
      - Resource allocation reasoning
      - Coordination conflict resolution logic
    
  Requisito_Compliance:
    EU AI Act: High-risk AI systems require explainability (CUALQUIER dominio)
    HAIC: Explainability prerequisito accountability (I5)
  
  Bounded_Autonomy_M6:
    "Delegación M6 requiere límites explícitos en 6 dimensiones:"
    
    Dimensiones_Bounds:
      1. Financial_Bounds:
         Tipo: Budget ceiling
         Ejemplo: Max $10K aprobación sin escalación
         Enforcement: Block transaction si > limit
      
      2. Operational_Scope:
         Tipo: Domain boundary
         Ejemplo: Deploy solo services owned by team
         Enforcement: RBAC + policy checks
      
      3. Reputational_Risk:
         Tipo: Public impact assessment
         Ejemplo: No comunicación externa sin review
         Enforcement: Pre-publish approval gate
      
      4. Legal_Compliance:
         Tipo: Regulatory adherence
         Ejemplo: GDPR/SOC2/PCI-DSS mandatory
         Enforcement: Policy-as-Code (OPA)
      
      5. Temporal_Bounds:
         Tipo: Time windows
         Ejemplo: Cambios solo business hours
         Enforcement: Cron-based gate + on-call override
      
      6. Scope_Bounds:
         Tipo: Resource/data limits
         Ejemplo: Modificar solo DBs team owns
         Enforcement: Permission matrix + audit
    
    Operacionalización:
      Ver metodologia §0.4.1 para implementación ejecutable
      Ver metodologia §12.4 para gestión excepciones
```

## §7. DESDE I6: TRAJECTORY-AWARENESS

```yaml
Enunciado_I6: "Capacidad algorítmica evoluciona informada por trayectoria uso.
               Sistema registra, aprende y adapta."

PD22_Trajectory_Log:
  "Toda ejecución algorítmica registra input/output/contexto/feedback."
  
  Schema_Trajectory_Event:
    {
      execution_id: UUID,
      capacity_id: UUID,
      timestamp: Timestamp,
      input: JSON,
      output: JSON,
      context: {system_state, constraints_active},
      latency_ms: Integer,
      success: Boolean,
      human_feedback: {override: Boolean, rating: Float} | null
    }
    
  Retention:
    Mínimo: 90 días (análisis reciente)
    Óptimo: 1+ años (detectar patterns long-term)

PD23_Progresión_Gradual:
  "Autonomía algorítmica incrementa progresivamente con trajectory probada."
  
  Patrón_Típico:
    T0: M1 (Monitorear) - Acumula datos
    → IF success_rate > 70% AND executions > 100 THEN M2
    
    T1: M2 (Informar) - Humano evalúa sugerencias
    → IF acceptance_rate > 80% AND low_risk THEN M3
    
    T2: M3 (Habilitar) - Uso on-demand
    → IF success_rate > 85% AND latency_critical THEN M4
    
    T3: M4 (Controlar) - Mayoría automática
    → IF success_rate > 95% AND low_risk THEN M6
    
    T4: M6 (Ejecutar) - Altamente confiable
    
  Propiedad_NO_Saltar:
    NEVER: M1 → M6 directo (anti-pattern)
    ALWAYS: Validar cada nivel antes promoción

PD24_Drift_Detection:
  "Monitoreo continuo detecta degradación performance."
  
  Señales_Drift:
    - Success_rate decae > 5% vs baseline
    - Human_override_frequency aumenta > 20%
    - Latency aumenta sin causa infraestructural
    - Input_distribution diverge (KL divergence > threshold)
    
  Acción_Mitigación:
    IF drift_detected:
      1. Alert humano accountable
      2. Reducir autonomía (M6→M4, M4→M3)
      3. Trigger re-training
      4. Investigate root cause

PD25_Continuous_Learning:
  "Capacidad algorítmica mejora con trajectory acumulada."
  
  Técnicas:
    - Online_learning: Actualiza con cada observación
    - Periodic_retraining: Batch mensual/trimestral
    - Fine_tuning: Ajusta con datos org específicos
    - RLHF: Feedback humano informa reward function
    
  Frecuencia_Retraining:
    Depende drift_rate:
      Fast_drift (días): Weekly retraining
      Medium_drift (semanas): Monthly
      Slow_drift (meses): Quarterly
```

## §8. DESDE I7: EMERGENCIA COMPLEJIDAD

```yaml
Enunciado_I7: "Capacidades organizacionales emergen en niveles complejidad.
               No son módulos integrados, son propiedades emergentes."

PD26_Nivel_Apropiado:
  "Práctica se implementa solo si org alcanzó nivel complejidad mínimo."
  
  Niveles_Emergencia:
    Agile → L1 (Decisión Local) - 10+ personas
    DevOps → L2 (Reflexión Operacional) - 20+ personas
    EA → L3 (Reflexión Estructural) - 50+ personas
    TD → L4 (Reflexión Estratégica) - 200+ personas
    ORKO → L5 (Meta-Reflexión) - Framework level
    
  Anti-Pattern:
    Startup 15 personas intenta EA formal (L3)
    → Overhead > beneficio (complejidad insuficiente)
    
  Test_Readiness:
    IF personas_count < threshold_nivel(práctica)
    THEN defer_until_scaled

PD27_No_Saltar_Niveles:
  "Consolidar nivel N antes intentar N+2."
  
  Regla:
    L0 → L1 → L2 → L3 → L4 → L5
    NO saltar (ej: L1 → L4 directamente)
    
  Razón:
    Cada nivel provee fundación para siguiente
    Saltar = fundación débil, colapso eventual
    
  Ejemplo_Negativo:
    Org L1 (sin DevOps) intenta TD full-scale (L4)
    → Fracasa porque no tiene CI/CD, automation, metrics (L2)

PD28_Señales_Transición:
  "Transición nivel N→N+1 ocurre cuando señales umbral presentes."
  
  L0→L1: Volumen requiere decisiones distribuidas
  L1→L2: Ineficiencias repetidas requieren reflexión
  L2→L3: Coordinación inter-teams requiere estructura
  L3→L4: Ambiente cambia requiere nuevo propósito
  L4→L5: Frameworks existentes insuficientes
  
  Trigger_Cuantitativo:
    L2→L3: 
      - Personas > 50
      - Teams interdependientes > 5
      - Handoffs ralentizan (cycle_time 2x ideal)
      - Duplicación esfuerzos detectada

PD29_Inclusión_Niveles:
  "Org nivel N incluye capacidades niveles 0..(N-1)."
  
  Propiedad:
    Nivel_N CONTIENE Nivel_(N-1)
    NO reemplaza
    
  Ejemplo_L4_Org:
    - L0: RPA, automation (ejecución mecánica)
    - L1: Supervisores, decisiones locales
    - L2: Teams, retrospectives, mejora continua
    - L3: Arquitectos, diseño estructural
    - L4: C-level, reflexión estratégica
    
    TODOS presentes simultáneamente

PD30_Health_Prerequisito:
  "H_org ≥ 70 prerequisito para transformación estructural."
  
  Regla_Bloqueo:
    IF H_org < 70 THEN block(transformaciones_mayores)
    
  Rationale:
    Org enferma no soporta cambio estructural adicional
    Primero estabilizar salud, luego transformar
    
  Acción:
    IF H_org < 70:
      1. Diagnose: Qué score bajo (A, P, D, O)
      2. Intervene: Playbooks específicos (Parte V)
      3. Stabilize: H_org > 70
      4. THEN: Permitir transformaciones

PD31_Cohesión_Máxima:
  "Dentro de dominio, maximizar cohesión:
   skills, información, autoridad co-located."
   
  Origen: AOC P4 (Cohesión Máxima)
  
  Formalización:
    cohesion(dominio) = internal_connectivity / potential_connectivity
    Target: cohesion > 0.70
    
  Complemento_PD7:
    - PD7: Relaciones explícitas (ortogonalidad ENTRE primitivos)
    - PD31: Cohesión máxima (integración DENTRO de dominio)
    → Juntos: Low coupling externa + High cohesion interna
    
  Mecánica:
    - T-shaped individuals (profundidad en especialidad dominio)
    - Información compartida (dashboards, docs accesibles)
    - Co-location (física/virtual reduce communication friction)
    - Cross-functional (todas skills dentro de equipo)
    
  Test_Verificación:
    ¿Equipo tiene todas skills para entregar value sin dependencies?
    ¿Información crítica accesible dentro equipo (no externa)?
    ¿Decisiones >70% tomadas dentro sin escalaciones?
    
  Métrica:
    Cohesion_Index = (internal_interactions) / (total_interactions)
    Target: >0.70

PD32_Incompatibilidad_α_β:
  "Arquetipos Creadores (α) y Operadores (β) NO coexisten en mismo dominio."
  
  Origen: AOC Matriz Incompatibilidad (α↔β interferencia destructiva)
  
  Rationale:
    - α (Creadores): Innovación requiere disrupción, experimentación
    - β (Operadores): Operación requiere estabilidad, consistencia
    → Valores fundamentalmente contradictorios
    
  Consecuencia_Violación:
    "Rainbow Group" anti-pattern (AP13):
    - Innovation sufre (no tiempo, risk-averse)
    - Operations sufre (instabilidad, incidents)
    - Team identity confusa ("¿qué somos?")
    - Mediocrity: Ni innova NI opera bien
    
  Solución_Estructural:
    Separar dominios:
    - Dominio_A (α): R&D, new products, innovation team
    - Dominio_B (β): Production, SRE, operations team
    - Interface: APIs, SLAs bien definidos
    - NO merge (mantener separados)
    
  Test_Detección:
    IF dominio.archetype={α,β} simultáneamente
    THEN warning("Rainbow Group detectado")
    
  Excepción_Permitida:
    Platform teams (AT2) pueden tener β dominante con α minoritario
    si purity_pct(β) > 80% (innovación incremental plataforma)

PD33_Incompatibilidad_γ_δ:
  "Arquetipos Conectores (γ) y Descubridores (δ) separados."
  
  Origen: AOC Matriz (γ↔δ interferencia)
  
  Rationale:
    - γ (Conectores): Facilitan, coordinan, bias hacia capacidades internas
    - δ (Descubridores): Diagnostican necesidades, requieren objetividad sin bias
    → Descubrir requiere diagnóstico limpio (no sesgo hacia soluciones propias)
    
  Ejemplo_Violación:
    Product Manager (γ) que también hace discovery (δ):
    → Sesgo hacia features su team puede construir (no necesidad real cliente)
    
  Solución:
    - Discovery team (δ): Independiente, diagnostica sin agenda
    - Product/PM (γ): Coordina delivery, NO hace discovery
    - Handoff: δ → γ (requisitos validados → ejecución)
    
  Test:
    IF rol_combina(facilitar, descubrir) THEN alert("Conflict of interest")

PD34_Incompatibilidad_γ_ε:
  "Arquetipos Conectores (γ) y Validadores (ε) separados."
  
  Origen: AOC Matriz (γ↔ε interferencia)
  
  Rationale:
    - γ (Conectores): Servir requiere confianza, colaboración
    - ε (Validadores): Auditar requiere distancia, arm's length
    → No se puede servir y auditar simultáneamente (conflict trust)
    
  Ejemplo_Violación:
    Scrum Master (γ) que también evalúa performance team (ε):
    → Team no confía (defensive), facilitación comprometida
    
  Solución:
    - Facilitators (γ): Enable sin juzgar
    - Auditors (ε): Independientes, reportan aparte
    - Separación física: Diferentes reporting lines
    
  Test:
    IF capacity.roles incluye {facilitar, auditar} THEN error("Incompatible")

PD35_Incompatibilidad_δ_ε:
  "Arquetipos Descubridores (δ) y Validadores (ε) separados."
  
  Origen: AOC Matriz (δ↔ε interferencia)
  
  Rationale:
    - δ (Descubridores): Descubrir necesidades requiere apertura, exploración
    - ε (Validadores): Validar requiere criterio estricto, cierre
    → Descubrimiento abierto incompatible con juicio cerrado
    
  Ejemplo_Violación:
    User Researcher (δ) que también valida compliance (ε):
    → Usuarios no abiertos (fear judgment), insights comprometidos
    
  Solución:
    - Discovery (δ): Explora sin juzgar (curiosidad)
    - Validation (ε): Juzga contra criteria (rigor)
    - Sequential: δ primero (understand), luego ε (validate)
    
  Test:
    IF capacity combina(discover, validate) THEN warning("Role conflict")
```

## §9. MÉTRICAS OPERABLES (AOC + Kelly): PD41-PD46

```yaml
Origen_Dual:
  "Principios PD41-46 derivan de marcos complementarios:
   - Meyer AOC (Quantum Organizational Architecture)
   - Kelly Digital Transformation Discipline"
   
Naturaleza:
  "Métricas operacionales con gates verificables.
   Thresholds configurables según contexto organizacional."

PD41_AOC_Coherencia_Gate:
  "Coherencia organizacional debe superar umbral mínimo"
  
  Origen: Meyer AOC (90_referencias_fundacionales/02_arquitectura_organizacional.md)
  
  Fórmula:
    Coherencia = Σ(Valor_entregado) / Σ(Energía_invertida)
    Energía = Esfuerzo + Fricción + Interferencia
    
  Criterio_Verificable:
    Coherencia ≥ θ_coh
    θ_coh_default = 0.7 (configurable según contexto)
    
  Aplicación:
    - Input H_org (Health Score integrado)
    - Gate decisiones arquitectónicas estructurales
    - Monitoring continuo interferencia cross-domain
    
  Observabilidad:
    Dashboard D1_Arquitectura + D3_Decisión

PD42_AOC_Resonancia_Gate:
  "Resonancia equipo (T-shaped profiles) debe ser suficiente"
  
  Origen: Meyer AOC
  
  Fórmula:
    Resonancia = Profundidad_Especialización × Amplitud_Conexión
    
  Criterio_Verificable:
    Resonancia ≥ θ_res
    θ_res_default = 0.65 (configurable)
    
  Aplicación:
    - Detectar gaps skill en equipos
    - Validar cross-functional teams
    - Trigger training/hiring decisions
    
  Observabilidad:
    Dashboard D1_Arquitectura (team composition)

PD43_AOC_Flujo_Gate:
  "Flujo transferencia conocimiento/valor debe ser eficiente"
  
  Origen: Meyer AOC
  
  Fórmula:
    Flujo = Tasa_Creación_Valor / (1 + Fricción_Transferencia)
    
  Criterio_Verificable:
    Flujo ≥ θ_flu
    θ_flu_default = 0.6 (configurable)
    
  Aplicación:
    - Optimización handoffs cross-team
    - Reducción dependencies bloqueantes
    - Flow efficiency metrics
    
  Observabilidad:
    Dashboard D4_Operación (flow metrics)

PD44_TD_Small_Batches_Gate:
  "Mayoría trabajo debe ejecutarse en small batches"
  
  Origen: Kelly Digital Transformation
  
  Fórmula:
    Small_Batch_Ratio = % work_items con size ≤ threshold
    
  Criterio_Verificable:
    Small_Batch_Ratio ≥ θ_sb
    θ_sb_default = 0.80 (80% work en small batches)
    
  Aplicación:
    - Reducir batch size (story splitting)
    - Faster feedback loops
    - Lower risk per deployment
    
  Anti-Pattern:
    "Grandes lotes por defecto" (batch optimization local, global subóptimo)
    
  Observabilidad:
    Dashboard D4_Operación (work item sizing)

PD45_TD_Flow_Gate:
  "Lead time debe mantenerse bajo umbral contextual"
  
  Origen: Kelly Digital Transformation
  
  Fórmula:
    Lead_Time = time(committed) - time(delivered)
    
  Criterio_Verificable:
    p50(Lead_Time) ≤ θ_lt
    p95(Lead_Time) ≤ 2 × θ_lt
    θ_lt_default = contextual (tech: 7d, gov: 30d, configurable)
    
  Aplicación:
    - Monitoring flow efficiency
    - Detectar bottlenecks
    - Trigger process improvements
    
  Observabilidad:
    Dashboard D4_Operación (cycle time metrics)

PD46_TD_Quality_Speed_Gate:
  "Calidad y velocidad deben crecer juntas (no trade-off)"
  
  Origen: Kelly Digital Transformation
  
  Fórmula:
    Quality_Speed_Index = Defect_Rate × Cycle_Time (proxy inverso)
    Lower = Better (baja calidad ralentiza por rework)
    
  Criterio_Verificable:
    Quality_Speed_Index ≤ θ_qs
    θ_qs_default = contextual (configurable)
    
  Aplicación:
    - Validar quality ≠ slow (anti-correlation)
    - Detectar technical debt accumulation
    - Trigger refactoring/automation
    
  Anti-Pattern:
    "Move fast and break things" (no sostenible, rework loops)
    
  Observabilidad:
    Dashboard D4_Operación (quality × speed tracking)

Health_Score_Integration:
  "PD41-46 se integran como inputs H_org"
  
  Mapping:
    H1_Architecture ← PD41_Coherencia, PD42_Resonancia
    H4_Operation ← PD43_Flujo, PD44_Small_Batches, PD45_Flow, PD46_Quality_Speed
    
  Normalización:
    Todas métricas → [0..1] antes agregación weighted
    
  Configurabilidad:
    Thresholds θ_* ajustables vía Context Schema (PD36)
```

## §10. DESDE I8 (Parametrización Contextual): PD36-PD40

```yaml
PD36_Context_Explicit_Declaration:
  "Todo contexto organizacional debe declararse explícitamente mediante Context Schema"
  
  Origen: I8 (Parametrización Contextual)
  
  Rationale:
    - Adaptación requiere CONOCER contexto (36 parámetros)
    - Contexto implícito = decisiones arbitrarias, no trazables
    - Parametrización formal permite validación y repetibilidad
    
  Context_Schema_Obligatorio:
    ∀ organización O implementando ORKO:
      DEBE declarar:
        - ENV_TYPE, SECTOR, SUBSECTOR
        - SIZE, LOCATIONS, EMPLOYEES
        - JURISDICTION, LEGAL_FRAMEWORKS
        - H_org_CURRENT, INFRASTRUCTURE
        - CRISIS_TYPE, CRISIS_SEVERITY
        - BUDGET_ANNUAL, CONSTRAINTS
        - CHANGE_RESISTANCE, CULTURAL_FACTORS
        - GOAL_1, GOAL_2, GOAL_3
        
  Implementación:
    Template: context_schema.yaml
    Tool: context_analyzer (CLI/web)
    Validation: 36 parámetros completos
    
  Anti-Pattern:
    "Empezar implementación sin Context Schema"
    → Resulta en adaptación ad-hoc, no replicable
    
  Test:
    CHECK: ∃ context_schema.yaml en project root
    CHECK: 36 parámetros populated (no nulls críticos)

PD37_Genotype_Phenotype_Separation:
  "Separar estrictamente genoma (inmutable) de fenotipo (configurable)"
  
  Origen: I8 (Parametrización Contextual)
  
  Rationale:
    - Genoma = ontología universal (A1-A5, P1-P5, I1-I8, C1-C5)
    - Fenotipo = expresión contextual (metodología, templates, módulos)
    - Mixing niveles = pérdida coherencia ontológica
    
  Genoma_INMUTABLE:
    NO se puede:
      - Agregar/quitar axiomas
      - Modificar primitivos
      - Violar invariantes
      - Alterar contratos base
      
  Fenotipo_CONFIGURABLE:
    SÍ se puede:
      - Activar/desactivar módulos
      - Parametrizar templates
      - Seleccionar trajectory
      - Ajustar timelines
      
  Implementación:
    ../00_fundamentos_teoricos/ → INMUTABLE (genoma)
    ./ → INMUTABLE (contratos, principios base)
    ../30_metodologia_orko/ → CONFIGURABLE (expresión contextual)
    ../30_metodologia_orko/11_artefactos_templates/ → CONFIGURABLE (parametrizables)
    
  Anti-Pattern:
    "Modificar axiomas para acomodar contexto específico"
    → Destruye universalidad framework
    
  Test:
    CHECK: Genoma files read-only (metadata)
    CHECK: Cambios fenotipo NO modifican genoma
    CHECK: Trazabilidad fenotipo → genoma verificable

PD38_Parametric_Methodology_Expression:
  "Metodología debe expresarse mediante reglas parametrizadas, no hardcoded"
  
  Origen: I8 (Adaptación Contextual)
  
  Rationale:
    - Context Schema (36 params) → Expression Rules → Activation Profile
    - Reglas explícitas = auditables, repetibles, modificables
    - Hardcoding = frágil, no mantenible, no transferible
    
  Expression_Rules_Formales:
    R_COMPLIANCE(Context) → Modules:
      IF REGULATORY_PRESSURE = Critical:
        ACTIVATE: compliance_modules[jurisdiction]
        
    R_CRISIS(Context) → Trajectory:
      IF CRISIS_SEVERITY = Critical AND TIMELINE < 12:
        SELECT: Trajectory_MINIMAL
        
    R_SCALE(Context) → Orchestration:
      IF LOCATIONS > 20:
        ACTIVATE: multi_site_orchestration
        
    ... (6 reglas formales)
    
  Implementación:
    expression_engine.py:
      - Input: Context Schema
      - Process: Evaluate rules
      - Output: Activation Profile
      
  Anti-Pattern:
    "If org_name == 'GORE Ñuble' THEN activate_ltde()"
    → No generalizable, frágil, no principled
    
  Test:
    CHECK: Reglas declaradas como funciones puras
    CHECK: Context → Profile determinístico (mismas inputs = mismos outputs)
    CHECK: Nuevas reglas agregables sin modificar existentes

PD39_Adaptation_Traceability:
  "Toda adaptación contextual debe trazarse al genoma"
  
  Origen: I3 (Trazabilidad) + I8 (Adaptación Contextual)
  
  Rationale:
    - Adaptación sin trazabilidad = deriva conceptual
    - Cada módulo/template debe derivar formalmente de genoma
    - Permite validar fidelidad ontológica
    
  Trazabilidad_Obligatoria:
    ∀ módulo M activado:
      DEBE documentar:
        - genome_compatibility: [C*, I*, PD*] afectados
        - derivation_rationale: Por qué deriva de genoma
        - context_trigger: Qué parámetros contextuales lo activan
        - validation_passed: Checks genotype fidelity
        
  Implementación:
    module_spec.yaml:
      name: Module_LTDE_Adapter
      genome_compatibility:
        contracts: [C3, C4]
        invariants: [I8, I3]
        principles: [PD27, PD36]
      derivation:
        C3: "Ley 21.180 Art.18 requiere expedientes electrónicos → afecta P3 (INFORMACIÓN)"
        C4: "Deadline 2027 es límite temporal → afecta P4 (LÍMITE)"
      context_trigger:
        JURISDICTION: CHL
        LEGAL_FRAMEWORKS: contains(Ley_21180)
        
  Anti-Pattern:
    Módulo sin documentación derivación
    → No verificable si respeta genoma
    
  Test:
    CHECK: ∀ módulo, ∃ derivation docs
    CHECK: Contracts/invariants citados existen en genoma
    CHECK: Validation_passed = TRUE

PD40_Module_Composability:
  "Módulos deben ser componibles sin interferencias"
  
  Origen: I2 (Ortogonalidad) + I8 (Parametrización)
  
  Rationale:
    - Contextos complejos requieren MÚLTIPLES módulos simultáneos
    - Módulos interferentes = imposible satisfacer múltiples requisitos
    - Composabilidad = cada módulo independiente, interfaces claras
    
  Reglas_Composición:
    1. Ortogonalidad:
         ∀ (M1, M2): Overlap(M1, M2) < threshold
         → Módulos no duplican funcionalidad
         
    2. Interfaces_Compatibles:
         ∀ (M1, M2): Output(M1) compatible Input(M2)
         → Módulos pueden encadenarse
         
    3. No_Side_Effects_Globales:
         ∀ M: Cambios confinados a scope declarado
         → Módulo no modifica otros módulos
         
    4. Dependency_Explicit:
         IF M1 requiere M2:
           THEN dependencies: [M2] declarado
         → No dependencias ocultas
         
  Implementación:
    Validation_Composability:
      - Analyze module pairs interferencias
      - Check dependency graph acíclico
      - Verify interface contracts
      
  Anti-Pattern:
    Module_A modifica global state usado por Module_B
    → Composición impredecible, frágil
    
  Test:
    CHECK: ∀ pair(M1,M2), interference = NONE
    CHECK: Dependency graph is DAG (no cycles)
    CHECK: Integration tests múltiples módulos PASS
```

## §11. DESDE GUIDELINES G## (Operacionalización): PD47-PD76

```yaml
Origen_Guidelines:
  "Guidelines G## son extensiones operacionales de invariantes I1-I8,
   traduciendo teoría en criterios implementables específicos."
   
Derivación:
  I## (Invariantes Layer 0) → G## (Guidelines operacionales) → PD## (Principios diseño)
  
Mapeo_Completo:
  Ver ../00_introduccion.md §5 para lista completa G## y su fundamentación
  
Total_Principios: 30 (PD47-PD76)
  Distribución temática:
    - Definicionales: PD47-51 (composición, handoffs, alignment)
    - Lifecycle: PD52-54 (estados, transiciones, deprecación)
    - Estados: PD55-58 (snapshots, reachability, convergencia)
    - Execution/DORA: PD59-63 (tracking, métricas, incidents)
    - Governance: PD64-68 (portfolio, automation, patterns)
    - Vistas: PD69-72 (dashboards, templates, integración)
    - Refinamientos: PD73-76 (performance, validación, migración)
```

### Principios Definicionales (PD47-51, desde G26-G30)

#### PD47: Composition Acyclicity Transitive (desde G26)

```yaml
Origen: I2 (Ortogonalidad) + A2 (Capacidad)

Enunciado:
  "Composition cycles deben validarse transitivamente,
   no solo direct parent-child relationships."

Criterio_Verificable:
  ∀ update Capacidad.composition:
    Execute Q16_Validate_Composition_Acyclic()
    IF FALSE THEN REJECT WITH ERROR "Cycle detected: [path]"
    
  Validation: Topological sort algorithm (Kahn)
  Complexity: O(V+E) donde V=capacidades, E=composition edges

Ejemplo_Detección:
  Team_A composed_of [Person_1, Team_B]
  Team_B composed_of [Person_2, Team_C]
  Team_C composed_of [Person_3, Team_A]
  → Topological sort FAILS
  → System reports: "Composition cycle: A→B→C→A"

Performance:
  Run on INSERT/UPDATE only (not read)
  Cache composition graph structure
  Invalidate cache on any composition change

Anti-Pattern:
  Only check immediate parent-child
  → Miss transitive cycles (A→B→C→A)
```

#### PD48: Handoff Formal Definition (desde G27)

```yaml
Origen: A1 (Transformación) + A2 (Capacidad) + Conway's Law

Enunciado:
  "Handoff se cuenta SOLO si transición cross-team.
   Intra-team collaboration NO penaliza flow efficiency."

Definición_Formal:
  handoff(step_i, step_j) ⟺ 
    step_j depends_on step_i AND
    step_i.capacity.team_id ≠ step_j.capacity.team_id

Criterio_Verificable:
  ∀ flujo: handoff_ratio calculado consistentemente:
    handoffs = Σ handoff(step_i, step_i+1) for all sequential pairs
    transitions = COUNT(dependencies in DAG)
    handoff_ratio = handoffs / transitions
    
  Target: handoff_ratio < 0.20 (20%)

Casos_Especiales:
  - Intra-team handoff NO cuenta (mismo team_id)
  - Cross-person within team NO es handoff
  - Async queue ES handoff si cross-team
  - Parallel steps NO handoff (no sequential dependency)

Anti-Pattern:
  Contar TODOS handoffs (incluso intra-team)
  → Penaliza colaboración dentro equipos cohesivos
  → False positives en metrics

Implementación:
  Query Q14_Handoff_Count(flow_id) → {handoff_count, ratio}
```

#### PD49: Alignment Weighted Recursive (desde G28)

```yaml
Origen: A5 (Intencionalidad) + I4 (Classification Contextual)

Enunciado:
  "Alignment score calculado recursivamente desde leafs,
   weighted por importancia relativa KRs."

Fórmula:
  IF propósito LEAF:
    alignment = AVG(progress_kr_i)
    
  IF propósito PARENT:
    alignment = Σ(weight_i × progress_child_i × contribution_i) / Σ weight_i

Criterio_Verificable:
  ∀ propósito parent con children:
    alignment_score ∈ [0, 1]
    IF all children.progress = 1.0 THEN parent.alignment ≈ 1.0
    IF any child.progress = 0 THEN parent.alignment < 1.0
    
  Properties:
    - Recursive: Parent score deriva de children
    - Weighted: Importance-weighted average
    - Bounded: [0..1] score
    - Monotonic: Child progress ↑ → Parent ↑

Implementación:
  Recursive query Q15_Alignment_Score_Recursive
  Cache intermediate results (performance optimization)
  Update on OKR progress change (event-driven)

Anti-Pattern:
  Simple average sin weights
  → No refleja prioridades estratégicas
  → Todos KRs treated equally (unrealistic)
```

#### PD50: Violation Severity Weighted (desde G29)

```yaml
Origen: A4 (Restricción) + I1 (Minimalidad información)

Enunciado:
  "Violations deben ponderarse por severity, no solo contar.
   1 Critical >> 10 Minor en impacto organizacional."

Fórmula_Severity_Score:
  severity_score = Σ (weight_level × count_level)
  
  Weights:
    Minor: 1
    Moderate: 5
    Major: 20
    Critical: 100

Criterio_Verificable:
  ∀ límite con violations:
    violations_summary.severity_score calculado
    IF severity_score > threshold THEN alert escalation
    
  Thresholds:
    severity_score < 10: Normal operation
    severity_score 10-50: Atención requerida
    severity_score > 50: Crítico (bloquear new work PD30)

Implementación:
  A5_Violations métrica USA severity_score
  NO solo violations_count
  Dashboard muestra breakdown por severity

Anti-Pattern:
  COUNT(violations) sin severity
  → 100 minor violations = 1 critical (FALSE equivalence)
  → Priorización incorrecta remediación
```

#### PD51: Observable Standard Units (desde G30)

```yaml
Origen: I3 (Trazabilidad) + A3 (Información coordinación)

Enunciado:
  "Observables deben reportarse en units canónicas
   para comparabilidad cross-org y temporal."

Especificación:
  ∀ observable ∈ {EX1-8, IN1-8}:
    - primary_unit definida explícitamente
    - alt_units documented (si aplicable)
    - conversion_factors specified
    - measurement_protocol established

Criterio_Verificable:
  ∀ observable en dashboard:
    Display format: "value + unit + scale"
    Ejemplo: "NPS: 45 [-100..100]" NO solo "45"
    
  Validation:
    IF observable_id NOT NULL THEN unit especificada
    IF unit NOT in {primary, alt_units} THEN REJECT

Implementación:
  C3.observable_units_standard tabla completa
  D2.1 Dashboard shows "value + unit" siempre
  Export data includes unit metadata

Anti-Pattern:
  Heterogeneous units sin especificar
  → "Velocity: 10" (¿features? ¿story points? ¿LOC?)
  → Incomparable across teams/time
```

### Principios Lifecycle (PD52-54, desde G11-G24)

#### PD52: Lifecycle Explicit Transitions (desde G11)

```yaml
Origen: I7.5 (Lifecycle States) + A2 (Capacidad)

Enunciado:
  "Capacidades transitan lifecycle states con triggers y acciones explícitas.
   Automated cuando posible."

Criterio_Verificable:
  ∀ capacidad: lifecycle.current_state definido
  Triggers auto: utilization<20%(4wks) → Active→Idle, idle>12wks → Deprecated

Anti-Pattern:
  Status sin lifecycle formal → Capacidades "zombie" (idle años, nobody owns)
```

#### PD53: Achievement Criteria Explicit (desde G12)

```yaml
Origen: A5 (Intencionalidad) + I3 (Trazabilidad accountability)

Enunciado:
  "Key Results especifican achievement criteria explícitos,
   no solo target_value numérico."

Criterio_Verificable:
  ∀ key_result: achievement.type definido, Σ weighting = 1.0

Anti-Pattern:
  Target sin context → "Velocity: 10" (¿threshold? ¿target? ¿range?)
```

#### PD54: Deprecation Phased Timeline (desde G24)

```yaml
Origen: G11 (Lifecycle) + A2 (Capacidad dependencies)

Enunciado:
  "Deprecation sigue timeline faseado: Announce → Deprecate → Disable → Delete
   con grace periods y notificaciones."

Fases: Announce(T-90d) → Deprecate(T-60d) → Disable(T-30d) → Delete(T=0)

Anti-Pattern:
  Immediate sunset sin notice → Breaks production, team frustration
```

### Principios Estados y Transiciones (PD55-58, desde G1-G23)

#### PD55: State Snapshot Consistency (desde G1)

```yaml
Origen: A1 (Transformación) + meta.md (Coherencia Temporal)

Enunciado:
  "Estado arquitectónico es snapshot consistente que satisface
   todos invariantes (INV_C1-C8) y constraints (R1-R15)."

Criterio_Verificable:
  ∀ estado: validate_state_consistency(state_id) = TRUE
  Validation ejecuta: INV_C1-C8, R1-R15 checks sobre snapshot

Anti-Pattern:
  Estado inconsistente (ej: flujo sin purpose_id) → Planning inválido
```

#### PD56: Transition Executability (desde G23)

```yaml
Origen: R15 (Transition-Flow) + A1 (Transformación)

Enunciado:
  "Toda transición arquitectónica debe tener ≥1 flujo operacional
   que ejecute el cambio. No transitions abstractas."

Criterio_Verificable:
  ∀ transition: execution_flows.length ≥ 1
  ∀ flow IN execution_flows: flow.status = Active OR Planned

Anti-Pattern:
  Target state sin execution plan → "Aspirational architecture" no operable
```

#### PD57: Reachability Validation (desde G2)

```yaml
Origen: R14 (State Transitions DAG) + I3 (Trazabilidad)

Enunciado:
  "Target state debe ser alcanzable desde current state vía
   secuencia válida de transiciones que preservan constraints."

Criterio_Verificable:
  reachable = Q21_Reachability_Validation(current, target)
  IF NOT reachable THEN target_state = INVALID

Anti-Pattern:
  Target inalcanzable (ej: requiere capacidad no contratada) → Waste planning effort
```

#### PD58: Convergence Monitoring (desde G13)

```yaml
Origen: M13 (Δ_arch) + meta.md (Adaptabilidad Estructurada)

Enunciado:
  "Convergencia target state debe monitorearse continuamente
   vía Δ_arch metric. Drift detection trigger replanning."

Criterio_Verificable:
  Δ_arch calculado weekly (mínimo)
  IF Δ_arch increases 2 weeks consecutivas THEN alert
  Convergence_rate = d(Δ_arch)/dt expected negative

Anti-Pattern:
  No tracking convergence → "Transformation theater" (activity sin progress medible)
```

### Principios Execution & DORA (PD59-63, desde G3-G7)

#### PD59: Execution Instance Tracking (desde G3)

```yaml
Origen: A1 (Transformación) + E7 (Flow Execution)

Enunciado:
  "Toda ejecución flujo debe generar E7 instance con metrics
   completas (cycle_time, handoffs, outputs)."

Criterio_Verificable:
  ∀ flow execution: E7 record created WITH metrics
  E7.flow_id → Flujo válido, E7.executed_by → Capacidad activa

Anti-Pattern:
  Flujos sin tracking → No datos para optimización, DORA metrics imposibles
```

#### PD60: DORA Metrics Mandatory (desde G4)

```yaml
Origen: M1-M4 (DORA) + DevOps Research

Enunciado:
  "Deployment flows DEBEN reportar M1-M4 DORA metrics.
   Elite performance: deploy freq >1/day, lead time <1d, CFR <5%, MTTR <1h."

Criterio_Verificable:
  ∀ deployment flow: Q22-Q25 queries executable
  Dashboard D4 muestra DORA metrics actualizados

Anti-Pattern:
  Velocity sin quality → High deploy freq pero CFR >20% (thrashing)
```

#### PD61: Incident Flow Linkage (desde G5)

```yaml
Origen: M4 (MTTR) + Incident management

Enunciado:
  "Incidents deben linkear a E7 execution que causó failure
   para root cause analysis y CFR calculation."

Criterio_Verificable:
  ∀ incident: caused_by_execution_id OR external_cause specified
  MTTR calculable vía incident.resolution_time

Anti-Pattern:
  Incidents sin root cause → Reactive firefighting, no learning
```

#### PD62: Health Score Composite (desde G6)

```yaml
Origen: H_org (Ecuación Maestra) + Dominios D1-D4

Enunciado:
  "H_org compuesto weighted de H1-H5 dimension scores.
   H_org ≥ 70 prerequisito para transformación estructural (PD30)."

Fórmula:
  H_org = H1×0.30 + H2×0.25 + H3×0.20 + H4×0.15 + H5×0.10
  
  H1_Architecture: Clarity (purpose cascade, limits defined)
  H2_Perception: Freshness (observables <24h, dashboard active)
  H3_Decision: Execution (OKR progress, portfolio prioritized)
  H4_Operation: Performance (DORA metrics, flow efficiency)
  H5_Governance: Compliance (violations severity_score <10)

Criterio_Verificable:
  H_org calculado mensualmente mínimo
  IF H_org < 70 THEN transformations bloqueadas (PD30)
```

#### PD63: Decision Audit Trail (desde G7)

```yaml
Origen: I3 (Trazabilidad) + D3 (Decisión)

Enunciado:
  "Decisiones D3 (OKR approval, portfolio priority, etc)
   deben registrar audit trail: who, when, rationale."

Criterio_Verificable:
  ∀ decision event: {decision_type, decided_by, decided_at, rationale}
  Audit log queryable: "¿Quién aprobó target state X?"

Anti-Pattern:
  Decisiones sin rationale → Politics, no accountability
```

### Principios Governance & Portfolio (PD64-68, desde G8-G15)

#### PD64: Portfolio Value Maximization (desde G14)

```yaml
Origen: Ecuación Maestra V_org + Q26 Portfolio Optimization

Enunciado:
  "Portfolio selection maximiza V_org bajo constraints (budget, capacity, H_org≥70).
   Knapsack optimization: ROI-weighted prioritization."

Criterio_Verificable:
  Q26_Portfolio_Value_Optimization ejecutado quarterly
  Selected purposes: Σ cost <= budget AND Σ effort <= capacity
  H_org maintained >= 70 (PD30 enforcement)

Anti-Pattern:
  "Pet projects" sin ROI → Resource waste, low V_org
```

#### PD65: Cross-Domain Health Balance (desde G15)

```yaml
Origen: H_org = H1-H5 weighted + Theory of Constraints

Enunciado:
  "H_org bottlenecked por lowest H_i score. Optimize weakest domain first
   (Theory of Constraints: system performance = bottleneck performance)."

Criterio_Verificable:
  Q27_Cross_Domain_Health identifica bottleneck monthly
  Improvement efforts allocated to lowest H_i domain
  
Fórmula:
  IF H4_Operation = MIN(H1-H5) THEN focus DORA metrics improvement
  IF H1_Architecture = MIN(H1-H5) THEN focus clarity/limits definition

Anti-Pattern:
  Optimize already-strong domain → No H_org improvement (wasted effort)
```

#### PD66: Governance Automation Progressive (desde G10)

```yaml
Origen: M17 Governance Automation Rate + I5 HAIC

Enunciado:
  "Governance violations auto-remediate cuando posible (M17 target >60%).
   Human oversight siempre presente (I5 HAIC)."

Criterio_Verificable:
  ∀ violation type: auto-remediation rule defined OR manual override required
  Q28 tracks auto_remediated vs manual
  M17 > 0.60 (Elite governance automation)

Progression:
  Minor violations (severity=Minor): 90% auto-fix
  Moderate: 60% auto-fix
  Major: 30% auto-fix (human review)
  Critical: 100% human review (HAIC enforcement)

Anti-Pattern:
  100% automation sin human oversight → I5 violation
  0% automation → Manual toil, slow response
```

#### PD67: Pattern Catalog Mandatory (desde G8)

```yaml
Origen: 05_patrones.md + Empirical validation

Enunciado:
  "Soluciones recurrentes DEBEN documentarse como patterns.
   Anti-patterns detectados vía metrics triggers."

Criterio_Verificable:
  ∀ domain D1-D4: ≥3 patterns documentados
  Pattern includes: Context, Problem, Solution, Consequences, Metrics
  
Pattern_Selection:
  IF problem matches pattern.context THEN apply pattern.solution
  Track pattern effectiveness: success_rate per pattern

Anti-Pattern:
  Reinvent wheel cada proyecto → No learning org
```

#### PD68: Anti-Pattern Detection Automated (desde G9)

```yaml
Origen: Patterns catalog + Metrics thresholds

Enunciado:
  "Anti-patterns detectables vía metric thresholds automáticos.
   Alerts trigger remediation."

Detection_Rules:
  IF handoff_ratio > 0.30 THEN AP_Handoff_Hell detected
  IF CFR > 0.15 THEN AP_Deploy_Without_Quality detected
  IF H_org < 50 THEN AP_Organizational_Dysfunction detected
  IF violations_severity_score > 100 THEN AP_Governance_Collapse detected

Criterio_Verificable:
  Alert system monitors anti-pattern thresholds
  Remediation playbook linked per anti-pattern
  
Anti-Pattern:
  Ignore anti-pattern signals → Drift into failure mode
```

### Principios Vistas & Optimización (PD69-72, desde G16-G19)

#### PD69: Dashboard Real-Time Constraints (desde G16)

```yaml
Origen: D2 (Percepción) + Observable freshness requirements

Enunciado:
  "Dashboard observables actualizados según criticidad:
   Real-time (<1min): Incidents, Production metrics
   Near-time (<15min): DORA metrics, Flow execution
   Periodic (1-24h): OKR progress, Architecture metrics"

Criterio_Verificable:
  ∀ observable: refresh_frequency <= max_freshness_threshold
  Critical observables: freshness < 1 minute
  Dashboard shows last_updated timestamp

Anti-Pattern:
  Stale dashboard (24h+ lag) → Decision-making on outdated data
```

#### PD70: Artifact Templates Complete (desde G17)

```yaml
Origen: D1-D4 vistas + 04_vistas.md artifacts

Enunciado:
  "Cada artefacto D1-D4 tiene template completo:
   - Input fields specification
   - Validation rules
   - Output format
   - Example filled template"

Criterio_Verificable:
  ∀ artifact ∈ {Org Chart, RACI, OKR Canvas, VSM, DORA Dashboard}:
    Template file exists WITH examples
    Required fields documented
    Validation rules specified

Anti-Pattern:
  "Figure it out yourself" → Implementation inconsistency across teams
```

#### PD71: Metric Threshold Adaptive (desde G18)

```yaml
Origen: M1-M17 metrics + Statistical process control

Enunciado:
  "Metric thresholds ajustables por contexto organizacional.
   Elite targets aspirational, current baseline monitored."

Calibration:
  Initial: Industry benchmarks (DORA Elite/High/Medium/Low)
  After 3 months: Organization-specific p50/p90 baselines
  Quarterly: Reassess thresholds based on improvement trajectory

Criterio_Verificable:
  ∀ metric: {current_value, baseline, target, threshold_type}
  Alerts cuando deviation > 2σ from baseline

Anti-Pattern:
  Fixed thresholds ignore context → False alarms OR missed signals
```

#### PD72: Integration Points Explicit (desde G19)

```yaml
Origen: System integration + External tool compatibility

Enunciado:
  "Puntos integración explícitos para herramientas externas:
   - REST APIs (CRUD operations C1-C5, E6-E7)
   - Event streams (execution events, state changes)
   - Data exports (CSV, JSON for analytics)
   - Webhooks (notifications, triggers)"

Criterio_Verificable:
  API documentation completa (OpenAPI/Swagger)
  Event schema published (AsyncAPI)
  Authentication/Authorization specified (OAuth2, API keys)

Integration_Examples:
  - Jira ↔ Propósito (OKR sync)
  - GitHub ↔ E7 (deployment events)
  - Slack ↔ Alerts (governance violations)
  - Tableau ↔ Metrics (H_org dashboard)

Anti-Pattern:
  Closed system sin integraciones → Manual data entry, silos
```

### Principios Refinamientos Finales (PD73-76, desde G20-G25)

#### PD73: Query Performance Budgets (desde G20)

```yaml
Origen: Q1-Q28 queries + Performance engineering

Enunciado:
  "Queries tienen performance budgets. Optimization mandatory si exceeded."

Performance_Budgets:
  Simple queries (Q1-Q10): <100ms (p95)
  Complex queries (Q14-Q21): <500ms (p95)
  Analytics queries (Q26-Q28): <2s (p95)

Optimization_Techniques:
  - Indexes on foreign keys (all R1-R15 relationships)
  - Materialized views for aggregations (M1-M17)
  - Query result caching (5min TTL for dashboards)
  - Partitioning large tables (E7 executions by date)

Criterio_Verificable:
  Query performance monitored in production
  Slow query log analyzed weekly
  IF p95 > budget THEN optimization sprint triggered

Anti-Pattern:
  N+1 queries → Dashboard load time >10s (unusable)
```

#### PD74: Validation Rules Complete (desde G21)

```yaml
Origen: INV_C1-C8, INV_E6-E7 + Data integrity

Enunciado:
  "Validation rules enforced en 3 niveles:
   1. Schema validation (types, required fields)
   2. Business rule validation (INV checks)
   3. Cross-entity consistency (relationship integrity)"

Validation_Coverage:
  Level 1 (Schema): 100% entities (automated via JSON Schema)
  Level 2 (Business): All INV_XX rules (25+ invariantes)
  Level 3 (Consistency): All R1-R15 relationships

Enforcement:
  CREATE/UPDATE operations → Run validation pipeline
  IF validation fails → Reject with detailed error message
  Validation errors logged for analysis

Anti-Pattern:
  Validation solo en UI → Backend acepta invalid data (bypasses)
```

#### PD75: Migration Path Documented (desde G22)

```yaml
Origen: Adoption strategy + Change management

Enunciado:
  "Migration path desde estado actual organizacional a ORKO documented.
   Phased adoption plan con quick wins."

Migration_Phases:
  Phase 0 (Assessment): Map current state to ORKO primitives (1-2 weeks)
  Phase 1 (Quick Wins): Implement D2 Dashboard, DORA metrics (1 month)
  Phase 2 (Core): Deploy C1-C5 contracts, basic flows (2-3 months)
  Phase 3 (Advanced): E6 states, R14 transitions, portfolio optimization (3-6 months)
  Phase 4 (Excellence): Full governance automation, pattern library (6-12 months)

Criterio_Verificable:
  Migration playbook exists per organization size
  Success criteria per phase defined
  Rollback procedures documented

Anti-Pattern:
  "Big bang" migration → Organizational disruption, failure risk
```

#### PD76: Pattern Success Metrics (desde G25)

```yaml
Origen: PD66 Pattern Catalog + Empirical validation

Enunciado:
  "Patterns tracked con success metrics. Low-performing patterns deprecated."

Pattern_Metrics:
  - Adoption rate: % projects using pattern
  - Success rate: % implementations achieving expected outcomes
  - Time-to-value: Days from pattern application to measurable improvement
  - Satisfaction score: Team feedback (1-5 scale)

Lifecycle:
  Proposed → Experimental (3 trials) → Validated (>70% success) → Canonical
  IF success_rate < 50% after 10 trials → Deprecated

Criterio_Verificable:
  ∀ pattern: metrics dashboard tracking adoption and success
  Quarterly pattern review: promote/deprecate decisions
  
Anti-Pattern:
  Patterns sin validación → Cargo cult (copy without understanding)
```
