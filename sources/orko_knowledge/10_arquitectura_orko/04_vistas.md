# PARTE IV: VISTAS ARQUITECTÓNICAS

**4 Dominios Ortogonales con Artefactos Específicos**

> **Etiquetado Genoma/Fenotipo**: Este documento contiene elementos mixtos:
> - **[GENOMA]** D1-D4: Dominios ortogonales (derivados de T4, universales)
> - **[FENOTIPO]** Artefactos específicos: Org Chart, RACI, OKR Canvas, VSM, Dashboards (templates adaptables)
> - **[FENOTIPO]** Métricas scores: Fórmulas y thresholds recomendados (configurables según contexto)
>
> Ver ../00_fundamentos_teoricos/00_introduccion.md §0.1 para definición completa framework.

- [PARTE IV: VISTAS ARQUITECTÓNICAS](#parte-iv-vistas-arquitectónicas)
  - [§1. FUNDAMENTOS VISTAS](#1-fundamentos-vistas)
  - [§2. VISTA D1: ARQUITECTURA](#2-vista-d1-arquitectura)
    - [A. ARTEFACTO D1.1: ORG CHART ORKO](#a-artefacto-d11-org-chart-orko)
    - [B. ARTEFACTO D1.2: RACI MATRIX](#b-artefacto-d12-raci-matrix)
    - [C. ARTEFACTO D1.3: PURPOSE CASCADE](#c-artefacto-d13-purpose-cascade)
    - [D. MÉTRICAS D1: ARQUITECTURA SCORE](#d-métricas-d1-arquitectura-score)
  - [§3. VISTA D2: PERCEPCIÓN](#3-vista-d2-percepción)
    - [A. ARTEFACTO D2.1: DASHBOARD 16 OBSERVABLES](#a-artefacto-d21-dashboard-16-observables)
    - [B. ARTEFACTO D2.2: ANOMALY LOG](#b-artefacto-d22-anomaly-log)
    - [C. MÉTRICAS D2: PERCEPCIÓN SCORE](#c-métricas-d2-percepción-score)
    - [D. ARTEFACTO D2.2: COMPLIANCE LOG](#d-artefacto-d22-compliance-log)
  - [§4. VISTA D3: DECISIÓN](#4-vista-d3-decisión)
    - [A. ARTEFACTO D3.1: OKR PLANNING CANVAS](#a-artefacto-d31-okr-planning-canvas)
    - [B. ARTEFACTO D3.2: PORTFOLIO BOARD](#b-artefacto-d32-portfolio-board)
    - [C. MÉTRICAS D3: DECISIÓN SCORE](#c-métricas-d3-decisión-score)
    - [D. ARTEFACTO D3.3: DECISION AUDIT TRAIL](#d-artefacto-d33-decision-audit-trail)
  - [§5. VISTA D4: OPERACIÓN](#5-vista-d4-operación)
    - [A. ARTEFACTO D4.1: VALUE STREAM MAP](#a-artefacto-d41-value-stream-map)
    - [B. ARTEFACTO D4.2: DORA METRICS DASHBOARD](#b-artefacto-d42-dora-metrics-dashboard)
    - [C. ARTEFACTO D4.3: INCIDENT LOG](#c-artefacto-d43-incident-log)
    - [D. MÉTRICAS D4: OPERACIÓN SCORE](#d-métricas-d4-operación-score)
  - [§6. HEALTH SCORE INTEGRADO](#6-health-score-integrado)
  - [§7. MAPEO VISTAS ↔ CONTRATOS ↔ RELACIONES](#7-mapeo-vistas--contratos--relaciones)
  - [§8. IMPLEMENTACIÓN GRADUAL VISTAS](#8-implementación-gradual-vistas)

## §1. FUNDAMENTOS VISTAS

```yaml
Naturaleza_Vista:
  "Vista arquitectónica = Proyección del modelo desde perspectiva dominio.
   Mismos primitivos (P1-P5), diferentes énfasis y representaciones."

Principio_Separación_Concerns:
  D1_Arquitectura: Diseña ESTRUCTURA (quién, límites, autoridad)
  D2_Percepción: Observa ESTADO (qué pasa, métricas, anomalías)
  D3_Decisión: Dirige PROPÓSITO (qué hacer, priorización)
  D4_Operación: Ejecuta VALOR (cómo entregar, flujos)

Origen_Teórico:
  véase **03_invariantes.md** (I1–I8) y **00_introduccion.md**)
  4 dominios ortogonales y necesarios (Teorema T4)

Relación_Modelo:
  Vista NO añade entidades nuevas
  Vista ORGANIZA primitivos existentes según concern
  
Artefactos_Por_Vista:
  Cada vista define artefactos específicos para su dominio
  Artefactos implementan contratos Parte I usando modelo Parte III
```

## §2. VISTA D1: ARQUITECTURA

```yaml
Responsabilidad_Core:
  "Diseñar y mantener ESTRUCTURA organizacional:

- Distribución capacidades (org chart, teams, roles)
- Límites autoridad (RACI, decision rights)
- Alineación propósitos (cascada estratégica)"

Primitivos_Énfasis:
  Primario: P1 (Capacidad), P4 (Límite), P5 (Propósito)
  Secundario: P2 (Flujo - para optimizar estructura)
  Terciario: P3 (Información - métricas arquitectónicas)
```

### A. ARTEFACTO D1.1: ORG CHART ORKO

Definición:
  "Organigrama extendido que visualiza capacidades, composición y autoridad."

Estructura:
  Basado_En: R12 (Capacidad_Composición) + ownership
  
  Nodos:
    - Capacidad (substrate, capacity_type)
    - Relaciones parent-child (composition)
    - Owner/accountable marcado

  Edges:
    - ⊕ (Paralelo): Team composition
    - ⊗ (Secuencial): Pipeline
    - Reporta_a: Organizational hierarchy

Representación_Visual:

```markdown
[Org Root - Mixto C3]
│
├─[Product Unit - Mixto C2]
│  │
│  ├─[Engineering Team - Mixto C2] ⊕
│  │  ├─[Backend Dev - Humano C1]
│  │  ├─[Frontend Dev - Humano C1]
│  │  └─[QA Engineer - Humano C1]
│  │
│  └─[ML Team - Mixto C2] ⊕
│     ├─[ML Engineer - Humano C2]
│     └─[ML Model Churn - Algorítmico C1] (delegado de ML Eng)
│
└─[Operations Unit - Mixto C2]
   └─[SRE Team - Mixto C2]
      ├─[SRE - Humano C2]
      └─[Monitoring Bot - Algorítmico C0] (delegado de SRE)
```

Información_Incluida:
  Por cada nodo Capacidad:
    - name, substrate, capacity_type
    - role (Producción/Habilitación) + context
    - ownership.accountable_id
    - status
    - IF Algorítmico: delegation_mode (M1-M6)

Métricas_Derivadas:

- Span_of_Control = # direct reports por manager
    Target: 5-9 (véase **03_invariantes.md** (I1–I8) y **00_introduccion.md**)

- Depth = Niveles jerárquicos
    Indicador: > 7 niveles = excesiva burocracia

- Ratio_Prod_Hab = # Capacidades Producción / # Habilitación
    Target depende industria (tech: ~60/40)

Uso_Metodología:

- Diseño org inicial (L2 adopción)
- Quarterly review (detectar bottlenecks)
- Reorg planning

### B. ARTEFACTO D1.2: RACI MATRIX

Definición:
  "Matriz decisiones × capacidades especificando roles."

Estructura:
  Basado_En: Límite(type=Organizacional, constraint=decision_rights)
  
  Dimensiones:
    Rows: Decisiones críticas (ej: "Deploy to prod", "Hire engineer")
    Cols: Capacidades (teams, roles)

  Valores:
    R (Responsible): Ejecuta decisión
    A (Accountable): Único accountable resultado
    C (Consulted): Input antes decisión
    I (Informed): Notificado después decisión

Representación_Tabular:

  | Decision              | Eng Team | Product | SRE | CTO |
  |-----------------------|----------|---------|-----|-----|
  | Deploy to prod        | R        | C       | A   | I   |
  | Define roadmap        | C        | R       | C   | A   |
  | Hire engineer         | C        | I       | -   | A   |
  | Incident resolution   | C        | I       | R,A | I   |

Invariantes_RACI:

- Exactamente 1 'A' por decisión (accountability única, I5)
- Al menos 1 'R' (alguien ejecuta)
- 'A' debe ser Capacidad substrate ∈ {Humano, Mixto}
- **INV_GOLDEN_RULE**: Verificación automática por fila
  → Capacidad con 'A' debe tener authority_scope para esa decisión
  → Si violación detectada: requerir waiver (rationale, sponsor, expiry)

Implementación_Modelo:
  Límite {
    limit_type: Organizacional,
    constraint: {
      target_entity_type: Capacidad,
      constraint_expression: "RACI[decision_id] = {R,A,C,I}",
      enforcement: Preventivo
    }
  }

Uso_Metodología:

- Clarificar autoridad (reducir A3_Handoffs)
- Onboarding nuevos roles
- Conflict resolution (dos teams claim ownership)

### C. ARTEFACTO D1.3: PURPOSE CASCADE

Definición:
  "Árbol jerárquico propósitos org → unit → team → individual."

Estructura:
  Basado_En: R11 (Propósito_Jerarquía)
  
  Visualización:
    Tree con nodos = Propósito
    Edges = parent_purpose_id

  Por cada nodo:
    - Objective (qualitativo)
    - Key_Results (2-5 métricas)
    - Owner (capacity_id)
    - Progress (%)
    - Child purposes contributing

Representación_Visual:

```markdown
[ORG] "Liderar SaaS LATAM" (CTO owner)
│     KR1: ARR > $10M (current: $7M, 70%)
│     KR2: NPS > 50 (current: 45, 90%)
│
├─[UNIT Product] "Lanzar 5 features enterprise Q1" (VP Prod owner)
│  │  KR1: 5 features shipped (current: 3, 60%)
│  │  KR2: Adoption > 40% (current: 35%, 87%)
│  │
│  ├─[TEAM Auth] "Implementar SSO" (Auth Lead owner)
│  │  │  KR1: SAML integration done (80%)
│  │  │  KR2: 0 security issues (100%)
│  │  │
│  │  └─[INDIVIDUAL] "Okta integration" (Engineer owner)
│  │     KR1: Tests passing (90%)
│  │
│  └─[TEAM Analytics] "Dashboard real-time" (Analytics Lead)
│     KR1: Latency < 2s (60%)
│
└─[UNIT Ops] "Uptime 99.9%" (VP Ops owner)
   KR1: Incidents < 5/month (current: 3, 100%)
```

Validaciones:

- ∀ child: child.end_date ≤ parent.end_date (INV_P2)
- ∀ child: contributes_to(parent) (alignment)
- Path_to_root existe para todo propósito (no huérfanos)

Métricas_Derivadas:
  Alignment_Score = Σ (peso_child × progress_child) / Σ peso
  Target: > 0.85 (85% alignment)

Uso_Metodología:

- Quarterly OKR planning
- Weekly check-ins (update progress)
- Retrospective (adjust targets)

### D. MÉTRICAS D1: ARQUITECTURA SCORE

```yaml
Definición_A_Score:
  A_Score = weighted_avg(A1, A2, A3, A4, A5)

Componentes:
  
  A1_Claridad_Autoridad:
    Fórmula: % decisiones con RACI definido y único 'A'
    Target: > 0.90
    Data: RACI Matrix (D1.2)

  A2_Span_of_Control:
    Fórmula: % managers con span ∈ [5..9]
    Target: > 0.75
    Data: Org Chart (D1.1), query Q1

  A3_Handoff_Ratio:
    Fórmula: AVG(handoff_ratio) across flujos críticos
    Target: < 0.20
    Data: Flujo.metrics.handoff_ratio (R1)
    Interpretación: Alto handoff = estructura mal alineada con flujos

  A4_Alignment_OKRs:
    Fórmula: Alignment_Score from Purpose Cascade
    Target: > 0.85
    Data: Purpose Cascade (D1.3), R11

  A5_Governance_Violations:
    Fórmula: COUNT(límites org violados) último mes
    Target: = 0
    Data: Límite.compliance.violations_count (R6)

Agregación:
  A_Score = (
    A1_Claridad × 0.30 +
    A2_Span × 0.20 +
    A3_Handoffs × 0.25 +
    A4_Alignment × 0.20 +
    A5_Violations × 0.05
  )

Interpretación:
  A_Score ≥ 80: Arquitectura sana
  A_Score 70-79: Atención requerida
  A_Score < 70: Crítico, bloquear transformaciones (PD30)
```

## §3. VISTA D2: PERCEPCIÓN

```yaml
Responsabilidad_Core:
  "Observar y medir ESTADO organizacional:

- 16 observables (8 externos + 8 internos)
- Detectar anomalías y patterns
- Proyectar evolución futura"

Primitivos_Énfasis:
  Primario: P3 (Información - todo observable es información)
  Secundario: P1, P2 (para métricas internas)
  Terciario: P4, P5 (para detectar violaciones, at-risk OKRs)
```

### A. ARTEFACTO D2.1: DASHBOARD 16 OBSERVABLES

```yaml
Definición:
  "Panel unificado mostrando estado tiempo real 16 categorías."

Estructura_8_Externos:
  Basado_En: Información(observable_id ∈ {EX1..EX8})
  
  EX1_Demanda_Clientes:
    Métricas: Pipeline deals, inbound leads, feature requests
    Freshness: Diaria
    Source: CRM, product feedback

  EX2_Competidores:
    Métricas: New entrants, competitor features, pricing moves
    Freshness: Semanal
    Source: Market intelligence, press

  EX3_Regulatorio:
    Métricas: New regulations, compliance deadlines
    Freshness: Mensual (o event-driven)
    Source: Legal, industry associations

  EX4_Tecnológico:
    Métricas: New frameworks, platform updates, vulnerabilities
    Freshness: Semanal
    Source: Tech radar, security advisories

  EX5_Feedback_Clientes:
    Métricas: NPS, CSAT, support tickets sentiment
    Freshness: Diaria
    Source: Surveys, support system

  EX6_Disruptivo:
    Métricas: Emerging business models, category shifts
    Freshness: Trimestral
    Source: Strategy analysis, horizon scanning

  EX7_Social:
    Métricas: Brand sentiment, employee advocacy, PR
    Freshness: Diaria
    Source: Social listening, media monitoring

  EX8_Económico:
    Métricas: Market conditions, funding environment, FX
    Freshness: Semanal
    Source: Financial news, economic indicators

Estructura_8_Internos:
  Basado_En: Información(observable_id ∈ {IN1..IN8})
  
  IN1_Velocidad_Entrega:
    Métricas: Cycle time, lead time, deployment frequency
    Freshness: Continua (real-time)
    Source: Flujo.metrics (R2), DORA metrics

  IN2_Salud_Capacidades:
    Métricas: Engagement, burnout signals, turnover
    Freshness: Semanal
    Source: Capacidad health observables (R1)

  IN3_Eficiencia_Flujos:
    Métricas: Flow efficiency, bottlenecks, wait time
    Freshness: Continua
    Source: Flujo.metrics.flow_efficiency (R2)

  IN4_Calidad_Outputs:
    Métricas: Bug rate, defect density, rework %
    Freshness: Continua
    Source: Quality gates, testing

  IN5_Utilización_Capacidades:
    Métricas: Capacity utilization, idle time
    Freshness: Continua
    Source: Capacidad assignments (R1)
    Target: 0.70-0.85 (ni idle ni overload)

  IN6_Alineación_Propósitos:
    Métricas: OKR progress, alignment score
    Freshness: Semanal
    Source: Propósito.key_results.progress (R11)

  IN7_Violaciones_Límites:
    Métricas: Compliance breaches, policy violations
    Freshness: Event-driven
    Source: Límite.compliance.violations (R6-R8)

  IN8_Debt_Técnico:
    Métricas: Code quality, tech debt ratio, incident count
    Freshness: Continua
    Source: Static analysis, incident tracking
```

Representación_Visual:

```plain
┌─────────────────────────────────────────────────┐
│  OBSERVABLES DASHBOARD - ORKO                  │
├─────────────────────────────────────────────────┤
│                                                 │
│  EXTERNOS (Environment)        Status  Trend   │
│  ┌──────────────────────────┐                  │
│  │ EX1 Demanda Clientes     │  🟢     ↗      │
│  │ EX2 Competidores         │  🟡     →      │
│  │ EX3 Regulatorio          │  🟢     →      │
│  │ EX4 Tecnológico          │  🟡     ↗      │
│  │ EX5 Feedback Clientes    │  🟢     ↗      │
│  │ EX6 Disruptivo           │  🔴     ↘      │
│  │ EX7 Social               │  🟢     →      │
│  │ EX8 Económico            │  🟡     ↘      │
│  └──────────────────────────┘                  │
│                                                 │
│  INTERNOS (Organization)       Status  Trend   │
│  ┌──────────────────────────┐                  │
│  │ IN1 Velocidad Entrega    │  🟢     ↗      │
│  │ IN2 Salud Capacidades    │  🟡     ↘      │
│  │ IN3 Eficiencia Flujos    │  🟢     →      │
│  │ IN4 Calidad Outputs      │  🟢     ↗      │
│  │ IN5 Utilización          │  🟡     ↗      │
│  │ IN6 Alineación OKRs      │  🟢     →      │
│  │ IN7 Violaciones Límites  │  🟢     →      │
│  │ IN8 Debt Técnico         │  🔴     ↘      │
│  └──────────────────────────┘                  │
│                                                 │
│  P_Score: 78/100  (Acceptable)                 │
└─────────────────────────────────────────────────┘
```

Status_Legend:
  🟢 Green: Métrica dentro target
  🟡 Yellow: Atención requerida (10% fuera target)
  🔴 Red: Crítico (>20% fuera target)
  
  Trend: ↗ Improving, → Stable, ↘ Degrading

Implementación_Manual:

- Spreadsheet con 16 rows
- Actualización semanal (mínimo)
- Colores condicionales automáticos

Implementación_Platform:

- Dashboard real-time
- Alertas automáticas si status → Red
- Drill-down a métricas subyacentes

### B. ARTEFACTO D2.2: ANOMALY LOG

```yaml
Definición:
  "Registro eventos anómalos detectados en observables."

Estructura:
  Basado_En: Información(observable_id, deviation_detected)
  
  Campos:
    - anomaly_id: UUID
    - timestamp: Cuándo detectado
    - observable: EX/IN identificador
    - deviation: {
        expected_value: Float,
        actual_value: Float,
        deviation_pct: Float,
        threshold_exceeded: Boolean
      }
    - severity: {Low, Medium, High, Critical}
    - status: {New, Investigating, Resolved, False_Positive}
    - assigned_to: Capacidad_id (owner investigation)

Detección_Anomalías:
  Técnicas:
    - Statistical: > 2σ from rolling mean
    - Threshold: Hard limits (ej: violations > 0)
    - Trend: Degrading 3+ weeks consecutivas
    - Pattern: Unusual correlations

  Ejemplo_Detección:
    Observable: IN3_Eficiencia_Flujos
    Expected: 0.45 (baseline)
    Actual: 0.28
    Deviation: -38%
    Threshold: 20% degradation
    → ANOMALY triggered, severity: High

Workflow:

  1. Detect → Log anomaly
  2. Triage → Assign to capacity owner observable
  3. Investigate → Root cause analysis (5 Whys)
  4. Resolve → Implement intervention (Parte V Playbooks)
  5. Verify → Monitor recovery

Uso_Metodología:

- Daily standups (review new anomalies)
- Weekly health reviews (trend analysis)
- Monthly retrospectives (patterns over time)
```

### C. MÉTRICAS D2: PERCEPCIÓN SCORE

```yaml
Definición_P_Score:
  P_Score = weighted_avg(P1, P2, P3, P4, P5)

Componentes:
  
  P1_Coverage_Observables:
    Fórmula: COUNT(observables instrumentados) / 16
    Target: = 1.0 (100% cobertura)

  P2_Freshness:
    Fórmula: AVG(is_fresh) across observables
    is_fresh = (now - timestamp) < validity_period
    Target: > 0.90

  P3_Latencia_Detección:
    Fórmula: AVG(time_to_detect) anomalías críticas
    Target: < 1 hora (real-time ideal)

  P4_False_Positive_Rate:
    Fórmula: COUNT(anomalies marked false_positive) / COUNT(total anomalies)
    Target: < 0.15 (15%)

  P5_Actionability:
    Fórmula: % anomalies → intervention aplicada
    Target: > 0.80

Agregación:
  P_Score = (
    P1_Coverage × 0.25 +
    P2_Freshness × 0.25 +
    P3_Latencia × 0.20 +
    P4_FalsePos × 0.15 +
    P5_Actionability × 0.15
  )

Interpretación:
  P_Score ≥ 80: Observabilidad excelente
  P_Score 70-79: Gaps menores
  P_Score < 70: Blind spots críticos
```

### D. ARTEFACTO D2.2: COMPLIANCE LOG

```yaml
Definición:
  "Registro de cumplimiento límites regulatorios vinculado a C4.limit_type y evidence"
  
Estructura:
  compliance_event_id: UUID
  timestamp: Timestamp
  limit_id: UUID  # → C4 Límite
  limit_type: {Legal, Regulatorio, Ético, Presupuestario, Político}
  norm_level: {Ley, Reglamento, Norma_Técnica, Contrato, Política_Interna}
  
  jurisdiction: String  # Ej: "CHL", "EU", "USA"
  source_ref: String    # Ej: "Ley_21180_Art18", "GDPR_Art25"
  
  compliance_status: {Compliant, At_Risk, Violated, Remediated}
  
  # Si violated
  violation:
    severity: {Minor, Moderate, Major, Critical}
    detected_at: Timestamp
    detected_by: UUID  # Capacity ID
    affected_entities: List<{type, id}>
    
  evidence:
    audit_trail: URI  # Link a evidencia compliance
    policy_ref: String
    last_review: Timestamp
    next_review: Timestamp
    
  remediation:
    status: {Open, In_Progress, Resolved, Accepted}
    plan: String
    responsible: UUID  # Capacity ID
    deadline: Date
    resolution_date: Date | null
    
Uso:
  - Auditoría por jurisdicción y criticidad
  - Tracking compliance continuo
  - Alertas automáticas si violations Critical
  - Reportes regulatorios
```

## §4. VISTA D3: DECISIÓN

```yaml
Responsabilidad_Core:
  "Dirigir organización hacia propósitos:

- Definir OKRs cascadeados
- Priorizar portfolio iniciativas
- Asignar capacidades a trabajo
- Evaluar trade-offs"

Primitivos_Énfasis:
  Primario: P5 (Propósito)
  Secundario: P1 (Capacidad - para asignar), P2 (Flujo - iniciativas)
  Terciario: P3 (Información - para decidir), P4 (Límite - constraints)
```

### A. ARTEFACTO D3.1: OKR PLANNING CANVAS

Definición:
  "Template quarterly planning capturando contexto → objetivos → iniciativas."

Estructura:
  
  Sección_1_Contexto:
    - Qué cambió último quarter (EX observables)
    - Qué aprendimos (retrospective)
    - Constraints relevantes (límites activos)

  Sección_2_Objetivos:
    - Parent OKR (de nivel superior)
    - Proposed OKR este nivel
      *Objective (qualitativo, inspirador)
      * Key_Results (2-5, cuantitativos, SMART)
      *Owner (capacity_id)
      * Dependencies (otros OKRs)

  Sección_3_Iniciativas:
    - Flujos/proyectos para lograr OKR
    - Capacidades requeridas por iniciativa
    - Effort estimado (person-weeks)
    - Priorización (RICE, WSJF)

  Sección_4_Risks:
    - Dependencies externas
    - Capacidades faltantes (gaps)
    - Límites que pueden bloquear

Ejemplo_Completado:

  ```yaml
  Quarter: Q1 2025
  Team: Auth Engineering
  
  CONTEXTO:
    - EX1 Demanda: Enterprise customers pidiendo SSO
    - Aprendizaje: OAuth2 integration tomó 2x estimado
    - Constraints: Budget Q1 limitado, no nuevas contrataciones
    
  PARENT OKR:
    [Product Unit] "Lanzar 5 features enterprise Q1"
    
  PROPOSED OKR:
    Objective: "Implementar SSO enterprise-grade"
    Key_Results:
      - KR1: SAML integration con 3 providers (Okta, Azure AD, Google)
      - KR2: 0 security vulnerabilities críticas
      - KR3: Migration 10+ enterprise customers
    Owner: Auth Team Lead (capacity_id: uuid-123)
    
  INICIATIVAS:
    I1: SAML Integration
      Flujo: feature_development
      Capacidades: 2 backend devs, 1 security eng (part-time)
      Effort: 6 person-weeks
      Priorization_Score: 85 (RICE)
      
    I2: Migration Playbook
      Flujo: documentation
      Capacidades: 1 tech writer, 1 solutions architect
      Effort: 2 person-weeks
      Priority: 70
      
  RISKS:
    - Dependency: Security review team tiene backlog 3 semanas
    - Gap: No tenemos expertise SAML interno, requerir consultor
  ```

Uso_Metodología:

- Pre-planning (1 semana antes quarter)
- Planning session (facilitated, 4 horas)
- Review & commit (alignment check con parent)

Sección_Especial_OKR_Societal:
  "Para contexto e-Government: agregar panel OKR Societal"
  
  Campos_Adicionales:
    public_value:
      weights:
        accountability: Float[0..1]
        transparency: Float[0..1]
        efficiency: Float[0..1]
        effectiveness: Float[0..1]
        responsiveness: Float[0..1]
        justice: Float[0..1]
        equality: Float[0..1]
        equity: Float[0..1]
      # Suma ≤ 1.0
    
    jurisdiction: String  # Ej: "CHL", "EU", "USA"
    legal_basis_refs: List<String>  # Ej: ["Ley_21180_Art18", "DS_83"]
    
  Ejemplo:
    Objective: "Digitalizar expedientes judiciales"
    public_value:
      transparency: 0.40
      efficiency: 0.35
      accountability: 0.25
    jurisdiction: "CHL"
    legal_basis_refs: ["Ley_21180_Art18"]

### B. ARTEFACTO D3.2: PORTFOLIO BOARD

Definición:
  "Visualización trabajo en progreso + pipeline priorizado."

Estructura:
  Basado_En: R9 (Propósito-Flujo), allocation (Capacidad-Iniciativas)
  
  Dimensiones:
    Columns: {Backlog, Planning, In_Progress, Done, Blocked}
    Rows: Iniciativas (agrupadas por OKR)

  Metadata_Por_Iniciativa:
    - Name, OKR servido (purpose_id)
    - Capacidades asignadas
    - Progress (% complete)
    - Health: {On_Track, At_Risk, Blocked}
    - Priorization_Score (RICE/WSJF)

Representación_Visual:

```markdown
┌─────────────────────────────────────────────────────────┐
│  PORTFOLIO BOARD Q1 2025                                │
├──────────┬─────────┬─────────────┬──────┬─────────────┤
│ Backlog  │Planning │In Progress  │ Done │   Blocked   │
├──────────┼─────────┼─────────────┼──────┼─────────────┤
│          │         │ [I1: SAML]  │      │             │
│ [I5:...] │ [I3:...]│  OKR: SSO   │ [I2] │ [I4: Audit] │
│ RICE: 60 │ RICE:75 │  Progress:  │      │ Blocker:    │
│          │         │  60%        │      │ Security    │
│          │         │  Health: 🟢 │      │ review      │
│          │         │  Team: Auth │      │             │
├──────────┼─────────┼─────────────┼──────┼─────────────┤
│          │         │ [I6: API]   │      │             │
│          │         │  OKR: Scale │      │             │
│          │         │  Progress:  │      │             │
│          │         │  40%        │      │             │
│          │         │  Health: 🟡 │      │             │
│          │         │  Team: Infra│      │             │
└──────────┴─────────┴─────────────┴──────┴─────────────┘
```

WIP Limit: 8 iniciativas In Progress (current: 6)
Capacity Utilization: 78% (healthy)

Reglas_WIP_Limit:

- Max initiatives In_Progress = AVG(capacity throughput) × 1.2
- IF WIP > limit THEN defer new work
- Priorizar finish over start

Métricas_Derivadas:

- Throughput = # iniciativas Done / quarter
- Cycle_Time = AVG(time In_Progress → Done)
- Blocker_Rate = % time initiatives blocked

Uso_Metodología:

- Weekly review (update status, progress)
- Bi-weekly prioritization (reorder backlog RICE)
- Monthly capacity planning (adjust WIP)

### C. MÉTRICAS D3: DECISIÓN SCORE

```yaml
Definición_D_Score:
  D_Score = weighted_avg(D1, D2, D3, D4, D5)

Componentes:
  
  D1_Decision_Velocity:
    Fórmula: AVG(time_to_decision) decisiones críticas
    Target: < 7 días (no analysis paralysis)
    Data: Decision logs

  D2_OKR_Alignment:
    Fórmula: Alignment_Score cascade (D1.3)
    Target: > 0.85
    Data: R11 (Propósito jerarquía)

  D3_Portfolio_Balance:
    Fórmula: Distribution initiatives (Now/Next/Later o Horizons)
    Target: 70% Now, 20% Next, 10% Later (typical)
    Data: Portfolio Board

  D4_Execution_Rate:
    Fórmula: % OKRs completed (progress ≥ 100%)
    Target: > 0.70 (aspirational OK)
    Data: Propósito.key_results

  D5_Learning_Velocity:
    Fórmula: # experiments run / quarter
    Target: ≥ 5 (encourage exploration)
    Data: Initiatives tagged "experiment"

Agregación:
  D_Score = (
    D1_Velocity × 0.15 +
    D2_Alignment × 0.25 +
    D3_Balance × 0.20 +
    D4_Execution × 0.25 +
    D5_Learning × 0.15
  )

Interpretación:
  D_Score ≥ 80: Decisión excelente (data-driven, aligned, ejecutando)
  D_Score 70-79: Funcional pero mejorable
  D_Score < 70: Problemas decisión (slow, misaligned, o no ejecuta)
```

### D. ARTEFACTO D3.3: DECISION AUDIT TRAIL

```yaml
Definición:
  "Registro auditable de decisiones críticas (PD62) - Obligatorio para substrate algorítmico"
  
Estructura:
  decision_id: UUID
  timestamp: Timestamp
  decision_type: {Strategic, Tactical, Operational}
  decided_by: UUID  # Capacity ID
  substrate: {Humano, Algorítmico, Mixto}
  
  # Si substrate = Algorítmico
  delegation_info:
    delegated_from: UUID  # Humano accountable
    delegation_mode: {M1..M6}
    guardrails_applied: List<String>
    
  inputs:
    information_assets: List<UUID>
    context: JSON
    
  decision:
    option_selected: String
    alternatives_considered: List<String>
    rationale: String
    confidence_score: Float[0..1]  # Si algorítmico
    
  impacts:
    affected_purposes: List<UUID>
    affected_limits: List<UUID>
    estimated_cost: Float
    risk_level: {Low, Medium, High, Critical}
    
  audit:
    explainability: String  # Cómo se llegó a la decisión
    override_available: Boolean
    review_required: Boolean
    reviewer_id: UUID | null

Uso:
  - Obligatorio para decisiones con substrate=Algorítmico (PD62)
  - Recomendado para decisiones Strategic y High risk
  - Permite auditoría compliance y HAIC
  - Alimenta trajectory learning (I6)
```

## §5. VISTA D4: OPERACIÓN

```yaml
Responsabilidad_Core:
  "Ejecutar flujos de valor continuamente:
   - Delivery day-to-day (features, fixes, ops)
   - Mantener calidad y disponibilidad
   - Optimizar eficiencia flujos
   - Responder a incidentes"

Primitivos_Énfasis:
  Primario: P2 (Flujo - core de operación)
  Secundario: P1 (Capacidad - ejecuta), P3 (Información - output)
  Terciario: P4 (Límite - SLAs, budgets), P5 (Propósito - outcome entregado)
```

### A. ARTEFACTO D4.1: VALUE STREAM MAP

```yaml
Definición:
  "Mapa visual flujo crítico desde trigger hasta value delivered."

Estructura:
  Basado_En: R1 (Capacidad_Ejecuta_Flujo) + Flujo.steps
  
  Componentes_Visuales:
    - Steps secuenciales (boxes)
    - Capacidades ejecutoras (swimlanes)
    - Handoffs (flechas entre lanes)
    - Wait times (gaps entre steps)
    - Value-add vs waste (color coding)
    
  Métricas_Por_Step:
    - Process_Time: Tiempo trabajo real
    - Wait_Time: Tiempo esperando (queue, handoff)
    - % Complete_Accurate: Calidad output step
    
  Métricas_Flujo_Total:
    - Lead_Time = Σ (process_time + wait_time)
    - Process_Time_Total = Σ process_time
    - Flow_Efficiency = Process_Time_Total / Lead_Time
    - Handoff_Count = # cambios swimlane
```

Representación_Visual:

  ```

  VALUE STREAM: Feature Development
  
  [Product] ──────────────────────────────────────────────
             │ Spec      │          │         │
             │ 2d        │          │         │
             └───────────┘          │         │
                  ↓ (wait: 1d)      │         │
                                    │         │
  [Engineering] ──────────────────────────────────────────
                         │ Dev      │         │ Deploy
                         │ 5d       │         │ 0.5d
                         └──────────┘         └────────
                              ↓ (wait: 0.5d)      ↓

  [QA] ────────────────────────────────────────────────
                                │ Test    │
                                │ 2d      │
                                └─────────┘
                                     ↓ (wait: 1d)

  METRICS:
    Lead Time: 12 days
    Process Time: 9.5 days
    Wait Time: 2.5 days
    Flow Efficiency: 79% (good)
    Handoffs: 3 (acceptable)

  ```

Análisis_VSM:
  
  Waste_Identification:
    - Wait > 20% lead time → Bottleneck
    - Handoff > 20% steps → Conway problem
    - Rework loops → Quality issue

  Optimization_Targets:
    1. Reduce wait time (parallel work, smaller batches)
    2. Minimize handoffs (team restructuring)
    3. Automate manual steps (C0 → Algorítmico)
    4. Improve % C&A (reduce rework)

Uso_Metodología:

- Initial assessment (L1 adopción)
- Quarterly optimization (identify improvements)
- Post-incident review (find systemic issues)

### B. ARTEFACTO D4.2: DORA METRICS DASHBOARD

```yaml
Definición:
  "Panel 4 métricas DORA + contexto ORKO."

Estructura:
  Basado_En: Flujo.metrics (deployment, incident flows)
  
  Métricas_DORA_Core:

    M1_Deployment_Frequency:
      Definición: # deployments / time period
      Data: Flujo(type=deployment).executions
      Benchmark:
        Elite: Multiple/day
        High: Weekly-monthly
        Medium: Monthly-biannually
        Low: < biannually
        
    M2_Lead_Time_for_Changes:
      Definición: Time commit → production
      Data: Flujo(feature_development).metrics.cycle_time
      Benchmark:
        Elite: < 1 day
        High: 1 day - 1 week
        Medium: 1 week - 1 month
        Low: > 1 month
        
    M3_Change_Failure_Rate:
      Definición: % deployments → incident
      Data: COUNT(incidents) / COUNT(deployments)
      Benchmark:
        Elite: 0-15%
        High: 16-30%
        Medium: 31-45%
        Low: > 45%
        
    M4_Time_to_Restore_Service:
      Definición: Time incident detected → resolved
      Data: Flujo(incident_response).metrics.cycle_time
      Benchmark:
        Elite: < 1 hour
        High: < 1 day
        Medium: 1 day - 1 week
        Low: > 1 week

  Métricas_ORKO_Extended:

    M5_Flow_Efficiency:
      Definición: Value-add time / total time
      Data: VSM analysis
      Target: > 40%
      
    M6_Capacity_Utilization:
      Definición: % capacidades productivas (no idle, no overload)
      Data: R1 assignments
      Target: 70-85%
      
    M7_Quality_Rate:
      Definición: 100% - defect_rate
      Data: Flujo outputs quality metrics
      Target: > 97%
```

Representación_Dashboard:

  ```

  ┌─────────────────────────────────────────────────────┐
  │  DORA + ORKO METRICS - Q1 2025                     │
  ├─────────────────────────────────────────────────────┤
  │                                                     │
  │  DORA CORE                    Current   Benchmark  │
  │  ┌────────────────────────┐                        │
  │  │ Deployment Freq        │   Daily     Elite ✓   │
  │  │ Lead Time Changes      │   2.5d      High      │
  │  │ Change Failure Rate    │   12%       Elite ✓   │
  │  │ Time to Restore        │   45min     Elite ✓   │
  │  └────────────────────────┘                        │
  │                                                     │
  │  ORKO EXTENDED                Current   Target     │
  │  ┌────────────────────────┐                        │
  │  │ Flow Efficiency        │   47%       >40% ✓    │
  │  │ Capacity Utilization   │   78%       70-85% ✓  │
  │  │ Quality Rate           │   98.2%     >97% ✓    │
  │  └────────────────────────┘                        │
  │                                                     │
  │  PERFORMANCE: Elite (7/7 metrics in target)        │
  └─────────────────────────────────────────────────────┘

  ```

Uso_Metodología:

- Weekly review (track trends)
- Quarterly benchmarking (compare industry)
- Annual goal setting (target next level)

### C. ARTEFACTO D4.3: INCIDENT LOG

```yaml
Definición:
  "Registro estructurado incidentes producción."

Estructura:
  Basado_En: Flujo(incident_response) executions + E7.workaround + E7.handoff_friction_score
  
  Campos_Por_Incidente:
    - incident_id: UUID
    - timestamp_detected: When
    - timestamp_resolved: When
    - severity: {P0_Critical, P1_High, P2_Medium, P3_Low}
    - affected_capacity: Qué capacidad/flujo afectado
    - root_cause: String (post-mortem)
    - resolution: String (cómo se resolvió)
    - preventive_actions: List<Action> (evitar recurrencia)
    - status: {Open, Investigating, Resolved, Closed}
    
    # Nuevos campos vinculados a E7
    - workaround:
        flag: Boolean
        kind: {improvisation, bricolage, policy_gap}
        description: String
        frequency: Integer  # Debt acumulado si > threshold
    
    - handoff_friction_score: Integer[0..100]
        # Meyer friction: costo transferencia entre steps/roles
        # Si > 70 → indicador handoff problemático
    
    - linked_execution_id: UUID  # E7 FlowExecution que resolvió

Clasificación_Severidad:
  P0_Critical:
    - Service down para todos usuarios
    - Data loss
    - Security breach
    Response_SLA: < 15 min

  P1_High:
    - Degradación severa performance
    - Subset usuarios afectado
    Response_SLA: < 1 hora

  P2_Medium:
    - Minor degradation
    - Workaround disponible
    Response_SLA: < 4 horas

  P3_Low:
    - Cosmetic issues
    - No impact usuarios
    Response_SLA: < 1 día

Post_Mortem_Template:

- What happened (timeline)
- Why (root cause - 5 Whys)
- What we did (resolution steps)
- What we'll do (preventive actions)
- Lessons learned

Uso_Metodología:

- Real-time incident tracking
- Weekly incident review (patterns)
- Monthly post-mortem retrospective
```

### D. MÉTRICAS D4: OPERACIÓN SCORE

```yaml
Definición_O_Score:
  O_Score = weighted_avg(O1, O2, O3, O4, O5)

Componentes:
  
  O1_Flow_Efficiency:
    Fórmula: AVG(flow_efficiency) flujos críticos
    Target: > 0.40 (40% value-add time)
    Data: VSM analysis (D4.1)

  O2_Cycle_Time:
    Fórmula: AVG(cycle_time_actual / cycle_time_target)
    Target: ≤ 1.0 (dentro target)
    Data: Flujo.metrics.cycle_time

  O3_Throughput:
    Fórmula: Deployments/week (trend)
    Target: Stable or increasing
    Data: DORA M1

  O4_Quality:
    Fórmula: 100% - defect_rate
    Target: > 97%
    Data: Quality metrics, CFR

  O5_Availability:
    Fórmula: Uptime %
    Target: > 99.5% (dependent on SLA)
    Data: Incident log, monitoring

Agregación:
  O_Score = (
    O1_FlowEff × 0.20 +
    O2_CycleTime × 0.20 +
    O3_Throughput × 0.15 +
    O4_Quality × 0.25 +
    O5_Availability × 0.20
  )

Interpretación:
  O_Score ≥ 80: Operación excelente (high-performing)
  O_Score 70-79: Operación estable
  O_Score < 70: Operación con problemas (bottlenecks, quality issues)
```

## §6. HEALTH SCORE INTEGRADO

**Regla PD30/PD61:** *Si `H_org < 70`, bloquear transformaciones estructurales y despliegues de alto riesgo hasta recuperar salud mínima.*


```yaml
Definición_H_org:
  "Métrica compuesta salud organizacional desde 5 dimensiones:
   H1 Humano, H2 Arquitectura, H3 Flujo, H4 Percepción, H5 Decisión."

Dimensiones_5:

  H1_Humano (30% peso):
    "Bienestar, engagement, desarrollo y autonomía del talento"
    
    Componentes:
      H1.1_Bienestar (25%):
        - Workload_Index: % capacidad utilizada (target 85-95%)
        - Stress_Score: Survey 1-10 (target <6)
        - Burnout_Risk: Red flags (attrition, sick days)
        - Work-Life_Balance: Hours/week (target <50)
        
      H1.2_Engagement (25%):
        - Satisfaction: eNPS or similar (target >30)
        - Psychological_Safety: Team surveys (target >4/5)
        - Alignment: % entiende strategy (target >80%)
        - Retention: Voluntary_attrition (target <10% anual)
        
      H1.3_Desarrollo (25%):
        - Learning_Velocity: Training hours/quarter (target >8h)
        - Skill_Depth: Expertise level (T-shaped)
        - Career_Path: % con plan crecimiento (target >70%)
        - Promotion_Rate: Internal mobility (target 15-25% anual)
        
      H1.4_Autonomía (25%):
        - Independent_Decisions: % sin aprobación externa (target >70%)
        - Empowerment_Index: Survey confianza (target >4/5)
        - Decision_Velocity: Days decisiones (target <3)
        - Escalations: % decisiones suben (target <20%)
        
    Cálculo:
      H1 = avg(H1.1, H1.2, H1.3, H1.4) × 100
      
    Umbrales:
      H1 < 50: Crisis burnout (inmediato action)
      H1 50-65: At-risk (intervención 30 días)
      H1 65-80: Healthy (monitorear trends)
      H1 > 80: Elite (high-performing culture)

  H2_Arquitectura (25% peso):  # Renombrado A_Score
    "Claridad estructura, boundaries, handoffs, alignment"
    
    Componentes: A1-A5 (mantener) + A6_nuevo
      A1_Claridad_Autoridad: RACI único (target 100%)
      A2_Span_Control: 5-9 reports (target 100% compliance)
      A3_Handoff_Ratio: <20% interactions (target compliance)
      A4_Alignment_OKRs: Path-to-root (target 95%)
      A5_Violations_Límites: Compliance (target 0 critical)
      A6_Archetypal_Purity: % mono-archetypal (target >80%)  # NUEVO
      
    Cálculo:
      H2 = weighted_avg(A1×20%, A2×15%, A3×25%, A4×20%, A5×10%, A6×10%)
      
  H3_Flujo (20% peso):  # NUEVO fusión O_Score + AOC Flow
    "Eficiencia value streams, waste minimization, throughput"
    
    Componentes:
      O1_Flow_Efficiency (30%):
        - Fórmula: touch_time / total_cycle_time
        - Target: >0.40 (40% value-adding time)
        - Measurement: Track work items desde inicio a entrega
        
      O2_Cycle_Time (25%):
        - Lead_Time: Commit → production (target by type)
        - Predictability: Std_dev / mean (target <0.3)
        
      O3_Handoff_Waste (20%):  # Específico flow (vs A3 estructura)
        - Wait_Time: % cycle en handoffs (target <30%)
        - Rework_Rate: % iteraciones extra (target <10%)
        
      O4_WIP_Adherence (15%):
        - Limit_Compliance: % teams siguiendo WIP (target >90%)
        - Throughput_Stability: Coefficient variation (target <0.25)
        
      O5_Waste_Minimization (10%):
        - 8_Lean_Wastes tracked (Transport, Inventory, Motion, Waiting,
          Overprocessing, Overproduction, Defects, Skills)
        - Top_3_Wastes quantified (target: reduce 20% quarter)
        
    Cálculo:
      H3 = weighted_avg(O1×30%, O2×25%, O3×20%, O4×15%, O5×10%)
      
  H4_Percepción (15% peso):  # Mantener P_Score
    "Observable coverage, freshness, actionability"
    
    Componentes: P1-P5 (sin cambios)
    Cálculo: P_Score (ya definido §4)
    
  H5_Decisión (10% peso):  # Mantener D_Score  
    "OKR velocity, alignment, portfolio balance, execution"
    
    Componentes: D1-D5 (sin cambios)
    Cálculo: D_Score (ya definido §3)

Fórmula_Maestra:
  H_org = (
    H1_Humano × 0.30 +
    H2_Arquitectura × 0.25 +
    H3_Flujo × 0.20 +
    H4_Percepción × 0.15 +
    H5_Decisión × 0.10
  )

Justificación_Pesos:
  - Humano 30%: People-first (I5 HAIC)
  - Arquitectura 25%: Structure enables everything
  - Flujo 20%: Delivery efficiency critical
  - Percepción 15%: Observability enables decisions
  - Decisión 10%: Direction important but execution dominates

Invariantes_Críticos:

  INV_Humano_Ceiling:
    IF H1 < 50 THEN H_org = min(H_org, 60)
    Rationale: "Burnout organization cannot score >60 total"
    
  INV_Arquitectura_Base:
    IF H2 < 60 THEN H_org = min(H_org, 70)
    Rationale: "Disfuncional structure limits ceiling"
    
  INV_Transformación:
    IF H_org < 70 THEN block(transformaciones_mayores)
    Rationale: "PD30 + Saneamiento required first"

Interpretación_Niveles:
  
  H_org ≥ 85: Elite
    - Todas dimensiones >80
    - High-performing culture
    - Transformaciones aggressive posibles
    - Benchmark industry

  H_org 70-84: Healthy
    - Mayoría dimensiones >70
    - Organización funcional sostenible
    - Transformaciones graduales OK
    - Mejora continua activa

  H_org 60-69: At_Risk
    - ≥1 dimensión <60 (problema significativo)
    - Transformaciones limitadas
    - Intervención focalizada requerida
    - Timeline recovery: 2-4 meses

  H_org < 60: Critical
    - Múltiples dimensiones <60
    - MODO RECOVERY obligatorio
    - BLOQUEAR new initiatives
    - Timeline recovery: 3-6 meses
    - Ver PLAYBOOK_CR1 (Parte V §8)
```

Dashboard_H_org:

  ```

  ┌─────────────────────────────────────────────────────┐
  │  ORGANIZATIONAL HEALTH - ORKO                      │
  ├─────────────────────────────────────────────────────┤
  │                                                     │
  │  H_org: 78 / 100  (Healthy)                        │
  │                                                     │
  │  ████████████████████████████████████████░░░░░░░   │
  │                                                     │
  │  BREAKDOWN BY DOMAIN:                              │
  │  ┌──────────────────────────────────────┐          │
  │  │ D1 Arquitectura    │ 82 │ ████████▓  │          │
  │  │ D2 Percepción      │ 75 │ ███████▓░  │  ⚠️     │
  │  │ D3 Decisión        │ 80 │ ████████░  │          │
  │  │ D4 Operación       │ 76 │ ███████▓░  │          │
  │  └──────────────────────────────────────┘          │
  │                                                     │
  │  ALERTS:                                           │
  │  ⚠️  P2_Freshness below target (85%)               │
  │  ℹ️  O2_CycleTime trending up (+10% vs last month)│
  │                                                     │
  │  ACTION REQUIRED: Review Percepción gaps           │
  └─────────────────────────────────────────────────────┘

  ```

Uso_Metodología:

- Monthly Health Assessment (full calculation)
- Executive dashboard (C-level visibility)
- Trend tracking (quarter-over-quarter)
- Trigger interventions (when < 70)

## §7. MAPEO VISTAS ↔ CONTRATOS ↔ RELACIONES

Tabla_Integración_Completa:

| Vista | Artefactos | Contratos Usa | Relaciones Usa | Queries Usa |
|-------|------------|---------------|----------------|-------------|
| **D1 Arquitectura** | Org Chart | C1 Capacidad | R12 Composición | Q6 Components |
| | RACI Matrix | C4 Límite | R6 Restringe Cap | Q5 Límites Cap |
| | Purpose Cascade | C5 Propósito | R11 Jerarquía | Q4 Path Root |
| **D2 Percepción** | Dashboard 16 | C3 Información | - | - |
| | Anomaly Log | C3 Información | R5 Deriva Info | Q3 Lineage |
| **D3 Decisión** | OKR Canvas | C5 Propósito | R9 Direcciona | Q2 Flujos Purpose |
| | Portfolio Board | C2 Flujo, C5 | R9, R10 | Q1 Caps Flujo |
| **D4 Operación** | VSM | C2 Flujo | R1 Ejecuta | Q1 Caps Flujo |
| | DORA Dashboard | C2 Flujo | R2 Produce Info | - |
| | Incident Log | C2 Flujo | R4 Consume Info | - |

Total_Cobertura:

- 10 artefactos principales
- 5 contratos todos usados
- 9 de 12 relaciones directamente usadas
- 6 queries aplicadas

Propiedad_Consistencia:
  ✓ Todo artefacto mapea a ≥1 contrato (implementable)
  ✓ Todo contrato usado por ≥1 artefacto (útil)
  ✓ Relaciones permiten queries necesarias
  ✓ Vistas ortogonales (concerns separados)

## §8. IMPLEMENTACIÓN GRADUAL VISTAS

```yaml
Secuencia_Recomendada:

  Fase_1_Foundation (Semanas 1-4):
    Artefactos:
      - D1.1 Org Chart (manual: Miro/Lucidchart)
      - D2.1 Dashboard 16 (manual: Spreadsheet)
      - D3.1 OKR Canvas (manual: Google Docs)

    Beneficio: Visibilidad básica estructura + estado + dirección
    Esfuerzo: 2-3 person-weeks
    
  Fase_2_Optimization (Semanas 5-8):
    Artefactos:
      - D1.2 RACI Matrix
      - D4.1 VSM (1-2 flujos críticos)
      - D4.2 DORA Dashboard (básico)

    Beneficio: Claridad autoridad + optimización flujos
    Esfuerzo: 3-4 person-weeks
    
  Fase_3_Advanced (Semanas 9-12):
    Artefactos:
      - D1.3 Purpose Cascade (full tree)
      - D2.2 Anomaly Log
      - D3.2 Portfolio Board
      - D4.3 Incident Log

    Beneficio: Gestión completa 4 dominios
    Esfuerzo: 4-5 person-weeks
    
  Fase_4_Integration (Continuo):
    - Calculate H_org mensual
    - Refine thresholds basado en baseline
    - Monitorear con observability (D2)
    - Automatizar con platform (opcional)
```
