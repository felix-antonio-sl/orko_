# PARTE V: PATTERNS Y ANTI-PATTERNS CATÁLOGO

> **Etiquetado Genoma/Fenotipo**: Este documento es 100% **[FENOTIPO]**:
> - Patterns y Anti-Patterns son soluciones contextuales derivadas de principios PD1-PD76
> - Aplicabilidad depende de madurez org, sector, cultura (no universales)
> - Validados empíricamente pero adaptables según Context Schema (PD36)
>
> Ver ../00_fundamentos_teoricos/00_introduccion.md §0.1 para definición completa framework.

- [PARTE V: PATTERNS Y ANTI-PATTERNS CATÁLOGO](#parte-v-patterns-y-anti-patterns-catálogo)
  - [§1. FUNDAMENTOS PATTERNS](#1-fundamentos-patterns)
  - [§2. PATTERNS D1: ARQUITECTURA](#2-patterns-d1-arquitectura)
    - [PATTERN D1.1: TEAM TOPOLOGY ALIGNED](#pattern-d11-team-topology-aligned)
    - [PATTERN D1.2: DELEGATION LADDER](#pattern-d12-delegation-ladder)
    - [PATTERN D1.3: PURPOSE CASCADE](#pattern-d13-purpose-cascade)
  - [§3. PATTERNS D2: PERCEPCIÓN](#3-patterns-d2-percepción)
    - [PATTERN D2.1: OBSERVABLE INSTRUMENTATION](#pattern-d21-observable-instrumentation)
  - [§4. PATTERNS D3: DECISIÓN](#4-patterns-d3-decisión)
    - [PATTERN D3.1: RICE PRIORITIZATION](#pattern-d31-rice-prioritization)
    - [PATTERN D3.2: WIP LIMIT ENFORCEMENT](#pattern-d32-wip-limit-enforcement)
  - [§5. PATTERNS D4: OPERACIÓN](#5-patterns-d4-operación)
    - [PATTERN D4.1: CONTINUOUS DEPLOYMENT](#pattern-d41-continuous-deployment)
    - [PATTERN D4.2: OBSERVABILITY TRIAD](#pattern-d42-observability-triad)
    - [AP11: MATRIX ORGANIZATIONS](#ap11-matrix-organizations)
    - [AP12: PROCESS OWNERS SEPARADOS](#ap12-process-owners-separados)
    - [AP13: RAINBOW GROUPS](#ap13-rainbow-groups)
    - [AP14: ACTIVITY-BASED TEAMS](#ap14-activity-based-teams)
  - [§6. CROSS-CUTTING PATTERNS](#6-cross-cutting-patterns)
    - [PATTERN X1: HEALTH SCORE DASHBOARD](#pattern-x1-health-score-dashboard)
    - [PATTERN X2: QUARTERLY PLANNING RITUAL](#pattern-x2-quarterly-planning-ritual)
  - [§7. ANTI-PATTERNS CATÁLOGO EXTENDIDO](#7-anti-patterns-catálogo-extendido)
    - [AP1: CONWAY'S LAW IGNORED](#ap1-conways-law-ignored)
    - [AP2: AUTOMATION BLINDNESS](#ap2-automation-blindness)
    - [AP3: ORPHAN OKRS](#ap3-orphan-okrs)
    - [AP4: OBSERVABILITY THEATER](#ap4-observability-theater)
    - [AP5: HIPPO PRIORITIZATION](#ap5-hippo-prioritization)
    - [AP6: THRASHING](#ap6-thrashing)
    - [AP7: BIG BANG RELEASES](#ap7-big-bang-releases)
    - [AP8: PRINTF DEBUGGING](#ap8-printf-debugging)
    - [AP9: METRICS WITHOUT ACTION](#ap9-metrics-without-action)
    - [AP10: IVORY TOWER ARCHITECTURE](#ap10-ivory-tower-architecture)
  - [§8. REMEDIATION PLAYBOOKS](#8-remediation-playbooks)
    - [PLAYBOOK R1: LOW H\_ORG RECOVERY](#playbook-r1-low-h_org-recovery)
    - [PLAYBOOK R2: HANDOFF REDUCTION](#playbook-r2-handoff-reduction)
    - [PLAYBOOK R3: OKR ALIGNMENT](#playbook-r3-okr-alignment)
    - [PLAYBOOK R4-R6: TRANSFORMATION ROADMAP](#playbook-r4-r6-transformation-roadmap)
  - [§9. PATTERN SELECTION GUIDE](#9-pattern-selection-guide)

## §1. FUNDAMENTOS PATTERNS

> **✅ MAPEO CONCEPTUAL ACTUALIZADO**: 
> Related_Principles vinculados a PD1-76.
> Mapeo conceptual verificado. Auditoría textual línea-por-línea recomendada para PD bajos.
> 
> Estructura actual:
> - PD1-30: Invariantes I1-I7 (genoma)
> - PD31-35: AOC Arquetipos (fenotipo)
> - PD36-40: I8 Parametrización (genoma)
> - PD41-46: Métricas AOC/Kelly (fenotipo)
> - PD47-76: Guidelines G## (fenotipo)

```yaml
Definición_Pattern:
  "Pattern = Solución recurrente a problema común en contexto específico,
   derivada de principios diseño (Parte II) y validada empíricamente."

Origen_Derivación:
  - Base teórica: 8 Invariantes (I1-I8)
  - Operacionalización: 76 Principios Diseño (PD1-PD76)
  - Catálisis: Patterns emergen de aplicar principios en contextos específicos
  
Estructura_Pattern:
  Por cada pattern:
    - Name: Identificador memorable
    - Context: Cuándo aplicar
    - Problem: Qué problema resuelve
    - Solution: Cómo implementar
    - Consequences: Trade-offs, efectos secundarios
    - Related_Principles: PD vinculados
    - Related_Contracts: Contratos usados
    - Verification: Cómo validar correcta aplicación
    - Anti-Pattern: Qué NO hacer

Organización_Catálogo:
  Agrupados por dominio primario:
    - D1 Patterns: Arquitectura organizacional
    - D2 Patterns: Observabilidad
    - D3 Patterns: Decisión y priorización
    - D4 Patterns: Operación y delivery
    - Cross-Cutting: Multi-dominio
```

## §2. PATTERNS D1: ARQUITECTURA

### PATTERN D1.1: TEAM TOPOLOGY ALIGNED

```yaml
Context:
  - Organización con múltiples equipos (>3 teams)
  - Flujos de valor identificados
  - Handoffs frecuentes entre equipos
  
Problem:
  "Estructura organizacional genera friction: handoffs lentos, 
   dependencies bloqueantes, comunicación overhead."
  
  Síntoma: A3_Handoff_Ratio > 30% en flujos críticos

Solution:
  
  Paso_1_Mapear_Value_Streams:
    - Identificar 3-5 flujos críticos (VSM, D4.1)
    - Calcular handoff_ratio actual
    - Identificar capacidades involucradas
    
  Paso_2_Aplicar_Conway:
    Principio: "Estructura debe reflejar arquitectura deseada"
    
    Acción:
      - Agrupar capacidades que participan mismo flujo
      - Minimizar dependencies entre equipos
      - Target: Equipo end-to-end ownership flujo
      
  Paso_3_Definir_Team_Topologies:
    Tipos (según Team Topologies - Skelton):
      
      Stream_Aligned_Team:
        - Ownership flujo valor completo
        - Cross-functional (backend, frontend, QA)
        - Long-lived, stable
        - Ejemplo: "Checkout Team" (todo checkout flow)
        
      Enabling_Team:
        - Capacita otros equipos (I4 clasificación contextual)
        - Temporal interaction
        - Ejemplo: "Platform Engineering" (habilita autonomía)
        
      Complicated_Subsystem_Team:
        - Especialización profunda área compleja
        - Ejemplo: "ML Platform Team" (algorítmicos C2+)
        
      Platform_Team:
        - Producto interno (self-service)
        - Reduce cognitive load stream teams
        - Ejemplo: "Developer Platform Team"
        
  Paso_4_Establecer_Interaction_Modes:
    - Collaboration: Trabajo conjunto (discovery phase)
    - X-as-a-Service: Consumo asíncrono (APIs)
    - Facilitation: Enabling team → Stream team
    
Consequences:
  Positivos:
    + Handoffs reducidos (target < 20%)
    + Flow efficiency aumenta
    + Autonomía equipos (faster decisions)
    + Cognitive load reducido (clear boundaries)
    
  Negativos:
    - Requiere reorg (disruptivo corto plazo)
    - Puede duplicar capacidades (trade-off)
    - Requiere madurez técnica (platform capabilities)

Related_Principles:
  - PD48: Handoff Formal Definition (target < 20% handoffs cross-team)
  - PD14: Test Cliente Externo (clasificación Producción/Habilitación)
  - PD6: Separación Concerns (equipos responsabilidad única)
  - PD7: Relaciones Explícitas (interaction modes claros)

Related_Contracts:
  - C1 (Capacidad): composition, role
  - C2 (Flujo): steps, handoff_count
  
Verification:
  Métricas:
    - A3_Handoff_Ratio < 20%
    - Team autonomy index > 0.80 (% decisiones sin dependencies)
    - Lead time reducido 30-50%
    
  Queries:
    - Q1 (Capacidades por flujo): Verificar ownership
    - A3 handoff metric (Parte IV)

Anti-Pattern: CONWAY'S LAW IGNORED
  
  Síntoma:
    - Estructura funcional (Frontend Dept, Backend Dept, QA Dept)
    - Flujo cruza 5+ equipos
    - Handoff_ratio > 40%
    
  Problema:
    "Estructura no alineada con flujos genera friction masivo"
    
  Consecuencias:
    - Lead time alto (90th %ile > 1 mes)
    - Blame culture (handoffs = responsabilidad diluida)
    - Calidad baja (nadie owner end-to-end)
    
  Refactoring:
    Aplicar TEAM TOPOLOGY ALIGNED (este pattern)
```

### PATTERN D1.2: DELEGATION LADDER

```yaml
Context:
  - Capacidades algorítmicas (C0-C2) operando
  - Decisión/acción delegable de humano a algorítmico
  - Confianza en algorítmico variable (trajectory)
  
Problem:
  "¿Cuándo delegar decisión/acción a capacidad algorítmica?
   Delegar muy rápido → errores costosos
   Delegar muy lento → no capturar eficiencia"
  
  Origen: I6 (Trajectory-Awareness), véase **03_invariantes.md** (I1–I8)

Solution:
  
  Progressive_Delegation_Modes:
    Basado_En: 00_fundamentos_teoricos/03_invariantes.md §6 I5_[FENOTIPO]
    Canon: Modos M1-M6 definidos en invariante I5 HAIC
    
    M1_Manual_Total:
      Human_Role: Ejecuta 100% acción
      Algorítmico_Role: NO participa
      Cuándo: Nueva tarea, alta criticidad, zero trajectory
      Ejemplo: Primer deployment nueva aplicación
      
    M2_Sugerencia:
      Human_Role: Decide y ejecuta
      Algorítmico_Role: Sugiere opción (human puede ignorar)
      Cuándo: Algorítmico learning, low confidence
      Ejemplo: IDE code completion (human acepta/rechaza)
      Transition: M1→M2 cuando trajectory > 10 ejecuciones
      
    M3_Recomendación:
      Human_Role: Decide (veto power)
      Algorítmico_Role: Recomienda fuertemente
      Cuándo: Confidence media, decisiones reversibles
      Ejemplo: Autoscaling recommendations (human aprueba)
      Transition: M2→M3 cuando accuracy > 70%
      
    M4_Automatización_Supervisada:
      Human_Role: Supervisa, interviene si anomalía
      Algorítmico_Role: Ejecuta automáticamente
      Cuándo: Confidence alta, monitoring robusto
      Ejemplo: Auto-deploy staging (human watches)
      Transition: M3→M4 cuando accuracy > 85% Y monitoring real-time
      
    M5_Automatización_Excepción:
      Human_Role: Interviene solo si alerta
      Algorítmico_Role: Ejecuta, alerta anomalías
      Cuándo: Confidence muy alta, low-risk
      Ejemplo: Auto-scaling production (alerta si threshold)
      Transition: M4→M5 cuando error_rate < 5% Y false_positive < 10%
      
    M6_Automatización_Completa:
      Human_Role: Audita periódicamente (post-hoc)
      Algorítmico_Role: Totalmente autónomo
      Cuándo: Confidence extrema, well-understood domain
      Ejemplo: DNS auto-remediation, cache warming
      Transition: M5→M6 cuando error_rate < 1% Y 6+ meses stable
      
  Reglas_Transición:
    
    R1_No_Saltar_Niveles:
      "NO permitido M1 → M4 directamente"
      Justificación: Confianza debe construirse gradual
      Excepción: Migración de otro sistema con trajectory comprobada
      
    R2_Rollback_Si_Degrada:
      IF accuracy degrada > 20% THEN rollback 1 nivel
      IF incident crítico THEN rollback a M1 (manual total)
      
    R3_Humano_Accountable_Siempre:
      ∀ nivel M1-M6: Human capacity_id accountable resultado (I5)
      Algorítmico NO tiene accountability legal/ética
      
  Implementación_Técnica:
    
    Metadata_Capacidad_Algorítmica:
      ```yaml
      capacity:
        id: auto-deploy-bot
        substrate: Algorítmico
        capacity_type: C1
        delegation:
          current_mode: M4
          trajectory:
            executions: 543
            success_rate: 0.92
            last_incident: 2024-10-15
          transitions:
            - from: M1, to: M2, date: 2024-01-10, reason: "10 manual deploys ok"
            - from: M2, to: M3, date: 2024-03-15, reason: "accuracy 75%"
            - from: M3, to: M4, date: 2024-06-20, reason: "accuracy 88%, monitoring live"
          accountable_capacity_id: uuid-sre-lead
      ```

Consequences:
  Positivos:
    + Safety: Delegación gradual reduce risk
    + Efficiency: Captura automation benefits progresivamente
    + Learning: Trajectory informa evolution
    + Accountability: Human always responsible (I5)
    
  Negativos:
    - Overhead: Tracking modes per capacity
    - Discipline: Requiere NO saltar niveles
    - Monitoring: M4-M6 requieren observabilidad robusta

Related_Principles:
  - PD18: Accountability Humana Transversal (I5 HAIC - humano responsible siempre)
  - PD19: Delegación Explícita Cross Domain (I5 - modos M1-M6)
  - PD22: Trajectory Log (I6 - registrar ejecuciones)
  - PD23: Progresión Gradual (I6 - validar cada nivel antes promoción)
  - PD24: Drift Detection (I6 - monitorear degradación performance)

Related_Contracts:
  - C1 (Capacidad): delegation metadata, accountability
  
Verification:
  Métricas:
    - % capacidades algorítmicas con delegation mode definido (target: 100%)
    - Incident rate por modo (M6 debe ser < M4)
    - Transition velocity (meses promedio M1→M6)
    
  Auditoría:
    - Review quarterly delegation levels
    - Validate no mode jumps (M1→M4+)
    - Verify accountable_capacity_id presente

Anti-Pattern: AUTOMATION BLINDNESS
  
  Síntoma:
    - Deploy algorítmico en M6 sin trajectory
    - Human NO supervisa M4-M5
    - Incident algorítmico → "no vimos venir"
    
  Problema:
    "Over-trust en automation sin validar confiabilidad"
    
  Consecuencias:
    - Incidents críticos (downtime, data loss)
    - Violación I5 (accountability diluida)
    - Loss of control (no rollback plan)
    
  Ejemplos_Reales:
    - Knight Capital (2012): $440M pérdida, algo M6 sin supervision
    - AWS S3 Outage (2017): Typo comando automatizado
    
  Refactoring:
    1. Rollback a M3 (human approval)
    2. Instrument monitoring robusto
    3. Build trajectory (≥100 executions)
    4. Progressive delegation M3→M4→M5→M6
```

### PATTERN D1.3: PURPOSE CASCADE

```yaml
Context:
  - Organización multi-nivel (individual → team → unit → org)
  - OKRs o goals definidos nivel org
  - Necesidad alineación vertical
  
Problem:
  "Equipos/individuos trabajan sin claridad cómo contribuyen a propósito org.
   Resultado: esfuerzo misaligned, motivation baja, suboptimización."
  
  Síntoma: A4_Alignment_OKRs < 60%

Solution:
  
  Estructura_Jerárquica:
    Basado_En: R11 (Propósito_Jerarquía), véase **03_invariantes.md** (I1–I8)
    
    Niveles:
      L4_Organización:
        - Scope: Company-wide
        - Horizon: Anual (visión 1-3 años)
        - Owners: C-level
        - Ejemplo: "Liderar mercado SaaS LATAM (ARR $50M)"
        
      L3_Unidad:
        - Scope: Business unit / Department
        - Horizon: Quarterly-Anual
        - Owners: VPs, Directors
        - Ejemplo: "Product: Lanzar 10 enterprise features Q1-Q4"
        - Constraint: parent_purpose_id = L4
        
      L2_Equipo:
        - Scope: Team (5-9 personas)
        - Horizon: Quarterly
        - Owners: Team Leads, Engineering Managers
        - Ejemplo: "Auth Team: Implementar SSO enterprise-grade Q1"
        - Constraint: parent_purpose_id = L3
        
      L1_Individual:
        - Scope: Persona
        - Horizon: Sprint-Quarterly
        - Owners: Individual contributor
        - Ejemplo: "Engineer: Completar SAML Okta integration Sprint 5"
        - Constraint: parent_purpose_id = L2
        
  Propiedades_Cascada:
    
    P1_Parent_Link:
      ∀ propósito (excepto L4): MUST have parent_purpose_id
      Query Q4 (Path to Root) MUST succeed
      
    P2_Contribution_Explicit:
      ∀ child purpose: explain HOW contribuye a parent
      
      Ejemplo:
        L2 "Auth Team SSO": 
          contributes_to: L3 "10 enterprise features"
          contribution: "SSO es 1 de 10 features enterprise"
          
    P3_Metrics_Aligned:
      child.key_results → parent.key_results (causal link)
      
      Ejemplo:
        Parent KR: "10 features shipped"
        Child KR: "1 feature (SSO) shipped" → contributes 10%
        
    P4_Timeline_Nested:
      child.end_date ≤ parent.end_date (no desborde)
      
  Implementación_Workshop:
    
    Fase_1_Top_Down (Planning):
      - L4 (C-level) define org OKRs (annual kick-off)
      - L3 (VPs) draft unit OKRs (alignment session)
      - Review L4 ← L3 (verify contribution)
      - Commit L3 OKRs
      
    Fase_2_Middle (Cascading):
      - L2 (Teams) draft team OKRs (team planning)
      - Review L3 ← L2 (verify contribution)
      - Commit L2 OKRs
      
    Fase_3_Bottom (Execution):
      - L1 (Individuals) draft personal OKRs (1:1s)
      - Review L2 ← L1 (verify contribution)
      - Commit L1 OKRs
      
    Duration: 2-3 semanas (inicio quarter)
    
  Tracking_Continuo:
    
    Weekly_Updates:
      - Individuals update L1 progress
      - Roll-up automático L1 → L2 (weighted avg)
      
    Bi-Weekly_Reviews:
      - Teams review L2 progress
      - Identify at-risk OKRs
      
    Monthly_Executive:
      - VPs review L3 progress con C-level
      - Adjust if needed (pivot OKRs)
      
    Quarterly_Retrospective:
      - Score final OKRs (% completed)
      - Lessons learned (qué funcionó/no)
      - Plan next quarter cascade

Consequences:
  Positivos:
    + Alignment vertical (everyone knows "why")
    + Motivation increased (purpose clarity)
    + Prioritization easier (if not aligned, defer)
    + Accountability clear (ownership per level)
    
  Negativos:
    - Overhead: Planning 2-3 semanas/quarter
    - Rigidity: Puede limitar oportunismo (tradeoff)
    - Cascading lento: Changes L4 → L1 toman semanas

Related_Principles:
  - PD49: Alignment Weighted Recursive (G28 - fórmula alignment score OKRs)
  - PD10: Metadata Obligatoria (I3 - created_by, parent_id)
  - PD11: Lineage Completo (I3 - trazabilidad cascada OKR)
  - PD13: Decision Records (I3 - justificación propósitos)

Related_Contracts:
  - C5 (Propósito): parent_id, contribution
  
Related_Artefactos:
  - D1.3 Purpose Cascade (visual)
  - D3.1 OKR Planning Canvas

Verification:
  Métricas:
    - A4_Alignment_OKRs > 85%
    - % propósitos con parent_id (target: 100% L1-L3)
    - Alignment_Score = Σ(peso_child × progress) / Σ peso
    
  Queries:
    - Q4 (Path to Root): Todo propósito alcanza L4

Anti-Pattern: ORPHAN OKRS
  
  Síntoma:
    - Teams definen OKRs sin link a org
    - OKRs individuales sin link a team
    - Q4 (Path to Root) falla
    
  Problema:
    "Trabajo desconectado de propósito org → waste"
    
  Consecuencias:
    - Suboptimización (local maxima, global suboptimal)
    - Frustración (trabajo no valorado)
    - Misalignment (conflictos entre teams)
    
  Refactoring:
    1. Audit propósitos sin parent (Q4 check)
    2. Workshopping: Link to parent o deprecate
    3. Enforce: No commit OKR sin parent_id (L1-L3)
```

## §3. PATTERNS D2: PERCEPCIÓN

### PATTERN D2.1: OBSERVABLE INSTRUMENTATION

```yaml
Context:
  - Sistema productivo operando
  - Necesidad visibilidad estado (D2 responsabilidad)
  - Limitado presupuesto observability tools
  
Problem:
  "¿Qué instrumentar para tener visibilidad sin overwhelm?
   Instrumentar todo → noise, costo alto
   Instrumentar poco → blind spots"
  
  Síntoma: P1_Coverage_Observables < 70%

Solution:
  
  Priorización_16_Observables:
    Basado_En: véase **03_invariantes.md** (I1–I8) (EX1-8, IN1-8)
    
    Tier_1_Critical (MUST have):
      Externos:
        - EX5 Feedback Clientes (NPS, CSAT, support tickets)
        - EX3 Regulatorio (compliance deadlines)
        
      Internos:
        - IN1 Velocidad Entrega (DORA lead time)
        - IN4 Calidad Outputs (defect rate, incidents)
        - IN7 Violaciones Límites (compliance, security)
        - IN8 Debt Técnico (incident frequency, hotfix rate)
        
      Justificación: Risk mitigation (customers, compliance, quality)
      
    Tier_2_Important (SHOULD have):
      Externos:
        - EX1 Demanda Clientes (pipeline, inbound leads)
        - EX4 Tecnológico (vulnerabilities, platform updates)
        
      Internos:
        - IN2 Salud Capacidades (engagement, turnover)
        - IN3 Eficiencia Flujos (flow efficiency)
        - IN5 Utilización Capacidades (idle vs overload)
        - IN6 Alineación Propósitos (OKR progress)
        
      Justificación: Performance optimization
      
    Tier_3_Nice_to_Have:
      Externos:
        - EX2 Competidores (market intelligence)
        - EX6 Disruptivo (emerging business models)
        - EX7 Social (brand sentiment)
        - EX8 Económico (market conditions)
        
      Justificación: Strategic foresight
      
  Implementación_Gradual:
    
    Fase_1 (Mes 1-2):
      - Instrument Tier 1 (6 observables críticos)
      - Manual tracking (spreadsheet)
      - Weekly review
      Target: P1_Coverage = 37.5% (6/16)
      
    Fase_2 (Mes 3-4):
      - Instrument Tier 2 (6 observables importantes)
      - Semi-automated (scripts + dashboard)
      - Bi-weekly review
      Target: P1_Coverage = 75% (12/16)
      
    Fase_3 (Mes 5-6):
      - Instrument Tier 3 (4 observables strategic)
      - Automated dashboard (real-time)
      - Monthly review
      Target: P1_Coverage = 100% (16/16)
      
  Técnicas_Instrumentación:
    
    Para_Externos:
      EX5 Feedback:
        - Source: Zendesk API, survey tools
        - Metric: NPS score, CSAT rolling avg
        - Freshness: Daily
        
      EX3 Regulatorio:
        - Source: Legal team notifications, compliance calendar
        - Metric: # upcoming deadlines próximos 90 días
        - Freshness: Weekly
        
    Para_Internos:
      IN1 Velocidad:
        - Source: GitHub commits, CI/CD timestamps
        - Metric: Lead time commit → deploy (p50, p90)
        - Freshness: Real-time
        
      IN4 Calidad:
        - Source: Incident tracking, test results
        - Metric: Defect density, incident rate
        - Freshness: Real-time
        
      IN7 Violaciones:
        - Source: SIEM logs, policy checks
        - Metric: COUNT(violations) per type
        - Freshness: Event-driven
        
  Anomaly_Detection_Setup:
    
    Statistical_Baseline:
      - Collect 4 semanas data mínimo
      - Calculate mean, stddev per observable
      - Threshold: mean ± 2σ
      
    Alerting:
      - IF value > threshold THEN log anomaly (D2.2)
      - Severity based on deviation:
        * 2-3σ: Warning
        * 3-4σ: High
        * >4σ: Critical

Consequences:
  Positivos:
    + Visibilidad incrementada (blind spots reducidos)
    + Priorización ROI (Tier 1 primero)
    + Anomaly detection temprana
    + Decision-making informado
    
  Negativos:
    - Esfuerzo instrumentación (1-2 person-months)
    - Maintenance overhead (dashboards, alerts)
    - False positives iniciales (tuning required)

Related_Principles:
  - PD51: Observable Standard Units (G30 - units canónicas 16 observables)
  - PD10: Metadata Obligatoria (I3 - freshness, source tracking)
  - PD3: Eliminación Redundancia (I1 - priorizar observables ROI)

Related_Contracts:
  - C3 (Información): observable_id, freshness
  
Related_Artefactos:
  - D2.1 Dashboard 16 Observables

Verification:
  Métricas:
    - P1_Coverage > 75% (Tier 1+2 instrumentados)
    - P2_Freshness > 90% (observables actualizados)
    - P3_Latencia_Detección < 24h (anomalías detectadas rápido)

Anti-Pattern: OBSERVABILITY THEATER
  
  Síntoma:
    - Dashboard con 50+ métricas
    - Nadie mira dashboard
    - Anomalías NO detectadas (P3 latencia > 1 semana)
    
  Problema:
    "Instrumentar todo sin priorizar → information overload → no action"
    
  Consecuencias:
    - Wasted effort (dashboards no usados)
    - Blind spots (métricas críticas buried en noise)
    - Incidents NOT prevented
    
  Refactoring:
    1. Audit: ¿Qué métricas realmente se usan?
    2. Prune: Eliminar bottom 50% unused
    3. Focus: Tier 1 visible, alertado
    4. Review: Monthly relevance check
```

## §4. PATTERNS D3: DECISIÓN

### PATTERN D3.1: RICE PRIORITIZATION

```yaml
Context:
  - Portfolio de iniciativas > capacidad disponible (typical)
  - Necesidad priorización objetiva
  - Stakeholders con preferencias conflictivas
  
Problem:
  "¿Cómo priorizar iniciativas cuando todo es 'high priority'?"
  
  Síntoma: D3_Portfolio_Balance desbalanceado (todo urgent)

Solution:
  
  Framework_RICE:
    Fórmula: Score = (Reach × Impact × Confidence) / Effort
    
    Reach:
      Definición: # usuarios/clientes afectados por período
      
      Ejemplos:
        - Feature B2C: 10,000 users/month
        - Feature enterprise: 50 customers/quarter
        - Infrastructure: 100% engineering (200 people)
        
      Units: Usuarios o capacidades afectadas
      
    Impact:
      Definición: Magnitud efecto por usuario (escala 0.25-3)
      
      Escala:
        3.0 = Massive impact (game-changer, 10x improvement)
        1.0 = High impact (significativo, 3x improvement)
        0.5 = Medium impact (noticeable, 1.5x improvement)
        0.25 = Low impact (minimal, 1.1x improvement)
        
      Ejemplos:
        - SSO enterprise: 3.0 (massive - unblocks sales)
        - Performance optimization: 0.5 (medium - users notice)
        - UI polish: 0.25 (low - nice to have)
        
    Confidence:
      Definición: Certeza estimaciones (escala 0.5-1.0)
      
      Escala:
        1.0 = High confidence (validated data, clear requirements)
        0.8 = Medium confidence (some data, assumptions reasonable)
        0.5 = Low confidence (hypothesis, high uncertainty)
        
      Ejemplos:
        - Customer-requested feature: 1.0 (validated demand)
        - Optimization hypothesis: 0.8 (data suggests benefit)
        - Speculative bet: 0.5 (uncertain)
        
    Effort:
      Definición: Person-months trabajo total
      
      Incluye:
        - Development time (coding, testing)
        - Design time (UX, architecture)
        - Deployment time (migration, training)
        - Maintenance (ongoing, amortizado)
        
      Ejemplos:
        - Small feature: 0.5 person-months
        - Medium feature: 2 person-months
        - Large initiative: 10 person-months
        
  Ejemplo_Cálculo:
    
    Initiative_A_SSO:
      Reach: 50 enterprise customers
      Impact: 3.0 (massive - unblocks $2M ARR)
      Confidence: 0.8 (validated with sales)
      Effort: 3 person-months
      Score = (50 × 3.0 × 0.8) / 3 = 40
      
    Initiative_B_API:
      Reach: 200 developers
      Impact: 1.0 (high - better DX)
      Confidence: 0.8
      Effort: 6 person-months
      Score = (200 × 1.0 × 0.8) / 6 = 26.7
      
    Initiative_C_UI_Redesign:
      Reach: 10,000 users
      Impact: 0.5 (medium - aesthetics)
      Confidence: 0.5 (uncertain adoption)
      Effort: 4 person-months
      Score = (10,000 × 0.5 × 0.5) / 4 = 625
      
    Priorización: C (625) > A (40) > B (26.7)
    
  Implementación_Workflow:
    
    Input_Gathering:
      - Collect initiatives (backlog, stakeholders)
      - Workshop: Estimate RICE per initiative (2-4 horas)
      - Participants: Product, Engineering, Data
      
    Scoring:
      - Calculate RICE score per initiative
      - Sort descending (highest first)
      - Bucket: Now / Next / Later
      
    Capacity_Allocation:
      - Capacity available = Team throughput × period
      - Allocate top-scored hasta capacity full
      - Defer resto (explicit "Later")
      
    Review_Cadence:
      - Re-score quarterly (new data, context changed)
      - Add new initiatives (continuous)
      - Archive completed (track actuals vs estimates)

Consequences:
  Positivos:
    + Objectivity (formula-driven, less politics)
    + Transparency (stakeholders see scoring)
    + ROI-focused (maximize value/effort)
    + Confidence-adjusted (uncertainty accounted)
    
  Negativos:
    - Estimación required (effort uncertainty)
    - Gaming risk (inflate reach/impact)
    - Ignores dependencies (puede priorizar blocked initiative)

Related_Principles:
  - PD64: Portfolio Value Maximization (G14 - ROI-weighted prioritization)
  - PD63: Decision Audit Trail (G7 - documentar rationale priorización)

Related_Artefactos:
  - D3.2 Portfolio Board (RICE scores visible)

Verification:
  Métricas:
    - D3_Portfolio_Balance: 70% Now, 20% Next, 10% Later
    - D4_Execution_Rate > 70% (high-scored actually deliver value)
    - Correlation RICE_score vs actual_value delivered

Anti-Pattern: HIPPO PRIORITIZATION
  
  Síntoma:
    - Iniciativas priorizadas por "Highest Paid Person Opinion"
    - RICE score calculado pero ignorado
    - Low-RICE initiatives en "Now"
    
  Problema:
    "Decisión política override datos → suboptimal allocation"
    
  Consecuencias:
    - Low ROI (effort desperdiciado)
    - Team frustration (scoring exercise inútil)
    - Misaligned outcomes (prioridades personales vs org)
    
  Refactoring:
    1. Executive alignment: C-level commit seguir RICE
    2. Transparency: Publish scores público
    3. Override process: If override RICE, document WHY
    4. Retrospective: Compare RICE predictions vs actuals
```

### PATTERN D3.2: WIP LIMIT ENFORCEMENT

```yaml
Context:
  - Multiple iniciativas en progreso simultáneamente
  - Limited capacidad disponible
  - Lead times incrementando
  
Problem:
  "Too much work-in-progress → context switching, nothing finishes"
  
  Síntoma: D3 cycle time > 2× baseline

Solution:
  
  Calcular_WIP_Limit:
    Fórmula: WIP_max = Throughput × Lead_Time_Target
    
    Ejemplo:
      Team throughput: 4 features/quarter
      Lead time target: 4 weeks
      Period: 12 weeks
      WIP_max = 4 × (4/12) ≈ 1-2 initiatives simultáneas
      
  Enforcement_Rules:
    - IF WIP = WIP_max THEN NO new work starts
    - Finish work before starting new
    - Blocked work NO cuenta hacia WIP (parking lot)
    
  Beneficios:
    + Lead time reducido 40-60%
    + Focus increased
    + Throughput maintained or improved

Related_Principles:
  - PD44: TD Small Batches Gate (Kelly - reducir WIP, faster delivery)
  - PD45: TD Flow Gate (Kelly - lead time target, Little's Law)

Related_Artefactos:
  - D3.2 Portfolio Board (WIP visible)

Anti-Pattern: THRASHING
  
  Síntoma: WIP = 3× capacity, nothing finishes
  Refactoring: Apply WIP limit immediately
```

## §5. PATTERNS D4: OPERACIÓN

### PATTERN D4.1: CONTINUOUS DEPLOYMENT

```yaml
Context:
  - Software delivery team
  - Testing automated
  - Rollback capability exists
  
Problem:
  "Manual deploys → slow feedback, batch risk"

Solution:
  
  Pipeline_Stages:
    1. Commit → CI (build + unit tests) < 10 min
    2. Deploy staging → E2E tests < 30 min
    3. Deploy canary 5% → monitor < 1h
    4. Deploy 100% → monitor < 4h
    
  Automated_Rollback:
    IF error_rate > 2× baseline THEN auto-rollback
    
  Beneficios:
    + DORA M1: Multiple deploys/day
    + M2: Lead time < 1 day
    + M3: Change failure < 15%

Related_Principles:
  - PD60: DORA Metrics Mandatory (G4 - M1-M4 deployment frequency, lead time)
  - PD44: TD Small Batches (Kelly - deploy frecuente reduce riesgo)
  - PD59: Execution Instance Tracking (G3 - E7 records por deploy)

Anti-Pattern: BIG BANG RELEASES
  
  Síntoma: Monthly/quarterly deploys, high failure rate
  Refactoring: Incremental CD adoption
```

### PATTERN D4.2: OBSERVABILITY TRIAD

```yaml
Context:
  - Production system operating
  - Incidents occur
  - Root cause analysis difficult
  
Problem:
  "Can't debug production issues effectively"

Solution:
  
  Three_Pillars:
    
    Logs:
      - Structured (JSON format)
      - Contextual (trace_id, user_id)
      - Searchable (ELK, Splunk)
      
    Metrics:
      - RED (Rate, Errors, Duration)
      - USE (Utilization, Saturation, Errors)
      - Business metrics (conversions, revenue)
      
    Traces:
      - Distributed tracing (Jaeger, DataDog)
      - Request flow visibility
      - Latency breakdown per service
      
  Integration:
    - Correlation IDs link logs ↔ metrics ↔ traces
    - Single pane dashboard
    - Alert → log → trace workflow

Related_Principles:
  - PD51: Observable Standard Units (G30 - logs, metrics, traces estándar)
  - PD61: Incident Flow Linkage (G5 - root cause a deployment)
  - PD60: DORA Metrics (M4 MTTR - mean time to recovery)

Related_Artefactos:
  - D4.2 DORA Dashboard
  - D4.3 Incident Log

Anti-Pattern: PRINTF DEBUGGING
  
  Síntoma: No structured logging, manual SSH to debug
  Refactoring: Implement triad incrementally
```

### AP11: MATRIX ORGANIZATIONS

```yaml
Origen: AOC AP1 (Matrix Organizations)

Síntoma:
  - Dual reporting: Employee → Manager funcional AND Project manager
  - Autoridad fragmentada (no unique 'A')
  - Accountability ambigua (culpan al otro)
  - Conflicto prioridades (¿quién decide?)

Problema:
  "Matrix viola P1_Entrelazamiento_A-A (autoridad-accountability separados)"

Consecuencias:
  - Decisiones lentas (escalations constantes)
  - Meetings excesivos (coordinate conflicts)
  - Stress alto (employees in middle)
  - Performance mediocre (no ownership)
  - Politics dominate (lobbying, no merit)

Manifestación_Física:
  - Calendario saturado reuniones coordinación
  - Emails CC: listas largas (CYA behavior)
  - Decision velocity <1 per week (parálisis)

Remediation:
  1. Eliminar dual reporting:
     - Feature teams (stream-aligned): Single manager, end-to-end
     - Project manager → Product owner DENTRO team (no external)
  2. Functional expertise → Guilds:
     - Informal communities practice (no reporting line)
     - Knowledge sharing, no authority
  3. RACI único:
     - Por cada outcome: Exactamente 1 'A'
     - Validate matriz compliance 100%

Related_Principles:
  - PD18: Accountability Humana (violado por matrix)
  - PD31: Cohesión Máxima (matrix baja cohesion)
```

### AP12: PROCESS OWNERS SEPARADOS

```yaml
Origen: AOC AP2 (Process Owners separate from Executors)

Síntoma:
  - "Process owner" tiene autoridad sobre proceso
  - Executors implementan pero no controlan diseño
  - Process owner optimiza proceso, ignora outcome

Problema:
  "Autoridad-Accountability split (violates PD18)"

Consecuencias:
  - Procesos complejos (owner no ejecuta, no simplifica)
  - Compliance theater (check boxes, no value)
  - Innovation killed (executors no empowered)
  - Improvements slow (owner no siente pain)

Ejemplo_Real:
  - "Deployment Process Owner" (no deploys)
  - Define proceso complejo 15 steps, 8 approvals
  - Team frustrationsufre delays, no puede mejorar
  
Remediation:
  1. Reunificar:
     - Executor team OWNS process design (live it daily)
     - "Process owner" → Coach/Consultant (no authority)
  2. Continuous improvement by doers:
     - Kaizen ownership en team ejecutor
     - Measure pain (cycle time, errors)
     - Simplify directamente (no approval external)

Related_Principles:
  - PD18: Accountability Humana Transversal (I5 - violado por process owner separado)
  - Origen: AOC P1 Entrelazamiento Autoridad-Accountability
```

### AP13: RAINBOW GROUPS

```yaml
Origen: AOC AP3 (Mixed Archetypos Incompatibles)

Síntoma:
  - Team mezcla arquetipos incompatibles
  - Ej: Mismo team hace innovation (α) AND operations (β)
  - Valores conflictivos (speed vs stability)

Problema:
  "Viola PD32_Incompatibilidad_α_β (y similares PD33-35)"

Consecuencias:
  - Innovation sufre (no time, risk-averse)
  - Operations sufre (instability, tech debt)
  - Team identity confused ("¿qué somos?")
  - Mediocrity: Neither innovates NOR operates well
  - Context switching alto (cognitive load)
  - Internal conflicts (prioritization fights)

Detección:
  IF Capacity.archetype combina {α,β} OR {γ,δ} OR {γ,ε} OR {δ,ε}
  THEN alert("Rainbow Group - Incompatibilidad detectada")

Remediation:
  1. Separar dominios:
     - Dominio_A (α Creadores): R&D, new products, innovation
     - Dominio_B (β Operadores): Production, SRE, operations
  2. Define interfaces claras:
     - APIs, SLAs bien documentados
     - Handoff protocols (α → β transition)
  3. NO merge:
     - Mantener separados permanentemente
     - Resist presión consolidar "por eficiencia"

Metrics_Success:
  - Archetypal_Purity (A6) > 80% per domain
  - Team identity clear (survey "somos X")
  - Performance improvement both sides (+20% typical)

Related_Principles:
  - PD32-35: Incompatibilidades arquetipos
  - PD31: Cohesión Máxima (rainbow baja cohesion)
```

### AP14: ACTIVITY-BASED TEAMS

```yaml
Origen: AOC AP4 (Activity-Based Teams)

Síntoma:
  - Teams organizados por actividad, no outcome
  - Ej: "Testing team", "Deployment team", "Frontend team"
  - Especialización funcional extrema

Problema:
  "Maximiza handoffs (opuesto PD3_Acoplamiento_Mínimo + PD31_Cohesión)"

Consecuencias:
  - Handoffs maximizados (>40% typical)
  - Wait time dominante (dependencies everywhere)
  - Accountability difusa (nadie owns outcome)
  - Optimization local, no end-to-end
  - Cycle time >>2x benchmark
  - Blame games ("not my job")
  - Customer unhappy (nobody owns experience)

Ejemplo_Típico:
  Feature request flow:
  PM → Design → Backend → Frontend → QA → DevOps → Production
  6+ handoffs, 45 días cycle time (10% touch time)

Remediation:
  1. Reorganizar por VALUE_STREAM:
     - Feature teams (stream-aligned): Own outcome end-to-end
     - Cross-functional: All skills inside team
       * PM/UX + Backend + Frontend + QA integrated
  2. Minimize handoffs:
     - Target: <20% interactions external
     - Team autonomy: >70% decisions internal
  3. Shared services → Platform teams:
     - DevOps → Platform team (self-service CI/CD)
     - Infrastructure → APIs (no tickets)

Metrics_Success:
  - H3_O3_Handoff_Waste < 20%
  - Cycle time reduction 30-50%
  - Team satisfaction +2 points (ownership)

Related_Principles:
  - PD48: Handoff Formal Definition (G27 - target <20% cross-team handoffs)
  - PD31: Cohesión Máxima (cross-functional teams reduce handoffs)
  - PD7: Relaciones Explícitas (I2 - interfaces claras entre teams)
```

## §6. CROSS-CUTTING PATTERNS

### PATTERN X1: HEALTH SCORE DASHBOARD

```yaml
Context:
  - Organization operating ORKO
  - Need holistic health visibility
  - Executive reporting required

Problem:
  "How to measure organizational health objectively?"

Solution:
  
  Implement_H_org:
    - Calculate monthly A_Score, P_Score, D_Score, O_Score
    - Aggregate H_org = weighted average
    - Dashboard visible to all
    - Trigger interventions if H_org < 70
    
  Executive_Review:
    - Monthly review with C-level
    - Drill-down on red components
    - Action plans for improvement
    - Track trends quarter-over-quarter

Related_Principles:
  - PD62: Health Score Composite (G6 - H_org = weighted H1-H5)
  - PD41-43: AOC Coherencia/Resonancia/Flujo Gates (inputs H_org)
  - PD30: Health Prerequisito (I7 - H_org ≥ 70 para transformaciones)

Related_Artefactos:
  - §6 Parte IV (H_org integrado)
```

### PATTERN X2: QUARTERLY PLANNING RITUAL

```yaml
Context:
  - Quarter ending, next quarter planning
  - All 4 domains need alignment

Problem:
  "Coordinating D1-D4 planning"

Solution:
  
  3-Week_Cycle:
    
    Week_1_Retrospective:
      - Review H_org (all scores)
      - Identify problems (anomaly log review)
      - Lessons learned workshops
      
    Week_2_Strategy:
      - D3: OKR planning (cascade L4→L1)
      - D1: Structure adjustments if needed
      - D2: Observable targets next quarter
      
    Week_3_Execution:
      - D4: Capacity allocation to OKRs
      - Portfolio board population
      - Commitment ceremony
      
  Outputs:
    - Purpose Cascade updated (D1.3)
    - OKR Canvas per team (D3.1)
    - Portfolio Board committed (D3.2)
    - DORA targets set (D4.2)

Related_Principles:
  - PD49: Alignment Weighted Recursive (G28 - OKR cascade L4→L1)
  - PD64: Portfolio Value Maximization (G14 - portfolio planning quarterly)
  - PD63: Decision Audit Trail (G7 - documentar commitments)
```

## §7. ANTI-PATTERNS CATÁLOGO EXTENDIDO

### AP1: CONWAY'S LAW IGNORED

```yaml
Origen: Pattern D1.1 (TEAM TOPOLOGY ALIGNED) - anti-pattern implícito

Síntoma:
  - Estructura organizacional NO refleja flujos valor
  - Equipos organizados por función (Frontend, Backend, QA, DevOps)
  - Producto requiere coordinación 5+ equipos para feature simple
  - A3_Handoff_Ratio > 40% (target: <20%)
  - Meetings excesivos (coordination overhead dominante)
  
Problema:
  "Estructura org ignora Conway's Law: arquitectura sistema refleja estructura comunicación.
   Si estructura no alineada con flujos → friction inevitable."
   
  Viola:
    - PD48: Handoff Formal Definition (G27 - target <20% cross-team)
    - PD31: Cohesión Máxima (skills dispersos entre teams)
    
Consecuencias:
  Operacionales:
    - Lead time inflado (90th %ile > 30 días, target: <7 días)
    - Wait time dominante (80% cycle time = handoff delays)
    - Batch sizes grandes (para "justificar" coordination cost)
    
  Organizacionales:
    - Accountability difusa (nadie owns outcome end-to-end)
    - Blame culture ("not my job", finger pointing)
    - Suboptimización local (cada team optimiza su función, no flujo)
    
  Arquitecturales:
    - Sistema refleja org disfuncional (monolito acoplado o microservices caótico)
    - APIs internas mal diseñadas (reflejan boundaries políticos, no lógicos)
    - Technical debt acumulado (nadie owner refactoring cross-funcional)
    
Manifestation_Física:
  - Calendario saturado "sync meetings" (3-5 por día)
  - JIRA tickets bloqueados por dependencies (>30% en estado "waiting")
  - Deployment trains (monthly releases porque coordinación compleja)
  - War rooms frecuentes (incidents requieren 6+ personas)
  
Detección_Métricas:
  IF A3_Handoff_Ratio > 40% THEN alert("Conway ignored")
  IF Lead_Time > 30d AND Wait_Time > 70% THEN alert("Structural misalignment")
  IF Meeting_Hours_Week > 15 per person THEN alert("Coordination overhead")
  
Remediation:
  
  Fase_1_Assessment (2-4 semanas):
    1. Mapear value streams actuales:
       - Identificar 3-5 flujos críticos (ej: "New Feature", "Bug Fix", "Customer Onboarding")
       - Por cada flujo: steps, teams involved, handoffs count
       - Métrica: A3_Handoff_Ratio actual por flujo
       
    2. Analizar impacto:
       - Lead time vs benchmark industry
       - % tiempo value-add vs wait
       - Satisfaction survey equipos (frustration level)
       
  Fase_2_Redesign (4-8 semanas):
    3. Aplicar Team Topologies (Pattern D1.1):
       - Stream-aligned teams: 1 team owns 1 value stream end-to-end
       - Enabling teams: Capacitan otros (temporal)
       - Complicated subsystem teams: Especialización profunda necesaria
       - Platform teams: Self-service APIs (reduce dependencies)
       
    4. Definir interaction modes:
       - Collaboration: Discovery phase (temporal, <3 meses)
       - X-as-a-Service: Consumo APIs (async, scalable)
       - Facilitation: Enabling → Stream (knowledge transfer)
       
  Fase_3_Migration (6-12 meses):
    5. Reorganizar incrementalmente:
       - Pilot: 1 stream-aligned team (proof of concept)
       - Measure: A3 reduction, lead time improvement
       - Scale: Si pilot exitoso, expandir a 2-3 teams más
       - Full migration: 12-18 meses typical (org 100+ personas)
       
    6. Refactoring arquitectura:
       - APIs reflejan nuevos boundaries teams
       - Ownership código alineado con teams
       - CI/CD per team (reduce coordination deploys)
       
  Validación_Éxito:
    - A3_Handoff_Ratio < 20% (target alcanzado)
    - Lead time reducido 40-60% (industry benchmark)
    - Team autonomy > 80% (decisions internas, no external dependencies)
    - Meeting hours reducido 30-50% (less coordination overhead)
    - Deployment frequency aumentado 5-10x (less coordination required)
    
Related_Principles:
  - PD48: Handoff Formal Definition (G27)
  - PD31: Cohesión Máxima
  - PD6: Separación Concerns (I2)
  - PD7: Relaciones Explícitas (I2)
  - PD14: Test Cliente Externo (I4 - clasificación roles)
  
Related_Patterns:
  - D1.1: TEAM TOPOLOGY ALIGNED (solución)
  - AP14: ACTIVITY-BASED TEAMS (variante similar)
```

### AP2: AUTOMATION BLINDNESS

```yaml
Origen: Pattern D1.2 (DELEGATION LADDER) - anti-pattern implícito

Síntoma:
  - Capacidad algorítmica operando sin trajectory tracking
  - Delegation mode indefinido o M6 desde día 1 (no gradual)
  - Incidents causados por automated decisions (root cause: no human oversight)
  - NO existe accountable_capacity_id para algoritmicos
  - Override capability ausente o no funcional
  
Problema:
  "Automatizar sin delegación gradual ni accountability humana → riesgo incontrolado.
   'Set and forget' automation viola I5 HAIC (primacía humana)."
   
  Viola:
    - PD18: Accountability Humana Transversal (I5 - NO hay humano responsible)
    - PD19: Delegación Explícita Cross Domain (I5 - modo NO definido)
    - PD22: Trajectory Log (I6 - NO se registra ejecuciones)
    - PD23: Progresión Gradual (I6 - salto M1 → M6 directo)
    
Consecuencias:
  Operacionales:
    - Incidents críticos causados por automation (ej: auto-scaling excesivo → $100k bill)
    - Root cause analysis difícil (NO hay audit trail de decisiones algorítmicas)
    - Rollback lento (humano debe entender qué hizo automation antes revertir)
    
  Organizacionales:
    - Trust loss en automation (teams regresan a manual después incident)
    - Shadow IT (teams evitan platform automation, crean workarounds)
    - Blame shifting ("bot lo hizo" → accountability difusa)
    
  Éticas/Legales:
    - Decisiones algoritmicas sin explicabilidad (viola GDPR Art.22 si aplica)
    - Accountability gap (NO humano responsible → riesgo legal)
    - Bias no detectado (algoritmo perpetua sesgos sin trajectory review)
    
Ejemplos_Reales:
  
  Caso_1_Auto_Scaling_Gone_Wild:
    - K8s HPA configurado M6 desde día 1
    - Load spike → scale to 500 pods (expected: 50)
    - Cost: $80k/día por 3 días antes detección
    - Root cause: Metric bug + NO human oversight
    - Should have been: M4 (supervised) primeros 3 meses
    
  Caso_2_ML_Model_Drift:
    - Recommendation engine deployed M6
    - Performance degrada 30% en 2 meses (drift no detectado)
    - Revenue loss: $200k
    - Root cause: NO trajectory monitoring, NO drift detection
    - Should have been: M5 (exception-based oversight) + alertas drift
    
  Caso_3_Auto_Deploy_Production:
    - CI/CD auto-deploy M6 desde inicio
    - Bug critico → production down 4 horas
    - Root cause: Test suite incomplete + NO human gate
    - Should have been: M1→M2→M3→M4 progression (6+ meses)
    
Detección_Métricas:
  IF Capacity.substrate = Algorítmico AND accountable_capacity_id IS NULL
    THEN alert("HAIC violation - no accountability")
    
  IF Capacity.delegation_mode IS NULL OR delegation_mode = M6 AND created_at < 6_months
    THEN alert("Automation Blindness - progression too fast")
    
  IF Incident.root_cause LIKE '%automation%' AND trajectory_log IS NULL
    THEN alert("No trajectory tracking for algorithmic capacity")
    
Remediation:
  
  Fase_1_Audit (1-2 semanas):
    1. Inventario capacidades algorítmicas:
       - Query: SELECT * FROM Capacity WHERE substrate = 'Algorítmico'
       - Por cada una: delegation_mode actual, accountable_capacity_id, trajectory_log exists?
       - Clasificar riesgo: CRITICAL (M6 production), HIGH (M5-M6 staging), MEDIUM (M3-M4)
       
    2. Identificar gaps HAIC:
       - % sin accountable: target 0%
       - % sin trajectory log: target 0%
       - % sin override capability: target 0%
       
  Fase_2_Compliance (2-4 semanas):
    3. Establecer accountability:
       - Por cada algorítmico: asignar humano accountable (mandatory)
       - Documentar: quién, por qué, escalation path
       - Tool: Update Capacity.ownership.accountable_id
       
    4. Implementar trajectory logging:
       - Schema: execution_id, timestamp, input, output, context, feedback
       - Retention: mínimo 90 días (recommendation: 1+ años)
       - Dashboard: Trajectory metrics por capacity
       
    5. Habilitar override:
       - Circuit breaker: Human can stop automation instantly
       - Manual veto: Human can reject automated decision pre-execution
       - Escalation: Clear path humano → algoritmo intervention
       
  Fase_3_Progression (3-12 meses):
    6. Degradar automation excesiva:
       - IF delegation_mode = M6 AND trajectory < 6_months → downgrade to M4
       - IF incidents caused → downgrade 1 level
       - Enforce: NO saltar niveles (M3 → M4 → M5 → M6)
       
    7. Gradual re-promotion:
       - Criteria per level (ver Pattern D1.2):
         * M2→M3: accuracy >70%, 10+ executions
         * M3→M4: accuracy >85%, monitoring real-time
         * M4→M5: error_rate <5%, false_positive <10%
         * M5→M6: error_rate <1%, 6+ meses stable
       - Review quarterly: ¿capacity lista next level?
       
  Validación_Éxito:
    - 100% capacidades algorítmicas con accountable_capacity_id
    - 100% con trajectory_log activo
    - 100% con override_capability funcional
    - Incident rate causado por automation reducido 70-90%
    - Mean time to recovery (MTTR) para automation issues reducido 50%
    - Trust score automation (team survey) > 7/10
    
Related_Principles:
  - PD18: Accountability Humana Transversal (I5)
  - PD19: Delegación Explícita Cross Domain (I5)
  - PD20: Override Capability Universal (I5)
  - PD21: Explainability Transversal (I5)
  - PD22: Trajectory Log (I6)
  - PD23: Progresión Gradual (I6)
  - PD24: Drift Detection (I6)
  
Related_Patterns:
  - D1.2: DELEGATION LADDER (solución)
  - D4.2: OBSERVABILITY TRIAD (monitoring algorítmicos)
```

### AP3: ORPHAN OKRS

```yaml
Origen: Pattern D1.3 (PURPOSE CASCADE) - anti-pattern implícito

Síntoma:
  - OKRs individuales o de equipo sin parent_id (disconnected from org purpose)
  - Query Q4 (Path to Root) falla (no alcanza L4 org purpose)
  - A4_Alignment_Propósitos < 70% (target: >85%)
  - OKR planning happens bottom-up (no cascade L4→L1)
  - Teams "pick their own" OKRs sin link a strategy org
  
Problema:
  "Trabajo desconectado de propósito org → waste.
   Equipos optimizan sub-goals que NO contribuyen a outcomes org."
   
  Viola:
    - PD49: Alignment Weighted Recursive (G28 - NO hay fórmula alignment porque NO hay parent)
    - PD11: Lineage Completo (I3 - cadena trazabilidad rota)
    - PD13: Decision Records (I3 - NO hay justificación link org)
    
Consecuencias:
  Estrategicas:
    - Misalignment (teams trabajan cross-purposes)
    - Org goals NO alcanzan (cada team "busy" pero org estancada)
    - Resource waste (effort en iniciativas NO prioritarias org)
    
  Operacionales:
    - Priorización conflictiva (teams compiten por recursos sin clarity org priority)
    - Duplicación esfuerzos (2+ teams atacan mismo problem desde ángulos distintos)
    - Gaps críticos (nadie trabaja en objetivos org importantes porque NO cascaded)
    
  Psicológicas:
    - Frustration (teams sienten trabajo NO valorado por org)
    - Cynicism ("OKRs son ejercicio vacío, nadie los sigue")
    - Autonomy mal entendida ("podemos hacer lo que queramos" vs "autonomy HOW, not WHAT")
    
Ejemplos_Reales:
  
  Caso_1_Feature_Teams_Diverging:
    - Org goal L4: "Reducir churn 15%" (retención customers)
    - Team A OKR: "Lanzar 10 features nuevas" (orphan, NO link)
    - Team B OKR: "Mejorar performance app 30%" (orphan)
    - Result: Teams busy, churn NO mejora
    - Should have been:
        * Team A: "Implementar onboarding mejorado" (contributes to churn reduction)
        * Team B: "Reducir bugs críticos 40%" (contributes to churn reduction)
    
  Caso_2_Individual_OKRs_Scattered:
    - Org goal L4: "Expandir a mercado LATAM" (growth)
    - Engineer OKR: "Aprender Rust" (orphan, desarrollo personal NO alineado)
    - PM OKR: "Mejorar UX dashboard" (orphan, NO contribuye LATAM)
    - Result: Expansion LATAM stalled, individuals "achieving" OKRs irrelevantes
    - Should have been:
        * Engineer: "Implementar i18n/l10n" (enables LATAM)
        * PM: "Validar PMF con 10 customers LATAM" (contributes expansion)
    
Detección_Métricas:
  Query_Q4_Failures:
    SELECT purpose_id, name FROM Purpose 
    WHERE NOT EXISTS (recursive_path_to_root(purpose_id, L4))
    
  IF COUNT(orphan_purposes) > 0 THEN alert("Orphan OKRs detected")
  IF A4_Alignment < 70% THEN alert("Low alignment - investigate orphans")
  
  Survey_Quarterly:
    "Do you understand HOW your OKRs contribute to org goals?"
    IF avg_score < 4/5 THEN orphan problem likely
    
Remediation:
  
  Fase_1_Audit (1-2 semanas):
    1. Identificar orphans:
       - Run Q4 (Path to Root) per OKR
       - List: OKRs without valid parent_id
       - Classify: CRITICAL (L1-L2 teams), HIGH (L3 individuals)
       
    2. Analizar causa:
       - ¿Process failure? (no cascade ritual)
       - ¿Cultural? ("autonomy" mal entendida)
       - ¿Strategic vacuum? (org goals unclear L4)
       
  Fase_2_Workshopping (2-4 semanas):
    3. Re-link orphans:
       - Por cada orphan: ¿Cuál L3/L4 goal contribuye?
       - Si NO contribuye a ninguno → candidato deprecate
       - Si contribuye → establecer parent_id explícito
       - Documentar contribution (% esperado o narrative)
       
    4. Deprecar irrelevantes:
       - Si OKR NO linkable a org goals → deprecate
       - Reallocate effort a OKRs alineados
       - Comunicar: "Focusing resources on aligned initiatives"
       
  Fase_3_Process (ongoing):
    5. Implementar cascade ritual (Pattern X2 QUARTERLY PLANNING):
       - Week 1: L4 sets org OKRs (C-level)
       - Week 2: L3 cascades to departments (cascade workshops)
       - Week 3: L2-L1 cascades to teams/individuals (1:1s + team sessions)
       - Enforce: NO commit OKR sin parent_id (L1-L3)
       - Tool: Purpose.parent_id = MANDATORY (L1-L3), NULL only allowed for L4
       
    6. Validación recurrente:
       - Monthly: Run Q4, alert if failures
       - Quarterly: A4_Alignment score review
       - Annual: Retrospective process cascade
       
  Validación_Éxito:
    - Query Q4 = 0 failures (100% OKRs L1-L3 traceable to L4)
    - A4_Alignment_Propósitos > 85%
    - Survey "understand contribution" > 4.2/5
    - Org goals achieved (outcome validation, not just activity)
    - Resource utilization en aligned initiatives > 90%
    
Related_Principles:
  - PD49: Alignment Weighted Recursive (G28)
  - PD10: Metadata Obligatoria (I3 - parent_id requerido)
  - PD11: Lineage Completo (I3 - cadena purpose completa)
  - PD13: Decision Records (I3 - justificar link parent)
  
Related_Patterns:
  - D1.3: PURPOSE CASCADE (solución)
  - X2: QUARTERLY PLANNING RITUAL (proceso)
```

### AP4: OBSERVABILITY THEATER

```yaml
Origen: Pattern D2.1 (OBSERVABLE INSTRUMENTATION) - anti-pattern implícito

Síntoma:
  - Dashboards complejos pero nadie los usa
  - Métricas instrumentadas pero NO accionables
  - P1_Coverage_Observables alto (>80%) PERO P5_Actionability bajo (<30%)
  - Alertas ignoradas (alert fatigue, 90%+ false positives)
  - "We have observability" pero incidents descubiertos por customers
  
Problema:
  "Instrumentación sin propósito claro → noise, no signal.
   Dashboards como 'checkbox' compliance, NO herramienta operacional."
   
  Viola:
    - PD51: Observable Standard Units (G30 - instrumentado pero NO con units accionables)
    - PD3: Eliminación Redundancia (I1 - métricas duplicadas, no tiles)
    - PD10: Metadata Obligatoria (I3 - NO freshness, NO ownership claro)
    
Consecuencias:
  Operacionales:
    - Incidents detectados tarde (MTTR alto, >2 horas)
    - Root cause analysis difícil (data presente pero NO navegable)
    - On-call burnout (alertas 3am por false positives)
    
  Económicas:
    - Cost observability tools alto ($50k-$200k/año) sin ROI
    - Engineering time waste (mantener dashboards que nadie usa)
    - Opportunity cost (NO instrumentar lo que realmente importa)
    
  Psicológicas:
    - False sense of control ("tenemos dashboards" ≠ "entendemos sistema")
    - Alert fatigue → ignoring all alerts (boy who cried wolf)
    - Cynicism ("observability es theater, NO ayuda")
    
Patrones_Theater_Comunes:
  
  Theater_1_Dashboard_Graveyard:
    - 50+ dashboards en Grafana/DataDog
    - 80% NO abiertos en últimos 90 días
    - Ownership unclear (creator left team 2 años atrás)
    - Metrics obsoletos (services deprecados hace meses)
    
  Theater_2_Vanity_Metrics:
    - "Total API calls" (so what? success rate?)
    - "Database size GB" (growth rate? queries slow?)
    - "Container count" (utilization? right-sizing?)
    - Problema: Métricas NO accionables (no trigger decisions)
    
  Theater_3_Alert_Spam:
    - 500 alertas/día (99% false positives)
    - On-call ignora PagerDuty (learned helplessness)
    - Real incidents lost in noise
    - Post-mortem: "Alert existed but we ignored it"
    
  Theater_4_Coverage_Obsession:
    - "Instrument everything" sin priorization
    - Tier 3 observables (nice-to-have) implementados
    - Tier 1 críticos (customer feedback, quality) ausentes
    - Inversion: effort en low-value high-effort observables
    
Detección_Métricas:
  Dashboard_Usage:
    IF dashboard.last_viewed > 90_days THEN candidate_deprecate
    IF dashboard.views_last_month < 10 THEN low_value
    
  Alert_Quality:
    IF alert_rate > 100/day AND action_rate < 10% THEN alert_fatigue
    IF false_positive_rate > 50% THEN broken_thresholds
    
  Actionability:
    Survey: "This metric triggered a decision last month" (per metric)
    IF avg_score < 3/5 THEN observability_theater
    
  Incident_Detection:
    IF %_incidents_discovered_by_customers > 30% THEN observability_failure
    (Target: <10% customer-discovered, 90% internal-detected)
    
Remediation:
  
  Fase_1_Audit (2-3 semanas):
    1. Inventario completo:
       - List: ALL dashboards (Grafana, DataDog, Splunk, custom)
       - Per dashboard: owner, last_viewed, metrics count
       - List: ALL alerts (PagerDuty, Opsgenie, Slack)
       - Per alert: trigger_rate, action_rate, false_positive_rate
       
    2. Usage analysis:
       - Dashboard_Usage_Score = views_last_90d / team_size
       - Alert_Quality_Score = (1 - false_positive_rate) × action_rate
       - Classify: KEEP (high usage/quality), REVIEW (medium), DEPRECATE (low)
       
  Fase_2_Cleanup (2-4 semanas):
    3. Deprecar waste:
       - Dashboards no vistos 90+ días → archive
       - Alertas >80% false positive → disable (fix or delete)
       - Métricas vanity sin actionability → stop collecting
       - Cost savings: 30-50% typical en tools bills
       
    4. Fix alert fatigue:
       - Tune thresholds (baselines actualizados, 2-3σ not 1σ)
       - Aggregate: 10 related alerts → 1 alert composite
       - Severity correct: 90% should be INFO/WARNING, 10% CRITICAL
       - On-call rotation: Max 5 pages/week target
       
  Fase_3_Focus (ongoing):
    5. Priorizar Tier 1 (Pattern D2.1):
       - Externos: EX5 Feedback, EX3 Regulatory
       - Internos: IN1 Velocidad, IN4 Calidad, IN7 Violaciones
       - Implement: Tier 1 primero (6 observables críticos)
       - Defer: Tier 3 hasta Tier 1 + Tier 2 completos
       
    6. Actionability-first:
       - Per cada métrica nueva: "What decision this enables?"
       - If NO clear decision → NO instrument
       - Dashboard design: Start con "Questions to answer", then metrics
       - Test: Show dashboard to team → "Can you act on this?" → iterate
       
    7. Ownership claro:
       - Per dashboard: Assign owner (team + individual)
       - Quarterly review: Owner valida relevancia, actualiza o depreca
       - Tool: Dashboard.metadata.owner = MANDATORY
       - Process: No orphan dashboards allowed
       
  Validación_Éxito:
    - Dashboard_Usage_Score > 10 views/person/month (active use)
    - Alert_Quality_Score > 0.70 (30% false positive max, 70%+ action rate)
    - P5_Actionability > 70% (métricas drive decisions)
    - Incident_Detection: >90% detected internally before customers
    - MTTR reducido 40-60% (faster root cause with good observability)
    - On-call satisfaction > 7/10 (not overwhelmed by noise)
    - Observability cost optimizado 30-50% (pay for value, not theater)
    
Related_Principles:
  - PD51: Observable Standard Units (G30)
  - PD3: Eliminación Redundancia (I1 - deprecar dashboards no usados)
  - PD10: Metadata Obligatoria (I3 - owner, freshness)
  - PD60: DORA Metrics (G4 - MTTR target <1 hora)
  
Related_Patterns:
  - D2.1: OBSERVABLE INSTRUMENTATION (solución priorizada)
  - D4.2: OBSERVABILITY TRIAD (logs/metrics/traces integrados)
```

### AP5: HIPPO PRIORITIZATION

```yaml
Origen: Pattern D3.1 (RICE PRIORITIZATION) - anti-pattern implícito

Síntoma:
  - Iniciativas priorizadas por "Highest Paid Person Opinion" (HIPPO)
  - RICE scores calculados pero ignorados en decisions
  - Low-RICE initiatives en "Now" bucket (portfolio board incongruente)
  - Retrospective: High-RICE deferred, Low-RICE executed
  - Decision rationale: "CEO quiere", "VP insiste", "Cliente VIP pidió"
  
Problema:
  "Decisión política override datos → suboptimal resource allocation.
   Priorization process existe pero NO respetado."
   
  Viola:
    - PD64: Portfolio Value Maximization (G14 - NO ROI-weighted, poder-weighted)
    - PD63: Decision Audit Trail (G7 - rationale vacío o no documentado)
    - PD10: Metadata Obligatoria (I3 - scoring exists but ignored)
    
Consecuencias:
  Estratégicas:
    - Low ROI initiatives consume resources (opportunity cost alto)
    - Org optimiza para politics, not value
    - Strategy incoherence (direction changes con personón flavor of month)
    
  Operacionales:
    - Team frustration (effort en scoring "inútil")
    - Thrashing (prioridades cambian cada meeting con exec)
    - Technical debt (no time for foundations, solo "CEO pet projects")
    
  Culturales:
    - Cynicism ("data doesn't matter, only who you know")
    - Politics dominate (lobbying skills > execution skills)
    - Talent flight (high performers leave, politicians stay)
    
Ejemplos_Reales:
  
  Caso_1_Pet_Project_Override:
    - RICE scoring session: 30 initiatives ranked
    - Top 3 RICE:
      1. "Payment flow optimization" (RICE 450)
      2. "Mobile onboarding" (RICE 380)
      3. "API performance" (RICE 320)
    - CEO in planning meeting: "I want social login NOW"
    - Social login RICE: 85 (low reach, low impact)
    - Result: Social login goes to "Now", top 3 deferred
    - Outcome: 3 months later, social login used by <5% users
    
  Caso_2_VIP_Customer_Escalation:
    - Customer Success escalates: "VIP cliente quiere feature X"
    - Feature X RICE: 60 (1 customer, high effort, low confidence)
    - Team: "RICE score bajo, priorizar features multi-customer?"
    - VP Sales override: "Este cliente paga $500k/año"
    - Result: 2 engineers 6 semanas en feature X
    - Outcome: Feature X usado por 1 cliente, 0 adoption otros
    
Detección_Métricas:
  Scoring_Utilization:
    IF EXISTS (initiatives in "Now" WHERE RICE < median(RICE_all))
      THEN alert("Low-RICE in execution - HIPPO detected")
      
  Retrospective_Analysis:
    Correlation(RICE_score, actually_executed)
    IF correlation < 0.5 THEN "Scoring not respected"
    
  Portfolio_Health:
    Actual_ROI = SUM(value_delivered) / SUM(effort_spent)
    Expected_ROI = SUM(RICE_top_10) / SUM(effort_estimated_top_10)
    IF Actual_ROI < 0.7 × Expected_ROI THEN "Suboptimal allocation"
    
Remediation:
  
  Fase_1_Commitment (2-4 semanas):
    1. Executive alignment:
       - Workshop C-level: "Por qué RICE?"
       - Present: Cost of HIPPO (cases 1-2 above, $$ impact)
       - Commitment: "We follow RICE unless exceptional override"
       - Define "exceptional": Legal, compliance, existential customer churn
       - Publish: C-level signed commitment visible org-wide
       
    2. Override protocol:
       - IF exec wants override RICE → MUST document WHY
       - Template: "Override rationale: [legal/compliance/churn], Expected cost: $X, Risk accepted by: [exec name]"
       - Transparency: Override published Slack channel (accountability pública)
       - Retrospective: Track override outcomes (learn)
       
  Fase_2_Process (ongoing):
    3. RICE governance:
       - Quarterly planning: RICE session facilitated
       - Top N initiatives ranked (N = capacity next quarter)
       - "Now" = Top N exactly (no additions without removing another)
       - Portfolio board published: RICE scores visible
       
    4. Stakeholder education:
       - Training: "How RICE works" (for PMs, execs, Sales)
       - "How to influence": Improve RICE inputs (Reach/Impact/Confidence/Effort)
       - NOT: Lobby exec para override
       - Sales: "Sell what we have, not what VIP wants" (product-led)
       
  Fase_3_Validation (quarterly):
    5. Retrospective rigor:
       - Per initiative executed: Actual vs Predicted (Reach/Impact/Effort)
       - Learn: Calibrate estimation (confidence intervals)
       - Publish: "RICE accuracy report" (build trust en scoring)
       
    6. Override audit:
       - List: All overrides last quarter
       - Per override: Rationale, outcome, value delivered
       - IF override pattern → address root cause
       - Example: If 80% overrides "VIP customer" → revisit VIP strategy
       
  Validación_Éxito:
    - Correlation(RICE_score, executed) > 0.80 (scoring respected)
    - Override rate < 10% (exceptional, not routine)
    - Override rationale documented 100% (accountability)
    - Actual_ROI / Expected_ROI > 0.90 (allocation optimizada)
    - Team survey "prioritization fair" > 4/5
    - Exec survey "trust RICE" > 4/5
    
Related_Principles:
  - PD64: Portfolio Value Maximization (G14)
  - PD63: Decision Audit Trail (G7 - override rationale)
  - PD10: Metadata Obligatoria (I3 - RICE scoring)
  
Related_Patterns:
  - D3.1: RICE PRIORITIZATION (solución)
  - X2: QUARTERLY PLANNING RITUAL (proceso governance)
```

### AP6: THRASHING

```yaml
Origen: Pattern D3.2 (WIP LIMIT ENFORCEMENT) - anti-pattern implícito

Síntoma:
  - WIP (Work In Progress) = 3-5× team capacity
  - Nada termina (cycle time > 2× baseline)
  - Context switching constante (engineers en 3-4 initiatives simultáneamente)
  - Standups largos (too many things "in progress")
  - Burnout visible (exhaustion sin output)
  
Problema:
  "Too much WIP → context switching → nothing finishes.
   Equipo 'busy' pero throughput = 0."
   
  Viola:
    - PD44: TD Small Batches Gate (Kelly - batch size creep)
    - PD45: TD Flow Gate (Kelly - Little's Law violado: Lead Time ∝ WIP)
    - PD3: Eliminación Redundancia (I1 - multiple starts, single finish)
    
Consecuencias:
  Operacionales:
    - Lead time explode (feature 2 semanas → 2 meses)
    - Throughput collapse (4 features/mes → 0.5 features/mes)
    - Quality degraded (rushed finishes, technical debt)
    
  Psicológicas:
    - Context switching fatigue (cognitive load 10x)
    - Learned helplessness ("nothing ever finishes")
    - Burnout epidemic (effort alto, accomplishment zero)
    
  Económicas:
    - Opportunity cost massive (features NOT delivered)
    - Coordination overhead (sync meetings para 5 initiatives)
    - Sunk cost trap ("already started 10 things, can't stop now")
    
Little's_Law_Violado:
  Lead_Time = WIP / Throughput
  
  Example:
    Throughput = 4 features/month (team capacity)
    WIP = 2 features → Lead Time = 0.5 months (2 weeks) ✅
    WIP = 12 features → Lead Time = 3 months (12 weeks) ❌
    
  Thrashing:
    WIP = 12, pero context switching → Effective_Throughput = 1 feature/month
    → Lead Time = 12 months (!)
    
Ejemplos_Reales:
  
  Caso_1_Startup_Overcommitment:
    - Team: 5 engineers
    - Commitments: 15 features para "next quarter"
    - WIP: 15 (all started week 1)
    - Week 12: 0 features done, 15 at 60% progress
    - CEO: "Why nothing shipping?"
    - Team: Thrashing (3 features per engineer concurrently)
    
  Caso_2_Sales_Driven_Chaos:
    - Sales cierra deals con custom features (5 clientes, 5 features)
    - Engineering: Start all 5 ("cada cliente es prioritario")
    - Month 1: Progress 20% each
    - Month 2: Progress 40% each (pero clients unhappy "dónde está?")
    - Month 3: Rush finish 1 feature (other 4 stalled)
    - Outcome: 1/5 delivered, 4 clientes churned (waited 3+ meses)
    
Detección_Métricas:
  WIP_Ratio:
    WIP_Ratio = Current_WIP / Team_Capacity
    IF WIP_Ratio > 2.0 THEN alert("Thrashing risk")
    IF WIP_Ratio > 3.0 THEN alert("Thrashing CRITICAL")
    
  Cycle_Time_Degradation:
    IF Cycle_Time_Current > 2 × Cycle_Time_Baseline THEN "Flow blocked"
    
  Throughput_Collapse:
    IF Throughput_Current < 0.5 × Throughput_Baseline THEN "Thrashing detected"
    
Remediation:
  
  Fase_1_Stop_The_Bleeding (inmediato):
    1. WIP freeze:
       - NO new work starts (hard stop)
       - Finish what's in progress primero
       - Communicate: "Finishing > Starting"
       
    2. Priorize ruthlessly:
       - Rank current WIP por value/urgency
       - Top 30%: Finish (all hands)
       - Middle 30%: Parking lot (explicit defer)
       - Bottom 40%: Cancel (sunk cost accepted)
       - Rationale: Better finish 3/10 than 0/10
       
  Fase_2_Calculate_WIP_Limit (1 semana):
    3. Measure capacity:
       - Historical throughput: Features_per_month (trailing 6 months)
       - Target lead time: Days_acceptable
       - WIP_max = Throughput × (Lead_Time_Target / 30)
       
       Example:
         Throughput = 4 features/month
         Lead_Time_Target = 2 weeks (14 days)
         WIP_max = 4 × (14/30) = 1.9 ≈ 2 features
         
    4. Enforce limit:
       - Tool: Jira/Linear column "In Progress" max = WIP_max
       - IF WIP = WIP_max THEN block new card moves
       - Finish before start (pull system)
       
  Fase_3_Discipline (ongoing):
    5. Daily WIP check:
       - Standup: "WIP count = X / X_max"
       - IF at limit: "What finishes today?"
       - Swarm: Team focuses 1-2 items (NOT distribute)
       
    6. Stakeholder management:
       - Communicate: "WIP limit = faster delivery"
       - Show: Lead time improvement graphs
       - Educate: Little's Law (math, not opinion)
       - Push back: "We finish X before starting Y"
       
  Validación_Éxito:
    - WIP_Ratio < 1.5 (sustainable)
    - Cycle Time restored to baseline (2x improvement typical)
    - Throughput improved 40-60% (paradox: doing less → delivering more)
    - Team satisfaction +2 points (less chaos)
    - Stakeholder NPS improved (predictable delivery)
    
Related_Principles:
  - PD44: TD Small Batches Gate (Kelly)
  - PD45: TD Flow Gate (Kelly - Little's Law)
  - PD3: Eliminación Redundancia (I1)
  
Related_Patterns:
  - D3.2: WIP LIMIT ENFORCEMENT (solución)
  - D3.1: RICE PRIORITIZATION (qué entra en WIP)
```

### AP7: BIG BANG RELEASES

```yaml
Origen: Pattern D4.1 (CONTINUOUS DEPLOYMENT) - anti-pattern implícito

Síntoma:
  - Deploys monthly o quarterly ("release trains")
  - Batch size grande (50-200 changes per deploy)
  - Deploy windows largos (4-8 horas downtime)
  - War rooms deploy (10+ personas sincronizadas)
  - Change failure rate alto (>30%, target: <15%)
  - Rollback complejo ("too many changes, can't isolate")
  
Problema:
  "Batch deploys grande → risk concentrado → failures frecuentes.
   Coordination overhead > value delivered."
   
  Viola:
    - PD60: DORA Metrics Mandatory (G4 - M1 deployment frequency bajo)
    - PD44: TD Small Batches (Kelly - batch size antipattern)
    - PD59: Execution Instance Tracking (G3 - NO granular tracking)
    
Consecuencias:
  Operacionales:
    - MTTR alto (>4 horas, debugging 200 changes)
    - Change failure rate alto (30-50% vs <15% industry elite)
    - Downtime planned frecuente (maintenance windows)
    
  Económicas:
    - Revenue loss (downtime 4h/mes = $X0k-$X00k depend scale)
    - Opportunity cost (features ready pero esperan release train)
    - Coordination cost (war rooms, weekend deploys, overtime)
    
  Culturales:
    - Fear of deploy ("it's always a disaster")
    - Hero culture ("only senior can deploy")
    - Burnout (weekend/night deploys routine)
    
DORA_Metrics_Comparación:
  Elite_Performers:
    - Deployment Frequency: Multiple per day
    - Lead Time: <1 day
    - Change Failure Rate: <15%
    - MTTR: <1 hour
    
  Big_Bang_Anti-Pattern:
    - Deployment Frequency: Monthly (30x slower)
    - Lead Time: 30+ days (30x slower)
    - Change Failure Rate: 30-50% (2-3x worse)
    - MTTR: 4+ hours (4x slower)
    
Ejemplos_Reales:
  
  Caso_1_Quarterly_Release_Disaster:
    - Company: E-commerce 100M GMV/year
    - Release: Q2 big bang (180 changes, 3 months acumulados)
    - Deploy: Friday 8pm, war room 15 personas
    - 10pm: Critical bug detected (checkout broken)
    - 11pm: Rollback attempt fails (DB migration irreversible)
    - 2am: Hotfix deployed (1 change)
    - Downtime: 6 horas
    - Revenue loss: $50k (Friday night peak)
    - Root cause: Change #87/180 (needle in haystack)
    - Should have been: Deploy 180 changes × 1 per day = 0 incidents
    
  Caso_2_Waterfall_Carryover:
    - Team migrating "Agile" pero deploys monthly
    - Sprint 1: 10 features ready → wait
    - Sprint 2: 12 features ready → wait
    - Sprint 3: 8 features ready → wait
    - Month end: Deploy 30 features (4-hour window)
    - Failure: 3/30 features break production
    - Diagnosis: 2 days (which of 30?)
    - Team: "Agile doesn't work" (wrong: deployment anti-pattern)
    
Detección_Métricas:
  DORA_M1_Deployment_Frequency:
    IF deploys_per_month < 10 THEN alert("Big Bang risk")
    IF deploys_per_month < 4 THEN alert("Big Bang confirmed")
    
  Batch_Size:
    IF changes_per_deploy > 20 THEN "High risk batch"
    IF changes_per_deploy > 50 THEN "Big Bang batch"
    
  DORA_M3_Change_Failure_Rate:
    IF failure_rate > 30% THEN "Batch size problema likely"
    
Remediation:
  
  Fase_1_Decouple_Deploy_From_Release (2-4 semanas):
    1. Feature flags:
       - Tool: LaunchDarkly, Unleash, or custom
       - Pattern: Deploy code OFF, enable feature post-deploy
       - Benefit: Deploy risk ≠ feature risk
       
    2. Blue/Green or Canary:
       - Blue/Green: Deploy to parallel env, switch traffic
       - Canary: Deploy to 5% traffic, monitor, scale to 100%
       - Rollback: Instant (traffic switch, no code change)
       
  Fase_2_Automate_Pipeline (4-8 semanas):
    3. CI/CD pipeline:
       - Commit → Build + Unit Tests (<10 min)
       - → Deploy Staging + E2E Tests (<30 min)
       - → Deploy Canary 5% + Monitor (<1 hour)
       - → Deploy 100% production
       - Total: <2 hours commit → production
       
    4. Automated rollback:
       - IF error_rate > 2× baseline THEN auto-rollback
       - IF latency p99 > 1.5× baseline THEN auto-rollback
       - Alert: "Rollback executed, investigate"
       
  Fase_3_Cultural_Shift (6-12 meses):
    5. Small batch discipline:
       - Target: 1 deploy per day minimum
       - Rule: 1 feature = 1 deploy (NOT batch)
       - Metric: Batch size trend (decreasing)
       
    6. Deploy = routine:
       - "Deploy" button click, not war room
       - Any engineer can deploy (not hero culture)
       - Deploys during business hours (confidence)
       
    7. Continuous improvement:
       - Weekly: Review DORA M1-M4
       - Monthly: Retrospective deploy failures
       - Quarterly: Benchmark vs industry (elite performers)
       
  Validación_Éxito:
    - DORA M1: Deploys multiple per day (elite)
    - DORA M2: Lead time <1 day (commit → production)
    - DORA M3: Change failure rate <15%
    - DORA M4: MTTR <1 hour (fast rollback)
    - Team survey "confident deploying" > 4/5
    - NO more war rooms (routine operation)
    - Downtime planned → 0 (blue/green eliminates)
    
Related_Principles:
  - PD60: DORA Metrics Mandatory (G4)
  - PD44: TD Small Batches (Kelly)
  - PD59: Execution Instance Tracking (G3)
  
Related_Patterns:
  - D4.1: CONTINUOUS DEPLOYMENT (solución)
  - D4.2: OBSERVABILITY TRIAD (monitoring deploys)
```

### AP8: PRINTF DEBUGGING

```yaml
Origen: Pattern D4.2 (OBSERVABILITY TRIAD) - anti-pattern implícito

Síntoma:
  - Incidents debugged con printf/console.log manual
  - SSH to production servers (cowboy debugging)
  - "Can you add more logs and redeploy?" (iterative guessing)
  - NO structured logging (grep text files)
  - NO distributed tracing (black box microservices)
  - MTTR alto (>4 horas, mostly debugging time)
  
Problema:
  "Debugging manual sin observability structured → MTTR 10x.
   Production es black box, SSH last resort."
   
  Viola:
    - PD51: Observable Standard Units (G30 - NO logs/metrics/traces standard)
    - PD60: DORA M4 MTTR (G4 - recovery lento por debugging manual)
    - PD61: Incident Flow Linkage (G5 - NO trace deploy → incident)
    
Consecuencias:
  Operacionales:
    - MTTR alto (4-8 horas typical vs <1 hora elite)
    - Repeated incidents (root cause never found)
    - Production instability (cowboy fixes → new bugs)
    
  Económicas:
    - Downtime cost alto (minutes = $X, hours = $XX)
    - Engineering time waste (senior engineers SSH debugging)
    - Customer churn (repeated incidents → trust loss)
    
  Culturales:
    - On-call nightmare ("I have no idea what's happening")
    - Hero worship ("only Jane can debug production")
    - Fear production ("it's a black box")
    
Why_Printf_Fails_Production:
  
  Problem_1_Missing_Context:
    - Log: "Error: user not found"
    - Questions: Which user? Which endpoint? Which request?
    - Printf: NO correlation ID, NO request context
    
  Problem_2_Not_Structured:
    - Log: "Error processing order 12345 for customer John"
    - Query: "Show me all orders with this error"
    - Printf: grep text → false positives/negatives
    - Structured: JSON query → precise
    
  Problem_3_No_Distributed_View:
    - Microservices: A → B → C → D
    - Incident: Timeout at D
    - Printf: Must SSH each service, correlate timestamps manually
    - Tracing: Single view A→B→C→D with latency breakdown
    
Ejemplos_Reales:
  
  Caso_1_Microservices_Mystery:
    - Incident: Checkout failing 20% requests
    - Engineer: SSH to checkout-service
    - Logs: "Timeout calling payment-service"
    - Engineer: SSH to payment-service
    - Logs: "Timeout calling fraud-service"
    - Engineer: SSH to fraud-service
    - Logs: "Database connection pool exhausted"
    - Time: 3 horas SSH safari
    - Should have been: Distributed trace → root cause 5 min
    
  Caso_2_Iterative_Logging:
    - Incident: API slow
    - Engineer: "Add timing logs"
    - Deploy: 30 min
    - Logs: "Function X slow"
    - Engineer: "Add more logs inside X"
    - Deploy: 30 min
    - Logs: "Database query Y slow"
    - Time: 2 horas (4 redeploys)
    - Should have been: APM tracing → query Y identified instantly
    
Detección_Métricas:
  MTTR_Analysis:
    IF MTTR > 2 hours THEN "Observability gap likely"
    
  SSH_Sessions:
    IF ssh_sessions_to_production > 10/month THEN "Printf debugging detected"
    
  Log_Maturity:
    Survey: "Can you debug production without SSH?"
    IF avg_score < 3/5 THEN "Printf anti-pattern"
    
Remediation:
  
  Fase_1_Structured_Logging (2-4 semanas):
    1. Log format standard:
       - JSON structured (NOT text)
       - Fields: timestamp, level, service, trace_id, span_id, message, context
       - Example:
         {
           "timestamp": "2024-11-13T22:00:00Z",
           "level": "ERROR",
           "service": "checkout",
           "trace_id": "abc123",
           "message": "Payment failed",
           "context": {"user_id": "u456", "order_id": "o789"}
         }
       
    2. Log aggregation:
       - Tool: ELK, Splunk, DataDog, Loki
       - Centralized: ALL services → single pane
       - Query: Fast search por trace_id, user_id, etc.
       
  Fase_2_Metrics (2-4 semanas):
    3. RED metrics (Rate, Errors, Duration):
       - Per endpoint: request_rate, error_rate, latency_p50/p99
       - Dashboard: Real-time visibility
       - Alert: IF error_rate > 5% OR latency_p99 > 2s
       
    4. USE metrics (Utilization, Saturation, Errors):
       - Per resource: CPU, memory, disk, network
       - Saturation: queue depth, connection pool
       - Alert: IF saturation > 80% (preventive)
       
  Fase_3_Distributed_Tracing (4-8 semanas):
    5. Instrumentation:
       - Tool: Jaeger, Zipkin, DataDog APM
       - Pattern: trace_id propagated all requests
       - Span: cada service call, DB query, external API
       
    6. Correlation:
       - Link: logs ↔ metrics ↔ traces (same trace_id)
       - Workflow: Alert → Dashboard (metrics) → Logs (error) → Trace (latency breakdown)
       - Single click: metrics → traces → logs
       
  Fase_4_Culture (ongoing):
    7. SSH = last resort:
       - Rule: Try logs/metrics/traces FIRST
       - SSH only if observability insufficient
       - Post-mortem: "Why SSH needed?" → improve observability
       
    8. Observability-driven development:
       - Per feature: "How will I debug this in production?"
       - Add: Logging, metrics, tracing upfront (NOT reactive)
       - Code review: "Observability sufficient?"
       
  Validación_Éxito:
    - MTTR reducido 70-80% (<1 hora typical)
    - SSH sessions production → <2/month (exceptional)
    - Survey "can debug without SSH" > 4.5/5
    - Incident root cause found <15 min (tracing)
    - Repeated incidents → 0 (root cause fixed, not band-aided)
    - On-call satisfaction +3 points (tooling confidence)
    
Related_Principles:
  - PD51: Observable Standard Units (G30 - logs/metrics/traces)
  - PD60: DORA M4 MTTR (G4 - <1 hora target)
  - PD61: Incident Flow Linkage (G5 - trace deploy → incident)
  
Related_Patterns:
  - D4.2: OBSERVABILITY TRIAD (solución)
  - D2.1: OBSERVABLE INSTRUMENTATION (qué instrumentar)
```

### AP9: METRICS WITHOUT ACTION

```yaml
Síntoma:
  - Dashboards completos pero nadie actúa
  - Anomalías detectadas, no resueltas
  - P5_Actionability < 30%

Problema:
  "Observar sin intervenir → waste"

Consecuencias:
  - False sense of control
  - Problems compound
  - Team ignores metrics ("boy who cried wolf")

Remediation:
  1. Por cada métrica: Define QUIEN actúa cuando threshold
  2. Playbook: Anomaly → Owner → Action en 48h
  3. Review: Monthly actionability rate
  4. Prune: Eliminar métricas sin action owner
```

### AP10: IVORY TOWER ARCHITECTURE

```yaml
Síntoma:
  - D1 diseña estructura sin D4 input
  - Reorgs sin validar con equipos
  - A3_Handoffs empeora post-reorg

Problema:
  "Arquitectura desconectada de operación"

Consecuencias:
  - Structure-reality mismatch
  - Team frustration
  - Productivity drop post-reorg

Remediation:
  1. D1 ← D4 feedback loop (friction signals)
  2. Pilot reorgs (1 team, validate)
  3. VSM before/after comparison
  4. Rollback if A_Score degrades > 15%
```

## §8. REMEDIATION PLAYBOOKS

### PLAYBOOK R1: LOW H_ORG RECOVERY

**Nota**: Este playbook es versión conceptual. Para implementación ejecutable completa ver ../30_metodologia_orko/06_playbooks_recovery/ §2 (Manuales R1-R6).

```yaml
Trigger: H_org < 70 (Critical threshold)

Manuales_Espec\u00edficos_Metodolog\u00eda:
  - ../30_metodologia_orko/06_playbooks_recovery/P01_low_h_org_recovery.md §2.1: Manual R1 (Recuperación Salud General, 4 fases, 12-16 sem)
  - ../30_metodologia_orko/06_playbooks_recovery/P02_handoff_reduction.md §2.2: Manual R2 (Reducción Traspasos, VSM, 6-8 sem)
  - ../30_metodologia_orko/06_playbooks_recovery/P03_okr_alignment.md §2.3: Manual R3 (Alineación OKRs, Cascada, 4-6 sem)
  - ../30_metodologia_orko/06_playbooks_recovery/P04_security_remediation.md §2.4: Manual R4 (Reinicio Gobernanza, Policy-as-Code, 3-4 sem)
  - ../30_metodologia_orko/07_playbooks_transformation/P05_bounded_autonomy_m6.md §2.5: Manual R5 (Impulso Observabilidad, Data quality, 4-6 sem)
  - ../30_metodologia_orko/07_playbooks_transformation/P06_pilot_transformation.md §2.6: Manual R6 (Marco Decisión, Q1-Q6, 4-5 sem)
  
  Cada manual incluye: fases ejecutables, métricas éxito, templates, roles, timelines

Steps_Conceptuales:
  
  1. Diagnose (Week 1):
     - Identify lowest score (A/P/D/O)
     - Drill down components
     - Root cause (5 Whys)
     - Seleccionar manual(es) aplicable(s)
     
  2. Stabilize (Week 2-4):
     - FREEZE new initiatives (PD30)
     - Focus bottleneck domain
     - Daily standups on recovery
     
  3. Intervene (Week 5-8):
     - Apply manual específico (R1-R6)
     - Measure improvement weekly
     - Adjust if not improving
     
  4. Validate (Week 9-12):
     - Re-calculate H_org
     - IF ≥ 70 THEN exit recovery mode
     - ELSE repeat cycle

Success_Criteria:
  - H_org ≥ 70 sustained 2 months
  - No component < 60
```

### PLAYBOOK R2: HANDOFF REDUCTION

```yaml
Trigger: A3_Handoff_Ratio > 30%

Steps:
  
  1. Map (Week 1):
     - VSM 3 critical flows (D4.1)
     - Identify all handoffs
     - Calculate waste per handoff
     
  2. Analyze (Week 2):
     - Classify handoffs:
       * Eliminable (move capacity to same team)
       * Reducible (async integration)
       * Necessary (different expertise)
       
  3. Restructure (Week 3-4):
     - Apply Team Topology pattern (D1.1)
     - Move capacities to reduce handoffs
     - Define new team boundaries
     
  4. Verify (Week 5-8):
     - Re-measure handoff ratio
     - Target: < 20%
     - Monitor flow efficiency improvement

Success_Criteria:
  - A3 < 20%
  - Flow efficiency +20%
```

### PLAYBOOK R3: OKR ALIGNMENT

```yaml
Trigger: A4_Alignment < 70%

Steps:
  
  1. Audit (Week 1):
     - Query Q4 all purposes
     - Identify orphans (no parent)
     - Identify conflicts (competing goals)
     
  2. Workshop (Week 2):
     - Facilitated cascade session
     - Link orphans to parents
     - Resolve conflicts
     
  3. Commit (Week 3):
     - Leadership approval cascade
     - Publish OKR tree visible
     - Update Portfolio board
     
  4. Track (Ongoing):
     - Weekly progress updates
     - Monthly alignment score
     - Quarterly refresh

Success_Criteria:
  - A4 > 85%
  - 0 orphan OKRs
  - Path to root 100%
```

### PLAYBOOK R4-R6: TRANSFORMATION ROADMAP

```yaml
R4_PILOT_TRANSFORMATION:
  Trigger: H_org ≥ 70 AND readiness assessment passed
  
  Objetivo:
    Validar ORKO approach en value stream aislado, bajo riesgo
    
  Duración: 12-16 semanas
  
  Fases_Clave:
    - Selection (Week 1-2): Criterios pilot (criticidad media, willing team)
    - Design (Week 3-4): Target topology (AT1 stream-aligned)
    - Execution (Week 5-12): Restructure, empower, monitor
    - Validation (Week 13-16): Measure vs baseline
    
  Success_Criteria:
    - Cycle time -20%
    - Handoffs < 30% (interim target)
    - Team satisfaction >4/5
    - Stakeholders approve scale
    
  Output: Pilot validated → Proceed R5 (Scale)

R5_SCALE_TRANSFORMATION:
  Trigger: R4 successful AND C-level commitment
  
  Objetivo:
    Extender ORKO a 50-80% organización, systematize
    
  Duración: 6-9 meses
  
  Wave_Strategy:
    - Wave 1 (Month 1-3): Adjacent value streams (2-3 teams)
    - Wave 2 (Month 4-6): Core value streams (4-6 teams)
    - Wave 3 (Month 7-9): Remaining (long tail)
    
  Systemic_Changes:
    - Architecture Council deployed (governance)
    - Guilds formed (practice communities)
    - Platforms built (DevOps, Data, ML self-service)
    - Observability deployed (H_org tracking)
    
  Output: 50-80% org operating ORKO → Proceed R6 (Optimization)

R6_OPTIMIZATION_CONTINUOUS:
  Trigger: R5 completed AND H_org ≥ 70 sustained
  
  Objetivo:
    Fine-tune, institutionalize, sustain improvements
    
  Duración: 6-12 meses (transition to steady-state)
  
  Activities:
    - Kaizen velocity: >3 mejoras/quarter per stream
    - Platform maturity: v2+ iterations
    - Culture embedding: Principles in performance reviews
    - Advanced patterns: Complicated Subsystems (AT4) where needed
    
  Sustainability:
    - Internal capability (no external consultants)
    - Architecture Council self-sustaining
    - Automated governance (Policy Engine)
    
  Success_Criteria:
    - H_org > 80 sustained 6 months
    - All dimensions >70
    - Kaizen velocity high
    - Self-sustaining operations

Total_Timeline_R4-R6: 24-36 meses (pilot → optimization)

Related_Documents:
- ../30_metodologia_orko/README.md: Detalles completos playbooks transformación
  - Fase 0 Assessment: Ver L1_Assessment_ORKO (metodología)
```

## §9. PATTERN SELECTION GUIDE

```yaml
Decision_Tree:

  IF H_org < 70:
    → Apply PLAYBOOK R1 (Recovery)
    
  IF A3_Handoffs > 30%:
    → Apply PATTERN D1.1 (Team Topology)
    → Apply PLAYBOOK R2 (Handoff Reduction)
    
  IF A4_Alignment < 70%:
    → Apply PATTERN D1.3 (Purpose Cascade)
    → Apply PLAYBOOK R3 (OKR Alignment)
    
  IF P1_Coverage < 75%:
    → Apply PATTERN D2.1 (Observable Instrumentation)
    
  IF D3_Balance broken:
    → Apply PATTERN D3.1 (RICE Prioritization)
    
  IF D3 cycle time high:
    → Apply PATTERN D3.2 (WIP Limit)
    
  IF O1_FlowEfficiency < 40%:
    → Apply PATTERN D4.1 (Value Stream Map + optimize)
    
  IF M2_LeadTime > target:
    → Apply PATTERN D4.1 (Continuous Deployment)
    
  IF M4_MTTR > 1 day:
    → Apply PATTERN D4.2 (Observability Triad)
```
