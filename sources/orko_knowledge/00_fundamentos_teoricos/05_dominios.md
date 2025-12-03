# PARTE V: DOMINIOS

> **Etiquetado Genoma/Fenotipo**: Este documento contiene [GENOMA] (derivación D1-D4, definiciones, ortogonalidad) y [FENOTIPO] (métricas A_Score/P_Score/D_Score/H_org concretas, thresholds 70/80, heurísticas 70/30-70/20/10, técnicas portafolio). Ver §0.1 en 00_introduccion.md.

- [PARTE V: DOMINIOS](#parte-v-dominios)
  - [Dominios ortogonales](#dominios-ortogonales)
    - [§3. DERIVACIÓN DE LOS 4 DOMINIOS](#3-derivación-de-los-4-dominios)
    - [§4. DOMINIO D1: ARQUITECTURA (Fundamentos Teóricos)](#4-dominio-d1-arquitectura-fundamentos-teóricos)
    - [§5. DOMINIO D2: PERCEPCIÓN (Fundamentos Teóricos)](#5-dominio-d2-percepción-fundamentos-teóricos)
    - [§6. DOMINIO D3: DECISIÓN (Fundamentos Teóricos)](#6-dominio-d3-decisión-fundamentos-teóricos)
    - [§7. DOMINIO D4: OPERACIÓN (Fundamentos Teóricos)](#7-dominio-d4-operación-fundamentos-teóricos)
    - [§8. SÍNTESIS: INTERACCIONES DOMINIOS](#8-síntesis-interacciones-dominios)

## Dominios ortogonales

### §3. DERIVACIÓN DE LOS 4 DOMINIOS

```yaml
Pregunta_Ontológica:
  "¿Cuáles son las DIMENSIONES IRREDUCIBLES de complejidad organizacional?"

Derivación_Desde_Primitivos:

  Análisis_Complejidad:
    P1-P5 definen QUÉ es sistema
    Falta: ¿CÓMO organizar P1-P5 en sistema COMPLEJO?
    
    Pregunta_Descomposición:
      ¿Qué ASPECTOS ortogonales requiere sistema complejo?
      
  Identificación_Dominios:
    
    D1_ARQUITECTURA:
      Pregunta: "¿CÓMO estructurar sistema estáticamente?"
      Primitivos_Primarios: P1 (Capacidad), P4 (Límite), P5 (Propósito)
      Primitivos_Secundarios: P2 (Flujo - quién participa), P3 (Información - documentación)
      Scope: Diseño componentes, relaciones, fronteras
      
    D2_PERCEPCIÓN:
      Pregunta: "¿CÓMO capturar y comprender información?"
      Primitivos_Primarios: P3 (Información)
      Primitivos_Secundarios: P1 (Capacidad - sensores), P5 (Propósito - qué medir)
      Scope: Observabilidad, analytics, inteligencia
      
    D3_DECISIÓN:
      Pregunta: "¿CÓMO elegir acciones bajo límites?"
      Primitivos_Primarios: P5 (Propósito) bajo P4 (Límites)
      Primitivos_Secundarios: P2 (Flujo - portfolio), P3 (Información - evidencias)
      Scope: Gobernanza, estrategia, planificación
      
    D4_OPERACIÓN:
      Pregunta: "¿CÓMO ejecutar trabajo dinámicamente?"
      Primitivos_Primarios: P2 (Flujo), P1 (Capacidad)
      Primitivos_Secundarios: P3 (Información - outputs), P5 (Propósito - outcomes)
      Scope: Delivery, flujo valor, operaciones

Ortogonalidad_Dominios:
  
  Validación_Independencia:
    D1 ⊥ D2: Arquitectura vs Observabilidad (estructura vs captura)
    D1 ⊥ D3: Arquitectura vs Gobernanza (diseño vs dirección)
    D1 ⊥ D4: Arquitectura vs Operación (estático vs dinámico)
    D2 ⊥ D3: Percepción vs Decisión (captura vs acción)
    D2 ⊥ D4: Percepción vs Operación (observar vs ejecutar)
    D3 ⊥ D4: Decisión vs Operación (planificar vs hacer)
    
    Resultado: 6 pares validados → Ortogonalidad total ✓

Mapeo_SDA_Dominios:
  SENSE → D2 (Percepción captura estado)
  DECIDE → D3 (Decisión evalúa opciones)
  ACT → D4 (Operación ejecuta)
  Arquitectura (D1) → Estructura que habilita SDA
```

### §4. DOMINIO D1: ARQUITECTURA (Fundamentos Teóricos)

```yaml
D1_ARQUITECTURA:

  Definición_Formal:
    "Dominio que diseña ESTRUCTURA organizacional: 
     distribución capacidades, límites autoridad, alineación propósitos"

  Pregunta_Central: "¿Quién hace qué, con qué autoridad, para qué propósito?"

Primitivos_Operados:

  Primario_1_Capacidad:
    Responsabilidad: Definir, agrupar, asignar capacidades
    
    Actividades:
      - Identificar capacidades requeridas (skills, roles)
      - Agrupar capacidades en equipos/unidades
      - Definir ownership y accountability
      - Establecer span of control (límite 5-9 reports)
      
  Primario_2_Límite:
    Responsabilidad: Establecer boundaries organizacionales
    
    Actividades:
      - Definir límites autoridad (decision rights)
      - Establecer límites económicos (budgets)
      - Implementar límites organizacionales (policies, RACI)
      - Governance structures
      
  Primario_3_Propósito:
    Responsabilidad: Alinear propósitos jerárquicamente
    
    Actividades:
      - Cascada propósitos (Org → Unit → Team → Individual)
      - Verificar alignment vertical
      - Resolver conflictos propósitos
      
  Uso_Secundario:
    - Flujo: Define quién participa en qué flujos
    - Información: Documenta estructura (org charts, RACI)

Responsabilidades_Detalladas:

  R1_Diseño_Estructural:
    Qué: Determinar forma organizacional
    
    Decisiones:
      - Funcional vs divisional vs matricial vs red
      - Centralización vs descentralización
      - Jerarquía profunda vs plana
      - Equipos estables vs project-based
      
    Principios_Guía:
      - Conway's Law: Estructura → arquitectura sistema
      - Span of control: 5-9 reports (límite cognitivo manager)
      - Autonomy with alignment: Equipos autónomos, estrategia alineada
      - Minimize handoffs: < 20% pasos en flujos críticos
      
  R2_Asignación_Autoridad:
    Qué: Definir quién decide qué
    
    Mecanismos:
      - RACI matrices (Responsible, Accountable, Consulted, Informed)
      - Decision rights frameworks
      - Type 1 vs Type 2 decisions (reversible vs irreversible)
      - Delegation rules (M1-M6 para algorítmicos)
      
    Invariante_Crítico:
      ∀ decisión: ∃ exactamente 1 Accountable (autoridad única)
      
  R3_Gestión_Límites:
    Qué: Establecer y monitorear boundaries
    
    Tipos_Límites_Gestionados:
      - Organizacionales: Policies, procedures, approval gates
      - Económicos: Budget allocations, cost centers
      - Técnicos: Technology standards, architecture principles
      
    NO gestiona (otros dominios):
      - Regulatorios: Externos, D1 solo implementa compliance
      - Físicos: Naturales, D1 solo reconoce constraints

Niveles_Abstracción:

  L1_Estratégico:
    Scope: Organización completa
    Horizon: 1-3 años
    Actores: C-level, Board
    Decisiones: Modelo organizacional, major reorgs
    Refresh: Anual o cambio estratégico
    
  L2_Táctico:
    Scope: Unidades de negocio, departamentos
    Horizon: Trimestral
    Actores: VPs, Directors
    Decisiones: Team structures, capability builds
    Refresh: Trimestral
    
  L3_Operacional:
    Scope: Teams (5-9 personas)
    Horizon: Sprint (2 semanas)
    Actores: Engineering Managers, Team Leads
    Decisiones: Task assignment, on-call rotation
    Refresh: Sprint
    
  L4_Inmediato:
    Scope: Individuo
    Horizon: Diario
    Actores: Individual contributors
    Decisiones: Qué tarea priorizar hoy
    Refresh: Daily

Interacciones_Con_Otros_Dominios:

  D1 → D2 (Arquitectura → Percepción):
    Información: Métricas estructura
      - IN1_Velocidad_Decisión: Cycle time decisiones
      - IN2_Salud_Talento: Engagement, turnover, burnout
      - Clarity_Score: % personas que saben quién decide qué
      
  D1 ← D2 (Percepción → Arquitectura):
    Señales: Problemas estructurales
      - Bottlenecks organizacionales
      - Conflictos autoridad frecuentes
      - Silos comunicacionales
      → Trigger reorg
      
  D1 → D3 (Arquitectura → Decisión):
    Input: Capacidades disponibles
      - Qué teams existen
      - Qué skills disponibles
      - Capacity throughput
      → D3 usa para asignar iniciativas
      
  D1 ← D3 (Decisión → Arquitectura):
    Dirección: Estrategia organizacional
      - Nuevas capabilities requeridas
      - Growth plans (hiring)
      - Sunset capabilities (layoffs, pivots)
      → D1 rediseña estructura
      
  D1 → D4 (Arquitectura → Operación):
    Estructura: Quién ejecuta qué
      - Team membership
      - Roles y responsabilidades
      - Interfaces entre teams
      → D4 opera dentro estructura
      
  D1 ← D4 (Operación → Arquitectura):
    Feedback: Friction operacional
      - Handoffs lentos
      - Dependencies bloqueantes
      - Duplicación esfuerzos
      → D1 ajusta estructura

Métricas_Health:

  [GENOMA] Concepto_Salud_Arquitectura:
    Definición: "∃ función health_D1: Estructura → [0,1] que mide calidad arquitectura"
    Propiedades_Requeridas:
      - Monotonía: Mejor estructura → mayor health
      - Accionabilidad: health baja → diagnóstico + intervención
      - Constraint: health_D1 < H_min → bloquear transformaciones estructurales
    Fundamentación:
      - Estructura enferma no soporta cambio estructural adicional
      - Correlación: health_D1 ↔ velocity, quality, employee_satisfaction
      
  [FENOTIPO] A_Score_Implementación:
    "Métrica recomendada salud arquitectura (0-100)"
    
    Componentes_Sugeridos:
      A1_Claridad_Autoridad: % decisiones con accountable único claro
        Target_Recomendado: > 90%
        
      A2_Span_Control: % managers con 5-9 reports
        Target_Recomendado: > 80%
        
      A3_Handoff_Ratio: Promedio handoffs / steps en flujos críticos
        Target_Recomendado: < 20%
        
      A4_Alignment_Propósitos: % propósitos individuales alineados con org
        Target_Recomendado: > 85%
        
      A5_Violaciones_Governance: # violaciones policies / mes
        Target_Recomendado: < 5 (org 100 personas)
        
    Fórmula_Sugerida:
      A_Score = weighted_avg(A1×30%, A2×20%, A3×25%, A4×20%, A5×5%)
      
    Interpretación_Típica:
      A_Score > 80: Excelente (estructura clara, funciona bien)
      A_Score 70-80: Bueno (funcional, mejoras incrementales)
      A_Score 60-70: Aceptable (friction notable, requiere atención)
      A_Score < 60: Crítico (disfuncional, requiere intervención urgente)
      
    Threshold_Default:
      H_min = 70 (alineado con 07_ecuacion_maestra)
      IF A_Score < 70 THEN bloquear transformaciones estructurales
      
    NOTA: Pesos, targets y thresholds son CONFIGURABLES según contexto org

Emergence_Level:

  Arquitectura emerge en Nivel_3 (Reflexión Estructural)
  
  Señales_Necesidad:
    - Organización > 50 personas
    - > 5 teams interdependientes
    - Handoffs frecuentes ralentizan
    - Duplicación esfuerzos
    - Conway's Law problems (código refleja mal org)
    
  Pre-Nivel_3:
    Estructura informal suficiente
    Todos se conocen, comunicación ad-hoc funciona
    
  Post-Nivel_3:
    Requiere diseño explícito
    RACI formal, org charts, governance
    Arquitectos organizacionales

Fundamentación_Teórica:
  - Organizational Design Theory: Galbraith Star Model
  - Contingency Theory: Structure follows strategy (Chandler)
  - Systems Theory: Hierarchical decomposition (Simon)
  - Conway's Law: Architecture mirrors communication structure
  
Validación_Operativa:
  CHECK: D1 responsable ESTRUCTURA, no estrategia (eso es D3)
  CHECK: D1 ortogonal a D2, D3, D4 (validado §3)
  CHECK: A_Score medible y accionable
```

### §5. DOMINIO D2: PERCEPCIÓN (Fundamentos Teóricos)

```yaml
D2_PERCEPCIÓN:

  Definición_Formal:
    "Dominio que captura ESTADO interno/externo sistema,
     detecta anomalías, patterns, y proyecta evolución"

  Pregunta_Central: "¿Qué está pasando? ¿Qué detectamos?"

Primitivos_Operados:

  Primario_Información:
    Responsabilidad: Capturar, procesar, interpretar observables
    
    Actividades:
      - Instrumentar observability (logs, metrics, traces)
      - Agregar información (dashboards, reports)
      - Detectar anomalías (outliers, drift)
      - Proyectar tendencias (forecasting)
      
  Secundario_Capacidad:
    Uso: Sensores, analytics engines, ML models
    
    Tipos:
      - Pasivos: Logs, metrics collectors (C0)
      - Activos: Anomaly detectors, forecasters (C1-C2)

Responsabilidades_Detalladas:

  R1_Instrumentación:
    Qué: Capturar observables 16 tipos
    
    Externos (EX1-EX8):
      EX1_Demanda_Mercado:
        - Fuentes: CRM, sales data, market research
        - Frecuencia: Diaria-mensual
        - Ejemplos: Lead flow, conversion rates, market share
        
      EX2_Competidores:
        - Fuentes: Competitive intelligence, news, análisis
        - Frecuencia: Semanal-mensual
        - Ejemplos: Lanzamientos competidores, pricing, features
        
      EX3_Regulatorio:
        - Fuentes: Legal, compliance tracking
        - Frecuencia: Continua (alertas), revisión trimestral
        - Ejemplos: Nuevas leyes, cambios GDPR, auditorías
        
      EX4_Tecnológico:
        - Fuentes: Tech radar, vendor landscape, research
        - Frecuencia: Mensual-trimestral
        - Ejemplos: Emergencia LLMs, cloud trends, frameworks
        
      EX5_Feedback_Clientes:
        - Fuentes: Support tickets, NPS, reviews, user research
        - Frecuencia: Continua
        - Ejemplos: Feature requests, bugs reported, satisfaction

      EX6_Eventos_Disruptivos:
        - Fuentes: News, risk monitoring
        - Frecuencia: Ad-hoc (eventos)
        - Ejemplos: Pandemia, crisis económica, desastres
        
      EX7_Tendencias_Sociales:
        - Fuentes: Social media, demographic data
        - Frecuencia: Mensual-trimestral
        - Ejemplos: Remote work adoption, sustainability concerns
        
      EX8_Condiciones_Económicas:
        - Fuentes: Economic indicators, forecasts
        - Frecuencia: Mensual
        - Ejemplos: Inflación, unemployment, GDP growth
        
    Internos (IN1-IN8):
      IN1_Velocidad_Decisión:
        - Métrica: Decision cycle time (días)
        - Fuente: Project tracking, workflows
        - Target: < 2 semanas decisiones tácticas
        
      IN2_Salud_Talento:
        - Métricas: Engagement score, turnover rate, burnout signals
        - Fuente: Surveys, HR analytics, 1-1s
        - Target: Engagement > 7/10, Turnover < 15% anual
        
      IN3_Eficiencia_Flujos:
        - Métricas: Cycle time, throughput, bottlenecks
        - Fuente: Kanban boards, DORA metrics
        - Target: Cycle time < 2 semanas, deploy freq > 1/día
        
      IN4_Calidad_Outputs:
        - Métricas: Defect escape rate, rework %
        - Fuente: Quality gates, customer incidents
        - Target: Defects < 2%, Rework < 10%
        
      IN5_Utilización_Capacidades:
        - Métricas: Idle time, overload signals
        - Fuente: Resource tracking, capacity planning
        - Target: Utilization 70-85% (ni idle ni burnout)
        
      IN6_Alineación_Propósitos:
        - Métrica: OKR alignment score
        - Fuente: OKR tracking, surveys
        - Target: > 85% propósitos individuales alineados con org
        
      IN7_Violaciones_Límites:
        - Métricas: Compliance violations, budget overruns
        - Fuente: Audit logs, finance systems
        - Target: < 5 violaciones/mes (org 100 personas)
        
      IN8_Debt_Acumulado:
        - Métricas: Tech debt, process debt, knowledge debt
        - Fuente: Code quality tools, process audits
        - Target: Debt remediation velocity > debt accumulation
        
  R2_Detección_Anomalías:
    Qué: Identificar desviaciones significativas
    
    Técnicas:
      Statistical: Outlier detection (>3σ desde media)
      ML-based: Isolation forests, autoencoders
      Rule-based: Threshold alerts
      
    Ejemplos:
      - Latencia API > 2s (threshold)
      - Deploy failure rate > 10% (statistical)
      - Patrón inusual traffic (ML)
      
  R3_Comprensión_Contextual:
    Qué: Interpretar señales en contexto
    
    Actividades:
      - Correlacionar múltiples observables
      - Distinguir noise de señal real
      - Enriquecer con contexto histórico
      
    Ejemplo:
      - Spike traffic:
        + ¿Marketing campaign? (esperado)
        + ¿DDoS attack? (crítico)
        + ¿Viral growth? (oportunidad)
        
      Contexto determina interpretación
      
  R4_Proyección_Tendencias:
    Qué: Anticipar evolución futura
    
    Horizontes:
      - Inmediato: Próximas horas (capacity planning)
      - Táctico: Próximas semanas (sprint planning)
      - Estratégico: Próximos meses-año (roadmap)
      
    Técnicas:
      - Time series forecasting (ARIMA, Prophet)
      - Causal models (when mechanism known)
      - Scenario planning (uncertainty high)

Niveles_Abstracción:

  L1_Estratégico:
    Observables: Externos dominantes (EX1-EX8)
    Horizon: 1-3 años
    Refresh: Trimestral
    Outputs: Market intelligence, strategic insights
    Consumers: C-level, Board
    
  L2_Táctico:
    Observables: Mix externo-interno
    Horizon: Meses
    Refresh: Mensual
    Outputs: Business metrics, capability health
    Consumers: VPs, Directors
    
  L3_Operacional:
    Observables: Internos dominantes (IN1-IN8)
    Horizon: Semanas
    Refresh: Semanal
    Outputs: Team metrics, sprint health
    Consumers: Engineering Managers, Product Managers
    
  L4_Inmediato:
    Observables: Real-time técnicos
    Horizon: Minutos-horas
    Refresh: Continuo
    Outputs: System health, alerts
    Consumers: SRE, On-call engineers

Interacciones_Con_Otros_Dominios:

  D2 → D1 (Percepción → Arquitectura):
    Señales: Health arquitectura
      - IN1 (Velocidad decisión): Bottlenecks estructurales
      - IN2 (Salud talento): Burnout, turnover
      → Trigger ajustes estructura
      
  D2 → D3 (Percepción → Decisión):
    Input: Estado sistema para decisiones
      - Performance actual vs targets
      - Opportunities detectadas
      - Risks emergentes
      → D3 decide basado en estado percibido
      
  D2 → D4 (Percepción → Operación):
    Monitoreo: Health operacional
      - IN3 (Eficiencia flujos): Bottlenecks
      - IN4 (Calidad): Defects
      → D4 ajusta ejecución
      
  D2 ← D1 (Arquitectura → Percepción):
    Estructura: Qué observar
      - Boundaries monitorear
      - Teams health tracking
      
  D2 ← D3 (Decisión → Percepción):
    Dirección: Qué métricas priorizar
      - OKRs definen métricas clave
      - Initiatives requieren tracking específico
      
  D2 ← D4 (Operación → Percepción):
    Datos: Eventos operacionales
      - Logs aplicaciones
      - Métricas infraestructura
      - Traces distribuidos

Métricas_Health:

  [GENOMA] Concepto_Salud_Percepción:
    Definición: "∃ función health_D2: Coverage_Observables → [0,1]"
    Propiedades: Monotonía, Accionabilidad, Freshness crítico
    
  [FENOTIPO] P_Score: Métrica recomendada salud percepción (0-100)
  
  Componentes:
    P1_Coverage:
      = % observables 16 instrumentados
      Target: > 80%
      
    P2_Freshness:
      = % métricas actualizadas < validity_period
      Target: > 95%
      
    P3_Latencia_Detección:
      = Tiempo anomalía → alerta
      Target: < 5 minutos (críticos)
      
    P4_False_Positive_Rate:
      = % alertas que son falsos positivos
      Target: < 10%
      
    P5_Actionability:
      = % insights que generan acción
      Target: > 60%
      
  Fórmula:
    P_Score = weighted_avg(P1×20%, P2×20%, P3×25%, P4×15%, P5×20%)

Emergence_Level:

  Percepción básica: Todos niveles (0-5)
    - Nivel 0: Sensors físicos
    - Nivel 1: Dashboards operacionales
    - Nivel 2: Analytics mejora continua
    - Nivel 3: Business intelligence
    - Nivel 4: Strategic foresight
    
  Percepción sofisticada emerge con complejidad
    - ML-based anomaly detection: Nivel 2+
    - Predictive analytics: Nivel 3+
    - Strategic scenario planning: Nivel 4

Fundamentación_Teórica:
  - Cybernetics: Feedback loops (Wiener)
  - Control Theory: Observability (Kalman)
  - Signal Processing: Noise vs signal (Shannon)
  - Observability Engineering: Logs, metrics, traces (honeycomb.io)
  
Validación_Operativa:
  CHECK: D2 responsable OBSERVAR, no decidir (eso es D3)
  CHECK: 16 observables cubren interno+externo comprehensivo
  CHECK: P_Score medible y accionable
```

### §6. DOMINIO D3: DECISIÓN (Fundamentos Teóricos)

```yaml
D3_DECISIÓN:

  Definición_Formal:
    "Dominio que planifica EVOLUCIÓN organizacional:
     define propósitos, prioriza iniciativas, asigna capacidades"

  Pregunta_Central: "¿Qué deberíamos hacer? ¿Cómo priorizamos?"

Primitivos_Operados:

  Primario_1_Propósito:
    Responsabilidad: Definir, cascadear, evaluar propósitos
    
    Actividades:
      - Establecer OKRs (Objectives & Key Results)
      - Cascada jerárquica propósitos (Org → Unit → Team → Individual)
      - Tracking progreso contra targets
      - Refinamiento continuo basado en feedback
      
  Primario_2_Flujo:
    Responsabilidad: Priorizar portfolio flujos/iniciativas
    
    Actividades:
      - Evaluar ROI/valor iniciativas
      - Priorizar backlog (qué hacer primero)
      - Asignar capacidades a iniciativas
      - Balancear producción vs habilitación
      
  Uso_Secundario:
    - Capacidad: Evalúa disponibilidad para asignar
    - Información: Usa insights D2 para decisiones
    - Límite: Opera dentro constraints (budget, regulatorio)

Responsabilidades_Detalladas:

  R1_Definición_Propósitos:
    Qué: Establecer outcomes deseados medibles
    
    Estructura_OKR:
      Objective: Descripción cualitativa inspiradora
        - Específico pero no métrico
        - Time-bound (horizonte claro)
        - Alcanzable pero ambicioso
        
      Key_Results: Métricas cuantitativas (2-5 por objetivo)
        - Medibles inequívocamente
        - Tienen valor actual y target
        - Progreso rastreable
        
    Ejemplo_Completo:
      Objective: "Convertirse en líder mercado enterprise SaaS LATAM"
      
      Key_Results:
        KR1: ARR > $10M (actual: $3M, target: $10M)
        KR2: Enterprise customers > 50 (actual: 15, target: 50)
        KR3: NPS enterprise > 60 (actual: 42, target: 60)
        KR4: Churn enterprise < 5% (actual: 12%, target: 5%)
        
      Scope: Organización
      Horizon: Estratégico (12 meses)
      Owner: CEO
      
    Cascada_Jerárquica:
      L1_Org: "Líder mercado LATAM"
        ↓
      L2_Product: "Lanzar 5 features enterprise Q1"
        KR: Feature adoption > 70% enterprise customers
        ↓
      L3_Team_Auth: "Implementar SSO enterprise-grade"
        KR: SSO integración SAML + OIDC completa
        ↓
      L4_Engineer: "Completar SAML provider integration"
        KR: Tests passing + documentación + deploy
        
    Propiedad_Alineación:
      ∀ propósito_nivel_N:
        contribuye_a(propósito_nivel_(N+1))
        
      Medible:
        Alignment_Score = 
          Σ (peso_child × progress_child) / total_peso
          
  R2_Priorización_Portfolio:
    Qué: Decidir qué iniciativas ejecutar y cuándo
    
    Frameworks_Priorización:
      
      RICE_Score:
        = (Reach × Impact × Confidence) / Effort
        
        Reach: # usuarios afectados
        Impact: Nivel impacto (0.25=minimal, 3=massive)
        Confidence: % certeza estimación (0-100%)
        Effort: Person-months requeridos
        
        Ejemplo:
          Feature_A:
            Reach: 1000 users
            Impact: 2 (high)
            Confidence: 80%
            Effort: 3 person-months
            RICE = (1000 × 2 × 0.8) / 3 = 533
            
          Feature_B:
            Reach: 100 users
            Impact: 3 (massive)
            Confidence: 50%
            Effort: 1 person-month
            RICE = (100 × 3 × 0.5) / 1 = 150
            
          Prioridad: Feature_A > Feature_B
          
      Weighted_Shortest_Job_First (WSJF):
        = Cost_of_Delay / Duration
        
        Cost_of_Delay = User_Value + Time_Criticality + Risk_Reduction
        
        Usado en: SAFe, Lean portfolio management
        
      Value_vs_Effort_Matrix:
        Cuadrantes:
          - High Value, Low Effort → DO FIRST (quick wins)
          - High Value, High Effort → DO LATER (strategic)
          - Low Value, Low Effort → DO IF TIME (nice-to-have)
          - Low Value, High Effort → DON'T DO (waste)
          
    Balanceo_Portfolio:
      Dimensión_1_Producción_vs_Habilitación:
        Target típico: 70% producción, 30% habilitación
        
        Justificación:
          - Demasiado producción → debt acumula, velocity decae
          - Demasiado habilitación → no delivery valor visible
          
      Dimensión_2_Horizonte_Temporal:
        Target típico (Kelly):
          - 70% now (Q actual)
          - 20% next (Q siguiente)
          - 10% later (exploración futura)
          
      Dimensión_3_Riesgo:
        - Core business (bajo riesgo, high confidence)
        - Adjacent opportunities (medio riesgo)
        - Transformational bets (alto riesgo, high upside)
        
        Target: 70% core, 20% adjacent, 10% transformational
        
  R3_Asignación_Capacidades:
    Qué: Mapear capacidades disponibles a iniciativas priorizadas
    
    Algoritmo_Asignación:
      Input:
        - Iniciativas priorizadas (ordenadas por score)
        - Capacidades disponibles (con throughput, skills)
        - Límites (budget, time, dependencies)
        
      Process:
        1. Ordenar iniciativas descendente por prioridad
        2. FOR EACH iniciativa:
             a. Verificar capacidades requeridas disponibles
             b. IF disponibles THEN asignar
             c. ELSE defer o escalar (contratar, reasignar)
        3. Monitorear utilización capacidades
             IF utilization > 85% THEN riesgo burnout
             IF utilization < 60% THEN capacidad ociosa
             
      Output:
        - Initiative-to-Team mapping
        - Resource allocation plan
        - Capacity gaps identificados
        
  R4_Gestión_Decisiones:
    Qué: Tomar y documentar decisiones arquitectónicas/estratégicas
    
    Tipos_Decisión:
      Type_1 (Irreversible):
        - Ejemplos: Contratar 100 personas, M&A, pivote modelo negocio
        - Requiere: Análisis profundo, consenso C-level
        - Delegación: Solo humanos C2-C3
        - Documentación: ADR (Architecture Decision Record) obligatorio
        
      Type_2 (Reversible):
        - Ejemplos: Experimento feature, A/B test, tech spike
        - Requiere: Análisis ligero, decisión rápida
        - Delegación: Puede delegar a teams (C1-C2)
        - Documentación: Opcional, ticket/issue suficiente
        
    Decision_Velocity:
      Métrica: Tiempo desde propuesta hasta decisión
      
      Targets:
        Type_1: < 2 semanas (decisiones mayores)
        Type_2: < 2 días (decisiones reversibles)
        
      Bottlenecks_Comunes:
        - Too many stakeholders (difusión responsabilidad)
        - Información insuficiente (analysis paralysis)
        - Falta ownership (nadie accountable)

Niveles_Abstracción:

  L1_Estratégico:
    Horizon: 1-3 años
    Decisiones: Visión, estrategia empresa, M&A, pivotes
    Actores: CEO, Board
    Cadencia: Anual + ad-hoc (crisis, oportunidades)
    Outputs: Strategic plan, OKRs anuales
    
    Ejemplos:
      - "Expandir a mercado enterprise"
      - "Adquirir competidor X"
      - "Pivotar de B2C a B2B"
      
  L2_Táctico:
    Horizon: Trimestral
    Decisiones: Capabilities, platforms, major features
    Actores: VPs, Directors
    Cadencia: Quarterly planning
    Outputs: Quarterly OKRs, roadmap trimestral
    
    Ejemplos:
      - "Construir plataforma payments interna"
      - "Migrar a microservices"
      - "Lanzar producto tier enterprise"
      
  L3_Operacional:
    Horizon: Sprint (2 semanas)
    Decisiones: Features, tech debt, optimizaciones
    Actores: Product Managers, Engineering Managers
    Cadencia: Sprint planning (bi-semanal)
    Outputs: Sprint backlog, sprint goals
    
    Ejemplos:
      - "Implementar dark mode"
      - "Refactorizar módulo autenticación"
      - "Optimizar query lenta dashboard"
      
  L4_Inmediato:
    Horizon: Diario
    Decisiones: Tasks, bugs, priorización diaria
    Actores: Individual contributors
    Cadencia: Daily standup
    Outputs: Task assignments, blockers identificados
    
    Ejemplos:
      - "Fix bug crítico producción"
      - "Review PR antes de nueva feature"
      - "Investigar spike latencia"

Interacciones_Con_Otros_Dominios:

  D3 ← D2 (Percepción → Decisión):
    Input_Crítico: Estado sistema para decidir
      - Performance actual vs targets (gap analysis)
      - Opportunities (EX1: demanda mercado)
      - Threats (EX2: competidores, EX3: regulación)
      - Internal health (IN1-IN8)
      
    SIN D2 → D3 decide ciego (dangerous)
    
  D3 → D4 (Decisión → Operación):
    Dirección: Qué ejecutar
      - Iniciativas priorizadas
      - Recursos asignados
      - Success criteria (KRs)
      
    D4 ejecuta lo que D3 decide
    
  D3 ← D4 (Operación → Decisión):
    Feedback: Execution reality
      - Estimaciones vs actual (velocity real)
      - Blockers encontrados (dependencies)
      - Learnings (pivots requeridos)
      
    Informa re-priorización
    
  D3 ← D1 (Arquitectura → Decisión):
    Constraints: Capacidades disponibles
      - Qué teams existen
      - Skills disponibles
      - Throughput capacity
      
    Límita qué puede decidirse ejecutar
    
  D3 → D1 (Decisión → Arquitectura):
    Strategic_Direction: Capabilities requeridas
      - Growth plans → hiring
      - New capabilities → team formation
      - Sunset → reorganización
      
    Trigger cambios estructurales

Métricas_Health:

  [GENOMA] Concepto_Salud_Decisión:
    Definición: "∃ función health_D3: (Velocity × Quality × Alignment) → [0,1]"
    Propiedades: Trade-off velocity/quality, Portfolio balance obligatorio
    
  [FENOTIPO] D_Score: Métrica recomendada salud decisión (0-100)
  
  Componentes:
    D1_Decision_Velocity:
      = 1 / avg_days_to_decision
      Normalizado: Score = min(100, 100/avg_days × 2)
      Target: < 2 días Type_2, < 14 días Type_1
      
    D2_Alignment_OKRs:
      = % OKRs cascadeados correctamente
      Target: > 85%
      
    D3_Portfolio_Balance:
      = 1 - |actual_distribution - target_distribution|
      Dimensiones: Producción/Habilitación, Now/Next/Later
      Target: < 15% desviación
      
    D4_Execution_Rate:
      = % iniciativas completadas vs iniciadas
      Target: > 80% (no over-commit)
      
    D5_Learning_Velocity:
      = % decisiones con retrospective/postmortem
      Target: > 90% (Type_1), > 30% (Type_2)
      
  Fórmula:
    D_Score = weighted_avg(
      D1×25%, D2×20%, D3×20%, D4×25%, D5×10%
    )
    
  Regla_Health:
    IF D_Score < 60 THEN decisión disfuncional
      → Síntomas: Parálisis análisis, over-commitment, desalineación

Patrones_Anti:

  AP1_Analysis_Paralysis:
    Síntoma: Decisiones tardan semanas/meses
    Causa: Información perfecta imposible, fear of failure
    Fix: Time-box decisiones Type_2 (48h max), bias to action
    
  AP2_Overcommitment:
    Síntoma: Execution_Rate < 50%
    Causa: Optimismo sesgado, no considera constraints
    Fix: Conservative capacity planning (use 70% capacity)
    
  AP3_Lack_Alignment:
    Síntoma: Teams trabajan objetivos contradictorios
    Causa: OKRs no cascadeados, communication breakdown
    Fix: Quarterly OKR alignment sessions
    
  AP4_HiPPO_Decisions:
    Síntoma: Highest Paid Person's Opinion wins siempre
    Causa: Cultura jerárquica, no data-driven
    Fix: Require data backing decisiones, diverse input
    
  AP5_Sunk_Cost_Fallacy:
    Síntoma: Continuar iniciativas fallidas (too invested)
    Causa: Ego, política, no admitir error
    Fix: Kill criteria explícitos, celebrate stopping bad bets

Emergence_Level:

  Decisión básica: Todos niveles
    - Nivel 1: Decisiones locales operacionales
    - Nivel 2: Decisiones tácticas mejora continua
    
  Decisión sofisticada emerge:
    - Portfolio management: Nivel 3+ (requiere vista cross-team)
    - Strategic planning: Nivel 4 (requiere reflexión propósito)
    - OKR cascades: Nivel 3+ (requiere alineación jerárquica)

Fundamentación_Teórica:
  - Decision Theory: Expected utility maximization
  - Organizational Learning: Single/double loop (Argyris)
  - OKR Framework: Google, Intel origins (Doerr)
  - Lean Portfolio Management: Epic hypothesis, WSJF
  - Behavioral Economics: Biases en decisión (Kahneman)
  
Validación_Operativa:
  CHECK: D3 responsable PLANIFICAR, no ejecutar (eso es D4)
  CHECK: D3 ortogonal a D1, D2, D4 (validado §3)
  CHECK: D_Score medible y accionable
```

### §7. DOMINIO D4: OPERACIÓN (Fundamentos Teóricos)

```yaml
D4_OPERACIÓN:

  Definición_Formal:
    "Dominio que EJECUTA flujos de valor:
     transforma inputs en outputs continuamente entregando valor"

  Pregunta_Central: "¿Cómo entregamos valor? ¿Cómo operamos día a día?"

Primitivos_Operados:

  Primario_1_Flujo:
    Responsabilidad: Ejecutar flujos producción/habilitación
    
    Actividades:
      - Ejecutar transformaciones (steps en flujo)
      - Monitorear progreso (WIP, cycle time)
      - Resolver blockers
      - Entregar outputs
      
  Primario_2_Capacidad:
    Responsabilidad: Utilizar capacidades (teams, individuos)
    
    Actividades:
      - Asignar tareas a capacidades
      - Coordinar handoffs
      - Balancear carga trabajo
      - Desarrollar skills (learning)
      
  Uso_Secundario:
    - Información: Genera logs, métricas, outputs
    - Límite: Opera dentro quality gates, SLAs
    - Propósito: Ejecuta hacia outcomes definidos D3

Responsabilidades_Detalladas:

  R1_Ejecución_Continua:
    Qué: Ejecutar flujos repetidamente entregando valor
    
    Flujos_Producción:
      Ejemplos:
        - Development: Code → Review → Test → Deploy
        - Support: Ticket → Triage → Resolve → Close
        - Sales: Lead → Qualify → Demo → Close
        
      Característica: Output consumido por cliente externo
      
    Flujos_Habilitación:
      Ejemplos:
        - CI/CD: Build → Test → Deploy automation
        - Monitoring: Collect → Aggregate → Alert
        - Onboarding: Hire → Train → Ramp up
        
      Característica: Output amplifica otros flujos
      
    Propiedad_Repetición:
      Flujos operacionales se ejecutan N veces
      Mejora continua cada iteración (kaizen)
      
  R2_Gestión_Flujo:
    Qué: Optimizar flujo trabajo (flow efficiency)
    
    Métricas_Core:
      
      Cycle_Time:
        = Tiempo desde inicio hasta entrega
        Ejemplo: Feature spec → deployed = 8 días
        Target: Minimizar (< 2 semanas típico)
        
      Lead_Time:
        = Tiempo desde solicitud hasta entrega
        Incluye: Queue time + cycle time
        Ejemplo: Feature request → deployed = 4 semanas
        
      Throughput:
        = Unidades completadas / periodo
        Ejemplo: 20 features / quarter
        Target: Maximizar sosteniblemente
        
      WIP (Work In Progress):
        = Unidades en proceso simultáneamente
        Ley Little: Lead_Time = WIP / Throughput
        Target: Minimizar WIP para reducir lead time
        
      Flow_Efficiency:
        = Value_Add_Time / Lead_Time
        Ejemplo: 2 días coding / 14 días total = 14%
        Target: > 40% (típico industry 15%)
        
    Optimizaciones:
      - Reduce WIP (limit WIP Kanban)
      - Elimina waits (handoffs, approvals)
      - Automatiza repetitivo (CI/CD, tests)
      - Paraleliza donde posible
      - Reduce batch sizes (deploy frecuente)
      
  R3_Gestión_Calidad:
    Qué: Asegurar outputs cumplen criterios aceptación
    
    Quality_Gates:
      - Unit tests (coverage > 80%)
      - Integration tests (critical paths)
      - Code review (2 approvers)
      - Security scan (SAST, DAST)
      - Performance tests (latency < SLA)
      
    Defect_Management:
      Defect_Escape_Rate = Defects_Prod / Total_Defects
      Target: < 5% (mayoría detectados pre-prod)
      
      Cuando escapa:
        1. Incident response (mitigate)
        2. Root cause analysis (5 whys)
        3. Fix + test
        4. Postmortem (blameless)
        5. Prevention (process improvement)
        
    Quality ≠ Velocity_Tradeoff:
      Falacia: "Más rápido = menos calidad"
      Realidad: Quality HABILITA velocity
      
      Evidencia:
        - Tech debt ralentiza futuro
        - Defects consumen capacity (rework)
        - Automated testing acelera confidence
        
  R4_Coordinación_Teams:
    Qué: Sincronizar trabajo entre capacidades
    
    Intra-Team:
      Daily_Standup:
        - Frecuencia: Diaria (15 min)
        - Propósito: Sincronizar, identificar blockers
        - Formato: Yesterday/Today/Blockers
        
      Sprint_Planning:
        - Frecuencia: Cada sprint (2 semanas)
        - Propósito: Comprometer trabajo sprint
        - Output: Sprint backlog, sprint goal
        
      Retrospective:
        - Frecuencia: Fin sprint
        - Propósito: Mejorar proceso
        - Output: Action items mejora
        
    Inter-Team:
      Scrum_of_Scrums:
        - Frecuencia: 2-3x semana
        - Participantes: Reps de cada team
        - Propósito: Coordinar dependencies
        
      Architecture_Sync:
        - Frecuencia: Semanal
        - Participantes: Tech leads
        - Propósito: Decisiones técnicas cross-team
        
  R5_Manejo_Incidents:
    Qué: Responder a disrupciones operacionales
    
    Severidades:
      SEV1_Critical:
        - Definición: Sistema down, data loss, security breach
        - Response: Inmediata (< 15 min)
        - Escalation: On-call → Manager → VP
        - Postmortem: Obligatorio (48h post-resolve)
        
      SEV2_Major:
        - Definición: Degradación significativa, workaround posible
        - Response: < 1 hora
        - Escalation: On-call → Team lead
        - Postmortem: Recomendado
        
      SEV3_Minor:
        - Definición: Issues menores, low impact
        - Response: Próximo business day
        - Escalation: Backlog normal
        - Postmortem: Opcional
        
    Incident_Response_Cycle:
      1. Detect (monitoring, alerts)
      2. Triage (severidad, impact)
      3. Mitigate (restore service)
      4. Resolve (fix root cause)
      5. Learn (postmortem, prevention)

Niveles_Abstracción:

  L1_Estratégico:
    Scope: N/A (D4 no opera en estratégico)
    Nota: Estrategia definida D3, ejecutada D4 en táctico-operacional
    
  L2_Táctico:
    Horizon: Quarter
    Operaciones: Ejecutar OKRs trimestrales
    Actores: Teams (5-9 personas)
    Cadencia: Sprints (2 semanas)
    Outputs: Features, capabilities entregadas
    
  L3_Operacional:
    Horizon: Sprint (2 semanas)
    Operaciones: Ejecutar stories, tasks
    Actores: Individual contributors
    Cadencia: Daily
    Outputs: Commits, PRs, deploys
    
  L4_Inmediato:
    Horizon: Tiempo real
    Operaciones: Monitoreo, alerts, hotfixes
    Actores: On-call engineers, SRE
    Cadencia: Continuo
    Outputs: System uptime, incident resolution

Interacciones_Con_Otros_Dominios:

  D4 ← D3 (Decisión → Operación):
    Input_Crítico: Qué ejecutar
      - Iniciativas priorizadas
      - Sprint backlog
      - Success criteria
      
    D4 NO decide QUÉ, solo CÓMO ejecutar eficientemente
    
  D4 → D3 (Operación → Decisión):
    Feedback: Execution reality
      - Velocity real (story points / sprint)
      - Blockers (dependencies, risks)
      - Learnings (assumptions incorrectas)
      
    Informa re-planning
    
  D4 → D2 (Operación → Percepción):
    Data_Stream: Eventos operacionales
      - Logs aplicaciones
      - Métricas infraestructura (CPU, memory, latency)
      - Traces distribuidos
      - Business events (orders, signups, churn)
      
    D2 agrega/analiza estos datos
    
  D4 ← D2 (Percepción → Operación):
    Monitoring: Health operacional
      - Alerts (incidents)
      - Dashboards (performance)
      - Anomalies (potential issues)
      
  D4 ← D1 (Arquitectura → Operación):
    Estructura: Cómo organizados
      - Team composition
      - Roles responsibilities
      - Interfaces entre teams
      
    D4 opera DENTRO estructura D1 define

Métricas_Health:

  O_Score: Métrica salud operación (0-100)
  
  Componentes:
    O1_Flow_Efficiency:
      = Value_Add_Time / Lead_Time × 100
      Target: > 40%
      
    O2_Cycle_Time:
      = Avg días desde start hasta done
      Target: < 14 días (2 semanas)
      Normalizado: Score = min(100, 1400/avg_days)
      
    O3_Throughput_Stability:
      = 1 - std_dev(throughput) / mean(throughput)
      Target: Low variance (predictable)
      
    O4_Quality:
      = (1 - Defect_Escape_Rate) × 100
      Target: > 95% (< 5% escapes)
      
    O5_Availability:
      = Uptime / Total_Time × 100
      Target: > 99.9% (< 43 min downtime/month)
      
  Fórmula:
    O_Score = weighted_avg(
      O1×20%, O2×25%, O3×15%, O4×20%, O5×20%
    )
    
  DORA_Metrics_Correlación:
    O2_Cycle_Time ≈ DORA Lead Time for Changes
    Throughput ≈ DORA Deployment Frequency
    O5_Availability ≈ DORA Availability
    (1-O4) ≈ DORA Change Failure Rate
    
    Elite performers (DORA):
      - Deploy freq: On-demand (múltiples/día)
      - Lead time: < 1 día
      - MTTR: < 1 hora
      - Change failure: < 15%

Patrones_Anti:

  AP1_Overutilization:
    Síntoma: Utilización > 90%, burnout
    Causa: Over-commitment (D3), no slack time
    Consecuencia: Quality degrada, velocity eventual colapso
    Fix: Target 70-80% utilization, preserve slack
    
  AP2_Hero_Culture:
    Síntoma: Few individuals "save the day" repetidamente
    Causa: Procesos frágiles, knowledge silos
    Consecuencia: Bus factor = 1, burnout héroes
    Fix: Documentation, pairing, rotation
    
  AP3_Firefighting_Mode:
    Síntoma: >50% tiempo en incidents/unplanned
    Causa: Tech debt, poor monitoring, reactive
    Consecuencia: No progreso planned work
    Fix: Invest en prevención (monitoring, automation)
    
  AP4_Feature_Factory:
    Síntoma: Output alto, outcome bajo (features no usadas)
    Causa: No validación valor, no customer feedback
    Consecuencia: Waste effort, opportunity cost
    Fix: Measure outcomes (usage, impact), kill features low value
    
  AP5_Handoff_Hell:
    Síntoma: Cycle time >> value-add time
    Causa: Silos funcionales, handoffs frecuentes
    Consecuencia: Wait time domina, frustration
    Fix: Cross-functional teams (minimize handoffs)

Emergence_Level:

  Operación: Todos niveles (0-5)
    - Nivel 0: Ejecución mecánica (RPA, automation)
    - Nivel 1: Ejecución con decisión local (operadores)
    - Nivel 2: Mejora continua (retrospectives, kaizen)
    
  Operación sofisticada emerge:
    - DevOps: Nivel 2 (CI/CD, automation, metrics)
    - SRE: Nivel 2 (error budgets, toil reduction)
    - Flow optimization: Nivel 2-3 (cross-team coordination)

Fundamentación_Teórica:
  - Lean Manufacturing: Flow, pull, kaizen (Toyota)
  - Theory of Constraints: Bottleneck management (Goldratt)
  - Queuing Theory: Little's Law, WIP limits
  - DevOps: CALMS (Culture, Automation, Lean, Measurement, Sharing)
  - SRE: Google SRE book (error budgets, toil, SLOs)
  
Validación_Operativa:
  CHECK: D4 responsable EJECUTAR, no planificar (eso es D3)
  CHECK: D4 ortogonal a D1, D2, D3 (validado §3)
  CHECK: O_Score medible y correlaciona con DORA metrics
```

### §8. SÍNTESIS: INTERACCIONES DOMINIOS

```yaml
Flujo_Información_Completo:

  Ciclo_Principal (OODA_Organizacional):
    
    D2_Percepción → D3_Decisión:
      "Observamos estado actual/externo"
      → "Decidimos qué hacer basado en propósitos"
      
    D3_Decisión → D4_Operación:
      "Priorizamos iniciativas"
      → "Ejecutamos iniciativas priorizadas"
      
    D4_Operación → D2_Percepción:
      "Ejecutamos y generamos outputs/eventos"
      → "Capturamos resultados para observar"
      
    D2_Percepción → [loop completes]:
      Nuevo ciclo con estado actualizado
      
  Arquitectura_Como_Estructura:
    
    D1 NO está en loop principal
    D1 DEFINE estructura donde loop ocurre
    
    D1 ← D2: Señales health estructural
    D1 → D3: Constraints capacidades disponibles
    D1 ← D3: Requirements nuevas capabilities
    D1 → D4: Estructura teams
    
    D1 cambia menos frecuente (reorgs trimestrales-anuales)
    D2-D3-D4 loop continuo (diario-semanal)

Validación_Completitud:

  ¿Falta algún dominio fundamental?
  
  Test_Coverage:
    ✓ Estructura (D1): Quién hace qué - CUBIERTO
    ✓ Observación (D2): Qué pasa - CUBIERTO
    ✓ Dirección (D3): Qué hacer - CUBIERTO
    ✓ Ejecución (D4): Cómo entregar - CUBIERTO
    
  Dimensiones_Organizacionales_Fundamentales:
    - Espacial: ¿Quién? → D1
    - Temporal: ¿Cuándo? → Implícito en horizontes D1-D4
    - Informacional: ¿Qué sabemos? → D2
    - Intencional: ¿Para qué? → D3
    - Transformacional: ¿Cómo transformamos? → D4
    
  Conclusión: 4 dominios necesarios y suficientes ✓

Propiedad_Closure:
  
  Pregunta: ¿Dominios se auto-contienen?
  
  Test:
    ∀ actividad_organizacional A:
      ∃ dominio_único D: A pertenece a D
      
  Evidencia:
    - Diseñar org chart → D1 (no D2, D3, D4)
    - Monitorear métricas → D2 (no D1, D3, D4)
    - Priorizar backlog → D3 (no D1, D2, D4)
    - Ejecutar sprint → D4 (no D1, D2, D3)
    
  Casos_Ambiguos_Resueltos:
    
    "Contratar persona":
      - Decidir contratar → D3 (decisión iniciativa)
      - Definir rol/salary → D1 (estructura)
      - Ejecutar hiring process → D4 (operación)
      - Trackear candidate pipeline → D2 (observación)
      Descompone en 4 actividades, cada una dominio claro
      
    "Lanzar feature":
      - Decidir feature en roadmap → D3
      - Asignar team → D1
      - Monitorear desarrollo → D2
      - Codear/deployar → D4
      Descompone claramente
      
  Propiedad: Actividades complejas descomponibles en sub-actividades,
            cada sub-actividad mapea a exactamente 1 dominio ✓

Composición_Temporal:

  Dominios operan en diferentes cadencias:
  
  D1_Arquitectura:
    Cambios: Trimestral a anual
    Estabilidad: Alta (estructura no cambia diario)
    Trigger: Growth, performance issues, strategy shifts
    
  D2_Percepción:
    Operación: Continua (24/7)
    Refresh: Tiempo real (alerts) a mensual (reports)
    Estabilidad: Media (observables cambian con contexto)
    
  D3_Decisión:
    Operación: Semanal (sprint planning) a trimestral (OKR setting)
    Estabilidad: Media (prioridades ajustan con info)
    Trigger: Percepción signals (D2), capacity changes (D1)
    
  D4_Operación:
    Operación: Continua (delivery diario)
    Estabilidad: Baja (ejecución constante)
    Dependencia: Estructura (D1), dirección (D3)
    
  Relación_Frecuencia:
    D4 (más frecuente) → D3 → D2 → D1 (menos frecuente)
    
    Justificación:
      - Estructura (D1) es cimiento (no cambia seguido)
      - Operación (D4) es actividad diaria (alta frecuencia)
      - Decisión (D3) ajusta según ejecución
      - Percepción (D2) monitorea constante pero análisis periódico

Health_Score_Organizacional:

  [GENOMA] Concepto_Health_Integrado:
    
    Definición:
      "∃ función health_org: (health_D1 × health_D2 × health_D3 × health_D4 × health_humano) → [0,1]
       que integra salud multi-dimensional organizacional."
       
    Propiedades_Requeridas:
      P1_Composicionalidad: H_org agrega health por dominio
      P2_Humano_Crítico: Refleja I5 (Primacía Humana) con peso significativo
      P3_Constraint_Transformación: H_org < H_min → bloquear transformaciones
      P4_Invariantes_Acoplamiento:
        - Health_Humano muy bajo → ceiling H_org (org burned out)
        - Health_Arquitectura bajo → ceiling H_org (estructura disfuncional)
        
    Fundamentación:
      - Ver 07_ecuacion_maestra: V_org maximización require H_org ≥ H_min
      - Correlación empírica: H_org ↔ retention, velocity, quality, NPS
      
  [FENOTIPO] H_org_Implementación_Recomendada:
    
    Fórmula_Sugerida_5D:
      H_org = weighted_avg(
        H1_Humano       × 30%,  # Bienestar, engagement, desarrollo, autonomía
        H2_Arquitectura × 25%,  # Estructura, boundaries, alignment (A_Score)
        H3_Flujo        × 20%,  # Eficiencia value streams, waste minimization
        H4_Percepción   × 15%,  # Observable coverage, freshness (P_Score)
        H5_Decisión     × 10%   # OKR velocity, portfolio balance (D_Score)
      )
      
    Pesos_Justificación:
      - H1_Humano 30%: People-first (I5 Primacía Humana)
      - H2_Arquitectura 25%: Estructura habilita todo
      - H3_Flujo 20%: Delivery efficiency crítico
      - H4_Percepción 15%: Observability habilita decisiones
      - H5_Decisión 10%: Dirección importante, ejecución domina
      
    NOTA: Pesos son CONFIGURABLES según valores org y contexto industria
      
    Variante_Simplificada_4D (orgs iniciando):
      H_org_simple = weighted_avg(
        H2_Arquitectura × 30%,
        H3_Flujo        × 35%,
        H4_Percepción   × 20%,
        H5_Decisión     × 15%
      )
      Evolución: Añadir H1_Humano cuando surveys implementados (3-6 meses)
      
    Interpretación_Típica:
      H_org > 80: Elite (top 10% industry)
      H_org 70-80: High performing
      H_org 60-70: Functional (mejoras necesarias)
      H_org 50-60: Struggling (intervención urgente)
      H_org < 50: Crisis (disfuncional)
      
    Invariantes_Implementación (enforcement constraints genoma):
    
      INV_Humano_Ceiling:
        IF H1_Humano < 50 THEN H_org = min(H_org, 60)
        Rationale: "Burnout organization cannot score >60 total"
      
      INV_Arquitectura_Base:
        IF H2_Arquitectura < 60 THEN H_org = min(H_org, 70)
        Rationale: "Disfuncional structure limits ceiling"
      
      INV_Transformación:
        H_min_default = 70
        IF H_org < 70 THEN block(transformaciones_mayores)
        Rationale: "Organización enferma no soporta cambio estructural"
      
  Interpretación_Niveles:
    H_org ≥ 85: Elite (top 10% industry)
    H_org 70-84: Healthy (functional, mejora continua)
    H_org 60-69: At-Risk (intervención focalizada requerida)
    H_org < 60: Critical (modo recovery obligatorio)
      
  Correlaciones_Teóricas:
    - H_org correlaciona con retention (r>0.7)
    - H_org correlaciona con velocity (r>0.6)
    - H_org anti-correlaciona con incidents (r<-0.5)
```

**Referencia cruzada:** ver PARTE VII (Ecuación Maestra) para el uso operativo de **H_org ≥ 70** como restricción de salud en decisiones de inversión.
