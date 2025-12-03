# PARTE VIII: MODELO RELACIONAL

- [PARTE VIII: MODELO RELACIONAL](#parte-viii-modelo-relacional)
  - [§1. FUNDAMENTOS MODELO](#1-fundamentos-modelo)
  - [§2. ENTIDADES CORE](#2-entidades-core)
  - [§3. RELACIONES FUNDAMENTALES](#3-relaciones-fundamentales)
  - [§4. TABLA RESUMEN RELACIONES](#4-tabla-resumen-relaciones)
  - [§5. CONSTRAINTS INTEGRIDAD](#5-constraints-integridad)
  - [§6. DIAGRAMA ER CONCEPTUAL](#6-diagrama-er-conceptual)
  - [§7. PROPIEDADES DERIVABLES](#7-propiedades-derivables)

> **Etiquetado Genoma/Fenotipo**: Este documento contiene [GENOMA] (formas relacionales teóricas E1-E5, R1-R13) y [FENOTIPO] (implementaciones SQL/JSON, constraints específicos). Ver §0.1 en 00_introduccion.md.

## §1. FUNDAMENTOS MODELO

**[GENOMA]**

```YAML
Naturaleza_Modelo:
  "Modelo relacional teórico define estructura abstracta y relaciones entre primitivos.
   Es LÓGICO (genoma), independiente de implementación física (fenotipo)."
  
Nivel_Abstracción:
  GENOMA: Formas relacionales (E1-E5, R1-R13), multiplicidades, constraints lógicos
  FENOTIPO: Schemas SQL/JSON, CHECK() clauses, indexing strategies

Propósito_Genoma:
  1. Especificar relaciones permitidas entre entidades primitivas
  2. Definir multiplicidades teóricas (1:1, 1:N, N:M)
  3. Establecer constraints lógicos integridad referencial
  4. Validar consistencia primitivos P1-P5
  
Propósito_Fenotipo:
  1. Proveer ejemplos implementación (SQL, JSON, GraphQL)
  2. Especificar validaciones concretas (CHECK, triggers)
  3. Optimizaciones físicas (indexes, partitioning)

Notación:
  Entidad [min..max] ←relación→ [min..max] Entidad
  
  Ejemplos:
    [1] = exactamente uno
    [0..1] = opcional (cero o uno)
    [1..*] = uno o más
    [0..*] = cero o más
```

## §2. ENTIDADES CORE

**[GENOMA]** - Definiciones Teóricas

```YAML
Listado_Entidades_Primitivas:

  E1_Capacidad:
    Schema: Contrato C1 (§2 Parte I)
    PK: id (UUID)
    Derivación: Primitivo P1, Axioma A2
    
  E2_Flujo:
    Schema: Contrato C2 (§3 Parte I)
    PK: id (UUID)
    Derivación: Primitivo P2, Axioma A1
    
  E3_Información:
    Schema: Contrato C3 (§4 Parte I)
    PK: id (UUID)
    Derivación: Primitivo P3, Axioma A3
    
  E4_Límite:
    Schema: Contrato C4 (§5 Parte I)
    PK: id (UUID)
    Derivación: Primitivo P4, Axioma A4
    
  E5_Propósito:
    Schema: Contrato C5 (§6 Parte I)
    PK: id (UUID)
    Derivación: Primitivo P5, Axioma A5

Total_Entidades_Primitivas: 5 (minimal y suficiente por I1)

Scope_Genoma:
  "Este modelo define ÚNICAMENTE entidades PRIMITIVAS (E1-E5).
   Son el núcleo irreducible del modelo relacional ORKO."
   
Scope_Fenotipo_Arquitectura:
  "La arquitectura ORKO (Layer 1) extiende genoma con entidades COMPUESTAS:
   
   • E6_Estado_Arquitectónico: Snapshot(E1+E2+E4+E5) - coherencia temporal
   • E7_Ejecución_Flujo: Instance(E2) - tracking DORA metrics
   
   Estas derivan formalmente de primitivos E1-E5 (no nuevos primitivos).
   
   Dirección: GENOMA (E1-E5 aquí) → ARQUITECTURA (E6-E7 allá)
   Post-lectura: ../10_arquitectura_orko/03_relaciones.md §2"
```

## §3. RELACIONES FUNDAMENTALES

**[GENOMA]** - Formas Relacionales Teóricas

R1_Capacidad_Ejecuta_Flujo:

```YAML  
  Definición:
    "Capacidad ejecuta steps en flujo. Flujo requiere capacidades para ejecutarse."
    
  Estructura:
    Capacidad [0..*] ←ejecuta→ [1..*] Flujo
    
  Multiplicidad:
    - Una capacidad ejecuta 0+ flujos (puede estar idle)
    - Un flujo requiere 1+ capacidades (al menos 1 step)
    
  Forma_Relacional:
    Capacidad × Flujo (relación N:M vía atributo steps[])
    
  Derivación_Teórica:
    A1 (Transformación) + A2 (Capacidad efectúa transformación)
    → Flujo = secuencia transformaciones requiere capacidades
    
  Constraints_Lógicos:
    - ∀ step ∈ Flujo.steps: ∃ c ∈ Capacidad (referencia válida)
    - ∀ step: capacity.type ≥ step.type_min_required (compatibilidad tipos)
    
  Propiedad_Direccional:
    Flujo → Capacidad (dependency)
    Capacidad ↛ Flujo (independencia)

R2_Flujo_Produce_Información:
  
  Definición:
    "Flujo transforma inputs en outputs. Outputs son información."
    
  Estructura:
    Flujo [1] ←produce→ [1..*] Información
    
  Multiplicidad:
    - Un flujo produce 1+ informaciones (al menos output)
    - Una información es producida por 1 flujo (single producer)
    
  Forma_Relacional:
    Flujo → Información (relación 1:N, FK en Información)
    
  Derivación_Teórica:
    A1 (Transformación S₁→S₂) + A3 (Información coordina)
    → Transformación observable vía información producida
    
  Constraints_Lógicos:
    - ∀ I ∈ Información: I.producer_flow → Flujo ∪ {null}
    - IF I.type ≠ external THEN I.producer_flow ≠ null (información interna requiere productor)
    
  Excepción:
    Información externa (imported) puede tener produced_by_flow = null

R3_Capacidad_Produce_Información:
  
  Definición:
    "Capacidad genera información como parte ejecución."
    
  Estructura:
    Capacidad [1] ←produce→ [0..*] Información
    
  Multiplicidad:
    - Una capacidad produce 0+ informaciones
    - Una información producida por 1 capacidad específica
    
  Forma_Relacional:
    Capacidad → Información (relación 1:N, FK en Información)
    
  Derivación_Teórica:
    A2 (Capacidad efectúa) + A3 (Información estructura significado)
    → Capacidad al actuar genera información
    
  Relación_Con_R2:
    R2 + R3 juntos forman lineage completo:
    Información producida por (Flujo, Capacidad específica en step)

R4_Capacidad_Consume_Información:
  
  Definición:
    "Capacidad decisional (C1+) requiere información para decidir."
    
  Estructura:
    Capacidad [0..*] ←consume→ [0..*] Información
    
  Multiplicidad:
    - Capacidad C0 consume 0 información (mecánica)
    - Capacidad C1+ consume 1+ información (para decidir)
    - Información consumida por 0+ capacidades
    
  Forma_Relacional:
    Capacidad × Información (relación N:M vía steps[] inputs)
    
  Derivación_Teórica:
    Capacidad C1+ requiere input para decisión (A3)
    
  Constraint_Lógico:
    ∀ C ∈ Capacidad WHERE C.type = C0:
      |consumed_info(C)| = 0 (capacidad mecánica no consume info)

R5_Información_Deriva_Información:
  
  Definición:
    "Información agregada deriva de información padres (DAG)."
    
  Estructura:
    Información [0..*] ←parent_of→ [0..*] Información
    
  Multiplicidad:
    - Información puede tener 0+ padres
    - Información puede ser padre de 0+ hijos
    
  Forma_Relacional:
    Información × Información (relación N:M recursiva, DAG)
    
  Derivación_Teórica:
    A3 (Información coordina) + Propiedad agregación
    → Información compuesta deriva de fuentes
    
  Constraints_Lógicos:
    - DAG: ¬∃ cycles (acyclic graph property)
    - IF I.type = Agregada THEN |parents(I)| ≥ 2 (agregación requiere múltiples fuentes)
    - IF I.type = Transitoria THEN |parents(I)| = 0 (eventos no derivan)
    
  Propiedad_Recursiva:
    lineage_depth(I) = 1 + max(lineage_depth(parent) for parent in parents)

R6_Límite_Restringe_Capacidad:
  
  Definición:
    "Límite acota qué puede hacer capacidad."
    
  Estructura:
    Límite [0..*] ←restringe→ [0..*] Capacidad
    
  Multiplicidad:
    - Límite aplica a 0+ capacidades (puede ser global)
    - Capacidad restringida por 0+ límites
    
  Forma_Relacional:
    Límite × Capacidad (relación N:M)
    
  Derivación_Teórica:
    A4 (Restricción acota posibilidades)
    → Capacidad opera dentro límites
    
  Ejemplos:
    - Límite_Budget → [Capacidad_TeamA, Capacidad_TeamB]
    - Límite_GDPR → [Capacidad_All WHERE processes_PII]

R7_Límite_Restringe_Flujo:
  
  Definición:
    "Límite acota cómo/cuándo flujo puede ejecutarse."
    
  Estructura:
    Límite [0..*] ←restringe→ [0..*] Flujo
    
  Multiplicidad:
    - Límite aplica a 0+ flujos
    - Flujo restringido por 0+ límites
    
  Forma_Relacional:
    Límite × Flujo (relación N:M)
    
  Derivación_Teórica:
    A4 (Restricción) + A1 (Transformación)
    → Flujo ejecuta dentro límites
    
  Ejemplos:
    - Límite_ApprovalRequired → [Flujo_Deployment, Flujo_Budget_Spend]
    - Límite_Horario_Laboral → [Flujo_Producción (no 24/7)]

R8_Límite_Restringe_Información:
  
  Definición:
    "Límite acota qué información puede crearse/accederse."
    
  Estructura:
    Límite [0..*] ←restringe→ [0..*] Información
    
  Multiplicidad:
    - Límite aplica a 0+ informaciones
    - Información restringida por 0+ límites
    
  Implementación:
    Límite.constraint.target_entity_ids → List<Información.id>
    WHERE Límite.constraint.target_entity_type = Información
    
  Derivación_Teórica:
    A4 + A3 → Información sujeta a límites (privacy, retention)
    
  Ejemplos:
    - Límite_GDPR_Retention → [Información WHERE contains_PII]
    - Límite_Classification_Secret → [Información WHERE sensitivity=Secret]

R9_Propósito_Direcciona_Flujo:
  
  Definición:
    "Flujo existe para servir propósito. Todo flujo tiene outcome deseado."
    
  Estructura:
    Propósito [1] ←direcciona→ [1..*] Flujo
    
  Multiplicidad:
    - Un propósito es servido por 1+ flujos
    - Un flujo sirve exactamente 1 propósito
    
  Implementación:
    Flujo.purpose_id → Propósito.id (FK NOT NULL)
    
  Derivación_Teórica:
    A5 (Intencionalidad) + A1 (Transformación)
    → Transformación tiene propósito
    
  Constraint_Crítico:
    ∀ F ∈ Flujo: F.purpose_id NOT NULL
    Violación imposible (schema enforced)
    
  Interpretación:
    Flujo sin propósito = waste (violates A5)

R10_Propósito_Asigna_Capacidad:
  
  Definición:
    "Propósito tiene capacidad owner accountable."
    
  Estructura:
    Propósito [0..*] ←asigna→ [1] Capacidad
    
  Multiplicidad:
    - Un propósito tiene exactamente 1 owner (accountability única)
    - Una capacidad puede ser owner de 0+ propósitos
    
  Implementación:
    Propósito.ownership.owner_capacity_id → Capacidad.id (FK NOT NULL)
    
  Derivación_Teórica:
    A5 (Intencionalidad) + I5 (Primacía Humana)
    → Propósito requiere humano accountable
    
  Constraint:
    ∀ P ∈ Propósito: 
      P.owner_capacity.substrate ∈ {Humano, Mixto}

R11_Propósito_Jerarquía:
  
  Definición:
    "Propósitos forman árbol jerárquico (cascada org → individual)."
    
  Estructura:
    Propósito [0..1] ←parent→ [0..*] Propósito
    
  Multiplicidad:
    - Propósito tiene 0 o 1 padre (0 = root org)
    - Propósito tiene 0+ hijos (0 = leaf individual)
    
  Implementación:
    Propósito.hierarchy.parent_purpose_id → Propósito.id | null
    
  Derivación_Teórica:
    A5 (Intencionalidad) + Propiedad alineación
    → Propósitos individuales contribuyen a org
    
  Constraints:
    - Tree structure (no cycles)
    - Root propósitos: scope=Organization AND parent_id=null
    - Leaf propósitos: child_purpose_ids.length=0
    - ∀ child: child.end_date ≤ parent.end_date
    
  Propiedad_Path:
    path_to_root(P) = [P, parent(P), parent(parent(P)), ..., root]
    Representa alignment chain

R12_Capacidad_Composición:
  
  Definición:
    "Capacidad Mixta compuesta de otras capacidades (recursive)."
    
  Estructura:
    Capacidad [0..1] ←compuesta_de→ [2..*] Capacidad
    
  Multiplicidad:
    - Capacidad Mixta tiene 2+ componentes
    - Capacidad puede ser componente de 0 o 1 mixta
    
  Implementación:
    Capacidad.composition.component_ids → List<Capacidad.id>
    WHERE Capacidad.substrate = Mixto
    
  Derivación_Teórica:
    A2 (Capacidad) + Propiedad composición
    → Capacidades combinables
    
  Constraints:
    - IF substrate = Mixto THEN composition NOT NULL
    - composition.component_ids.length ≥ 2
    - ∃ component: component.substrate = Humano
    - Recursive pero acíclico (no self-reference chain)
    
  Operadores:
    ⊕ (Paralelo): Team = C1 ⊕ C2 ⊕ ... ⊕ Cn
    ⊗ (Secuencial): Pipeline = C1 ⊗ C2 ⊗ C3
```

R13_Delegación_HAIC:

```YAML
  Definición:
    "Capacidad Algorítmica DEBE ser delegada por Capacidad Humana.
     Enforcement de I5: HAIC/Primacía humana."
    
  Estructura:
    Capacidad(Algorítmica) [1] ←delegada_por→ [1] Capacidad(Humana)
    
  Multiplicidad:
    - Toda capacidad algorítmica tiene EXACTAMENTE 1 humano responsable (mandatory)
    - Un humano puede delegar a 0+ capacidades algorítmicas
    
  Implementación:
    Capacidad.accountable_capacity_id → Capacidad.id
    WHERE source.substrate = Algorítmico
    AND target.substrate ∈ {Humano, Mixto}
    
  Derivación_Teórica:
    I5_HAIC (Primacía humana): "Capacidad algorítmica opera bajo supervisión
     y responsabilidad humana explícita con autonomía acotada progresiva."
     Ver 03_invariantes.md §6 para teorema completo
    
  Constraints_Genoma:
    - IF substrate = Algorítmico AND capacity_type ≥ C1 
      THEN accountable_capacity_id NOT NULL (mandatory)
    - accountable_capacity.substrate ∈ {Humano, Mixto}
    - accountable_capacity.substrate ≠ Algorítmico (no delegation loop)
    - Si accountable es Mixto, ∃ humano en composition (transitivo)
    
  Delegation_Mode_Abstract:
    Campo: delegation_mode: DelegationMode?
    Dominio: Tipo abstracto representando nivel autonomía
    Valores_Concretos: Ver I5_[FENOTIPO] (03_invariantes.md §6) para:
      - Espectro M1-M6 (Monitorear → Informar → ... → Ejecutar)
      - Progresión recomendada entre niveles
      - Thresholds success_rate para cambios autonomía
    NOTA: Genoma solo define ∃ delegation_mode, no valores específicos
    
  Propiedad_Trazabilidad:
    ∀ output algorítmico: audit_trail registra
      (humano_accountable, delegation_mode, timestamp)
    Fundamentación: I3 (Trazabilidad) + I5 (HAIC)
    
  Anti-Pattern:
    Capacidad algorítmica sin accountable_capacity_id → INVALID STATE
    (Viola I5, bloquea validación sistema)
```

## §4. TABLA RESUMEN RELACIONES

Matriz_Relaciones:

  |              | Capacidad      | Flujo | Información | Límite | Propósito |
  |--------------|----------------|-------|-------------|--------|-----------|
  | Capacidad    | R12 (⊕⊗), R13 | R1    | R3, R4      | R6     | R10       |
  | Flujo        | R1             | -     | R2          | R7     | R9        |
  | Información  | R3, R4         | R2    | R5 (DAG)    | R8     | -         |
  | Límite       | R6             | R7    | R8          | -      | -         |
  | Propósito    | R10            | R9    | -           | -      | R11       |

Total_Relaciones_Primitivas: 13 fundamentales

- R1-R11: Relaciones entre primitivos P1-P5
- R12: Capacidad ⊕⊗ Capacidad (composición)
- R13: Capacidad(Algorítmica) ← Capacidad(Humana) (delegación HAIC)

Nota_Arquitectural:
  "La arquitectura ORKO extiende este modelo con relaciones DERIVADAS:

   • R14_Estado_Transitions: Estado → Transition → Estado (DAG evolutivo)
   • R15_Transition_Flow: Transition → Flujo (planning-execution link)

   Estas relaciones operan sobre entidades compuestas (E6-E7) y son
   formalmente derivables desde primitivos.
  Ver ../10_arquitectura_orko/03_relaciones.md §3 para especificación completa."

Propiedad_Completitud:
  ✓ Todas combinaciones primitivos cubiertas (E1-E5)
  ✓ Relaciones derivadas de axiomas (no inventadas)
  ✓ Multiplicidades consistentes con invariantes
  ✓ Extensiones arquitectónicas trazables a primitivos

## §5. CONSTRAINTS INTEGRIDAD

**[GENOMA]** - Constraints Lógicos Teóricos

```YAML
Constraints_Globales_Genoma:

  C1_Referential_Integrity:
    Enunciado: "Toda referencia apunta a entidad existente"
    Forma_Lógica:
      ∀ relación R con referencia externa:
        ∀ entity.ref_field:
          entity.ref_field ∈ target_entity.id ∨ ref_field = null (si opcional)
        
  C2_Acyclicity:
    Enunciado: "Relaciones recursivas forman DAG (no cycles)"
    Aplicable_a:
      - R5: Información.parent_info_ids (lineage)
      - R11: Propósito.parent_purpose_id (tree)
      - R12: Capacidad.component_ids (composición)
    Validación: topological_sort(graph) ≠ ∅
    
  C3_Type_Consistency:
    Enunciado: "Relaciones respetan tipos compatibles"
    Ejemplos_Lógicos:
      - R1: Capacidad.type ≥ Flujo.step.min_required_type
      - R10: Propósito.owner.substrate ∈ {Humano, Mixto}
      - R12: Mixto.components contiene ≥1 Humano
      
  C4_Mandatory_Relations:
    Enunciado: "Relaciones obligatorias siempre presentes"
    Especificación:
      - R9: ∀ Flujo f: f.purpose_id ≠ null (fundamentado en A5)
      - R10: ∀ Propósito p: p.owner_capacity_id ≠ null
      - R13: ∀ Capacidad c: (c.substrate = Algorítmico ∧ c.type ≥ C1) → c.accountable_capacity_id ≠ null

  C9_Minimum_Steps:
    Enunciado: "Todo Flujo contiene al menos una Capacidad ejecutora"
    Forma_Lógica:
      ∀ Flujo f: |f.steps| ≥ 1
    Fundamentación: Flujo sin steps no transforma (contradice definición P2)

Constraints_Derivados_Invariantes_Genoma:

  I1_Minimalidad → C5_Justification:
    Enunciado: "Toda entidad tiene campo justification documentado"
    Validación: Meta-constraint (verificado vía PD1 arquitectura)
    
  I3_Trazabilidad → C6_Audit_Trail:
    Enunciado: "Toda entidad tiene (created_by, created_at, version)"
    Fundamentación: Trazabilidad requiere registro cambios
    
  I5_HAIC → C7_Human_Accountability:
    Enunciado: "Toda Capacidad algorítmica decisional tiene accountable humano"
    Forma_Lógica:
      ∀ cap ∈ Capacidad:
        (cap.substrate = Algorítmico ∧ cap.type ≥ C1) →
          cap.accountable_capacity_id → Capacidad(substrate ∈ {Humano, Mixto})
      ∀ prop ∈ Propósito:
        prop.owner_capacity.substrate ∈ {Humano, Mixto}
      ∀ lim ∈ Límite:
        (lim.criticality = HIGH) → lim.owner_capacity.substrate = Humano
    Enforcement: R13_Delegación_HAIC
    
  I7_Emergencia → C8_Level_Appropriateness:
    Enunciado: "Org nivel N no usa prácticas nivel N+2"
    Validación: No enforced en schema (metodología valida)
```

---

**[FENOTIPO]** - Implementaciones SQL/JSON

```sql
-- Ejemplo implementación C9_Minimum_Steps en PostgreSQL:
CREATE TABLE flow (
  id UUID PRIMARY KEY,
  steps JSONB NOT NULL,
  CONSTRAINT flow_min_steps CHECK (jsonb_array_length(steps) >= 1),
  CONSTRAINT flow_steps_have_capacity CHECK (
    (SELECT COUNT(*) FROM jsonb_array_elements(steps) step
     WHERE step->>'capacity_id' IS NULL) = 0
  )
);

-- Ejemplo implementación C2_Acyclicity en trigger:
CREATE FUNCTION validate_dag_constraint() RETURNS TRIGGER AS $$
BEGIN
  IF EXISTS (SELECT 1 FROM detect_cycle(NEW.parent_id, NEW.id)) THEN
    RAISE EXCEPTION 'Cycle detected in relationship';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Ejemplo implementación C7_Human_Accountability:
CREATE TABLE capacity (
  id UUID PRIMARY KEY,
  substrate VARCHAR(20) NOT NULL CHECK (substrate IN ('Humano', 'Algorítmico', 'Mecánico', 'Mixto')),
  capacity_type VARCHAR(10) NOT NULL CHECK (capacity_type IN ('C0', 'C1', 'C2', 'C3')),
  accountable_capacity_id UUID REFERENCES capacity(id),
  delegation_mode VARCHAR(2) CHECK (delegation_mode IN ('M1', 'M2', 'M3', 'M4', 'M5', 'M6')),
  CONSTRAINT algo_needs_accountable CHECK (
    substrate != 'Algorítmico' OR 
    (capacity_type = 'C0' AND accountable_capacity_id IS NULL) OR
    (capacity_type >= 'C1' AND accountable_capacity_id IS NOT NULL)
  )
);
```

## §6. DIAGRAMA ER CONCEPTUAL

Representación_Textual:

```
┌─────────────┐
│  PROPÓSITO  │ (E5)
│  [P5]       │
└──────┬──────┘
       │ R11 (parent_of)
       │ [0..1] ↔ [0..*]
       ├─────────┐
       │         │
       │ R10 (owner)    R9 (direcciona)
       │ [1]            [1] ↔ [1..*]
       ↓                ↓
┌─────────────┐    ┌─────────────┐
│  CAPACIDAD  │    │    FLUJO    │ (E2)
│  [P1]       │←───│    [P2]     │
└──────┬──────┘ R1 └──────┬──────┘
       │ ejecuta         │
       │ [1..*]↔[0..*]   │ R2 (produce)
       │                 │ [1] → [1..*]
       │ R3 (produce)    │
       │ [1]→[0..*]      ↓
       │            ┌─────────────┐
       │            │ INFORMACIÓN │ (E3)
       │            │    [P3]     │
       │            └──────┬──────┘
       │                   │ R5 (deriva)
       │ R4 (consume)      │ [0..*]↔[0..*]
       │ [0..*]↔[0..*]     │ (DAG)
       └───────────────────┘
       
       R12 (composición)
       [0..1] ↔ [2..*]
       Capacidad ←→ Capacidad
       (recursive)

┌─────────────┐
│   LÍMITE    │ (E4)
│    [P4]     │
└──────┬──────┘
       │ R6, R7, R8
       │ restringe
       │ [0..*] ↔ [0..*]
       └──→ [Capacidad, Flujo, Información]
```

Lectura_Diagrama:

- Rectángulos = Entidades (E1-E5)
- Flechas = Relaciones (R1-R13)
- [X..Y] = Multiplicidad
- (DAG) = Constraint acyclicity
- ↔ = Bidireccional
- → = Unidireccional

## §7. PROPIEDADES DERIVABLES

**[FENOTIPO]** - Queries y Métricas Operacionales

Queries_Típicas:

```SQL
  Q1_Capacidades_de_Flujo:
    INPUT: flujo_id
    OUTPUT: List<Capacidad>
    
    SELECT DISTINCT c.*
    FROM Flujo f
    JOIN Flujo.steps s ON s.flow_id = f.id
    JOIN Capacidad c ON c.id = s.capacity_id
    WHERE f.id = :flujo_id
    
  Q2_Flujos_Serviendo_Propósito:
    INPUT: propósito_id
    OUTPUT: List<Flujo>
    
    SELECT f.*
    FROM Flujo f
    WHERE f.purpose_id = :propósito_id
    
  Q3_Lineage_Información:
    INPUT: info_id
    OUTPUT: DAG<Información>
    
    WITH RECURSIVE lineage AS (
      SELECT * FROM Información WHERE id = :info_id
      UNION ALL
      SELECT i.* FROM Información i
      JOIN lineage l ON i.id IN (SELECT unnest(l.parent_info_ids))
    )
    SELECT * FROM lineage
    
  Q4_Path_Propósito_Root:
    INPUT: propósito_id
    OUTPUT: List<Propósito> (leaf → root)
    
    WITH RECURSIVE path AS (
      SELECT * FROM Propósito WHERE id = :propósito_id
      UNION ALL
      SELECT p.* FROM Propósito p
      JOIN path pt ON p.id = pt.parent_purpose_id
    )
    SELECT * FROM path
    
  Q5_Límites_Aplicables_Capacidad:
    INPUT: capacidad_id
    OUTPUT: List<Límite>
    
    SELECT l.*
    FROM Límite l
    WHERE l.constraint.target_entity_type = 'Capacidad'
      AND :capacidad_id = ANY(l.constraint.target_entity_ids)
    
  Q6_Componentes_Capacidad_Mixta:
    INPUT: capacidad_mixta_id
    OUTPUT: List<Capacidad>
    
    WITH RECURSIVE components AS (
      SELECT * FROM Capacidad WHERE id = :capacidad_mixta_id
      UNION ALL
      SELECT c.* FROM Capacidad c
      JOIN components cmp ON c.id IN (SELECT unnest(cmp.composition.component_ids))
    )
    SELECT * FROM components WHERE id != :capacidad_mixta_id
```

Métricas_Derivables:

```SQL
  M1_Utilización_Capacidad:
    = COUNT(DISTINCT flujo_id ejecutando capacidad) / capacidad.throughput_max
    
  M2_Complejidad_Flujo:
    = Flujo.steps.length + Flujo.dependencies.length
    
  M3_Freshness_Información:
    = NOW() - Información.temporal.created_at
    
  M4_Cobertura_Límites:
    = COUNT(entidades con límites) / COUNT(entidades totales)
    
  M5_Alignment_Propósito:
    = AVG(progreso propósitos hijos) para propósito padre
```

**R3 — Excepción para información externa:** Si `source_kind = external`, `produced_by_capacity_id` puede ser `null` con `source_system/source_org` obligatorios.

**Linaje:** se garantiza **DAG por ejecución**; la recursión se modela como nuevas ejecuciones/versiones.
