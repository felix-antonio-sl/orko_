# PARTE IV: CICLO FUNDAMENTAL

- [PARTE IV: CICLO FUNDAMENTAL](#parte-iv-ciclo-fundamental)
  - [Ciclo fundamental](#ciclo-fundamental)
    - [§1. CICLO SDA (Sense-Decide-Act)](#1-ciclo-sda-sense-decide-act)
    - [§2. CICLO WSLC (Work System Life Cycle)](#2-ciclo-wslc-work-system-life-cycle)

## Ciclo fundamental

### §1. CICLO SDA (Sense-Decide-Act)

**[GENOMA]** - Ciclo Canónico Irreducible

```yaml
Derivación_Formal_Desde_Primitivos:
  
  Pregunta_Ontológica:
    "¿Cuál es el patrón MINIMAL universal para transformación intencional?"
    
  Derivación:
    Dados: P1 (Capacidad), P3 (Información), P5 (Propósito)
    
    ∀ transformación intencional T:
      T requiere conocer estado actual → SENSE (P3)
      T requiere seleccionar acción según objetivo → DECIDE (P5)
      T requiere efectuar cambio → ACT (P1)
      
    Validación_Minimalidad:
      ¿Puede existir transformación intencional sin SENSE? NO (operaría ciego)
      ¿Puede existir transformación intencional sin DECIDE? NO (acción aleatoria)
      ¿Puede existir transformación intencional sin ACT? NO (inerte, sin efecto)
      
    Conclusión: SDA = (Sense, Decide, Act) es patrón IRREDUCIBLE
      - NO existe patrón < 3 fases para transformación intencional
      - SDA es MINIMAL y UNIVERSAL (genoma)

Estructura_SDA_Formal:
  
  Definición_Matemática:
    SDA: (Estado × Propósito × Capacidad) → Estado'
    
    Donde:
      Sense: Estado_ambiente → Información_interna (observación)
      Decide: (Información × Propósito) → Acción_seleccionada (cognición)
      Act: (Acción × Capacidad) → Estado_ambiente' (efectuación)
      
  Propiedades_Algebraicas:
    - Composicionalidad: SDA puede contener SDA (recursión)
    - Identidad: SDA(null_action) = Estado (no-op)
    - Asociatividad: SDA₁ ∘ SDA₂ ∘ SDA₃ = (SDA₁ ∘ SDA₂) ∘ SDA₃

Fases_Canónicas_Genoma:

  SENSE (Observación):
    Definición: "Capturar información estado ambiente relevante para propósito"
    Fundamentación: Axioma A3 (Información estructura significado)
    Input: Estado_ambiente + Sensores (P1)
    Output: Información_observada (P3)
    Constraint: ∀ SDA: SENSE ≠ ∅ (siempre hay observación, aunque mínima)
    
  DECIDE (Cognición):
    Definición: "Seleccionar acción según propósito y límites"
    Fundamentación: Axioma A5 (Propósito orienta)
    Input: Información_observada + Propósito (P5) + Límites (P4)
    Output: Acción_seleccionada + Justificación_decisión
    Constraint: Capacidad.type ≥ C1 (decisión requiere inteligencia)
    
  ACT (Efectuación):
    Definición: "Ejecutar acción seleccionada, modificando estado ambiente"
    Fundamentación: Axioma A2 (Capacidad efectúa transformación)
    Input: Acción_seleccionada + Capacidad_ejecutora (P1)
    Output: Estado_ambiente' (transformado)
    Constraint: ∃ Capacidad con substrate capaz ejecutar acción

Propiedades_Universales_Genoma:
  
  P_SDA_1_Universalidad:
    Enunciado: "∀ transformación intencional T: T implementa SDA"
    Validación: Por definición transformación intencional (A5)
    Scope: Humanos, animales, algoritmos, organizaciones
    
  P_SDA_2_Recursividad:
    Enunciado: "SDA puede contener sub-SDA en cualquier fase"
    Ejemplo: DECIDE puede ejecutar SDA interno para evaluar opciones
    Propiedad: SDA forma estructura fractal (self-similar)
    
  P_SDA_3_Minimalidad:
    Enunciado: "¬∃ ciclo < 3 fases que preserve intencionalidad"
    Demostración: Por validación negativa (arriba)
    Implicación: SDA es genoma irreducible

Fundamentación_Teórica:
  Inspiración: OODA (Boyd), Control Theory, TSTI-SADE, Cognitive Science
  NOTA: ORKO deriva SDA desde primitivos P1+P3+P5 (bottom-up)
        Teorías externas validan convergencia (top-down)
```

---

**[FENOTIPO]** - Expansión SADE (Sense-Analyze-Decide-Execute)

```yaml
NOTA_Fenotipo:
  "Esta sección describe una INSTANCIA RECOMENDADA del genoma SDA.
   Es contextual, parametrizable, NO obligatoria.
   Fuente inspiracional: TSTI-SADE (90_referencias_fundacionales/04_...)"

Expansión_SENSE:
  
  Subfases_Detalladas:
    Detectar (C0): Sensores capturan señales raw
      Latencia: Microsegundos a milisegundos
      Ejemplos: IoT sensors, log collectors, API polling
      
    Comprender (C1): Interpretar señales en contexto
      Latencia: Segundos a minutos
      Ejemplos: Pattern recognition, anomaly detection
      
    Proyectar (C2-C3): Anticipar tendencias futuras
      Latencia: Minutos a horas
      Ejemplos: Forecasting, scenario planning
      
  Observables_TSTI (16 dimensiones):
    
    Externos (EX1-8):
      EX1: Demanda_mercado (volumen, tendencias)
      EX2: Competidores (movimientos, share)
      EX3: Regulación (nuevas leyes, compliance)
      EX4: Tecnología (disrupciones, oportunidades)
      EX5: Feedback_clientes (NPS, quejas)
      EX6: Eventos_disruptivos (crisis, shocks)
      EX7: Factores_sociales (cultura, demografía)
      EX8: Indicadores_económicos (PIB, tasas)
      
    Internos (IN1-8):
      IN1: Velocidad_decisión (cycle time)
      IN2: Salud_talento (engagement, turnover)
      IN3: Eficiencia_flujos (throughput, waste)
      IN4: Calidad_outputs (defects, rework)
      IN5: Utilización_capacidades (idle time)
      IN6: Alineación_estratégica (OKR progress)
      IN7: Compliance_interna (policy violations)
      IN8: Debt_acumulado (technical, process, cultural)
      
  Aplicabilidad_Contextual:
    - Org madura: Monitorear 16 observables (dashboard completo)
    - Org startup: Foco en EX1, EX5, IN3, IN4 (4 críticos)
    - Contexto estable: Polling lento (diario/semanal)
    - Contexto volátil: Streaming real-time

Expansión_DECIDE:
  
  Modos_Decisión_por_Complejidad:
    
    Directa (C1, <10ms):
      Descripción: Lookup table, regla simple
      Ejemplos: Routing, classification
      Delegación_HAIC: M6 (AA autónomo, humano notificado)
      
    Basada_Reglas (C1, <1seg):
      Descripción: Motor reglas (if-then-else)
      Ejemplos: Business rules, compliance checks
      Delegación_HAIC: M5 (AA propone, H aprueba batch)
      
    Asociativa (C1-C2, 1seg-1min):
      Descripción: Pattern matching, similarity search
      Ejemplos: Recommender systems, case-based reasoning
      Delegación_HAIC: M4 (H + AA coproducen)
      
    Analítica (C2-C3, 1min-horas):
      Descripción: Optimización, simulación, análisis profundo
      Ejemplos: Planning, resource allocation, strategy
      Delegación_HAIC: M2-M3 (AA informa, H decide)
      
  Output_Enriquecido:
    - Acción_recomendada (qué hacer)
    - Justificación (por qué)
    - Confianza (certeza 0-1)
    - Alternativas (opciones descartadas)
    - Riesgos (qué puede fallar)

Expansión_ACT:
  
  Subfases_Ejecución:
    
    Planificar (C1):
      Descomponer acción en pasos ejecutables
      Asignar recursos, secuenciar
      
    Especificar (C1):
      Detallar parámetros exactos cada paso
      Validar precondiciones
      
    Ejecutar (C0):
      Efectuar transformación física/digital
      Monitorear progreso (SDA recursivo)
      
  Monitoreo_Recursivo:
    Durante ejecución ACT, ejecutar SDA micro-ciclo:
      SENSE: ¿Ejecución progresa OK?
      DECIDE: ¿Continuar o abortar?
      ACT: Ajustar o escalar excepción
      
  Límite_Recursión_Heurístico:
    Máximo 3 niveles anidados (Miller 7±2 capacidad cognitiva)
    Nivel 0: Tarea atómica
    Nivel 1: Tarea compuesta
    Nivel 2: Workflow
    Nivel 3: Orquestación
    Nivel 4+: Complejidad no manejable, simplificar

Aceleración_Algorítmica:
  
  Comparativa_Latencias (orden magnitud):
    Humano SENSE: 100ms - 10seg
    Algorítmico SENSE: 1µs - 100ms (100x - 100,000x más rápido)
    
    Humano DECIDE: 1seg - horas
    Algorítmico DECIDE: 1ms - segundos (1,000x - 10,000x)
    
    Humano ACT (digital): 1seg - minutos
    Algorítmico ACT: 1ms - segundos (1,000x - 100,000x)
    
  Implicación:
    AA permite ciclos SDA 100x-100,000x más rápidos
    → Valor organizacional aumenta proporcionalmente (V_org ∝ velocity)
    → Justifica investment en automatización (ROI)
```

### §2. CICLO WSLC (Work System Life Cycle)

**[GENOMA]** - Ciclo Vida Universal

```yaml
Derivación_Formal_Complementariedad:
  
  Pregunta_Ontológica:
    "¿Cuál es el patrón universal para EVOLUCIÓN de work systems?"
    
  Complementariedad_SDA_WSLC:
    SDA: Patrón OPERACIÓN (transformación DENTRO de sistema existente)
    WSLC: Patrón EVOLUCIÓN (transformación DEL sistema mismo)
    
    Analogía_Biológica:
      SDA = Metabolismo (operación momento-a-momento)
      WSLC = Desarrollo orgánico (nacimiento → madurez → muerte)
      
  Fundamentación:
    Todo work system WS tiene ciclo vida finito:
      - WS nace (creación intencional por A5)
      - WS opera (entrega valor durante W4)
      - WS muere (obsolescencia, reemplazo por WS')

Fases_WSLC_Canónicas:

  W1_INITIATION (Concepción):
    Definición: "Detectar necesidad y aprobar creación sistema"
    Input: Oportunidad o problema identificado
    Output: Visión + Caso negocio + Autorización recursos
    Fundamentación: A5 (todo sistema tiene propósito explícito)
    Constraint: ∀ WS: W1 precede W2 (no se desarrolla sin visión)
    
  W2_DEVELOPMENT (Desarrollo):
    Definición: "Construir sistema funcional"
    Input: Visión aprobada + Recursos asignados
    Output: Sistema funcional validado
    Fundamentación: A2 (capacidad efectúa transformación)
    Constraint: ∀ WS: W2 precede W3 (no se despliega sin construcción)
    
  W3_IMPLEMENTATION (Despliegue):
    Definición: "Poner sistema en operación productiva"
    Input: Sistema funcional
    Output: Sistema operativo en ambiente producción
    Fundamentación: Transición Estado₁ → Estado₂ (A1)
    Constraint: ∀ WS: W3 precede W4 (no opera sin despliegue)
    
  W4_OPERATION (Operación):
    Definición: "Ejecutar sistema para entregar valor sostenido"
    Input: Sistema operativo
    Output: Valor acumulado + Feedback uso
    Fundamentación: P5 (propósito) se realiza en esta fase
    Relación_SDA: Esta fase ejecuta SDA repetidamente (operación)
    Constraint: W4 es fase más larga (típicamente 80-90% ciclo vida)
    
  W5_RETIREMENT (Retiro):
    Definición: "Desactivar sistema preservando conocimiento"
    Input: Sistema obsoleto o ineficiente
    Output: Sistema desactivado + Lecciones aprendidas
    Fundamentación: Ciclo vida finito (entropía, obsolescencia)
    Transición: Migrar a sistema sucesor (nuevo W1)

Integración_SDA_WSLC:
  
  Relación_Temporal:
    WSLC = Escala larga (meses-años)
    SDA = Escala corta (microsegundos-días)
    
  Relación_Estructural:
    ∀ fase W ∈ WSLC: W ejecuta múltiples instancias SDA
    Ejemplo: W2_Development ejecuta miles de SDA (codificar, revisar, testear)
    
  Relación_Alcance:
    SDA transforma DENTRO del sistema
    WSLC transforma EL sistema mismo (meta-nivel)
    
  Recursión_Multi-Nivel:
    L0: Tarea (SDA básico)
    L1: Feature (WSLC corto, días-semanas)
    L2: Platform (WSLC medio, meses-trimestres)
    L3: Transformation (WSLC largo, años)

Propiedades_Universales_Genoma:
  
  P_WSLC_1_Universalidad:
    Enunciado: "∀ work system WS: WS atraviesa WSLC completo"
    Validación: Ciclo vida emerge de naturaleza evolutiva sistemas
    Excepción: Sistemas instantáneos (despreciables en práctica)
    
  P_WSLC_2_Secuencialidad:
    Enunciado: "Saltar fases WSLC → problemas futuros"
    Evidencia: Deploy sin development = bugs; Operation sin implementation = caos
    Implicación: W1 → W2 → W3 → W4 → W5 es secuencia obligatoria
    
  P_WSLC_3_Paralelismo_Organizacional:
    Enunciado: "Org ejecuta N instancias WSLC simultáneas"
    Ejemplo: Sistema_A en W4, Sistema_B en W2, Sistema_C en W1
    Implicación: Portfolio management crítico (capacity allocation)
    
  P_WSLC_4_Feedback_Evolutivo:
    Enunciado: "W4_Operation informa {W5_Retirement, W1_Next_Iteration}"
    Propiedad: Ciclo cerrado con aprendizaje
    Implicación: Org que aprende mejora WSLC sucesivos

Fundamentación_Teórica:
  Inspiración: Alter TSTI, SDLC, Agile Lifecycle, Change Management
  NOTA: ORKO deriva WSLC desde primitivos (ciclo vida universal WS)
        Teorías externas validan convergencia
```

---

**[FENOTIPO]** - Operacionalización WSLC

```yaml
NOTA_Fenotipo:
  "Esta sección describe configuraciones OPERATIVAS del genoma WSLC.
   Duraciones, estrategias, subfases son contextuales y parametrizables."

Duraciones_Indicativas (% ciclo vida):
  
  NOTA: Estos porcentajes son ORIENTATIVOS (orden magnitud)
        NO deben sumarse estrictamente
        Varían según contexto, madurez org, tipo sistema
        
  W1_INITIATION: 5-10%
    Startup: 1-2% (decisiones rápidas)
    Corp tradicional: 10-15% (governance pesado)
    
  W2_DEVELOPMENT: 5-10%
    Greenfield: 5-8%
    Legacy modernization: 10-20% (complejidad integración)
    
  W3_IMPLEMENTATION: 1-5%
    Cloud-native: 1-2% (deployment automatizado)
    On-premise enterprise: 5-10% (coordinación compleja)
    
  W4_OPERATION: 80-90%
    Sistema estable: 90%+
    Sistema experimental: 60-70% (ciclo vida corto)
    
  W5_RETIREMENT: <5%
    Gradual: 2-5%
    Big bang cutover: <1%

Estrategias_W3_Implementation:
  
  Big_Bang:
    Descripción: Cutover total en momento T
    Riesgo: Alto (rollback difícil)
    Uso: Sistemas pequeños, bajo tráfico
    
  Canary:
    Descripción: Deploy a subset usuarios (5-10%), luego expandir
    Riesgo: Medio
    Uso: Alta disponibilidad, validación gradual
    
  Blue_Green:
    Descripción: Dos ambientes paralelos, switch instantáneo
    Riesgo: Medio-Bajo
    Uso: Zero-downtime deployment
    
  Feature_Flags:
    Descripción: Deploy código inactivo, activar selectivamente
    Riesgo: Bajo
    Uso: A/B testing, gradual rollout, kill switch

Subfases_Operativas:
  
  W2_DEVELOPMENT_Detallado:
    Design: Arquitectura, interfaces, contratos
    Build: Codificación, configuración
    Test: Unit, integration, E2E, performance
    
  W3_IMPLEMENTATION_Detallado:
    Deploy: Código a ambiente producción
    Train: Capacitación usuarios, documentación
    Cutover: Switch tráfico a nuevo sistema
    
  W4_OPERATION_Detallado:
    Run: Ejecución normal (múltiples SDA)
    Monitor: Observabilidad, alerting
    Maintain: Bug fixes, patches
    Enhance: Mejoras incrementales (micro-WS LCs)

Ciclos_Recursivos:
  
  Feature_Lifecycle (días-semanas):
    Típico: 2-4 semanas (sprint)
    W1: Story kickoff (1 día)
    W2: Development (5-10 días)
    W3: Deploy (1 día)
    W4: In production (indefinido)
    W5: Feature flag off / deprecated (1 día)
    
  Platform_Lifecycle (meses-trimestres):
    Típico: 3-12 meses
    Ejemplo: Migración microservices, platform upgrade
    
  Transformation_Lifecycle (años):
    Típico: 1-3 años
    Ejemplo: Digital transformation, cloud migration completa
```
