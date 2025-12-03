# PARTE II: DERIVACIÓN DE PRIMITIVOS

>5 Primitivos Necesarios y Suficientes (P1-P5)

> **Etiquetado Genoma/Fenotipo**: Este documento es mayormente [GENOMA] (derivación P1-P5, formas abstractas). Ejemplos ilustrativos pueden mencionar valores fenotipo (ej: M3_Habilitar) como casos concretos, pero valores M1-M6 se definen en I5_[FENOTIPO]. Ver §0.1 en 00_introduccion.md.

- [PARTE II: DERIVACIÓN DE PRIMITIVOS](#parte-ii-derivación-de-primitivos)
  - [§1. METODOLOGÍA DE DERIVACIÓN](#1-metodología-de-derivación)
  - [§2. PRIMITIVO P1: CAPACIDAD](#2-primitivo-p1-capacidad)
  - [§2.5. RESOLUCIÓN TERMINOLÓGICA: ACTOR vs AGENTE vs CAPACIDAD](#25-resolución-terminológica-actor-vs-agente-vs-capacidad)
  - [§3. PRIMITIVO P2: FLUJO](#3-primitivo-p2-flujo)
  - [§4. PRIMITIVO P3: INFORMACIÓN](#4-primitivo-p3-información)
  - [§5. PRIMITIVO P4: LÍMITE](#5-primitivo-p4-límite)
  - [§6. PRIMITIVO P5: PROPÓSITO](#6-primitivo-p5-propósito)

## §1. METODOLOGÍA DE DERIVACIÓN

```yaml
Principio_Derivación:
  "Cada primitivo es la MÍNIMA estructura necesaria 
   para operacionalizar su axioma correspondiente"

Criterios_Validación:
  1. Necesidad: ¿Primitivo es mínimo requerido por axioma?
  2. Suficiencia: ¿Primitivo captura todo lo que axioma implica?
  3. Ortogonalidad: ¿Primitivo independiente de otros?
  4. Operabilidad: ¿Primitivo tiene propiedades medibles?
```

## §2. PRIMITIVO P1: CAPACIDAD

```yaml
Derivación_Desde_A2:
  Axioma: "Existe capacidad que efectúa transformación"
  
  Pregunta_Ontológica: ¿Qué propiedades MÍNIMAS define una capacidad?
  
  Respuesta:
    1. Tipo_Capacidad: ¿QUÉ puede hacer?
    2. Sustrato: ¿QUIÉN/QUÉ lo hace?
    3. Rol_Valor: ¿PARA QUÉ (producción vs habilitación)?

Propiedad_1_Tipo_Capacidad:
  
  Análisis:
    Capacidades difieren en NIVEL COGNITIVO requerido
    
    Evidencia_Empírica:
      - RPA bot ejecuta sin decidir (mecánico)
      - ML model decide dentro reglas (decisional)
      - Arquitecto reflexiona sobre estructura (meta-cognitivo)
      - Estratega reflexiona sobre cómo reflexionar (meta-meta-cognitivo)
      
  Fundamentación_Teórica:
    - TSTI (Smartness Grades 0-4): Espectro capacidad cognitiva
    - Meyer (Niveles Decisionales 1-5): Jerarquía decisión
    - Alter (IS Roles R1-R6): Desde monitor hasta ejecutar
    
  Clasificación_Minimal:
    C0_Ejecutar: Transformación sin decisión
      - Definición: Aplicar regla determinista
      - Ejemplos: RPA, sensor, actuador, operario tarea mecánica
      - Cycle: Solo ACT (sin Sense ni Decide)
      
    C1_Decidir: Elección entre opciones según criterio
      - Definición: Evaluar alternativas y seleccionar
      - Ejemplos: Supervisor, ML model, rule engine, LLM (M2-M4)
      - Cycle: SENSE-DECIDE-ACT completo (scope local)
      
    C2_Reflexionar: Observar operación propia y ajustar
      - Definición: Metacognición sobre procesos propios
      - Ejemplos: Manager, arquitecto, RL agent, AutoML
      - Cycle: SDA recursivo (nivel 2) - observa SDA nivel 1
      
    C3_Meta_Reflexionar: Observar cómo reflexiona y evolucionar
      - Definición: Meta-metacognición sobre reflexión
      - Ejemplos: Executive, estratega, AGI (futuro hipotético)
      - Cycle: SDA recursivo (nivel 3) - observa SDA nivel 2
      
  Validación_Completitud:
    ¿Falta nivel cognitivo? 
    - C(-1)? NO - por debajo de C0 no hay transformación controlada
    - C4? POSIBLE pero fuera de alcance empírico actual
    
    Límite_3_Niveles_Recursión:
      - SDA se limita a 3 niveles de profundidad por practicidad
      - Corresponde a C0 (base) + C1 + C2 + C3 = 4 niveles
      - Justificación: Límite cognitivo humano (Miller 7±2)
      
  Validación_Ortogonalidad:
    ¿C0-C3 son ortogonales? SÍ
    - C0 ⊄ C1 (ejecutar ≠ decidir)
    - C1 ⊄ C2 (decidir ≠ reflexionar sobre decisión)
    - C2 ⊄ C3 (reflexionar ≠ reflexionar sobre reflexión)
    
    Pero: C(n+1) INCLUYE capacidades C(n)
    - C3 PUEDE ejecutar, decidir, reflexionar
    - C2 PUEDE ejecutar, decidir
    - C1 PUEDE ejecutar
    
    Relación: C3 ⊃ C2 ⊃ C1 ⊃ C0 (inclusión capacidades)

Propiedad_2_Sustrato:
  
  Análisis:
    Capacidad cognitiva INDEPENDIENTE de sustrato físico
    
    Evidencia:
      - Humano C0 (operario mecánico) ≠ Humano C3 (CEO)
      - Algorítmico C0 (sensor) ≠ Algorítmico C1 (LLM)
      - Mismo sustrato, diferente capacidad cognitiva
      
  Clasificación_Minimal:
    Sustrato ∈ {Humano, Algorítmico, Mecánico, Mixto}
    
    Humano:
      - Ventajas: Juicio contextual, creatividad, ética
      - Límites: Cognitive load, bias, disponibilidad
      
    Algorítmico:
      - Ventajas: Escala, velocidad, consistencia
      - Límites: Datos, scope definido, no generaliza fuera dominio
      
    Mecánico:
      - Ventajas: Fuerza, precisión, 24/7
      - Límites: Solo C0, no adapta
      
    Mixto:
      - Ejemplo: Ciborg, human-in-the-loop system
      - Poco común, modelar como composición capacidades
      
  Ortogonalidad_Sustrato_Capacidad:
    Sustrato ⊥ Tipo_Capacidad
    
    Matriz_Posible:
    |           | C0 | C1 | C2 | C3 |
    |-----------|----|----|----|----|
    | Humano    | ✓  | ✓  | ✓  | ✓  |
    | Algorítm. | ✓  | ✓  | ○  | ○  |
    | Mecánico  | ✓  | ○  | ✗  | ✗  |
    
    ✓ = Común, ○ = Emergente/raro, ✗ = No observado
    
    Implicación: 
      Sustrato y Capacidad son dimensiones INDEPENDIENTES
      → Primitivo debe tener AMBOS atributos

Propiedad_3_Rol_Valor:
  
  Análisis:
    Componente organizacional tiene ROL en flujo de valor
    
    Confusión_Fundamental (de tus reflexiones):
      "Se confunde la operación entre lo que es producción 
       de lo que es habilitación"
       
    Problema:
      - Software puede ser producto (SaaS) o herramienta (CI/CD)
      - Data pipeline puede ser core (fintech) o support (retail)
      - NO es propiedad INHERENTE, es CONTEXTUAL
      
  Fundamentación_Teórica:
    - Alter WST (IS Roles): IS puede ser desde monitor hasta ejecutor
    - Organism EA (3+1 Model): Shop/Factory = Producción, Warehouse/Mgmt = Habilitación
    - Kelly (Product vs Platform): Mismo artefacto, diferente rol
    
  Clasificación_Minimal:
    Rol ∈ {Producción, Habilitación}
    
    Producción:
      - Definición: En flujo DIRECTO a destinatario valor
      - Test: ¿Destinatario pagaría por esto directamente?
      - Ejemplos: Feature de producto, consultoría entregable
      
    Habilitación:
      - Definición: AMPLIFICA capacidad de otros componentes
      - Test: ¿Su valor es indirecto vía componente producción?
      - Ejemplos: CI/CD, monitoring, plataforma interna
      
  Propiedad_Contextual:
    Rol = f(Organización, Flujo_Valor)
    
    Ejemplo_Stripe_API:
      - En Fintech: Producción (core revenue generator)
      - En Retail: Habilitación (permite checkout)
      
    Implicación:
      - Rol NO es propiedad inherente
      - Rol se ASIGNA según contexto organizacional
      - Mismo componente puede reclasificarse

Definición_Formal_P1:

  Capacidad := (capacity_type, substrate, rol, propiedades_operativas)
  
  Donde:
    capacity_type ∈ {C0, C1, C2, C3}
    substrate ∈ {Humano, Algorítmico, Mecánico, Mixto}
    rol ∈ {Producción, Habilitación}
    propiedades_operativas = {
      availability: Boolean,
      throughput: ℝ⁺,
      latency: ℝ⁺,
      cost_per_hour: ℝ⁺
    }
    
  Relaciones:
    IF substrate = Algorítmico THEN ∃ Capacidad_Humana responsable
      (Fundamenta Invariante I5: HAIC/Primacía humana)
      
    IF capacity_type = C(n) THEN puede ejecutar operaciones C(0..n)
      (Inclusión capacidades)

Validación_P1:
  
  ✓ Necesidad: Sin capacity_type, substrate, rol → capacidad no caracterizable
  ✓ Suficiencia: 3 propiedades capturan todo aspecto capacidad
  ✓ Ortogonalidad: Las 3 dimensiones son independientes
  ✓ Operabilidad: Todas propiedades medibles/asignables
```

## §2.5. RESOLUCIÓN TERMINOLÓGICA: ACTOR vs AGENTE vs CAPACIDAD

```yaml
Problema_Ontológico:
  En fuentes y literatura, términos "Actor", "Agente", "Capacidad" usados
  ambiguamente y con solapamiento semántico.
  
  Objetivo: Establecer relación formal y eliminar ambigüedad.

Decisión_Arquitectural:

  Primitivo_Único:
    P1: CAPACIDAD (único primitivo nivel agencia)
    
  Conceptos_Derivados:
    Actor := Clasificación de Capacidad por sustrato
    Agente := Clasificación de Capacidad por cognición
    
  ⚠️ NI Actor NI Agente son primitivos separados
     Son PERSPECTIVES sobre el mismo primitivo P1

Formalización_Relaciones:

  Capacidad ::= (capacity_type, substrate, rol, propiedades)
    - Es el PRIMITIVO (P1, derivado de A2)
    - Captura TODO lo necesario para agencia
    
  Actor ::= Vista_Sustrato(Capacidad)
    - Pregunta: ¿QUIÉN ejecuta?
    - Clasificación: substrate ∈ {Humano, Algorítmico, Mecánico}
    - Uso: Cuando enfoque es en QUIÉN (identidad física)
    
  Agente ::= Vista_Cognitiva(Capacidad)
    - Pregunta: ¿QUÉ NIVEL de decisión?
    - Clasificación: capacity_type ∈ {C0, C1, C2, C3}
    - Restricción: Agente ⟺ capacity_type ≥ C1
    - Uso: Cuando enfoque es en CAPACIDAD DECISIONAL
    
  Relación_Formal:
    Actor(substrate=s) = {c ∈ Capacidad | c.substrate = s}
    Agente = {c ∈ Capacidad | c.capacity_type ≥ C1}
    
    Ejemplo:
      "Actor Humano" = Capacidad(substrate=Humano, capacity_type=cualquiera)
      "Agente Humano" = Capacidad(substrate=Humano, capacity_type≥C1)
      
      Todo humano es Actor (tienen sustrato humano)
      La mayoría humanos son Agentes (capacity_type ≥ C1, deciden)
      Algunos humanos son solo Ejecutores si capacity_type=C0 (tareas mecánicas)

Matriz_Ontológica:

  Tabla_Clarificación:
    ┌──────────────┬─────────────────────────────────────────────┐
    │ Concepto     │ Status Ontológico                           │
    ├──────────────┼─────────────────────────────────────────────┤
    │ CAPACIDAD    │ ✓ PRIMITIVO (P1, fundamental)              │
    │ Actor        │ ○ Derivado (vista por sustrato)            │
    │ Agente       │ ○ Derivado (vista por cognición)           │
    │ Ejecutor     │ ○ Derivado (Capacidad con C0)              │
    │ Decisor      │ ○ Derivado (Capacidad con C1)              │
    │ Reflexionador│ ○ Derivado (Capacidad con C2-C3)           │
    └──────────────┴─────────────────────────────────────────────┘
    
  Ortogonalidad_Vistas:
    Actor ⊥ Agente (dimensiones independientes)
    
    Prueba:
      - Actor Humano puede ser Agente (C1+) o Ejecutor (C0)
      - Actor Algorítmico puede ser Agente (C1+) o Ejecutor (C0)
      → Sustrato NO determina cognición
      
    Implicación:
      Sistema modela AMBAS dimensiones en Capacidad
      NO necesita primitivos separados

Ejemplos_Concretos:

  Caso_1_Developer:
    Capacidad(
      capacity_type = C2 (Reflexiona sobre código/arquitectura),
      substrate = Humano,
      rol = Producción (si software es producto) | Habilitación (si internal tool),
      propiedades = {throughput: 5 stories/sprint, ...}
    )
    
    Perspectiva Actor: "Actor Humano developer"
    Perspectiva Agente: "Agente decisional nivel C2"
    
  Caso_2_LLM_Copilot:
    Capacidad(
      capacity_type = C1 (Decide sugerencias dentro prompt),
      substrate = Algorítmico,
      rol = Habilitación (asiste developers),
      propiedades = {latency: 200ms, bounded_autonomy: M3, ...}
    )
    
    Perspectiva Actor: "Actor Algorítmico LLM"
    Perspectiva Agente: "Agente IA nivel C1"
    
  Caso_3_RPA_Bot:
    Capacidad(
      capacity_type = C0 (Solo ejecuta sin decidir),
      substrate = Algorítmico,
      rol = Habilitación (automatiza data entry),
      propiedades = {throughput: 1000 forms/hora, ...}
    )
    
    Perspectiva Actor: "Actor Algorítmico bot"
    Perspectiva Agente: NO ES AGENTE (C0 no decide)
    Término correcto: "Ejecutor mecánico"
    
  Caso_4_CEO:
    Capacidad(
      capacity_type = C3 (Meta-reflexiona sobre estrategia),
      substrate = Humano,
      rol = Habilitación (direcciona pero no produce directamente),
      propiedades = {decision_scope: organizacional, ...}
    )
    
    Perspectiva Actor: "Actor Humano C-level"
    Perspectiva Agente: "Agente estratégico nivel C3"

Uso_Recomendado:

  En_Arquitectura:
    Usar "Capacidad" (término técnico preciso)
    
  En_Conversación_Técnica:
    Usar "Actor" cuando enfoque es QUIÉN
    Usar "Agente" cuando enfoque es COGNICIÓN
    
  En_Documentación:
    Aclarar contexto: "Actor Humano" vs "Agente C1"
    
  En_Código:
    Entidad base: Capacity
    Filtros: capacity.substrate, capacity.capacity_type
    NO crear clases separadas Actor/Agente

Validación_Decisión:

  ✓ Necesidad: Capacidad captura TODO lo requerido por A2
  ✓ Suficiencia: Actor y Agente derivables de Capacidad
  ✓ Ortogonalidad: Capacidad ortogonal a otros primitivos P2-P5
  ✓ Parsimonia: 1 primitivo vs múltiples (Occam's razor)
  ✓ Expresividad: Todos casos de uso modelables
  
  Conclusión: Decisión arquitectural validada ✓
```

---

## §3. PRIMITIVO P2: FLUJO

```yaml
Derivación_Desde_A1:
  Axioma: "Existe transformación que cambia estado S₁ → S₂"
  
  Pregunta_Ontológica: ¿Qué estructura MÍNIMA modela transformación?
  
  Respuesta:
    1. Secuencia_Pasos: Orden transformaciones
    2. Vinculación_Capacidades: QUÉ ejecuta cada paso
    3. Información_Procesada: Input/Output de cada paso

Propiedad_1_Secuencia:
  
  Análisis:
    Transformación organizacional rara vez es atómica
    - Orden importa: CleanData → Train ≠ Train → CleanData
    - Composición: Flujos componen de sub-flujos
    
  Estructura_Minimal:
    Flujo = DAG (Directed Acyclic Graph)
    
    Nodos = Steps (transformaciones atómicas)
    Edges = Dependencias (información fluye)
    
    Propiedades:
      - Directed: Orden temporal
      - Acyclic: No loops infinitos (práctica, no teórico)
      - Permite paralelismo: Steps sin dependencia → paralelos
      
  Fundamentación:
    - Alter WST: "Activities = conjunto pasos ordenados"
    - TSTI: "Process = secuencia coordinada actividades"
    - BPA (fuentes): Orchestration patterns (BPMN, saga)

Propiedad_2_Vinculación_Capacidades:
  
  Análisis:
    Cada step requiere capacidad que lo ejecute
    
    Step := (input, capacity, output)
    
    Donde:
      input: Información requerida
      capacity: Capacidad que transforma
      output: Información producida
      
  Handoff:
    Definición: Step donde capacity(step_i) ≠ capacity(step_{i+1})
    
    Propiedad_Crítica:
      Handoffs son costosos (Meyer: Minimize Handoffs)
      
    Métrica:
      Handoff_Ratio = #Handoffs / #Steps
      Target: < 20% (Kelly + Meyer)

Propiedad_3_Rol_Valor:
  
  Análisis:
    Flujo (como Capacidad) tiene rol contextual
    
  Clasificación:
    Flujo_Producción: Entrega valor a destinatario
    Flujo_Habilitación: Amplifica otros flujos
    
  Ejemplo:
    OrderFulfillment: Producción (cliente recibe producto)
    CI/CD_Pipeline: Habilitación (permite deploy features)

Definición_Formal_P2:

  Flujo := (steps, dependencies, rol, propiedades_operativas)
  
  Donde:
    steps: List<Step>
    Step := (capacity, input_info, output_info, is_handoff)
    dependencies: DAG sobre steps
    rol ∈ {Producción, Habilitación}
    propiedades_operativas = {
      avg_cycle_time: ℝ⁺,
      throughput: ℝ⁺,
      handoff_ratio: [0, 1]
    }
    
  Invariante:
    ∀ step_i: step_i.output_info compatible con step_{i+1}.input_info
    (Type safety en composición)

Validación_P2:
  
  ✓ Necesidad: Sin steps/dependencies → no hay secuencialidad
  ✓ Suficiencia: DAG + capacidades captura toda transformación posible
  ✓ Ortogonalidad: Flujo ⊥ Capacidad (flujo USA capacidad, no ES capacidad)
  ✓ Operabilidad: Cycle time, throughput, handoffs medibles
```

## §4. PRIMITIVO P3: INFORMACIÓN

```yaml
Derivación_Desde_A3:
  Axioma: "Existe estructura portadora significado que coordina transformaciones"
  
  Pregunta_Ontológica: ¿Qué estructura MÍNIMA modela información?
  
  Respuesta:
    1. Contenido: Qué información es
    2. Tipo: Persistente, Transitoria, Agregada
    3. Temporal: Cuándo válida

Unificación_Conceptual:
  
  Principio:
    Dato, Señal y Estado son manifestaciones temporales de un mismo concepto: Información
    - Diferencia es PROPIEDAD temporal, NO naturaleza ontológica
    
  Modelado:
    UN primitivo (Información) + propiedad temporal
    
    Información := (schema, persistencia, temporal_properties)
    
  Solución:
    UN primitivo "Información" con atributo tipo

Propiedad_1_Tipo_Información:
  
  Persistente:
    - Definición: Almacenada indefinidamente
    - Ejemplos: Customer record, transaction log, documento
    - Validity: Infinita (hasta que se elimine explícitamente)
    - Tipo: Dato
    
  Transitoria:
    - Definición: Relevante solo en ventana temporal
    - Ejemplos: Click event, sensor reading, webhook
    - Validity: Segundos/minutos
    - Tipo: Señal
    - Propiedad_Adicional: puede tener trigger semántico
    
  Agregada:
    - Definición: Consolidación múltiples informaciones en T
    - Ejemplos: Dashboard, report, system snapshot
    - Validity: Depende de freshness componentes
    - Tipo: Estado

Propiedad_2_Temporal:
  
  Atributos:
    timestamp: Cuándo se capturó/generó
    validity_period: Cuánto tiempo válida (puede ser ∞)
    expires_at: timestamp + validity_period
    
  Freshness:
    age = now() - timestamp
    is_fresh = age < validity_period
    
  Fundamentación:
    - Data Quality (fuentes): Freshness como dimensión calidad
    - Event-Driven (fuentes): TTL en mensajes
    - TSTI: Temporal validity de Knowledge Objects

Propiedad_3_Trazabilidad:
  
  Lineage:
    Información tiene origen rastreable
    
  Atributos:
    produced_by_flow: Qué flujo la generó
    produced_by_capacity: Qué capacidad la generó
    lineage_parents: Lista información que la generó (DAG)
    
  Fundamentación:
    - Data Lineage (OpenLineage): Trazabilidad producción datos
    - Invariante I3: Trazabilidad obligatoria

Definición_Formal_P3:

  Información := (content, information_type, temporal, lineage)
  
  Donde:
    content: Estructura semántica (schema-aware)
    information_type ∈ {Persistente, Transitoria, Agregada}
    temporal := (timestamp, validity_period, expires_at)
    lineage := (produced_by_flow, produced_by_capacity, parent_ids)
    
  Invariante:
    IF information_type = Transitoria THEN validity_period < ∞
    IF information_type = Agregada THEN |parent_ids| > 1

Validación_P3:
  
  ✓ Necesidad: Sin tipo/temporal/lineage → información no caracterizable
  ✓ Suficiencia: Unifica Dato + Señal + Estado (reducción 3→1)
  ✓ Ortogonalidad: Información ⊥ {Capacidad, Flujo} (transforman/procesan información)
  ✓ Operabilidad: Freshness, lineage, tipo son medibles/rastreables
```

## §5. PRIMITIVO P4: LÍMITE

```yaml
Derivación_Desde_A4:
  Axioma: "No todo es posible en todo momento. 
           Existen restricciones que acotan espacio de posibilidades"
  
  Pregunta_Ontológica: ¿Qué estructura MÍNIMA modela restricción?
  
  Respuesta:
    1. Tipo_Límite: Origen/naturaleza restricción
    2. Scope: Qué componentes afecta
    3. Enforcement: Cómo se aplica

Análisis:
  
  Validación:
    ✓ Irreducible (no derivable de otros primitivos)
    ✓ Ortogonal (límite ≠ capacidad, flujo, información)
    ✓ Necesario (sin límites, espacio infinito no operable)
    
  Decisión: PRESERVAR de KERNEL con refinamientos menores

Propiedad_1_Tipo_Límite:
  
  Clasificación_Fundamental:
    
    Físico:
      - Origen: Leyes naturales, geografía, biología
      - Ejemplos: Velocidad luz, horas/día, distancia física
      - Modificable: NO (inmutable)
      - Severidad: Critical (violación imposible, no solo indeseable)
      
    Regulatorio:
      - Origen: Leyes, normas, compliance (GDPR, SOX, HIPAA)
      - Ejemplos: Data residency, retención docs, auditoría
      - Modificable: NO dentro organización (requiere cambio externo)
      - Severidad: Critical-Error (violación tiene consecuencias legales)
      
    Organizacional:
      - Origen: Políticas internas, governance, autoridad
      - Ejemplos: Approval workflows, RACI, presupuestos
      - Modificable: SÍ (decisión interna)
      - Severidad: Error-Warning (violación controlable)
      
    Económico:
      - Origen: Presupuesto, costo oportunidad, ROI
      - Ejemplos: Budget cap, pricing, resource allocation
      - Modificable: SÍ con justificación (business case)
      - Severidad: Warning-Info (violación evaluable)
      
    Técnico:
      - Origen: Arquitectura, infraestructura, capacidad técnica
      - Ejemplos: API rate limits, storage capacity, latencia
      - Modificable: SÍ con inversión (escalar infra)
      - Severidad: Error-Warning (violación degradativa)
      
  Fundamentación_Teórica:
    - Alter WST: "Environment constraints: regulatorios, competitivos, físicos"
    - Meyer: "Anti-interferencia = límites estructurales preservan coherencia"
    - TSTI: "Constraints = límites físicos + organizacionales + económicos"

Propiedad_2_Scope:
  
  Análisis:
    Límite aplica a qué componentes del sistema
    
  Granularidad:
    Global: Todo el sistema
    Dominio: Arquitectura | Percepción | Decisión | Operación
    Flujo: Flujo específico
    Capacidad: Capacidad específica
    Información: Tipo información específica
    
  Ejemplo_GDPR:
    - Tipo: Regulatorio
    - Scope: Información (tipo=PersonalData)
    - Enforcement: Data governance policies
    
  Ejemplo_Budget:
    - Tipo: Económico
    - Scope: Flujo (tipo=Habilitación)
    - Enforcement: Approval workflow si costo > threshold

Propiedad_3_Enforcement:
  
  Mecanismos:
    
    Preventivo:
      - Definición: Bloquea acción ANTES de violar
      - Ejemplos: Type checker, authorization gates, circuit breaker
      - Ventaja: Violación imposible
      - Costo: Rigidez, puede bloquear casos válidos edge
      
    Detectivo:
      - Definición: Detecta violación DESPUÉS, alerta
      - Ejemplos: Monitoring, audit logs, anomaly detection
      - Ventaja: Flexibilidad
      - Costo: Violación ya ocurrió, requiere corrección
      
    Correctivo:
      - Definición: Rollback o compensación automática
      - Ejemplos: Saga compensation, circuit breaker, auto-scaling
      - Ventaja: Self-healing
      - Costo: Complejidad implementación
      
  Severidad_Determina_Enforcement:
    Critical → Preventivo obligatorio
    Error → Preventivo + Detectivo
    Warning → Detectivo + Correctivo
    Info → Detectivo (logging)

Propiedad_4_Transversalidad:
  
  Observación_Crítica:
    Security NO es dominio (D5), es Límite transversal
    
  Justificación:
    - Security = conjunto límites (authn, authz, encryption, audit)
    - Security NO es responsabilidad única (todos dominios tienen security)
    - Security aplica a TODOS primitivos:
      * Capacidad: Control acceso, least privilege
      * Flujo: Secure transmission, authorization gates
      * Información: Encryption, privacy, retention
      * Límite: Security policies enforcement
      * Propósito: Security objectives (compliance OKRs)

Definición_Formal_P4:

  Límite := (limit_type, scope, enforcement, severidad, propiedades)
  
  Donde:
    limit_type ∈ {Físico, Regulatorio, Organizacional, Económico, Técnico}
    scope: Granularidad aplicación
    enforcement ∈ {Preventivo, Detectivo, Correctivo}
    severidad ∈ {Info, Warning, Error, Critical}
    propiedades := {
      source: Origen límite (ley, policy, constraint),
      modifiable: Boolean,
      violation_count: ℕ,
      active: Boolean
    }
    
  Relación_Severidad_Enforcement:
    IF severidad = Critical THEN enforcement MUST include Preventivo
    IF severidad = Info THEN enforcement = Detectivo ONLY

Validación_P4:
  
  ✓ Necesidad: Sin límites, espacio infinito no operable
  ✓ Suficiencia: 5 tipos + scope + enforcement capturan todas restricciones
  ✓ Ortogonalidad: Límite ⊥ {Capacidad, Flujo, Información, Propósito}
  ✓ Operabilidad: Violaciones, severidad, enforcement medibles
```

## §6. PRIMITIVO P5: PROPÓSITO

```yaml
Derivación_Desde_A5:
  Axioma: "Transformación organizacional tiene propósito: 
           existe outcome deseado que direcciona acción"
  
  Pregunta_Ontológica: ¿Qué estructura MÍNIMA modela intencionalidad?
  
  Respuesta:
    1. Outcome_Deseado: Qué se busca lograr
    2. Métrica: Cómo medir progreso
    3. Jerarquía: Alineación propósitos individuales ↔ organizacionales

Justificación_Como_Primitivo:
  
  Necesidad_Ontológica:
    Propósito es fundamental porque:
    - Distingue organización de caos browniano
    - Es el "PARA QUÉ" que justifica el "QUÉ" (transformación)
    - NO derivable de otros primitivos
    
  Capacidades_Habilitadas:
    Con Propósito como primitivo es posible:
    - Alinear capacidades con objetivos formalmente
    - Evaluar si flujo sirve propósito
    - Detectar trabajo sin propósito claro
    - Rastrear progreso hacia outcomes

Propiedad_1_Outcome_Deseado:
  
  Estructura_Minimal:
    Propósito define estado futuro deseado
    
  Componentes:
    Objetivo: Descripción cualitativa (qué lograr)
    Target_Value: Cuantificación (cuánto lograr)
    Current_Value: Estado actual
    Gap: Target - Current
    
  Ejemplo_OKR:
    Objetivo: "Reducir churn de clientes enterprise"
    Key_Results:
      - KR1: Churn rate < 5% (current: 8%, target: 5%, gap: -3%)
      - KR2: NPS > 50 (current: 42, target: 50, gap: +8)
      - KR3: Retention 12M > 85% (current: 78%, target: 85%, gap: +7%)
      
  Fundamentación:
    - Kelly: "OKRs como mecanismo central dirección y ejecución"
    - Alter WST: "Value = evaluación outputs según criteria objetivos/subjetivos"
    - TSTI: "Evaluation Theory - multi-criteria assessment"

Propiedad_2_Jerarquía_Propósitos:
  
  Análisis:
    Propósitos se organizan en jerarquía
    - Propósito individual alineado con equipo
    - Propósito equipo alineado con unidad
    - Propósito unidad alineado con organización
    
  Estructura:
    parent_purpose_id: Propósito superior al que sirve
    child_purposes: Lista propósitos que contribuyen a este
    
  Ejemplo_Cascada:
    L4_Org: "Liderar mercado SaaS en América Latina"
      ↓
    L3_Unit: "Product: Lanzar 5 features enterprise Q1"
      ↓
    L2_Team: "Auth Team: Implementar SSO SAML"
      ↓
    L1_Individual: "Engineer: Completar SAML integration con Okta"
    
  Propiedad_Alineación:
    ∀ propósito_hijo: contribuye a propósito_padre
    
    Medible:
      Alignment_Score = Σ (peso_hijo × progreso_hijo) / Σ peso_hijo
      
  Fundamentación:
    - Kelly: "Vertical integration estrategia → código"
    - Meyer: "Jerarquía pull - cada nivel tira del superior"
    - Organism EA: "Outside-In - propósito cliente permea toda org"

Propiedad_3_Scope_Temporal:
  
  Scope_Organizacional:
    scope ∈ {Individual, Equipo, Unidad, Organización}
    
    Individual: OKR personal (ingeniero, manager)
    Equipo: OKR team (5-9 personas)
    Unidad: OKR department (50-200 personas)
    Organización: OKR company-wide
    
  Horizon_Temporal:
    horizon ∈ {Inmediato, Táctico, Estratégico}
    
    Inmediato: Días-semanas (sprint goals)
    Táctico: Meses-trimestre (quarterly OKRs)
    Estratégico: Años (annual strategy, visión 3-5Y)
    
  Relación_Scope_Horizon:
    Tendencia (no estricta):
      Individual → Inmediato-Táctico
      Equipo → Táctico
      Unidad → Táctico-Estratégico
      Organización → Estratégico
      
  Fundamentación:
    - Kelly: "Fractal consistency - mismos patterns diferentes escalas temporales"
    - Meyer: "5 niveles decisionales mapean a horizontes temporales"

Propiedad_4_Evaluación_Continua:
  
  Atributos_Operativos:
    current_value: Valor actual métrica
    target_value: Valor objetivo
    progress_pct: 100 × (current / target)
    status ∈ {Draft, Active, Completed, Abandoned, At_Risk}
    
  Reglas_Status:
    At_Risk: IF progress < 50% AND time_elapsed > 60% period
    Completed: IF progress ≥ 100%
    Abandoned: IF explicitly cancelled
    
  Refresh_Cadence:
    Inmediato: Actualización diaria
    Táctico: Actualización semanal
    Estratégico: Actualización mensual
    
  Fundamentación:
    - Kelly: "OKR check-ins semanales"
    - Agile: "Inspect & adapt - retrospectives, reviews"

Propiedad_5_Ownership:
  
  Análisis:
    Todo propósito tiene owner accountable
    
  Atributo:
    owner_capacity_id: Capacidad responsable
    
  Regla:
    IF scope = Individual THEN owner.substrate = Humano
    IF scope = Equipo THEN owner = Team (capacidad compuesta)
    
  Accountability:
    Owner puede delegar EJECUCIÓN (a algorítmico, otros humanos)
    Owner NO delega ACCOUNTABILITY (siempre humano último)
    
  Fundamentación:
    - Invariante I5: Primacía Humana (humano accountable)
    - Principio: Autoridad Única (1 accountable por decisión)
    - Meyer: "Autoridad = Responsabilidad (entangled)"

Definición_Formal_P5:

  Propósito := (objetivo, metrics, jerarquía, temporal, ownership)
  
  Donde:
    objetivo: String (descripción cualitativa)
    metrics := {
      target_value: ℝ,
      current_value: ℝ,
      progress_pct: [0, 100+],
      key_results: List<KeyResult>
    }
    jerarquía := {
      parent_purpose_id: UUID | null,
      child_purposes: List<UUID>
    }
    temporal := {
      scope ∈ {Individual, Equipo, Unidad, Organización},
      horizon ∈ {Inmediato, Táctico, Estratégico},
      start_date: Date,
      end_date: Date
    }
    ownership := {
      owner_capacity_id: UUID,
      status ∈ {Draft, Active, Completed, Abandoned, At_Risk}
    }
    
  Invariantes:
    IF parent_purpose_id ≠ null THEN ∃ Propósito(id=parent_purpose_id)
    ∀ child ∈ child_purposes: child.end_date ≤ this.end_date
    owner_capacity MUST be Humano (direct) OR Mixto (team con humano líder)

Validación_P5:
  
  ✓ Necesidad: Sin propósito, no hay criterio éxito (caos)
  ✓ Suficiencia: Objetivo + métricas + jerarquía + temporal capturan intencionalidad
  ✓ Ortogonalidad: Propósito ⊥ {Capacidad, Flujo, Información, Límite}
  ✓ Operabilidad: Progress, alignment, status medibles
  ✓ Fundamento_Teórico: Derivado de axioma A5, operacionalmente necesario
```

```yaml
Capacidad := (
  capacity_type,         # {C0, C1, C2, C3}
  substrate,             # {Humano, Algorítmico, Mecánico, Mixto}
  rol,                   # {Producción, Habilitación}
  propiedades_operativas: {
    availability: Boolean,
    throughput: number,
    latency: number,
    cost_per_hour: number,

    # HAIC / Delegación y trazabilidad (ver I5_HAIC)
    delegation_mode: DelegationMode?,        # Modo autonomía (valores en I5_[FENOTIPO])
    accountable_capacity_id: UUID?,          # FK Capacidad (Humano o Mixto)
    override_capability: boolean?,           # Humano puede cambiar decisiones
    override_channel: OverrideChannel?       # Mecanismo override (valores en I5_[FENOTIPO])
  }
)
```

```yaml
Flujo := (
  steps: List<Step>,
  dependencies: DAG(steps),    # DAG por ejecución
  rol: {Producción, Habilitación},
  propiedades_operativas: {
    avg_cycle_time: number,
    throughput: number,
    handoff_ratio: [0,1]
  }
)

Step := (
  capacity_id: UUID,                 # FK → Capacidad
  capacity_type_min: {C0, C1, C2, C3},   # valida R1
  input_info: List<InfoRef>,
  output_info: List<InfoRef>,
  is_handoff: boolean
)
```

```yaml
Información := (
  content, information_type, temporal, lineage
)

lineage := (
  produced_by_flow_id: UUID?,
  produced_by_capacity_id: UUID?,
  parent_info_ids: List<UUID>,
  source_kind: {internal, external},
  source_system: string?,
  source_org: string?
)
```
