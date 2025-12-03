# PARTE III: INVARIANTES Y AXIOMAS DERIVADOS

- [PARTE III: INVARIANTES Y AXIOMAS DERIVADOS](#parte-iii-invariantes-y-axiomas-derivados)
  - [§1. NATURALEZA DE LOS INVARIANTES](#1-naturaleza-de-los-invariantes)
  - [§2. INVARIANTE I1: MINIMALIDAD](#2-invariante-i1-minimalidad)
  - [§3. INVARIANTE I2: ORTOGONALIDAD](#3-invariante-i2-ortogonalidad)
  - [§4. INVARIANTE I3: TRAZABILIDAD](#4-invariante-i3-trazabilidad)
  - [§5. INVARIANTE I4: CLASIFICACIÓN CONTEXTUAL](#5-invariante-i4-clasificación-contextual)
  - [§6. INVARIANTE I5: HAIC (Human-AI Collaboration)](#6-invariante-i5-haic-human-ai-collaboration)
  - [§7. INVARIANTE I6: TRAJECTORY-AWARENESS](#7-invariante-i6-trajectory-awareness)
  - [§8. INVARIANTE I7: EMERGENCIA DE COMPLEJIDAD](#8-invariante-i7-emergencia-de-complejidad)
  - [§9. INVARIANTE I8: ADAPTACIÓN CONTEXTUAL](#9-invariante-i8-adaptación-contextual)
  - [§10. SÍNTESIS DE INVARIANTES](#10-síntesis-de-invariantes)

> 8 Propiedades Invariantes del Sistema (I1-I8)

## §1. NATURALEZA DE LOS INVARIANTES

```yaml
Definición_Invariante:
  "Propiedad que DEBE mantenerse verdadera en todo estado válido del sistema"
  
  Diferencia_con_Axioma:
    Axioma: Verdad fundamental NO derivable (base del sistema)
    Invariante: Propiedad derivable de axiomas que DEBE preservarse
    
  Rol_Operativo:
    Invariantes son CONSTRAINTS ejecutables
    - Validación: Rechazar estado que viola invariante
    - Diseño: Guiar decisiones arquitectónicas
    - Testing: Verificar corrección del sistema

Metodología_Derivación:
  1. Identificar propiedad necesaria para coherencia sistema
  2. Demostrar que deriva lógicamente de axiomas A1-A5
  3. Formalizar como constraint verificable
  4. Fundamentar en fuentes teóricas
```

## §2. INVARIANTE I1: MINIMALIDAD

```yaml
I1_MINIMALIDAD:
  Enunciado:
    "El sistema usa el mínimo número de primitivos necesarios y suficientes"
    
  Formulación_Formal:
    ∀ primitivo P ∈ {P1, P2, P3, P4, P5}:
      ¬∃ expresión(P) usando {P1...P5} \ {P}
      
    Traducción: Ningún primitivo es expresable como combinación de otros

Demostración_Necesidad:

  P1_Capacidad_irreducible:
    ¿Puede expresarse con {Flujo, Información, Límite, Propósito}?
    
    Argumento:
      - Flujo define SECUENCIA, no QUÉ ejecuta
      - Información define CONTENIDO, no quién procesa
      - Límite RESTRINGE, no habilita
      - Propósito DIRECCIONA, no ejecuta
      
    ∴ Capacidad NO derivable → Necesaria ✓
    
  P2_Flujo_irreducible:
    ¿Puede expresarse con {Capacidad, Información, Límite, Propósito}?
    
    Argumento:
      - Capacidad define POTENCIAL, no secuencia temporal
      - Información define CONTENIDO, no orden transformaciones
      - Límite + Propósito no implican secuencialidad
      
    ∴ Flujo NO derivable → Necesario ✓
    
  P3_Información_irreducible:
    ¿Puede expresarse con {Capacidad, Flujo, Límite, Propósito}?
    
    Argumento:
      - Capacidad sin información = potencial ciego
      - Flujo sin información = secuencia vacía (no observable)
      - Coordinación requiere información (A3)
      
    ∴ Información NO derivable → Necesaria ✓
    
  P4_Límite_irreducible:
    ¿Puede expresarse con {Capacidad, Flujo, Información, Propósito}?
    
    Argumento:
      - Capacidad + Flujo + Información no imponen restricciones inherentes
      - Propósito direcciona pero no restringe (puedes perseguir objetivo imposible)
      - Espacio acotado requiere límite explícito (A4)
      
    ∴ Límite NO derivable → Necesario ✓
    
  P5_Propósito_irreducible:
    ¿Puede expresarse con {Capacidad, Flujo, Información, Límite}?
    
    Argumento:
      - P1-P4 describen MECÁNICA (cómo), no TELEOLOGÍA (para qué)
      - Información puede describir propósito pero no ES el propósito
      - Sistema sin propósito = caos eficiente (A5)
      
    ∴ Propósito NO derivable → Necesario ✓

Demostración_Suficiencia:

  Tesis: P1-P5 pueden expresar TODO concepto organizacional
  
  Mapeo_Conceptos_Fundamentales:
    
    Humano → Capacidad(substrate=Humano)
    Máquina → Capacidad(substrate=Mecánico)
    IA → Capacidad(substrate=Algorítmico)
    
    Equipo → Capacidad(tipo=Compuesta, composición=⊕)
    Departamento → Capacidad(scope=Unidad)
    
    Proceso → Flujo(steps=[...])
    Pipeline → Flujo(tipo=Automatizado)
    Workflow → Flujo(tipo=Orquestado)
    
    Evento → Información(type=Transitoria)
    Documento → Información(type=Persistente)
    Métrica → Información(type=Agregada)
    
    Regulación → Límite(type=Regulatorio)
    Presupuesto → Límite(type=Económico)
    Política → Límite(type=Organizacional)
    
    Objetivo → Propósito(horizon=Táctico)
    Estrategia → Propósito(horizon=Estratégico, scope=Organización)
    Meta → Propósito(horizon=Inmediato)
    
  ∴ P1-P5 suficientes para modelar organizaciones ✓

Fundamentación_Teórica:
  - Ockham's Razor: "Entities should not be multiplied beyond necessity"
  - Category Theory: Minimal arrows/objects para completitud categorial
  - Systems Theory: Parsimonia en definición sistema
  
Validación_Operativa:
  CHECK: ∀ nuevo_concepto_organizacional, 
         ∃ expresión usando solo P1-P5
```

## §3. INVARIANTE I2: ORTOGONALIDAD

```yaml
I2_ORTOGONALIDAD:
  Enunciado:
    "Primitivos son mutuamente independientes sin overlap conceptual"

> **Nota de alcance (I2 vs R9).** La ortogonalidad afirma la *posibilidad ontológica* de un `Flujo` sin `Propósito` (independencia conceptual).
> El **modelo relacional** impone una *política de diseño* (R9): `Flujo.purpose_id NOT NULL` para asegurar teleología explícita.
> Ambas son coherentes si se distingue *posibilidad* vs *estado válido implementado*.

    
  Formulación_Formal:
    ∀ Pi, Pj ∈ {P1...P5}, i ≠ j:
      Pi ⊥ Pj ⟺ Pi puede variar independientemente de Pj
      
Demostración_Exhaustiva_Pares:

  P1_Capacidad ⊥ P2_Flujo:
    - Puede existir capacidad sin flujo (idle, disponible)
    - Puede existir flujo sin capacidad asignada (template abstracto)
    - Variar tipo capacidad (C0→C3) no cambia estructura flujo
    - Variar secuencia flujo no cambia capacidad ejecutora
    ✓ Ortogonales
    
  P1_Capacidad ⊥ P3_Información:
    - Puede existir capacidad sin información procesada (nueva, no usada)
    - Puede existir información sin capacidad que la procese (legacy, huérfana)
    - Variar tipo capacidad no determina contenido información
    - Variar información no determina capacidad requerida
    ✓ Ortogonales
    
  P1_Capacidad ⊥ P4_Límite:
    - Puede existir capacidad sin límites (ideal teórico)
    - Puede existir límite sin capacidad afectada (límite futuro, no aplicado)
    - Capacidad no CREA límites (límites son externos a capacidad)
    - Límite no OTORGA capacidad (solo restringe)
    ✓ Ortogonales
    
  P1_Capacidad ⊥ P5_Propósito:
    - Puede existir capacidad sin propósito asignado (disponible, sin misión)
    - Puede existir propósito sin capacidad para lograrlo (aspiración, visión)
    - Capacidad define POTENCIAL, propósito define DIRECCIÓN
    - Son dimensiones independientes
    ✓ Ortogonales
    
  P2_Flujo ⊥ P3_Información:
    - Puede existir flujo sin información específica (proceso genérico)
    - Puede existir información sin flujo que la produjo (dato externo)
    - Flujo define SECUENCIA, información define CONTENIDO
    - Cambiar orden flujo ≠ cambiar contenido información
    ✓ Ortogonales
    
  P2_Flujo ⊥ P4_Límite:
    - Puede existir flujo sin límites (ideal sin restricciones)
    - Puede existir límite sin flujo afectado (límite global, no aplicado aún)
    - Flujo no genera límites inherentemente
    - Límite solo RESTRINGE flujo, no lo define
    ✓ Ortogonales
    
  P2_Flujo ⊥ P5_Propósito:
    - Puede existir flujo sin propósito (mecánico, legacy sin owner)
    - Puede existir propósito sin flujo definido (objetivo sin plan)
    - Flujo define CÓMO, propósito define POR QUÉ
    - Son dimensiones complementarias pero independientes
    ✓ Ortogonales
    
  P3_Información ⊥ P4_Límite:
    - Puede existir información sin límites (ideal abierto)
    - Puede existir límite sin información específica (política abstracta)
    - Información ES (descripción estado), límite RESTRINGE (prescripción)
    ✓ Ortogonales
    
  P3_Información ⊥ P5_Propósito:
    - Puede existir información sin propósito (noise, dato no usado)
    - Puede existir propósito sin información completa (decisión con incertidumbre)
    - Información describe QUÉ ES, propósito prescribe QUÉ DEBE SER
    - Dimensión descriptiva vs normativa
    ✓ Ortogonales
    
  P4_Límite ⊥ P5_Propósito:
    - Puede existir límite sin propósito (ley física, constraint inevitable)
    - Puede existir propósito sin límites conocidos (visión audaz)
    - Límite RESTRINGE opciones, propósito SELECCIONA entre opciones
    - Son fuerzas complementarias pero independientes
    ✓ Ortogonales

Resultado:
  10 pares validados → Ortogonalidad total del sistema ✓

Fundamentación_Teórica:
  - Linear Algebra: Vectores ortogonales tienen producto punto = 0
  - Information Theory: Canales ortogonales no interfieren
  - Category Theory: Objetos distinguibles por morfismos únicos
  
Validación_Operativa:
  CHECK: Cambiar primitivo Pi no requiere cambiar Pj (i ≠ j)
```

## §4. INVARIANTE I3: TRAZABILIDAD

```yaml
I3_TRAZABILIDAD:
  Enunciado:
    "Toda transformación, decisión y artefacto tiene origen, responsable y justificación rastreables"
    
  Formulación_Formal:
    ∀ entidad E ∈ Sistema:
      ∃ metadata(E) = {
        created_by: Capacidad(substrate=Humano),
        created_at: Timestamp,
        reason: Propósito | Flujo,
        lineage: DAG(ancestros)
      }

Aplicación_Por_Primitivo:

  P1_Capacidad:
    Trazabilidad_Requerida:
      - created_by: Quién creó/definió capacidad
      - created_at: Cuándo se registró
      - IF substrate=Algorítmico THEN delegated_from: Capacidad(Humano)
      
    Justificación:
      Accountability requiere saber quién responsable de capacidad
      
  P2_Flujo:
    Trazabilidad_Requerida:
      - created_by: Quién diseñó flujo
      - version: Historial cambios flujo
      - purpose: Propósito que sirve
      
    Justificación:
      Auditoría requiere saber evolución flujos y por qué existen
      
  P3_Información:
    Trazabilidad_Requerida:
      - produced_by_flow: Flujo que generó
      - produced_by_capacity: Capacidad que produjo
      - lineage_parents: Información origen (DAG)
      - timestamp: Cuándo se creó
      
    Justificación:
      Data governance requiere lineage completo
      Regulaciones (GDPR) requieren origen datos
      
  P4_Límite:
    Trazabilidad_Requerida:
      - source: Origen límite (ley, policy, constraint)
      - created_by: Quién definió/registró
      - justification: Por qué existe límite
      
    Justificación:
      Compliance requiere demostrar origen restricciones
      
  P5_Propósito:
    Trazabilidad_Requerida:
      - owner: Capacidad accountable
      - parent_purpose: Propósito superior (alineación)
      - created_at: Cuándo se estableció
      - history: Cambios en métricas, status
      
    Justificación:
      Governance requiere accountability clara
      Estrategia requiere alignment vertical

Beneficios_Operativos:
  1. Accountability: Siempre hay responsable identificable
  2. Auditability: Historial completo reconstruible
  3. Debugging: Root cause analysis posible
  4. Compliance: Regulaciones satisfechas (SOX, GDPR, HIPAA)
  5. Learning: Decisiones pasadas informan futuras

Fundamentación_Teórica:
  - Data Lineage (OpenLineage): Trazabilidad producción datos
  - Event Sourcing: Todo cambio como evento rastreable
  - Blockchain: Immutable audit trail
  - Systems Thinking: Feedback loops requieren trazabilidad
  
Validación_Operativa:
  CHECK: ∀ entidad E, ∃ audit_trail(E) completo y consultable
```

## §5. INVARIANTE I4: CLASIFICACIÓN CONTEXTUAL

```yaml
I4_CLASIFICACIÓN_CONTEXTUAL:
  Enunciado:
    "Todo componente operativo tiene rol Producción o Habilitación según contexto organizacional"
    
  Formulación_Formal:
    ∀ C ∈ {Capacidad, Flujo}:
      ∃ clasificar(C, Organización, Contexto) → {Producción, Habilitación}
      
    Propiedad_Contextual:
      clasificar(C, Org1, Ctx1) puede ≠ clasificar(C, Org2, Ctx2)

Motivación_Fundamental:
  
  Problema_Resuelto:
    "Confusión entre producción y habilitación especialmente en organizaciones 
     que producen información o software"
     
  Ejemplos_Ambigüedad:
    - ¿API de pagos es producción o habilitación?
      → Depende: Fintech (producción), Retail (habilitación)
      
    - ¿Data pipeline es producción o habilitación?
      → Depende: Data-as-Product (producción), Analytics interno (habilitación)
      
    - ¿Plataforma CI/CD es producción o habilitación?
      → Depende: GitHub (producción), Internal DevOps (habilitación)

Definiciones_Precisas:

  Producción:
    Definición: Componente en flujo DIRECTO a destinatario final de valor
    Test_Operativo: ¿Destinatario pagaría por esto directamente?
    Característica: Output consumido FUERA de organización (o unidad)
    
  Habilitación:
    Definición: Componente que AMPLIFICA capacidad de otros componentes
    Test_Operativo: ¿Su valor es indirecto vía componentes producción?
    Característica: Output consumido DENTRO de organización (o unidad)

Reglas_Clasificación:

  R1_Flujo_Directo_Cliente:
    IF output(Componente) → Cliente_Externo THEN Producción
    
    Ejemplo:
      Feature_Producto → Usuario_Paga → Producción
      
  R2_Amplificación_Interna:
    IF output(Componente) → Capacidad_Interna THEN Habilitación
    
    Ejemplo:
      CI/CD → Desarrolladores → Habilitación
      
  R3_Híbrido_Contextual:
    IF Componente sirve AMBOS roles THEN clasificar por uso dominante
    
    Ejemplo:
      Internal_API:
        - 80% uso interno → Habilitación
        - 20% exposición externa → Producción minoritaria
      Clasificación: Habilitación (dominante)

Propiedad_Reclasificación:

  Componente puede reclasificarse si contexto cambia
  
  Ejemplo_Pivote:
    Herramienta_Interna:
      T0: Uso interno (habilitación)
      T1: Decisión productizar (comercializar)
      T2: Clientes externos usan (producción)
      
    Implicación:
      - Responsabilidades cambian
      - Governance cambia (producto requiere SLA, soporte)
      - Métricas cambian (revenue vs efficiency)

Aplicación_Dominios:

  Tecnológicos_Típicos:
    Software_Development → Contexto determina
    Data_Engineering → Contexto determina
    Infrastructure_Cloud → Típicamente habilitación
    UX/UI_Design → Contexto determina
    
  No_Tecnológicos:
    Legal → Habilitación (típico)
    Finance → Habilitación (típico)
    HR → Habilitación (típico)
    Sales → Producción (direct revenue)

Fundamentación_Teórica:
  - Work System Theory: IS roles R1-R6 (desde monitor hasta ejecutor)
  - Outside-In EA: 3+1 model (Shop/Factory vs Warehouse/Management)
  - Product vs Platform: Mismo artefacto, diferente posición valor
  
Validación_Operativa:
  CHECK: ∀ Capacidad/Flujo, ∃ clasificación explícita y justificada
  CHECK: Reclasificación documentada con razón cambio
```

## §6. INVARIANTE I5: HAIC (Human-AI Collaboration)

**[GENOMA]** - Teorema Ético-Estructural

```yaml
I5_HAIC_Núcleo_Irreducible:
  
  Enunciado_Minimal:
    "∀ capacidad algorítmica decisional (C1+) en sistema ORKO:
     ∃ exactamente UN accountable humano identificable
     con autoridad override y acceso explicabilidad"
     
  Formulación_Formal_Genoma:
    ∀ cap ∈ Capacidad:
      (cap.substrate = Algorítmico ∧ cap.capacity_type ≥ C1) →
        ∃! h ∈ Capacidad:
          (h.substrate ∈ {Humano, Mixto_con_Humano} ∧
           accountability_chain(cap) → h ∧
           h.can_override(cap) ∧
           cap.must_explain_to(h))
           
  Constraints_Fundamentales:
    C1_Accountability_Humana:
      Definición: "Responsabilidad última decisiones algorítmicas recae en humano"
      Fundamentación: A5 (Propósito requiere agencia moral, solo humanos la tienen)
      Prohibición: Accountability NO transferible a algoritmo (nunca)
      
    C2_Override_Capability:
      Definición: "Humano accountable puede cambiar/pausar decisión algorítmica"
      Implementación: ∃ mecanismo técnico accesible (circuit breaker, manual override)
      Fundamentación: A4 (Límite) - humano impone límite final sobre algorítmico
      
    C3_Explainability:
      Definición: "Capacidad algorítmica debe poder justificar decisiones"
      Propósito: Prerequisito accountability (no puedo ser responsable si no entiendo)
      Fundamentación: I3 (Trazabilidad) - decisión sin justificación = opaca
      
    C4_Bounded_Autonomy:
      Definición: "Autonomía algorítmica limitada explícitamente en N dimensiones"
      Dimensiones: {financiero, operativo, reputacional, legal, temporal, scope}
      Fundamentación: A4 (Límite) - autonomía NO puede ser ilimitada

Fundamentación_Ontológica_Genoma:

  Desde_Axiomas:
    A5 (Propósito): Intencionalidad requiere agencia moral
    → Solo humanos poseen agencia moral plena (estado actual conocimiento)
    → Algorítmicos son instrumentos capacidad, NO agentes morales autónomos
    
  Desde_Invariantes:
    I3 (Trazabilidad): Decisión sin explicación = no auditable
    → Explainability es prerequisito técnico accountability
    
  Validación_Empírica:
    - Marco regulatorio: EU AI Act, GDPR exigen human-in-control
    - Teoría ética: Responsabilidad moral requiere conciencia/volición
    - Sistema legal: Accountability última recae en personas/organizaciones

Propiedades_I5:
  
  P_I5_1_Transversalidad:
    Enunciado: "HAIC aplica en TODOS dominios D1-D4, no solo D1"
    Implicación: TF7 (Agentic Layer) es UNA implementación, no LA definición
    
  P_I5_2_No_Transferibilidad:
    Enunciado: "Accountability humana NUNCA se transfiere a algoritmo"
    Implicación: Delegación aumenta autonomía OPERATIVA, no responsabilidad MORAL
    
  P_I5_3_Progresión_Segura:
    Enunciado: "Autonomía algorítmica debe crecer gradualmente con evidencia"
    Implicación: Salto directo a alta autonomía sin validación = anti-pattern
```

---

**[FENOTIPO]** - Operacionalización HAIC

```yaml
NOTA_Fenotipo:
  "Esta sección describe patrones, modos y estrategias RECOMENDADAS
   para implementar el núcleo genoma I5. Son contextuales y adaptables."

Espectro_Delegación_M1-M6:
  
  Clasificación_Autonomía_Progresiva:
    "Taxonomía de 6 modos delegación según nivel autonomía algorítmica"
    
    M1_Monitorear (Autonomía: 0%):
      Descripción: AA solo observa, NO actúa
      Decisión: 100% humano
      Uso_típico: Nuevas capacidades sin validación, aprendizaje inicial
      Ejemplos: Dashboard analytics, logging, observability pasiva
      
    M2_Informar (Autonomía: 10-20%):
      Descripción: AA sugiere acciones, humano decide siempre
      Decisión: 100% humano (AA informa)
      Uso_típico: Decision support, recomendaciones
      Ejemplos: BI dashboards con insights, anomaly alerts, recommender systems
      
    M3_Habilitar (Autonomía: 30-50%):
      Descripción: Humano invoca, AA ejecuta bajo supervisión
      Decisión: Humano inicia, AA ejecuta
      Uso_típico: Automation on-demand, copilots
      Ejemplos: GitHub Copilot (humano acepta), RPA invocado manualmente
      
    M4_Controlar (Autonomía: 60-70%):
      Descripción: AA decide dentro reglas claras, humano maneja excepciones
      Decisión: AA rutina, humano edge cases
      Uso_típico: Automatización guiada por reglas, workflows establecidos
      Ejemplos: Approval workflows, rules engines, policy enforcement
      
    M5_Coproducir (Autonomía: 50-70%, mixto):
      Descripción: Humano + AA colaboran simultáneamente en tarea
      Decisión: Negociada H↔AA
      Uso_típico: Tareas complejas requiriendo ambos (creatividad + escala)
      Ejemplos: Pair programming H+AI, content creation asistida
      
    M6_Ejecutar (Autonomía: 80-95%):
      Descripción: AA autónomo dentro bounded autonomy, humano supervisa periódicamente
      Decisión: AA autonomía acotada, humano override disponible
      Uso_típico: Operaciones críticas, alta frecuencia, bajo riesgo unitario
      Ejemplos: Trading algorithms, dynamic pricing, auto-scaling cloud

  Progresión_Recomendada:
    Principio: "NO saltar niveles sin validación"
    
    Patrón_seguro:
      Nueva_capacidad → M1 (observar)
        ↓ (validación: patterns identificados)
      M1 → M2 (sugerir)
        ↓ (validación: success_rate > 70%)
      M2 → M3 (habilitar)
        ↓ (validación: latency crítica AND success_rate > 85%)
      M3 → M4 (controlar)
        ↓ (validación: success_rate > 95% AND bajo riesgo)
      M4 → M6 (ejecutar)
      
    Anti-Pattern:
      M1 → M6 directo (catastrófico)
      M2 → M5 sin M3/M4 (riesgoso)

Implementaciones_Override:
  
  Circuit_Breaker:
    Descripción: "Kill switch pausar sistema completo"
    Aplicabilidad: Toda capacidad M4-M6
    Latencia: <1 segundo acción humana → pausa efectiva
    Testing: Obligatorio drill mensual
    
  Manual_Override:
    Descripción: "Corregir decisión específica algorítmica"
    Aplicabilidad: Toda capacidad M2-M6
    UI: Botón "Override" visible + justification field
    Audit: Override registrado con (timestamp, user, reason)
    
  Escalation_Path:
    Descripción: "Reglas automáticas escalar a humano"
    Triggers:
      - Confidence < threshold (e.g., <0.7)
      - High-risk scenario detectado
      - Conflict entre reglas
      - Novel situation (no precedente en training)
    Response: Pausar + notificar humano + esperar decisión

Explainability_Patterns:
  
  Nivel_Mínimo_Requerido:
    M1-M2: Explainability nice-to-have (solo observa/sugiere)
    M3-M4: Explainability OBLIGATORIA (actúa con impacto)
    M5-M6: Explainability CRÍTICA (alto autonomía)
    
  Técnicas_Recomendadas:
    Model-Agnostic:
      - LIME (Local Interpretable Model-agnostic Explanations)
      - SHAP (SHapley Additive exPlanations)
      - Counterfactual explanations
      
    Model-Specific:
      - Decision trees → path visualization
      - Neural nets → attention weights, saliency maps
      - LLMs → chain-of-thought prompting
      
    Business-Level:
      - Natural language explanations (LLM-generated)
      - Analogías con casos similares
      - Confidence scores + feature importance rankings

Límites_Primacía:

  NO_implica_micromanagement:
    Humano no debe estar en CADA decisión (no escala)
    Delegación M4-M6 permite autonomía ACOTADA
    
  NO_implica_humano_perfecto:
    Reconoce límites cognitivos humanos:
      - Bias
      - Fatigue
      - Limited working memory
      
    Por eso delegación a algorítmico es NECESARIA
    Pero accountability permanece con humano

Transversalidad_HAIC_Por_Dominio:

  HAIC_NO_es_Tejido_Específico:
    - TF7 (Agentic Layer) es IMPLEMENTACIÓN avanzada, NO definición HAIC
    - HAIC es PATRÓN COLABORACIÓN aplicable a TODOS dominios
    - Cada dominio D1-D4 puede (y debe) considerar colaboración humano-AI
    
  D1_Tecnológico_+_AI:
    Ejemplos_Colaboración:
      - GitHub Copilot: AI asiste desarrollo código
      - AI DevOps: Optimización pipelines, detección anomalías
      - Infrastructure synthesis: IaC generado/validado por AI
      - Security scanning: AI detecta vulnerabilidades
    
    Modo_Delegación_Típico: M2-M4 (Informar, Habilitar, Controlar)
    Accountability: Equipo DevOps/Platform responsable final
    Override: Manual deploy capability, circuit breakers
    
  D2_Informacional_+_AI:
    Ejemplos_Colaboración:
      - AI data analyst: Genera insights desde data lake
      - Anomaly detection: AI detecta patterns no obvios
      - Data quality: AI valida completitud, consistencia
      - Lineage inference: AI reconstruye DAG dependencias
    
    Modo_Delegación_Típico: M2-M3 (Informar, Habilitar)
    Accountability: Data governance team responsable
    Override: Human veto análisis, ajuste thresholds
    
  D3_Organizacional_+_AI:
    Ejemplos_Colaboración:
      - AI coach 1:1: Asiste managers en conversaciones difíciles
      - Decision support: AI simula escenarios org changes
      - Meeting facilitation: AI resume, trackea action items
      - Onboarding assistant: AI guía nuevos empleados
    
    Modo_Delegación_Típico: M1-M3 (Monitorear, Informar, Habilitar)
    Accountability: Managers, HR responsables decisiones finales
    Override: Humano siempre decide sobre personas
    
  D4_Escalar_+_AI:
    Ejemplos_Colaboración:
      - Multi-site coordination: AI sincroniza across sedes
      - Language translation: AI traduce comunicaciones tiempo real
      - Cultural adaptation: AI ajusta mensajes por región
      - Resource optimization: AI balancea capacidad cross-sites
    
    Modo_Delegación_Típico: M3-M5 (Habilitar, Controlar, Coproducir)
    Accountability: Regional coordinators responsables
    Override: Escalation paths a humanos senior

Aplicación_Meta_ORKO_Mismo:

  ORKO_Practica_HAIC:
    "ORKO implementa lo que predica: usa AI para evolucionar"
    
    Future_Extensions:
      - AI puede asistir síntesis módulos avanzada (futuro)
      - Humano aprueba siempre (I5 HAIC preserved)
      - Explainability obligatoria en extensiones AI
      
    Documentación_ORKO:
      - AI puede asistir generación templates
      - AI puede sugerir refinamientos principios
      - PERO humano arquitecto aprueba cambios genoma
      - Genoma (A1-A5, P1-P5, I1-I8) permanece human-authored
      
    Implementaciones_ORKO:
      - AI puede generar código según contratos
      - AI puede optimizar workflows
      - AI puede sugerir mejoras observabilidad
      - PERO accountability con implementadores humanos

Transformación_Socio_Política:
  
  I5 HAIC implica que transformaciones con AI deben acompañarse de
  transformación socio-política. Resistencia a AI es natural y
  debe gestionarse explícitamente mediante:
  
  - Stakeholder engagement diferenciado por poder/interés/AI-readiness
  - Manejo explícito resistencia (4 tipos: cognitiva/emocional/política/skills)
  - Comunicación multi-canal sobre HAIC (Why-What-How AI collaboration)
  - Red de campeones AI grassroots distribuida
  - Upskilling explícito en trabajar CON AI (no solo sobre AI)
  
  Omitir dimensión socio-política HAIC = predictor #1 falla adopción AI
  Ver metodologia §16 Change Management para operacionalización completa

Fundamentación_Teórica:
  - Human-Centered AI (HCAI): Bounded autonomy, human-in-control
  - Human-AI Teaming: Colaboración vs automation (Parasuraman & Riley)
  - Agent-Responsibility Theory: Accountability distribuida humano-AI
  - Ethics of AI: Moral agency requiere conciencia/intencionalidad (humana)
  - Change Management: Transformación técnica + socio-política + AI literacy simultánea
  
Validación_Operativa:
  CHECK: ∀ Capacidad(Algorítmica) en CUALQUIER dominio D1-D4, ∃ Capacidad(Humana) responsable
  CHECK: Override mechanisms implementados y testeados TODOS dominios
  CHECK: Explainability verificada (NPS comprehension ≥ 7)
  CHECK: Plan change management HAIC activo si adopción AI organizacional
  CHECK: TF7 reconocido como implementación, NO definición HAIC
```

## §7. INVARIANTE I6: TRAJECTORY-AWARENESS

**[GENOMA]** - Teorema Evolución Algorítmica

```yaml
I6_TRAJECTORY_AWARENESS_Núcleo:
  
  Enunciado_Minimal:
    "∀ capacidad algorítmica: historial uso condiciona su autonomía y evolución.
     Trayectoria registrada permite mejora continua y ajuste delegation_mode."
     
  Formulación_Formal_Genoma:
    ∀ cap ∈ Capacidad:
      (cap.substrate = Algorítmico) →
        ∃ trajectory(cap) = {executions, feedback, metrics} ∧
        trajectory(cap) → {evolution_cap, adjustment_autonomy}
        
  Constraints_Fundamentales:
    
    C1_Registro_Obligatorio:
      Definición: "Toda ejecución algorítmica decisional debe registrarse"
      Mínimo: (timestamp, input, output, success/failure)
      Fundamentación: I3 (Trazabilidad) + aprendizaje requiere datos
      
    C2_Trajectory_Informa_Autonomía:
      Definición: "Progresión delegation_mode debe basarse en trajectory"
      Forma: trajectory.success_rate → decision(increase/decrease autonomy)
      Fundamentación: I5 (HAIC bounded autonomy) + evidencia empírica
      
    C3_Mejora_Continua:
      Definición: "Capacidad algorítmica debe mejorar con uso"
      Distinción: vs mecánica (degrada con uso)
      Fundamentación: Naturaleza algorítmica (más datos → mejor performance)

Fundamentación_Ontológica_Genoma:

  Diferenciación_Sustrato:
    
    Capacidad_Mecánica (P1.substrate = Mecánico):
      - Entropía: Deteriora con uso (wear and tear físico)
      - Aprendizaje: NO aprende de historial
      - Mantenimiento: Preventivo basado tiempo/ciclos uso
      
    Capacidad_Algorítmica (P1.substrate = Algorítmico):
      - MEJORA con uso (más datos, más patterns)
      - Aprende de errores y éxitos
      - Evoluciona basada en feedback
      
  Implicación_Clave:
    Trajectory NO es solo audit log (compliance)
    Trajectory ES mecanismo activo mejora continua (learning)
    
Propiedades_I6:
  
  P_I6_1_Universalidad_Algorítmica:
    Enunciado: "TODO substrate Algorítmico tiene trajectory"
    Scope: Capacidades C0+ (incluye mecánicas con sensores digitales)
    Excepción: Capacidades puramente mecánicas sin telemetría
    
  P_I6_2_Progresión_Evidenciada:
    Enunciado: "Cambio delegation_mode requiere evidencia trajectory"
    Anti-Pattern: Aumentar autonomía sin datos validación
    Validación: success_rate, drift_detection, human_override_frequency
    
  P_I6_3_Ciclo_Cerrado:
    Enunciado: "Trajectory → Learning → Evolution → Trajectory'"
    Propiedad: Sistema auto-mejora (feedback loop positivo)
    Límite: Bounded por I5 (humano always accountable)
```

---

**[FENOTIPO]** - Operacionalización Trajectory-Awareness

```yaml
NOTA_Fenotipo:
  "Esta sección describe dimensiones, mecanismos y casos uso RECOMENDADOS
   para implementar trajectory-awareness. Son adaptativos según contexto."

Dimensiones_Trajectory_Detalladas:

  D1_Execution_History:
    Registro completo de ejecuciones:
      - Input recibido
      - Output generado
      - Contexto (estado sistema, constraints activos)
      - Latencia
      - Success/Failure
      
    Propósito:
      - Pattern detection (casos comunes, edge cases)
      - Performance analysis (latencia trends)
      - Reliability tracking (success rate over time)
      
  D2_Human_Feedback:
    Registro correcciones humanas:
      - Overrides: Cuándo humano cambió decisión algorítmica
      - Ratings: Evaluación calidad output
      - Corrections: Qué debió ser el output correcto
      
    Propósito:
      - RLHF (Reinforcement Learning from Human Feedback)
      - Fine-tuning datos
      - Detectar systematic errors
      
  D3_Context_Shifts:
    Detección cambios contextuales:
      - Drift: Distribución inputs cambia
      - Seasonality: Patterns cíclicos
      - Regime changes: Cambios estructurales
      
    Propósito:
      - Trigger re-training
      - Ajustar confidence thresholds
      - Alertar degradación performance

Mecanismos_Evolución:

  E1_Progresión_Delegación:
    Trayectoria informa nivel autonomía
    
    Patrón_Típico:
      T0: M1 (Monitorear) - Sistema nuevo, observación
        → Acumula datos, humano valida patterns
        
      T1: M2 (Informar) - Suficientes datos, sugiere
        → Humano evalúa calidad sugerencias
        → IF success_rate > 70% THEN considerar M3
        
      T2: M3 (Habilitar) - Alta calidad, humano invoca
        → Uso on-demand, feedback positivo acumula
        → IF latency critical AND success_rate > 85% THEN considerar M4
        
      T3: M4 (Controlar) - Reglas claras, excep. humanas
        → Mayoría casos automáticos, humano solo edge cases
        → IF success_rate > 95% AND low-risk THEN considerar M6
        
      T4: M6 (Ejecutar) - Altamente confiable, supervisión periódica
        
    Propiedad_NO_Saltar_Niveles:
      NO: M1 → M6 directo (anti-pattern)
      SÍ: M1 → M2 → M3 → M4 → M6 (progresivo)
      
      Justificación:
        Cada nivel valida confiabilidad antes aumentar autonomía
        Saltar niveles = riesgo catastrófico no mitigado
        
  E2_Continuous_Learning:
    Capacidad mejora con trajectory
    
    Técnicas:
      Online_Learning:
        - Modelo actualiza con cada nueva observación
        - Ejemplos: Bandits, online gradient descent
        
      Periodic_Retraining:
        - Modelo re-entrena batch periódicamente
        - Frecuencia: Semanal, mensual (según drift rate)
        
      Fine_Tuning:
        - Modelo base ajustado con datos específicos organización
        - Ejemplos: LLM fine-tuning, transfer learning
        
      RLHF:
        - Feedback humano informa reward function
        - Modelo optimiza contra preferencias humanas
        
  E3_Drift_Detection:
    Monitoreo continuo degradación
    
    Señales_Drift:
      - Success rate decae > 5% respecto baseline
      - Latencia aumenta sin causa infraestructural
      - Human override frequency aumenta
      - Input distribution diverge (KL divergence)
      
    Acciones_Mitigación:
      IF drift_detected:
        1. Alertar humano responsable
        2. Reducir autonomía (M6→M4, M4→M3)
        3. Trigger re-training
        4. Investigar root cause (context shift? data quality?)

Casos_Uso_Específicos:

  LLM_Copilot:
    Trajectory captura:
      - Prompts usuarios
      - Outputs generados
      - Accept/reject/edit rate
      
    Evolución:
      - Prompts frecuentes → prompt templates
      - Patterns de edición → fine-tuning
      - Rechazos sistemáticos → mejora model/prompts
      
  ML_Churn_Prediction:
    Trajectory captura:
      - Features usadas
      - Predictions hechas
      - Outcomes reales (ground truth)
      
    Evolución:
      - Features más predictivas → feature engineering
      - False positives/negatives → threshold tuning
      - New patterns → model retraining
      
  RPA_Invoice_Processing:
    Trajectory captura:
      - Invoices procesadas
      - Campos extraídos
      - Errores corrección manual
      
    Evolución:
      - OCR errors patterns → improve OCR
      - Validation rules → refine rules
      - New invoice formats → expand training data

Trayectorias_Adopción_Organizacional:
  
  I6 se operacionaliza en metodología mediante dos trayectorias complementarias:
  
  Trayectoria_Minimal (tool-agnostic, manual):
    - No requiere capacidades algorítmicas complejas
    - Progresión autonomía limitada a M1-M3
    - Timeline: 6-12 meses
    - Aplicable: Orgs baja madurez o recursos limitados
  
  Trayectoria_Avanzada (tech stack completo):
    - Implementa 7 Tejidos Tecnológicos (TF1-TF7)
    - Progresión autonomía completa M1-M6
    - Timeline: 18-36 meses
    - Requiere: H_org ≥ 70, presupuesto, madurez DevOps
  
  Principio: Organizaciones deben elegir según trajectory actual (I7)
  No saltar de Minimal a Avanzada sin consolidar fundamentos
  Ver metodologia §0.5 para framework decisión trayectorias

Fundamentación_Teórica:
  - Reinforcement Learning: Agent mejora con reward signals
  - Active Learning: Sistema solicita labels casos inciertos
  - Continuous Deployment ML: MLOps lifecycle con monitoring
  - Human-in-the-Loop ML: Feedback humano como señal aprendizaje
  
Validación_Operativa:
  CHECK: ∀ Capacidad(Algorítmica), trajectory_log accesible y analizable
  CHECK: Drift detection implementado con alertas
  CHECK: Progresión autonomía documentada con evidencia trajectory
  CHECK: Trayectoria adopción elegida según madurez (I7)
```

## §8. INVARIANTE I7: EMERGENCIA DE COMPLEJIDAD

```yaml
I7_EMERGENCIA_COMPLEJIDAD:
  Enunciado:
    "Capacidades organizacionales emergen en niveles de complejidad creciente.
     No son módulos integrados, son PROPIEDADES EMERGENTES del sistema"
     
  Formulación_Formal:
    ∃ Jerarquía_Complejidad = {L0, L1, L2, L3, L4, L5}:
      L(n+1) emerge cuando complejidad L(n) supera umbral crítico
      
    ∧ ∀ práctica_organizacional P:
      ∃ nivel_mínimo(P) = min{L | P emerge naturalmente en L}

Tesis_Central:

  Enterprise_Architecture NO es módulo
    → Es EMERGENCIA de Nivel 3 (Reflexión Estructural)
    
  Transformación_Digital NO es módulo
    → Es EMERGENCIA de Nivel 4 (Reflexión Estratégica)
    
  ORKO NO integra EA + TD
    → ORKO es Nivel 5 (Meta-Reflexión) que HACE EMERGER EA y TD

Modelo_5_Niveles:

  Nivel_0_Ejecución_Mecánica:
    Característica: Transformación sin decisión
    
    Capacidad_Cognitiva: C0 (Ejecutar)
    
    Ciclo: Solo ACT (no Sense ni Decide)
    
    Horizon_Temporal: Microsegundos a minutos
    
    Actores_Típicos:
      - Máquinas CNC, bombas, sensores
      - RPA bots (deterministas)
      - Operarios tareas mecánicas
      
    Ejemplos:
      - Línea ensamblaje
      - ETL batch
      - Backup automático
      
    Gestión:
      - Supervisión directa
      - Procedures estrictos
      - Mantenimiento preventivo
      
    Prácticas_Emergentes:
      - Standard Operating Procedures (SOPs)
      - Checklists
      
  Nivel_1_Decisión_Local:
    Característica: Elección entre opciones dentro proceso
    
    Capacidad_Cognitiva: C1 (Decidir)
    
    Ciclo: SDA completo (scope limitado a tarea)
    
    Horizon_Temporal: Minutos a horas
    
    Actores_Típicos:
      - Operadores, supervisores
      - ML models (M4: reglas)
      - LLMs (M2-M3: asistencia)
      
    Ejemplos:
      - Aprobar factura <$10K
      - Triage ticket soporte
      - Deploy con quality gates
      
    Gestión:
      - Policies claras
      - Escalation paths
      - Training operadores
      
    Prácticas_Emergentes:
      - Agile (Scrum, Kanban) ← EMERGE AQUÍ
      - Daily standups
      - Sprint planning
      
  Nivel_2_Reflexión_Operacional:
    Característica: Observar operación y mejorar continuamente
    
    Capacidad_Cognitiva: C2 (Reflexionar)
    
    Ciclo: WSLC con mejora incremental (Operation → feedback → adjust)
    
    Horizon_Temporal: Días a semanas
    
    Actores_Típicos:
      - Teams (5-9 personas)
      - Tech Leads
      - Engineering Managers
      
    Ejemplos:
      - Retrospectives (qué mejorar)
      - A/B testing (qué funciona mejor)
      - Cycle time optimization
      
    Gestión:
      - OKRs tácticos
      - Metrics-driven decisions
      - Continuous improvement culture
      
    Prácticas_Emergentes:
      - DevOps ← EMERGE AQUÍ
      - SRE (error budgets, toil reduction) ← EMERGE AQUÍ
      - Lean (value stream mapping) ← EMERGE AQUÍ
      - Kaizen (mejora continua)
      
  Nivel_3_Reflexión_Estructural:
    Característica: Rediseñar componentes y relaciones
    
    Capacidad_Cognitiva: C2 (Reflexionar sobre estructura)
    
    Ciclo: WSLC completo (Initiation → Development → Implementation cambios estructurales)
    
    Horizon_Temporal: Meses a trimestres
    
    Actores_Típicos:
      - Arquitectos
      - Directors
      - VPs Engineering
      
    Ejemplos:
      - Reorganización teams
      - Microservices migration
      - Platform build (internal)
      
    Gestión:
      - Capability roadmaps
      - Architectural governance
      - Change management
      
    ⚠️ EMERGENCIA CRÍTICA:
      Enterprise Architecture ← EMERGE AQUÍ
      
      ¿Por qué Nivel 3?
        - EA requiere reflexión SOBRE estructura organizacional
        - EA diseña CÓMO organizamos capacidades
        - EA gestiona complejidad que supera capacity equipo único
        
      Señales_Necesidad_EA:
        - >50 personas (límite span informal)
        - >3 teams interdependientes
        - Handoffs frecuentes ralentizan
        - Duplicación esfuerzos no coordinados
        - Conway's Law problemas (arquitectura refleja mal org)
        
      Prácticas_EA_Emergentes:
        - TOGAF (framework arquitectura)
        - Zachman (taxonomía)
        - Capability maps
        - RACI matrices
        - Architecture Decision Records (ADRs)
        
  Nivel_4_Reflexión_Estratégica:
    Característica: Redefinir propósito y realinear organización
    
    Capacidad_Cognitiva: C3 (Meta-Reflexionar sobre propósito)
    
    Ciclo: Múltiples WSLC coordinados (transformación multi-año)
    
    Horizon_Temporal: Años
    
    Actores_Típicos:
      - C-level (CEO, CTO, CPO)
      - Board
      - Strategy consultants
      
    Ejemplos:
      - Pivote estratégico (modelo negocio)
      - M&A integration
      - Market expansion (nueva geografía/segmento)
      - Digital transformation (redefinir propuesta valor)
      
    Gestión:
      - Strategic planning (3-5 años)
      - Portfolio management
      - Scenario planning
      
    ⚠️ EMERGENCIA CRÍTICA:
      Transformación Digital ← EMERGE AQUÍ
      
      ¿Por qué Nivel 4?
        - TD requiere reflexión SOBRE propósito y estrategia
        - TD redefine QUÉ es la organización (no solo CÓMO opera)
        - TD es cambio estructural + cultural + estratégico
        
      Señales_Necesidad_TD:
        - Disrupción mercado (competidor digital)
        - Cambio preferencias clientes (digital-first)
        - Obsolescencia modelo negocio
        - Oportunidad nuevos modelos habilitados por digital
        
      Prácticas_TD_Emergentes:
        - Digital strategy formulation
        - Business model canvas (repensar)
        - Continuous Digital (Kelly) ← EMERGE AQUÍ
        - Agile at scale (SAFe, LeSS) - cuando >200 personas
        
  Nivel_5_Meta_Reflexión:
    Característica: Observar CÓMO reflexionamos y evolucionar capacidad reflexión
    
    Capacidad_Cognitiva: C3 (Meta-reflexionar sobre marcos conceptuales)
    
    Ciclo: Evolución del marco mismo (paradigm shifts)
    
    Horizon_Temporal: Multi-año, continuo
    
    Actores_Típicos:
      - Filósofos organizacionales
      - Framework designers
      - Thought leaders
      
    Ejemplos:
      - Crear ORKO (este framework)
      - Definir nuevos paradigmas gestión
      - Síntesis cross-disciplinaria
      
    Gestión:
      - Learning how to learn organizationally
      - Theory development
      - Meta-frameworks
      
    ⚠️ ORKO OPERA AQUÍ:
      ORKO es Nivel 5
      → No es práctica Nivel 3 (EA) ni Nivel 4 (TD)
      → Es META-MARCO desde el cual EA y TD emergen
      
      Analogía:
        Category Theory : Matemáticas :: ORKO : Organizaciones
        
        Category Theory NO es rama de matemáticas
        Category Theory es lenguaje que DESCRIBE estructuras matemáticas
        Desde Category Theory emergen álgebra, topología, etc.
        
        ORKO NO es práctica organizacional
        ORKO es lenguaje que DESCRIBE estructuras organizacionales
        Desde ORKO emergen EA, TD, Agile, DevOps, etc.

Propiedades_Emergencia:

  P1_Inclusión:
    Nivel(n) incluye capacidades Nivel(0..n-1)
    
    Ejemplo:
      Organización Nivel 4 (estratégica) TIENE:
        - Nivel 0: Ejecución mecánica (servers, RPA)
        - Nivel 1: Decisión local (operadores, supervisores)
        - Nivel 2: Mejora continua (teams, retrospectives)
        - Nivel 3: Diseño estructural (arquitectos)
        - Nivel 4: Reflexión estratégica (C-level)
        
  P2_No_Saltable:
    NO se puede saltar niveles
    
    Anti-Pattern:
      Startup (Nivel 0-1) intenta hacer EA formal (Nivel 3)
      → Overhead sin valor (no hay complejidad que gestionar)
      
    Anti-Pattern:
      Empresa tradicional (Nivel 1) declara "Digital Transformation" (Nivel 4)
      → Sin pasar por Nivel 2 (DevOps) y 3 (EA modernizada)
      → Fracasa porque no tiene fundación
      
  P3_Umbral_Crítico:
    Transición Nivel(n) → Nivel(n+1) ocurre cuando complejidad supera umbral
    
    Señales_Transición:
      L0→L1: Volumen requiere decisiones (no solo ejecución)
      L1→L2: Ineficiencias repetidas requieren reflexión (no solo más decisiones)
      L2→L3: Coordinación inter-teams requiere estructura (no solo mejora local)
      L3→L4: Ambiente cambia requiere nuevo propósito (no solo mejor estructura)
      L4→L5: Frameworks existentes insuficientes (requiere nuevo paradigma)
      
  P4_Recursión_Fractal:
    Patterns similares en cada nivel (diferentes escalas)
    
    Ejemplo_SDA:
      Nivel 1: SDA tarea individual (minutos)
      Nivel 2: SDA sprint (semanas)
      Nivel 3: SDA capability build (meses)
      Nivel 4: SDA transformation (años)
      
    Mismo patrón, diferente granularidad temporal

Implicaciones_Prácticas:

  Para_Startups_10_Personas:
    Nivel actual: 0-1
    NO necesita: EA formal, TD strategy
    SÍ necesita: SOPs, decisiones claras, ejecución rápida
    
  Para_ScaleUps_50_Personas:
    Nivel actual: 1-2
    Emergiendo: Agile, DevOps
    NO necesita: EA enterprise-grade
    SÍ necesita: Team structure, continuous improvement
    
  Para_MidSize_200_Personas:
    Nivel actual: 2-3
    Emergiendo: EA capability maps, governance
    NO necesita: TD full-scale (aún)
    SÍ necesita: Architectural clarity, platform thinking
    
  Para_Enterprise_1000+_Personas:
    Nivel actual: 3-4
    Necesita: EA formal, TD strategy
    Desafío: Mantener agilidad mientras escala

Fundamentación_Teórica:
  - Complexity Theory: Transiciones de fase, emergencia
  - Systems Thinking: Propiedades emergentes de interacciones
  - Organizational Design: Structural contingency (structure follows strategy)
  - Evolution Biology: Niveles organizacionales (célula → tejido → órgano → organismo)
  
Validación_Operativa:
  CHECK: Prácticas implementadas corresponden a nivel complejidad org
  CHECK: No intentar prácticas Nivel(n+2) sin haber consolidado Nivel(n)

I7.5_Lifecycle_States (G11):
  "Capacidades evolucionan a través estados lifecycle con transiciones
   formalizadas y triggers explícitos para capacity planning proactivo."
   
  Estados: Planning → Development → Active ↔ Idle → Deprecated → Sunset → Retired
  Transiciones_Prohibidas: Retired → * (terminal), Deprecated → Active
  Triggers_Auto: Active→Idle (utilization<20%, 4wks), Idle→Deprecated (12wks idle)
```

## §9. INVARIANTE I8: ADAPTACIÓN CONTEXTUAL

```yaml
I8_ADAPTACIÓN_CONTEXTUAL:
  Enunciado_Core:
    "ORKO adapta su expresión metodológica según contexto organizacional,
     manteniendo genoma teórico inmutable. Adaptación es INDEPENDIENTE
     de AI (manual viable, HAIC opcional amplificador)."
     
  Formulación_Formal:
    ∀ Organización O con contexto C:
      ∃ expresión metodológica M(C) tal que:
        1. M(C) es fiel a genoma G = {A1-A5, P1-P5, I1-I8} (INMUTABLE)
        2. M(C) respeta contratos C1-C5 (invariante)
        3. M(C) es mínima para satisfacer restricciones C (parsimonia)
        4. M(C₁) ≠ M(C₂) si C₁ ≠ C₂ (anti one-size-fits-all)
        5. M(C) determinable SIN AI (I5 HAIC opcional, no obligatorio)

Motivación_Fundamental:

  Problema_Resuelto:
    "Frameworks genéricos (TOGAF, ITIL, SAFe) asumen homogeneidad
     organizacional inexistente"
     
  Observación_Empírica:
    - GORE Chile ≠ ONG Botswana ≠ Clínicas USA ≠ Petrolera Rusa
    - Mismo framework genérico FALLA en contextos diversos
    - Adaptación ad-hoc post-facto = pérdida coherencia
    
  Solución_ORKO:
    Separar GENOMA (inmutable) de FENOTIPO (configurable)
    - Genoma: A1-A5, P1-P5, I1-I8 (ontología universal)
    - Fenotipo: Metodología, templates, módulos (expresión contextual)

Derivación_Formal:

  Base_Axiomática:
    A4 (Límites): Sistema opera en contexto restringido
    → Restricciones son CONTEXTUALES (varían por org)
    
    A5 (Propósito): Transformación dirigida por propósito org
    → Propósito es ESPECÍFICO (varía por org)
    
    ∴ Metodología debe SER ESPECÍFICA por contexto (I8)
    
  Extensión_I7:
    I7 establece: trajectory actual define nivel complejidad
    I8 generaliza: contexto COMPLETO define expresión metodológica
    
    I7: Bounded trajectory (dimensión temporal + madurez)
    I8: Bounded context (36 dimensiones ambientales)

Context_Schema:

  36_Parámetros_Ambientales:
    
    P1-P4: Tipo organizacional
      - ENV_TYPE: Public/Private/Nonprofit/Hybrid
      - SECTOR: Government/Healthcare/Energy/Finance/...
      - SUBSECTOR: específico
      - DOMAIN_STANDARDS: [ISO, HIPAA, MGDE, ...]
      
    P5-P8: Escala
      - SIZE: Micro/Small/Medium/Large/Enterprise
      - LOCATIONS: número sedes
      - EMPLOYEES: rango empleados
      - GEOGRAPHICAL_DISPERSION: Local/Regional/National/Multinational
      
    P9-P13: Marco regulatorio
      - JURISDICTION: país (ISO-3166)
      - LEGAL_FRAMEWORKS: [leyes aplicables]
      - REGULATORY_PRESSURE: Low/Medium/High/Critical
      - COMPLIANCE_DEADLINES: [fechas críticas]
      - AUDIT_FREQUENCY: periodicidad
      
    P14-P18: Madurez digital
      - H_org_CURRENT: 0-100
      - INFRASTRUCTURE: Legacy/Hybrid/Modern/Cloud_Native
      - DATA_MATURITY: Ad_Hoc/Defined/Managed/Optimized
      - DEVOPS_CAPABILITY: None/Basic/Intermediate/Advanced
      - TECH_STACK_OPENNESS: Locked_In/Partially_Open/Fully_Open
      
    P19-P22: Presión crisis
      - CRISIS_TYPE: None/Funding/Regulatory/Operational/Reputational/Existential
      - CRISIS_SEVERITY: Low/Medium/High/Critical
      - TIMELINE_SURVIVAL: meses hasta crisis irreversible
      - URGENCY_LEVEL: routine/important/urgent/emergency
      
    P23-P27: Restricciones
      - BUDGET_ANNUAL: USD
      - BUDGET_FLEXIBILITY: Rigid/Moderate/Flexible
      - STAFFING_CONSTRAINTS: Fixed/Partially_Flexible/Flexible
      - POLITICAL_CONSTRAINTS: High/Medium/Low (sector público/ONGs)
      - TECHNOLOGY_CONSTRAINTS: grado libertad elección tech
      
    P28-P31: Factores culturales
      - CHANGE_RESISTANCE: Low/Medium/High/Extreme
      - HIERARCHY_LEVEL: Flat/Moderate/Hierarchical/Extremely_Hierarchical
      - INNOVATION_APPETITE: Conservative/Moderate/Progressive/Disruptive
      - TRUST_TECHNOLOGY: Low/Medium/High
      
    P32-P36: Objetivos estratégicos
      - GOAL_1: {objective, urgency}
      - GOAL_2: {objective, urgency}
      - GOAL_3: {objective, urgency}
      - STRATEGIC_HORIZON: 1-year/3-year/5-year
      - SUCCESS_DEFINITION: métricas clave

Expression_Rules:

  Reglas_Parametrización (R_):
    
    R_COMPLIANCE:
      IF REGULATORY_PRESSURE = Critical:
        THEN ACTIVATE:
          - Compliance modules específicos jurisdicción
          - Gate G1 compliance mandatory
          - Audit trail enhanced
          
    R_CRISIS:
      IF CRISIS_SEVERITY = Critical AND TIMELINE_SURVIVAL < 12:
        THEN ACTIVATE:
          - Trajectory MINIMAL (low cost, fast)
          - Manual R4 (Quick Wins)
          - Compressed gates
        AND DEACTIVATE:
          - Trajectory AVANZADA (expensive)
          - Long-term strategic initiatives
          
    R_SCALE:
      IF LOCATIONS > 20:
        THEN ACTIVATE:
          - Multi-site orchestration module
          - Federated governance
          - Regional adaptation patterns
          
    R_MATURITY:
      IF H_org < 40:
        THEN ACTIVATE:
          - Manual R1 (Health Recovery) PRIORITARIO
          - Block transformation (hasta H_org ≥ 70)
        ELSE IF H_org ≥ 70 AND DEVOPS_CAPABILITY = Advanced:
          - Trajectory AVANZADA
          - Full tech stack (TF1-TF7)
          
    R_SECTOR:
      IF SECTOR = Healthcare:
        THEN ACTIVATE:
          - Lean Healthcare module
          - Patient safety metrics
          - Clinical pathway templates
      ELSE IF SECTOR = Government:
        THEN ACTIVATE:
          - Public sector governance
          - Transparency requirements
          - Political stakeholder mgmt

Adaptación_Con_Sin_AI:

  Modo_Manual (I8 independiente):
    Proceso:
      1. Arquitecto/consultor analiza organización
      2. Completa Context Schema manualmente (36 params)
      3. Evalúa Expression Rules manualmente
      4. Selecciona módulos/trayectoria apropiados
      5. Genera Activation Profile
      
    Ventajas:
      + No requiere AI (accesible cualquier org)
      + Funcional, viable, comprobado
      + Humano entiende contexto profundamente
      
    Limitaciones:
      - Slow (días/semanas)
      - No escala (requiere experto por org)
      - Sesgos humanos (experiencia limitada)
      
  Modo_Asistido_HAIC (I8 + I5):
    Proceso:
      1. AI analiza documentación org (I5 HAIC)
      2. AI sugiere Context Schema población
      3. AI evalúa Expression Rules automáticamente
      4. AI recomienda módulos/trayectoria
      5. HUMANO valida y aprueba (I5 accountability)
      6. AI genera Activation Profile
      
    Ventajas:
      + Fast (horas)
      + Escala (AI puede analizar múltiples orgs paralelo)
      + Aprende de patterns (I6 trajectory awareness)
      + Reduce sesgos (visión más amplia)
      
    Limitaciones:
      - Requiere TF7 o equivalente (inversión)
      - Requiere H_org ≥ 70 (madurez digital)
      - Explainability obligatoria (I5 PD21)
      
  Relación_I5_I8:
    I8: Define QUÉ adaptar (mecanismo parametrización)
    I5: Define CÓMO colaborar (si AI asiste)
    
    I8 NO depende de I5 (ortogonal)
    I5 AMPLIFICA I8 (opcional, poderoso)
    
    ∀ org puede usar I8 sin I5
    ∀ org con TF7 debería usar I8 + I5 (más eficiente)

Operacionalización:

  Metodología:
    Ver §17 Adaptación Contextual
    - Context Schema (input)
    - Expression Engine (transformation)
    - Activation Profile (output)
    
  Arquitectura:
    Ver PD35-PD40 (principios diseño adaptación)
    
  Validación:
    ∀ expresión M(C):
      CHECK: Derivable de genoma G
      CHECK: No viola invariantes I1-I8
      CHECK: Mínima para contexto C (I1)
      CHECK: Trazabilidad M(C) → G documentada (I3)

Fundamentación_Teórica:
  - Genotype-Phenotype Distinction (Biología): Genoma universal, expresión contextual
  - Context-Driven Architecture: Decisiones arquitectónicas dependen contexto
  - Situated Cognition: Conocimiento/práctica situados en contexto
  - Contingency Theory: No existe "one best way", depende contexto
  
Validación_Operativa:
  CHECK: ∀ org, ∃ Context Schema C poblado
  CHECK: ∀ C, ∃ expresión M(C) derivable de G
  CHECK: M(C) mínima según I1
  CHECK: Fidelidad genoma preservada
```

## §10. SÍNTESIS DE INVARIANTES

```yaml
Resumen_8_Invariantes:

  I1_Minimalidad:
    5 primitivos necesarios y suficientes
    Reducción conceptual = menor fricción cognitiva
    
  I2_Ortogonalidad:
    Primitivos mutuamente independientes
    Sin overlaps = mayor claridad
    
  I3_Trazabilidad:
    Todo rastreable a origen y responsable
    Accountability + auditability + learning
    
  I4_Clasificación_Contextual:
    Producción vs Habilitación es contextual
    Resuelve confusión fundamental
    
  I5_HAIC_Human_AI_Collaboration:
    Colaboración humano-AI transversal todos dominios
    Accountability humana, AI amplifica capacidades D1-D4
    TF7 es implementación, NO definición HAIC
    
  I6_Trajectory_Awareness:
    Algorítmicos mejoran con uso
    Trayectoria informa evolución
    
  I7_Emergencia_Complejidad:
    Capacidades emergen en niveles
    EA (L3), TD (L4), ORKO (L5)
    
  I8_Adaptación_Contextual:
    CORE: Expresión metodológica según contexto organizacional
    Genoma inmutable, fenotipo parametrizable
    INDEPENDIENTE: NO requiere AI (manual viable, HAIC opcional amplificador)
    Transversal D1-D4

Relaciones_Entre_Invariantes:

  I1 + I2 → Fundamento ontológico sólido (parsimonia + ortogonalidad)
  I3 → Operacionaliza accountability (I5) + learning (I6)
  I4 → Clarifica rol componentes contexto (I1)
  I5 HAIC → Amplificador OPCIONAL transversal (D1-D4)
  I5 + I6 → Evolución algorítmica controlada (trajectory-aware HAIC)
  I7 → Posiciona ORKO como meta-framework (emergencia niveles)
  I8 → Adaptación contextual CORE (independiente AI)
  
  Progresión_Adaptativa:
    I7: Nivel complejidad actual (trajectory org)
    I8: Adaptación contextos organizacionales (parametrización genoma→fenotipo)
    
  Relación_AI:
    I5: HAIC patrón colaboración (transversal D1-D4)
    I6: Aprendizaje trajectory (superior, todo algorítmico)
    I8: Independiente AI (manual viable, HAIC amplificador opcional)

Status_Teórico:
  ✓ 8 Invariantes derivados de axiomas A1-A5
  ✓ Fundamentados en fuentes (Alter, TSTI, Meyer, Kelly, Contingency Theory)
  ✓ Operacionalmente verificables
  ✓ Coherentes entre sí
  ✓ Ortogonales (28 pares validados)
```