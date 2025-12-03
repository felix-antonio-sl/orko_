# ARQUITECTURA DEL SISTEMA ORKO

**Especificación Lógica - Puente entre Teoría y Práctica**

- [ARQUITECTURA DEL SISTEMA ORKO](#arquitectura-del-sistema-orko)
  - [§0. PROPÓSITO Y POSICIÓN](#0-propósito-y-posición)
  - [§1. ESTRUCTURA MODULAR](#1-estructura-modular)
  - [§2. CONTENIDO MODULAR RESUMIDO](#2-contenido-modular-resumido)
    - [PARTE I: Contratos Canónicos (01\_contratos.md)](#parte-i-contratos-canónicos-01_contratosmd)
    - [PARTE II: Principios de Diseño (02\_diseño.md)](#parte-ii-principios-de-diseño-02_diseñomd)
    - [PARTE III: Modelo Relacional (03\_relaciones.md)](#parte-iii-modelo-relacional-03_relacionesmd)
    - [PARTE IV: Vistas Arquitectónicas (04\_vistas.md y 05\_patrones.md)](#parte-iv-vistas-arquitectónicas-04_vistasmd-y-05_patronesmd)
    - [PARTE V: Patterns \& Anti-Patterns (05\_patrones.md)](#parte-v-patterns--anti-patterns-05_patronesmd)
  - [§3. TRAZABILIDAD VERTICAL](#3-trazabilidad-vertical)
  - [§4. USO DEL MÓDULO](#4-uso-del-módulo)
    - [Para Arquitectos](#para-arquitectos)
    - [Para Implementadores](#para-implementadores)
    - [Para Metodólogos](#para-metodólogos)
  - [§5. COHERENCIA Y VERIFICACIÓN](#5-coherencia-y-verificación)

## §0. PROPÓSITO Y POSICIÓN

```yaml
Naturaleza:
  "Arquitectura ORKO = Operacionalización de fundamentos teóricos.
   Traduce axiomas A1-A5 y primitivos P1-P5 en especificaciones
   ejecutables: contratos, principios, relaciones, vistas, patterns."

Posición_Triádica:
  ../00_fundamentos_teoricos/ → 10_arquitectura_orko/ → ../30_metodologia_orko/
  Ontológico           → Lógico                    → Práctico
  ¿Qué ES el sistema?  → ¿Cómo DISEÑARLO?          → ¿Cómo USARLO?

Principio_Derivación:
  "Todo elemento deriva formalmente de fundamentos teóricos.
   Trazabilidad completa: A→P→I→C→E→PD→Patterns.
   Nada inventado, todo fundamentado."

Extensión_Modelo_Teórico:
  "Arquitectura EXTIENDE el modelo relacional teórico puro con:
   - Entidades COMPUESTAS (E6-E7) derivadas de primitivos (E1-E5)
   - Relaciones DERIVADAS (R14-R15) sobre entidades compuestas
   
   Fundamentos: E1-E5, R1-R13 (mínimo irreducible, teoría pura)
   Arquitectura: E1-E7, R1-R15 (extensión formal operable)
   
   Ver ../00_fundamentos_teoricos/08_modelo_relacional.md para base teórica."

Alcance:
  - Contratos C1-C5: Especificación formal primitivos P1-P5
  - Entidades E6-E7: Compuestos arquitectónicos (Estado, Ejecución)
  - Principios PD1-PD76: Reglas diseño desde invariantes I1-I8 + Guidelines G##
  - Relaciones R1-R15: Modelo datos y constraints (13 primitivos + 2 extendidos)
  - Vistas D1-D4: Artefactos por dominio ortogonal
  - Patterns: Soluciones recurrentes validadas
```

## §1. ESTRUCTURA MODULAR

```yaml
Organización_5_Módulos:

  arquitectura del sistema/
  ├── 00_introduccion.md       ← Estás aquí (guía completa)
  ├── 01_contratos.md         → PARTE I: Contratos Canónicos C1-C5 + E6-E7
  ├── 02_diseño.md            → PARTE II: Principios Diseño PD1-PD76 (76 principios)
  ├── 03_relaciones.md        → PARTE III: Modelo Relacional E1-E7, R1-R15
  ├── 04_vistas.md            → PARTE IV: Vistas D1-D4 + Artefactos
  └── 05_patrones.md          → PARTE V: Patterns & Anti-Patterns

Orden_Lectura_Recomendado:
  1. 01_contratos.md: Especificación formal primitivos P1-P5 + entidades E6-E7
  2. 02_diseño.md: 76 principios operativos (40 genoma I1-I8, 36 fenotipo AOC/G##)
  3. 03_relaciones.md: Modelo datos, E1-E7 + R1-R15 (13 fundamentales + 2 derivadas)
  4. 04_vistas.md: Artefactos por dominio D1-D4
  5. 05_patrones.md: Catálogo patterns & anti-patterns validados

Lectura_Rápida_Ejecutiva (1-2 horas):
  - §2 de este archivo: Resumen 5 partes
  - 01_contratos §1-§2: C1 Capacidad completo
  - 02_diseño §2-§6: Principios I1-I5 (core HAIC, PD1-21)
  - 03_relaciones §3-§4: E1-E7 + R1-R15 + tabla resumen
```

## §2. CONTENIDO MODULAR RESUMIDO

### PARTE I: Contratos Canónicos (01_contratos.md)

**Especificación OPERABLE de los 5 primitivos fundamentales**

```yaml
C1_CAPACIDAD (desde P1/A2):
  Schema: substrate, capacity_type, role, ownership, archetype, composition
  Invariantes: INV_C1-C7 (accountability humana, delegación HAIC)
  Interfaces: 4 dominios × operaciones
  Resolución: Actor/Agente unificados en P1

C2_FLUJO (desde P2/A1):
  Schema: DAG structure, steps, dependencies, metrics
  Invariantes: INV_F1-F5 (cycle time, handoff ratio <20%)
  Clasificación: Producción (cliente externo) vs Habilitación (interno)

C3_INFORMACIÓN (desde P3/A3):
  Schema: type (Persistente/Transitoria/Agregada), lineage, quality
  Observable_Mapping: 16 observables EX1-8 + IN1-8
  Trazabilidad: Lineage completo (DAG)

C4_LÍMITE (desde P4/A4):
  Schema: type (Físico/Regulatorio/Organizacional/Económico/Técnico)
  Enforcement: Preventivo, Detectivo, Correctivo

C5_PROPÓSITO (desde P5/A5):
  Schema: OKR structure (objective + key_results), hierarchy
  Jerarquía: org → unit → team → individual
  Ownership: Humano/Mixto únicamente (I5 HAIC)
```

### PARTE II: Principios de Diseño (02_diseño.md)

**76 principios operativos: 40 genoma (I1-I8) + 36 fenotipo (AOC/Kelly/G##)**

```yaml
Estructura_76_Principios:
  [GENOMA] PD1-PD30: Desde Invariantes I1-I7 (universales, obligatorios)
  [FENOTIPO] PD31-PD35: Arquetipos AOC Meyer (contextuales, best practices)
  [GENOMA] PD36-PD40: Desde I8 Parametrización (obligatorios, valores config)
  [FENOTIPO] PD41-PD46: Métricas AOC/Kelly (fórmulas, thresholds configurables)
  [FENOTIPO] PD47-PD76: Guidelines G## operacionales (implementación específica)

Principios_Genoma_I1-I7 (PD1-PD30):
  I1_Minimalidad (PD1-5): Justificación, composición, eliminación redundancia
  I2_Ortogonalidad (PD6-9): Separación concerns, relaciones explícitas
  I3_Trazabilidad (PD10-13): Metadata, lineage, audit trail, ADRs
  I4_Clasificación (PD14-17): Test cliente externo, amplificación, contexto
  I5_HAIC (PD18-21): Accountability humana, delegación M1-M6, override, explainability
  I6_Trajectory (PD22-25): Trajectory log, progresión gradual, drift, learning
  I7_Emergencia (PD26-30): Nivel apropiado, no saltar, señales, H_org≥70

Principios_Fenotipo_AOC (PD31-PD35):
  PD31: Cohesión máxima arquetipo
  PD32-35: Incompatibilidades (α↔β, γ↔δ, γ↔ε, δ↔ε)
  Origen: Meyer AOC (90_referencias_fundacionales/02_arquitectura_organizacional.md)

Principios_Genoma_I8 (PD36-PD40):
  PD36: Context explicit declaration
  PD37: Genotype-phenotype separation
  PD38: Parametric methodology
  PD39: Adaptation traceability
  PD40: Module composability

Principios_Fenotipo_Métricas (PD41-PD46):
  AOC: PD41 Coherencia, PD42 Resonancia, PD43 Flujo (gates verificables)
  Kelly: PD44 Small Batches, PD45 Flow Lead Time, PD46 Quality-Speed
  Thresholds: θ_* configurables por Context Schema (PD36)

Principios_Fenotipo_Guidelines (PD47-PD76):
  Definicionales (PD47-51): Composition, handoffs, alignment, violations, units
  Lifecycle (PD52-54): Transitions, achievement, deprecation
  Estados (PD55-58): Snapshots, executability, reachability, convergence
  Execution/DORA (PD59-63): Tracking, DORA metrics, incidents, health, audit
  Governance (PD64-68): Portfolio, balance, automation, patterns, anti-patterns
  Vistas (PD69-72): Dashboards, templates, thresholds, integration
  Refinamientos (PD73-76): Performance, validation, migration, pattern metrics
  
  Derivación: I1-I8 → G## (30 Guidelines) → PD47-76 (30 principios)
  Ver §5 para mapeo completo G##
```

### PARTE III: Modelo Relacional (03_relaciones.md)

**Modelo lógico: E1-E7 entidades + R1-R15 relaciones**

```yaml
Base_Teórica: ../00_fundamentos_teoricos/08_modelo_relacional.md
  [GENOMA] E1-E5: Entidades primitivas (desde P1-P5, teoría pura)
  [GENOMA] R1-R13: Relaciones fundamentales (mínimo irreducible)

Extensiones_Arquitectónicas:
  [GENOMA] E6-E7: Entidades COMPUESTAS derivadas formalmente de E1-E5
    E6 (Estado Arquitectónico): snapshot(E1-E5) en tiempo t
    E7 (Ejecución Flujo): runtime(E2_Flujo) con metrics DORA
    
  [GENOMA] R14-R15: Relaciones DERIVADAS sobre E6-E7
    R14 (State-Transitions): DAG estados arquitectónicos
    R15 (Transition-Flow): ejecutabilidad transiciones
    
  [FENOTIPO] Q1-Q28: Queries operacionales (verificación, dashboards)
  [FENOTIPO] M1-M17: Métricas derivables (DORA, health scores, governance)

Entidades: E1-E7
  Primitivos (E1-E5): Capacidad, Flujo, Información, Límite, Propósito
  Compuestos (E6-E7): Estado Arquitectónico, Ejecución Flujo

Relaciones_R1-R15:
  R1: Capacidad ejecuta Flujo [1..*]↔[0..*]
  R2: Flujo produce Información [1]→[1..*]
  R3: Capacidad produce Información [1]→[0..*]
  R4: Capacidad consume Información [0..*]↔[0..*]
  R5: Información deriva Información (DAG) [0..*]↔[0..*]
  R6: Límite restringe Capacidad [0..*]↔[0..*]
  R7: Límite restringe Flujo [0..*]↔[0..*]
  R8: Límite restringe Información [0..*]↔[0..*]
  R9: Propósito direcciona Flujo [1]→[1..*]
  R10: Propósito asigna Capacidad [0..*]←[1]
  R11: Propósito jerarquía (tree) [0..1]↔[0..*]
  R12: Capacidad composición ⊕⊗ (recursive) [0..1]↔[2..*]
  R13: Capacidad delegación HAIC ★ (Alg←Humana) [1]←[0..*]
  R14: Estado Transitions (DAG) [0..1]→[1] (Wave 2)
  R15: Transition ejecutada por Flujos [1]→[1..*] (Wave 2)

Constraints:
  C1: Referential integrity | C2: Acyclicity (R5, R11, R12, R14)
  C3: Type consistency | C4: Mandatory (R9, R10, R13, R15)
  C5-C8: Por invariante (I1→C5, I3→C6, I5→C7, I7→C8)

Queries: Q1-Q28 SQL típicas (actualizado Wave 0-4: +Q14-28)
  Q14-16: Handoff, Alignment, Composition (Wave 0)
  Q17-18: Lifecycle Forecast, Deprecation Impact (Wave 1)
  Q19-21: State Delta, Convergence, Reachability (Wave 2)
  Q22-25: DORA Deployment, Lead Time, CFR, MTTR (Wave 3)
  Q26-28: Portfolio Optimization, Cross-Domain Health, Governance (Wave 4)
Métricas: M1-M17 (DORA M1-M4, Convergence M13, Flow M14-15, Portfolio M16-17)
```

### PARTE IV: Vistas Arquitectónicas (04_vistas.md y 05_patrones.md)

**4 dominios ortogonales con artefactos específicos**

```yaml
D1_ARQUITECTURA (estructura):
  Primitivos: Primarios P1+P4+P5, Secundarios P2+P3
  Artefactos: Org Chart ORKO, RACI Matrix, Purpose Cascade
  Métricas: H1_Humano (30% peso H_org)

D2_PERCEPCIÓN (observar):
  Primitivos: Primario P3, Secundarios P1+P5
  Artefactos: Dashboard 16 Observables, Anomaly Log
  Métricas: H4_Percepción (15% peso H_org)

D3_DECISIÓN (dirigir):
  Primitivos: Primarios P5 bajo P4, Secundarios P2+P3
  Artefactos: OKR Planning Canvas, Portfolio Board
  Métricas: H5_Decisión (10% peso H_org)

D4_OPERACIÓN (ejecutar):
  Primitivos: Primarios P2+P1, Secundarios P3+P5
  Artefactos: Value Stream Map, DORA Dashboard, Incident Log
  Métricas: H3_Flujo (20% peso H_org)

H_org_Integrado:
  Fórmula: H_org = H1×0.30 + H2×0.25 + H3×0.20 + H4×0.15 + H5×0.10
  Constraint: H_org ≥ 70 prerequisito transformación estructural
```

### PARTE V: Patterns & Anti-Patterns (05_patrones.md)

**Soluciones recurrentes validadas empíricamente**

```yaml
Patterns_Por_Dominio:
  D1: Team Topology Aligned, Delegation Ladder, Purpose Cascade
  D2: Observable Instrumentation, Anomaly Detection Pipeline
  D3: RICE Prioritization, WIP Limit Enforcement
  D4: Continuous Deployment, Observability Triad

Anti-Patterns_Críticos:
  AP11: Matrix Organizations (dual reporting)
  AP12: Process Owners Separados (fragmentación)
  AP13: Rainbow Groups (arquetipos incompatibles)
  AP14-20: [Catálogo completo 20+ anti-patterns]

Derivación: I1-I8 → PD1-PD40 → Patterns (validación empírica)
```

## §3. TRAZABILIDAD VERTICAL

```yaml
Nota_Derivación:
  "Arquitectura extiende fundamentos teóricos (A→P→I) con:
   - Contratos (C) desde primitivos (P)
   - Entidades compuestas (E6-E7) desde primitivos (E1-E5)
   - Principios (PD) desde invariantes (I)
   - Patterns desde principios validados empíricamente"

Ejemplo_Cadena_Completa (A→P→I→C→E→PD→Pattern→Metodología):

A2_Capacidad:
  → P1_Capacidad
    → I5_HAIC (Invariante)
      → C1_Contrato_Capacidad (Schema)
        → PD18-21 (Principios HAIC)
          → R13_Delegación_HAIC (Relación)
            → Pattern_D1.2_Delegation_Ladder
              → ../30_metodologia_orko/08_playbooks_operational/README.md §4.2 HAIC Modes

A1_Transformación:
  → P2_Flujo
    → I2_Ortogonalidad
      → C2_Contrato_Flujo
        → PD7_Relaciones_Explícitas
          → R1_Capacidad_Ejecuta_Flujo
            → Pattern_D1.1_Team_Topology
              → ../30_metodologia_orko/06_playbooks_recovery/P02_handoff_reduction.md §2.2 Manual R2

A5_Propósito:
  → P5_Propósito
    → I4_Clasificación_Contextual
      → C5_Contrato_Propósito
        → PD14-17_Test_Cliente
          → R9_Propósito_Direcciona_Flujo + R10_Asigna_Capacidad
            → Pattern_D1.3_Purpose_Cascade
              → ../30_metodologia_orko/06_playbooks_recovery/P03_okr_alignment.md §2.3 Manual R3

Propiedad_Trazabilidad:
  ∀ elemento arquitectura: ∃ path desde fundamentos teóricos
  ∀ principio: ∃ invariante origen
  ∀ pattern: ∃ principio fundamenta
```

## §4. USO DEL MÓDULO

### Para Arquitectos

```yaml
Workflow_Diseño:
  1. Leer: 01_contratos.md (especificación formal C1-C5, E6-E7)
  2. Aplicar: 02_diseño.md PD1-PD75 (principios desde I1-I8)
  3. Modelar: 03_relaciones.md R1-R15 (schema DB/código)
  4. Implementar: 04_vistas.md y 05_patrones.md (artefactos D1-D4)
  5. Consultar: 05_patrones.md (soluciones recurrentes validadas)

Validación:
  - Verificar constraints C1-C8 (§5 Parte III)
  - Ejecutar queries Q1-Q28 (§7 Parte III)
  - Medir métricas M1-M17 (DORA, H_org, Portfolio)
```

### Para Implementadores

```yaml
Contratos_Como_Spec:
  - C1-C5 son schema formal implementable
  - Invariantes INV_C1-C7, INV_F1-F5 son tests automáticos
  - Interfaces D1-D4 son API contract

Anti-Patterns_Evitar:
  - AP11-AP20 (§6 Parte V)
  - Consultar antes diseñar
```

### Para Metodólogos

```yaml
Derivación_Prácticas:
  - Patterns son base playbooks
  - Artefactos D1-D4 definen qué entregar
  - Métricas H_org guían adopción progresiva
```

## §5. COHERENCIA Y VERIFICACIÓN

```yaml
Checklist_Completitud:
  ✓ 7 Contratos C1-C5+E6+E7 (primitivos + Estado + Ejecución) [COMPLETO]
  ✓ 76 Principios PD1-PD76 (40 genoma + 36 fenotipo) [COMPLETO]
    - PD1-30: Invariantes I1-I7
    - PD31-35: Arquetipos AOC
    - PD36-40: Parametrización I8
    - PD41-46: Métricas AOC/Kelly
    - PD47-76: Guidelines G## (30 guidelines operacionales)
  ✓ 15 Relaciones R1-R15 (13 fundamentales + 2 derivadas States/Transitions)
  ✓ 4 Vistas D1-D4 (artefactos específicos, templates PD70)
  ✓ 20+ Patterns (validados empíricamente, success metrics PD76)
  ✓ 28 Queries Q1-Q28 (performance budgets PD73)
  ✓ 17 Métricas M1-M17 (adaptive thresholds PD71)

Métricas_Coherencia:
  Coverage_Primitivos:   5/5 (100%)
  Coverage_Invariantes:  8/8 (100%) → 76 principios
  Coverage_Dominios:     4/4 (100%) → vistas completas
  Trazabilidad:          Completa (teoría ↔ arqui ↔ metodología ↔ práctica)
  Ortogonalidad:         Verificada (contratos independientes)
  Performance:           Budgeted (PD73: queries <2s p95)
  Validation:            3-level enforcement (PD74)
  Integration:           Open APIs (PD72)
  
Estado_Coherencia_Semántica: EXCELENTE (100%)
  - Definiciones isomórficas con fundamentos
  - Derivaciones lógicamente correctas
  - Enforcement invariantes completo
  - Nomenclatura unificada (I1-I8, PD1-PD76, R1-R15, Q1-Q28, M1-M17)
  - Adoption path documented (PD76)
  
Guidelines_Implementadas:
  "30 Guidelines G## operacionalizan invariantes I1-I8 en 76 principios PD##.
   Post-renumeración: PD41-46 (métricas AOC/Kelly), PD47-76 (Guidelines)."
  
  Definicionales (PD47-51):
  ✓ G26: Composition Acyclicity (INV_R12.1 + PD47 + Q16)
  ✓ G27: Handoff Definition (C2 + PD48 + Q14)
  ✓ G28: Alignment Formula (C5 + PD49 + Q15)
  ✓ G29: Violation Severity (C4 + PD50)
  ✓ G30: Observable Units (C3 + PD51)
  
  Lifecycle (PD52-54):
  ✓ G11: Capacity Lifecycle (I7.5 + C1 + INV_C8 + PD52 + Q17)
  ✓ G12: Purpose Achievement (C5 + PD53)
  ✓ G24: Deprecation Timeline (C1 + PD54 + Q18)
  
  Estados/Transiciones (PD55-58):
  ✓ G1: Architectural States (E6 + R14 + PD55 + Q19)
  ✓ G23: Transition-Flow (R15 + PD56)
  ✓ G2: Reachability Validation (R14 + PD57 + Q21)
  ✓ G13: State Convergence (M13 Δ_arch + PD58 + Q20)
  
  Execution/DORA (PD59-63):
  ✓ G3: Flow Execution Tracking (E7 + PD59)
  ✓ G4: DORA Metrics Formalization (M1-M4 + Q22-25 + PD60)
  ✓ G5: Incident Flow Linkage (E7.failure + PD61)
  ✓ G6: Health Score Formula (H_org = H1-H5 weighted + PD62)
  ✓ G7: Decision Audit Trail (PD63)
  
  Governance/Portfolio (PD64-68):
  ✓ G14: Portfolio Optimization (Q26 + M16 + PD64)
  ✓ G15: Cross-Domain Metrics (Q27 + PD65)
  ✓ G10: Governance Automation (M17 + Q28 + PD66)
  ✓ G8: Pattern Catalog Completeness (PD67)
  ✓ G9: Anti-Pattern Detection (PD68 + metric thresholds)
  
  Vistas/Optimización (PD69-72):
  ✓ G16: Dashboard Refresh Frequency (PD69 real-time constraints)
  ✓ G17: Artifact Template Completeness (PD70 templates)
  ✓ G18: Metric Threshold Calibration (PD71 adaptive thresholds)
  ✓ G19: Integration Points Specification (PD72 APIs/events)
  
  Refinamientos (PD73-76):
  ✓ G20: Query Performance Optimization (PD73 budgets <2s)
  ✓ G21: Validation Rule Completeness (PD74 3-level enforcement)
  ✓ G22: Migration Path Documentation (PD75 phased adoption)
  ✓ G25: Pattern Success Metrics (PD76 empirical validation)
``
