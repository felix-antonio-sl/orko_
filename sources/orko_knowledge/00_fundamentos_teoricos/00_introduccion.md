# FUNDAMENTOS TEÓRICOS

> Base ontológica ORKO: Axiomas, Primitivos, Invariantes, Ciclos, Dominios

- [FUNDAMENTOS TEÓRICOS](#fundamentos-teóricos)
  - [§0. PROPÓSITO Y ALCANCE](#0-propósito-y-alcance)
    - [§0.1. ARQUITECTURA DEL CONOCIMIENTO: GENOMA vs FENOTIPO](#01-arquitectura-del-conocimiento-genoma-vs-fenotipo)
  - [§1. ESTRUCTURA MODULAR](#1-estructura-modular)
  - [§2. ORDEN LECTURA RECOMENDADO](#2-orden-lectura-recomendado)
  - [§3. TRAZABILIDAD VERTICAL](#3-trazabilidad-vertical)
  - [§4. ÍNDICE CONCEPTUAL](#4-índice-conceptual)

## §0. PROPÓSITO Y ALCANCE

```yaml
Propósito_Directorio:
  "Fundamentos teóricos derivados formalmente desde axiomas irreducibles.
   Base ontológica sobre la cual se construye toda la arquitectura ORKO."

Alcance:
  - Derivación formal primitivos P1-P5 desde axiomas A1-A5
  - Invariantes sistema I1-I8 (propiedades que DEBEN preservarse)
  - Ciclos fundamentales (SDA operacional + WSLC evolutivo)
  - Dominios ortogonales D1-D4 (dimensiones complejidad organizacional)
  - Teoremas validación sistema (completitud, ortogonalidad, minimalidad)
  - Ecuación valor organizacional V_org
  - Modelo relacional primitivos (estructura datos)

Naturaleza:
  - TEORÍA pura (no implementación)
  - Rigor formal (demostraciones, fundamentación)
  - Independiente contexto (universalmente aplicable)
  - Trazable (toda derivación desde axiomas)

Relación_Arquitectura:
  ./                        → TEORÍA (qué es el sistema)
  ../10_arquitectura_orko/  → IMPLEMENTACIÓN (cómo construirlo)
  ../30_metodologia_orko/   → EJECUCIÓN (cómo usarlo)
```

### §0.1. ARQUITECTURA DEL CONOCIMIENTO: GENOMA vs FENOTIPO

**Distinción Crítica para Reducir Fricción Cognitiva**

Este directorio contiene DOS niveles de conocimiento que deben distinguirse claramente:

```yaml
GENOMA_ORKO (Núcleo Ontológico Irreducible):
  
  Definición:
    "Conjunto minimal de elementos teóricos que definen ORKO.
     Obligatorio, universal, NO parametrizable, NO contextual."
     
  Contenido_Genoma:
    - A1-A5: Axiomas fundamentales (verdades irreducibles)
    - P1-P5: Primitivos (estructuras mínimas operacionales)
    - I1-I8: Invariantes (propiedades preservar en todo estado válido)
    - D1-D4: Dominios (dimensiones ortogonales complejidad org)
    - R1-R13: Relaciones fundamentales (modelo relacional teórico)
    - T1-T6: Teoremas (validación formal sistema)
    - V_org: Ecuación maestra (formalización valor)
    - SDA: Ciclo canónico operacional (Sense-Decide-Act, 3 fases)
    - WSLC: Ciclo canónico evolutivo (Initiation→Development→Implementation→Operation→Retirement, 5 fases)
    
  Características_Genoma:
    ✓ Minimalidad: Solo elementos necesarios y suficientes (I1)
    ✓ Ortogonalidad: Componentes mutuamente independientes (I2)
    ✓ Universalidad: Aplica a toda organización, todo contexto
    ✓ Atemporalidad: No cambia con tendencias o tecnologías
    ✓ Auto-contenido: No depende de capas superiores
    
  Analogía_Biológica:
    DNA = Genoma ORKO
    - Mismo en todas células del organismo
    - Define qué es posible (espacio de estados válidos)
    - NO cambia durante vida del organismo

FENOTIPO_ORKO (Expresiones Contextuales Recomendadas):
  
  Definición:
    "Instancias, configuraciones, métricas y patrones que expresan
     el genoma en contextos específicos. Sugerido, parametrizable, adaptable."
     
  Contenido_Fenotipo:
    Métricas_Operativas:
      - H_org (Health organizacional)
      - A_Score, P_Score, D_Score (scores por dominio)
      - Confidence thresholds, precision/recall targets
      
    Thresholds_Heurísticos:
      - H_org ≥ 70 (umbral transformación)
      - Producción/Habilitación 70/30
      - Now/Next/Later 70/20/10
      
    Pesos_Configurables:
      - Coherencia: 0.4, Resonancia: 0.3, Flujo: 0.3 (AOC)
      - Weights en ecuaciones agregadas
      
    Expansiones_Detalladas:
      - SADE: Expansión 16 observables (EX1-8, IN1-8)
      - Subfases detalladas Sense/Decide/Execute
      - Modos delegación M1-M6 (HAIC)
      
    Implementaciones_Concretas:
      - Schemas SQL/JSON (modelo relacional)
      - Constraints específicos CHECK()
      - Governance patterns detallados
      
  Características_Fenotipo:
    ✓ Contextualidad: Ajustable según sector, madurez, cultura org
    ✓ Parametrización: Pesos, thresholds configurables
    ✓ Evolucionabilidad: Puede mejorar con evidencia empírica
    ✓ Opcionalidad: Implementación puede elegir variantes
    
  Analogía_Biológica:
    Proteínas = Fenotipo ORKO
    - Expresión contextual del DNA según ambiente
    - Define cómo se manifiesta el organismo
    - Varía entre individuos y contextos

Relación_Genoma_Fenotipo:
  
  Genoma_Define: QUÉ es válido (espacio de posibilidades)
  Fenotipo_Define: CÓMO se aplica efectivamente (instancia específica)
  
  Ejemplo_Concreto:
    [GENOMA]  P5_Propósito = (outcome, metrics, parent_id)
    [FENOTIPO] outcome_weights = {transactional: 0.7, societal: 0.3}
    
    [GENOMA]  I5_HAIC: "∀ AA_decisional: ∃! accountable_human"
    [FENOTIPO] delegation_modes = {M1, M2, M3, M4, M5, M6}
    
    [GENOMA]  SDA: Sense → Decide → Act (3 fases irreducibles)
    [FENOTIPO] SADE: 16 observables, subfases detalladas
    
  Validación_Fenotipo:
    ∀ fenotipo f: f DEBE respetar constraints genoma
    Ejemplo: H_org threshold puede variar, pero H_org definition (genoma) no

Lectura_Recomendada:
  
  Lectura_Rápida_Ejecutiva (2-3 horas):
    1. Leer SOLO secciones marcadas [GENOMA]
    2. Skip todo [FENOTIPO]
    3. Resultado: Comprensión núcleo ontológico ORKO
    
  Lectura_Completa_Implementador (1-2 días):
    1. Leer [GENOMA] primero (fundamento)
    2. Luego [FENOTIPO] (aplicación)
    3. Resultado: Listo para implementar/adaptar ORKO
    
  Lectura_Validación_Auditor:
    1. [GENOMA]: Verificar compliance obligatorio
    2. [FENOTIPO]: Revisar si instancia es razonable
    3. Resultado: Certificar implementación ORKO válida

Etiquetado_Documentos:
  
  00_introduccion.md (este archivo):
    - Estructura: 100% meta-información
    
  01_axiomas.md:
    - 100% [GENOMA]
    - A1-A5 son fundamento irreducible
    
  02_primitivos.md:
    - [GENOMA]: Definiciones P1-P5, derivaciones formales
    - [FENOTIPO]: Ejemplos aplicación, taxonomías detalladas
    
  03_invariantes.md:
    - [GENOMA]: Enunciados I1-I8, formulaciones formales
    - [FENOTIPO]: Validaciones concretas, governance patterns
    
  04_ciclo_fundamental.md:
    - [GENOMA]: SDA canónico (3 fases), WSLC, recursión
    - [FENOTIPO]: Expansión SADE (16 observables), subfases
    
  05_dominios.md:
    - [GENOMA]: D1-D4 definiciones, ortogonalidad
    - [FENOTIPO]: Scores (A/P/D), thresholds, heurísticas
    
  06_teoremas_fundamentales.md:
    - 100% [GENOMA]
    - T1-T6 validación formal sistema
    
  07_ecuacion_maestra.md:
    - [GENOMA]: V_org ecuación, derivación desde P5
    - [FENOTIPO]: Pesos AOC, parametrizaciones contextuales
    
  08_modelo_relacional.md:
    - [GENOMA]: E1-E5, R1-R13 (formas relacionales teóricas)
    - [FENOTIPO]: Schemas SQL/JSON, constraints implementación

Beneficio_Distinción:
  
  Problema_Resuelto:
    "Lector percibe framework complejo y cargado,
     contradice invariantes I1 (Minimalidad) e I2 (Ortogonalidad)"
     
  Solución:
    - Genoma es MINIMAL (5 axiomas, 5 primitivos, 8 invariantes, 4 dominios)
    - Complejidad aparente es FENOTIPO (opcional, contextual)
    - I1/I2 aplican a genoma, NO a fenotipo
    
  Validación_I1_Minimalidad:
    Genoma_Size = |{A1-A5, P1-P5, I1-I8, D1-D4, R1-R13, T1-T6}|
                = 5 + 5 + 8 + 4 + 13 + 6
                = 41 elementos teóricos
    ✓ Minimal (T3 demuestra no existe conjunto < 5 primitivos completo)
    
  Claridad_Cognitiva:
    Antes: "ORKO tiene 100+ conceptos, es complejo"
    Después: "Genoma ORKO = 41 elementos, fenotipo = expresiones contextuales"
```

**IMPORTANTE**: En todo el directorio `00_fundamentos_teoricos/`, las secciones están etiquetadas con `[GENOMA]` o `[FENOTIPO]` para guiar la lectura.

## §1. ESTRUCTURA MODULAR

```yaml
Organización_8_Módulos:

  00_introduccion.md (este archivo):
    Propósito: Guía navegación, contexto, trazabilidad
    Contenido: Estructura + orden lectura + índice conceptual
    
  01_axiomas.md:
    Título: "PARTE I: Axiomas Irreducibles A1-A5"
    Propósito: Fundamentos NO derivables del sistema
    Contenido:
      - A1: Transformación (base todo cambio)
      - A2: Capacidad (agencia efectúa transformación)
      - A3: Información (coordinación requiere estado)
      - A4: Límite (realidad finita requiere restricciones)
      - A5: Propósito (intencionalidad dirige sistema)
    
  02_primitivos.md:
    Título: "PARTE II: Derivación Primitivos P1-P5"
    Propósito: Mínima estructura operacionalizar axiomas
    Contenido:
      - P1: Capacidad (desde A2) - substrate, capacity_type, rol
      - P2: Flujo (desde A1) - secuencia transformaciones
      - P3: Información (desde A3) - tipo, persistencia, formato
      - P4: Límite (desde A4) - temporal, económico, organizacional
      - P5: Propósito (desde A5) - outcome, métricas, jerarquía
    
  03_invariantes.md:
    Título: "PARTE III: Invariantes Sistema I1-I8"
    Propósito: Propiedades que DEBEN preservarse en todo estado válido
    Contenido:
      - I1: Minimalidad (primitivos necesarios y suficientes)
      - I2: Ortogonalidad (primitivos mutuamente independientes)
      - I3: Trazabilidad (auditabilidad transformaciones)
      - I4: Clasificación Contextual (resolución paradoja AI/humano)
      - I5: HAIC (Human-AI Collaboration - primacía humana explícita)
      - I6: Trajectory-Awareness (progresión autonomía documentada)
      - I7: Emergencia de Complejidad (prácticas según madurez org)
      - I8: Adaptación Contextual (parametrización metodológica)
    
  04_ciclo_fundamental.md:
    Título: "PARTE IV: Ciclo Fundamental (SDA + WSLC)"
    Propósito: Patrones universales transformación intencional
    Contenido:
      - §1: Ciclo SDA (Sense-Decide-Act) - operacional
        · Derivación desde P1+P3+P5
        · 3 fases irreducibles + subfases
        · 16 observables (EX1-8 + IN1-8)
        · Propiedades: Universalidad, Recursividad, Aceleración
      - §2: Ciclo WSLC (Work System Life Cycle) - evolutivo
        · Fases: Initiation → Development → Implementation → Operation → Retirement
        · Complementariedad SDA (operación vs evolución sistema)
        · Recursión L0-L3 (strategic → tactical → operational)
    
  05_dominios.md:
    Título: "PARTE IV: Dominios Ortogonales D1-D4"
    Propósito: Dimensiones irreducibles complejidad organizacional
    Contenido:
      - §3: Derivación 4 dominios desde primitivos
      - §4: D1 Arquitectura (estructura estática)
      - §5: D2 Percepción (captura información)
      - §6: D3 Decisión (elección bajo límites)
      - §7: D4 Operación (ejecución dinámica)
      - §8: Síntesis - Interacciones dominios
        · Ciclo OODA organizacional (D2→D3→D4→D2)
        · D1 como estructura habilitante
        · Cadencias temporales
        · Health Score H_org integrado
        · Emergencia niveles complejidad
    
  06_teoremas_fundamentales.md:
    Título: "PARTE IV: Teoremas Fundamentales Sistema"
    Propósito: Validación formal propiedades sistema
    Contenido:
      - T1: Completitud Ontológica (P1-P5 cubren todo concepto org)
      - T2: Ortogonalidad Total (primitivos independientes)
      - T3: Minimalidad (no existe conjunto < 5 completo)
      - T4: Suficiencia Dominios (D1-D4 necesarios y suficientes)
      - T5: Emergencia Niveles (prácticas emergen según complejidad)
      - T6: Composicionalidad (primitivos componibles preservando tipos)
    
  07_ecuacion_maestra.md:
    Título: "PARTE IV: Ecuación Maestra Valor Organizacional"
    Propósito: Formalización matemática valor entregado por sistema
    Contenido:
      - §10: Ecuación V_org(t) = Σ outcomes - Σ costs
      - Descomposición outcomes (output × propósito × volume)
      - Descomposición costs (capacidad × tiempo × unit_cost)
      - Métricas derivadas: η_org (eficiencia), ROI, VFV (velocity)
      - Optimización portfolio bajo constraints (H_org ≥ 70)
      - Invariante health-valor (H_org < 70 → V_org degrada)
    
  08_modelo_relacional.md:
    Título: "PARTE V: Modelo Relacional Primitivos"
    Propósito: Estructura datos y relaciones TEÓRICAS entre primitivos
    Contenido:
      - Entidades primitivas (E1-E5 desde P1-P5) → TEORÍA PURA
      - Relaciones fundamentales (R1-R13):
        · R1-R11: Relaciones entre primitivos
        · R12: Capacidad ⊕⊗ Capacidad (composición)
        · R13: Capacidad(Alg) ← Capacidad(Humana) (delegación HAIC)
      - Multiplicidades (1:1, 1:N, N:M)
      - Constraints integridad referencial
    
    Scope: MODELO TEÓRICO (solo primitivos irreducibles)
    
    Nota: Arquitectura extiende con entidades COMPUESTAS (E6-E7) 
          y relaciones DERIVADAS (R14-R15).
          Ver ../10_arquitectura_orko/03_relaciones.md para extensiones.

Total_Tamaño: ~165 KB
```

## §2. ORDEN LECTURA RECOMENDADO

```yaml
Secuencia_Lógica_Derivación:

  Nivel_1_Fundamentos (CRÍTICO - leer primero):
    1. 01_axiomas.md
       "¿Cuáles son las VERDADES IRREDUCIBLES del sistema?"
       Output: A1-A5 (base de todo)
       
    2. 02_primitivos.md
       "¿Qué ESTRUCTURAS MÍNIMAS operacionalizan axiomas?"
       Output: P1-P5 (building blocks)
       Prerequisito: A1-A5
       
    3. 03_invariantes.md
       "¿Qué PROPIEDADES debe preservar sistema válido?"
       Output: I1-I8 (constraints)
       Prerequisito: A1-A5, P1-P5
       
  Nivel_2_Ciclos_y_Dominios (ESENCIAL - leer segundo):
    4. 04_ciclo_fundamental.md
       "¿Cuáles son PATRONES UNIVERSALES transformación?"
       Output: SDA (operacional) + WSLC (evolutivo)
       Prerequisito: P1-P5
       
    5. 05_dominios.md
       "¿Cuáles son DIMENSIONES IRREDUCIBLES complejidad org?"
       Output: D1-D4 dominios + interacciones + H_org
       Prerequisito: P1-P5, SDA
       
  Nivel_3_Validación_y_Formalización (COMPLEMENTARIO - leer tercero):
    6. 06_teoremas_fundamentales.md
       "¿Cómo VALIDAMOS propiedades sistema formalmente?"
       Output: T1-T6 teoremas con demostraciones
       Prerequisito: Todo lo anterior
       
    7. 07_ecuacion_maestra.md
       "¿Cómo MEDIMOS valor organizacional?"
       Output: V_org ecuación + métricas derivadas
       Prerequisito: P1-P5, D1-D4
       
    8. 08_modelo_relacional.md
       "¿Cómo se RELACIONAN primitivos estructuralmente?"
       Output: Entidades E1-E5 + Relaciones R1-R13
       Prerequisito: P1-P5

Lectura_Rápida_Ejecutiva (1-2 horas):
  - 01_axiomas.md (A1-A5 solamente)
  - 02_primitivos.md (definiciones P1-P5, skip demostraciones)
  - 04_ciclo_fundamental.md (SDA + WSLC esencial)
  - 05_dominios.md (§3 derivación + §8 síntesis solamente)
```

## §3. TRAZABILIDAD VERTICAL

```yaml
Cadena_Derivación:

  Layer_0_Axiomas:
    A1-A5: Verdades irreducibles
    Fuente: Fenomenología, Teoría Sistemas, Cibernética
    Características: NO derivables, universales, mínimos
    
  Layer_1_Primitivos:
    P1-P5: Estructuras operacionalizan axiomas
    Derivación: A1→P2, A2→P1, A3→P3, A4→P4, A5→P5
    Características: Necesarios, suficientes, ortogonales, medibles
    
  Layer_2_Invariantes:
    I1-I8: Propiedades preservar en todo estado
    Derivación: Lógica desde A1-A5 + P1-P5
    Características: Verificables, ejecutables como constraints
    
  Layer_2_Modelo_Relacional:
    E1-E5: Entidades primitivas (desde P1-P5)
    R1-R13: Relaciones fundamentales
    Ubicación: 08_modelo_relacional.md
    Características: TEORÍA PURA (mínimo irreducible)
    
  Layer_3_Contratos_Base:
    C1-C5: Esquemas operables primitivos
    Ubicación: ../10_arquitectura_orko/01_contratos.md
    Derivación: P1→C1, P2→C2, P3→C3, P4→C4, P5→C5
    
  Layer_4_Extensiones_Arquitectónicas:
    E6-E7: Entidades COMPUESTAS (no primitivos)
    R14-R15: Relaciones DERIVADAS
    Ubicación: ../10_arquitectura_orko/01_contratos.md + ../10_arquitectura_orko/03_relaciones.md
    Derivación:
      E6: Snapshot(E1+E2+E4+E5) - coherencia temporal
      E7: Instance(E2) - tracking operacional
      R14: Transitions DAG sobre E6
      R15: Transition ejecutada por E2
    
  Layer_5_Principios:
    PD1-PD75: Reglas diseño arquitectónico (75 principios operativos)
    Ubicación: ../10_arquitectura_orko/02_diseño.md
    Derivación: I1-I8 → PD1-PD75
    Cobertura:
      - PD1-PD45: Desde invariantes core I1-I8
      - PD46-PD75: Desde Waves 0-6 (gap remediation)
    
  Layer_6_Patterns:
    Patterns D1-D4 + Cross-cutting
    Ubicación: ../10_arquitectura_orko/04_vistas.md + ../10_arquitectura_orko/05_patrones.md
    Derivación: PD1-PD75 → Patterns recurrentes (20+ validados)
    
  Layer_7_Metodología:
    18 fases metodológicas (§0-§18)
    Ubicación: ../30_metodologia_orko/
    Derivación: SDA + WSLC + D1-D4 → Secuencia ejecución

Frontera_Crítica_Teoría_Arquitectura:
  Layer 0-2: TEORÍA PURA (axiomas, primitivos, invariantes, modelo relacional)
    - Fundamentos irreducibles
    - Mínimo necesario y suficiente (I1)
    - Independiente de implementación
    
  Layer 3-7: ARQUITECTURA OPERABLE (contratos, extensiones, principios, patterns)
    - Derivación formal desde teoría
    - Entidades compuestas (E6-E7) desde primitivos (E1-E5)
    - Relaciones extendidas (R14-R15) desde fundamentales (R1-R13)
    - Trazabilidad completa a fundamentos

Propiedad_Trazabilidad_Total:
  ∀ elemento ORKO: ∃ camino derivación desde axiomas A1-A5
  Verificable: Todo elemento cita su origen formal
```

## §4. ÍNDICE CONCEPTUAL

```yaml
Conceptos_Clave_Por_Módulo:

  Axiomas (01):
    - A1_Transformación: Base todo cambio intencional
    - A2_Capacidad: Agencia efectúa transformación
    - A3_Información: Coordinación requiere estado compartido
    - A4_Límite: Realidad finita impone restricciones
    - A5_Propósito: Intencionalidad dirige sistema
    
  Primitivos (02):
    - P1_Capacidad: (substrate, capacity_type, rol_valor)
    - P2_Flujo: (steps, dependencies, type)
    - P3_Información: (type, persistence, format)
    - P4_Límite: (type, scope, enforcement)
    - P5_Propósito: (outcome, metrics, parent_id)
    
  Invariantes (03):
    - I1_Minimalidad: Sistema usa mínimo necesario
    - I2_Ortogonalidad: Primitivos mutuamente independientes
    - I3_Trazabilidad: Auditabilidad completa
    - I4_Clasificación_Contextual: Resolución AI/humano
    - I5_HAIC: Human-AI Collaboration (primacía humana explícita)
    - I6_Trajectory-Awareness: Progresión autonomía documentada
    - I7_Emergencia_Complejidad: Prácticas según madurez org
    - I8_Adaptación_Contextual: Parametrización metodológica
    
  Ciclos (04):
    - SDA: Sense → Decide → Act (patrón operacional) [GENOMA]
    - WSLC: I → D → Impl → O → R (patrón evolutivo) [GENOMA]
    - 16_Observables_SADE: EX1-8 (externos) + IN1-8 (internos) [FENOTIPO]
    - Recursión_Multi-Nivel: L0-L3 (Tarea→Feature→Platform→Transformation) [FENOTIPO]
    
  Dominios (05):
    - D1_Arquitectura: Estructura estática
    - D2_Percepción: Captura información
    - D3_Decisión: Elección bajo límites
    - D4_Operación: Ejecución dinámica
    - H_org: Health organizacional integrado
    - Ortogonalidad: 6 pares validados (D1⊥D2, etc.)
    
  Teoremas (06):
    - T1_Completitud: P1-P5 expresan todo concepto org
    - T2_Ortogonalidad: Primitivos independientes
    - T3_Minimalidad: No existe conjunto < 5 completo
    - T4_Suficiencia_Dominios: D1-D4 necesarios y suficientes
    - T5_Emergencia: Prácticas emergen por complejidad
    - T6_Composicionalidad: Primitivos preservan tipos
    
  Ecuación (07):
    - V_org: Valor organizacional (outcomes - costs)
    - η_org: Eficiencia global
    - ROI_Habilitación: Retorno inversión flujos habilitación
    - Constraint: H_org ≥ 70 para transformaciones
    
  Modelo_Relacional (08):
    - E1-E5: Entidades primitivas desde P1-P5 → TEORÍA PURA
    - R1-R13: Relaciones fundamentales
      · R1-R11: Entre primitivos P1-P5
      · R12: Capacidad ⊕⊗ Capacidad (composición)
      · R13: Capacidad(Alg) ← Capacidad(Humana) (delegación HAIC)
    - Multiplicidades: 1:1, 1:N, N:M
    - Integridad: Foreign keys, constraints, DAG validation
    
    Extensiones_Arquitectónicas (ver ../10_arquitectura_orko/):
      · E6: Estado Arquitectónico - Snapshot(E1+E2+E4+E5)
      · E7: Ejecución Flujo - Instance(E2)
      · R14: Estado Transitions - DAG evolutivo
      · R15: Transition-Flow - Planning-execution link
```

1. **PARTE I — Axiomas Irreducibles (01_axiomas.md)**
2. **PARTE II — Derivación de Primitivos (02_primitivos.md)**
3. **PARTE III — Invariantes y Axiomas Derivados (03_invariantes.md)**
4. **PARTE IV — Ciclo Fundamental (SDA + WSLC) (04_ciclo_fundamental.md)**
5. **PARTE V — Dominios Ortogonales (05_dominios.md)**
6. **PARTE VI — Teoremas Fundamentales (06_teoremas_fundamentales.md)**
7. **PARTE VII — Ecuación Maestra (07_ecuacion_maestra.md)**
8. **PARTE VIII — Modelo Relacional de Primitivos (08_modelo_relacional.md)**
