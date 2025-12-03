# PARTE III: MODELO RELACIONAL

**Especificación Lógica de Estructura Datos y Relaciones**

> **Etiquetado Genoma/Fenotipo**: Este documento especifica el modelo lógico relacional:
> - **[GENOMA]** E1-E7, R1-R15: Entidades y relaciones abstractas (multiplicidades, constraints lógicos)
> - **[FENOTIPO]** Q1-Q28, M1-M17: Queries y métricas operacionales (implementación específica)
> - **[FENOTIPO]** Implementación física: SQL schemas, índices, optimizations (ver Layer 2 Tejidos)
>
> Ver ../00_fundamentos_teoricos/00_introduccion.md §0.1 para definición completa framework.

- [PARTE III: MODELO RELACIONAL](#parte-iii-modelo-relacional)
  - [§1. FUNDAMENTOS MODELO](#1-fundamentos-modelo)
  - [§2. ENTIDADES CORE](#2-entidades-core)
  - [§3. RELACIONES FUNDAMENTALES](#3-relaciones-fundamentales)
  - [§4. TABLA RESUMEN RELACIONES](#4-tabla-resumen-relaciones)
  - [§5. CONSTRAINTS INTEGRIDAD](#5-constraints-integridad)
    - [Regla\_Lineage\_Origen (consistencia R2/R3 \& C3)](#regla_lineage_origen-consistencia-r2r3--c3)
  - [§6. DIAGRAMA ER CONCEPTUAL](#6-diagrama-er-conceptual)
  - [§7. PROPIEDADES DERIVABLES](#7-propiedades-derivables)

## §1. FUNDAMENTOS MODELO

```YAML
Naturaleza_Modelo:
  "Modelo relacional arquitectónico EXTIENDE el modelo teórico puro
   (../00_fundamentos_teoricos/08_modelo_relacional.md) con entidades COMPUESTAS
   y relaciones DERIVADAS para arquitectura operable.
   
   Es LÓGICO (independiente implementación física DB/código)."

Derivación_Desde_Fundamentos:
 Base_Teórica (../00_fundamentos_teoricos/08_modelo_relacional.md):
    - E1-E5: Entidades primitivas (desde P1-P5) → IRREDUCIBLES
    - R1-R13: Relaciones fundamentales → MÍNIMO NECESARIO
  
  Extensiones_Arquitectónicas (este documento):
    - E6-E7: Entidades COMPUESTAS (derivadas formalmente de E1-E5)
    - R14-R15: Relaciones DERIVADAS (operan sobre E6-E7)
    - Queries Q1-Q28: Operaciones arquitectónicas
    - Métricas M1-M17: KPIs operacionales

Propósito:
  1. Extender modelo teórico con capacidades operacionales
  2. Especificar relaciones permitidas (primitivos + compuestos)
  3. Definir multiplicidades (1:1, 1:N, N:M)
  4. Establecer constraints integridad referencial
  5. Base para implementación (SQL schema, graph DB, código)

Notación:
  Entidad [min..max] ←relación→ [min..max] Entidad
  
  Ejemplos:
    [1] = exactamente uno
    [0..1] = opcional (cero o uno)
    [1..*] = uno o más
    [0..*] = cero o más
```

## §2. ENTIDADES CORE

```YAML
Listado_Entidades:

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

Total_Entidades: 5 (minimal y suficiente por I1)
```

## §3. RELACIONES FUNDAMENTALES

R1_Capacidad_Ejecuta_Flujo:

```YAML  
  Definición:
    "Capacidad ejecuta steps en flujo. Flujo requiere capacidades para ejecutarse."
    
  Estructura:
    Capacidad [1..*] ←ejecuta→ [0..*] Flujo
    
  Multiplicidad:
    - Una capacidad ejecuta 0+ flujos (puede estar idle)
    - Un flujo requiere 1+ capacidades (al menos 1 step)
    
  Implementación:
    Via Flujo.steps[].capacity_required.capacity_id → Capacidad.id
    
  Derivación_Teórica:
    A1 (Transformación) + A2 (Capacidad efectúa transformación)
    → Flujo = secuencia transformaciones requiere capacidades
    
  Constraints:
    - ∀ step ∈ Flujo.steps: step.capacity_id ∈ Capacidad (FK)
    - ∀ step: Capacidad.capacity_type ≥ step.capacity_type_min
    
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
    
  Implementación:
    Información.lineage.produced_by_flow_id → Flujo.id
    
  Derivación_Teórica:
    A1 (Transformación S₁→S₂) + A3 (Información coordina)
    → Transformación observable vía información producida
    
  Constraints:
    - ∀ I ∈ Información: I.lineage.produced_by_flow_id → Flujo | null
    - IF Información.information_type ≠ external THEN produced_by_flow NOT NULL
    
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
    
  Implementación:
    Información.lineage.produced_by_capacity_id → Capacidad.id
    
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
    
  Implementación:
    Via Flujo.steps[].input_information → Información.id
    (consumo implícito cuando capacidad ejecuta step)
    
  Derivación_Teórica:
    Capacidad C1+ requiere input para decisión (A3)
    
  Constraint:
    ∀ C ∈ Capacidad WHERE capacity_type = C0:
      consumed_information.count = 0

R5_Información_Deriva_Información:
  
  Definición:
    "Información agregada deriva de información padres (DAG)."
    
  Estructura:
    Información [0..*] ←parent_of→ [0..*] Información
    
  Multiplicidad:
    - Información puede tener 0+ padres
    - Información puede ser padre de 0+ hijos
    
  Implementación:
    Información.lineage.parent_info_ids → List<Información.id>
    
  Derivación_Teórica:
    A3 (Información coordina) + Propiedad agregación
    → Información compuesta deriva de fuentes
    
  Constraints:
    - DAG (no cycles): topological_sort(parent_ids) succeeds
    - IF information_type = Agregada THEN parent_info_ids.length > 1
    - IF information_type = Transitoria THEN parent_info_ids.length = 0
    
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
    
  Implementación:
    Límite.constraint.target_entity_ids → List<Capacidad.id>
    WHERE Límite.constraint.target_entity_type = Capacidad
    
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
    
  Implementación:
    Límite.constraint.target_entity_ids → List<Flujo.id>
    WHERE Límite.constraint.target_entity_type = Flujo
    
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
    A5 (Intencionalidad) + I5 (HAIC)
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
    Capacidad(Algorítmica) [1] ←delegada_por→ [1] Capacidad(Humana|Mixta)
    
  Multiplicidad:
    - Toda capacidad algorítmica tiene EXACTAMENTE 1 humano responsable (mandatory)
    - Un humano puede delegar a 0+ capacidades algorítmicas
    
  Implementación:
    Capacidad.ownership.accountable_id → Capacidad.id
    WHERE source.substrate = Algorítmico
    AND target.substrate ∈ {Humano, Mixto}
    
  Derivación_Teórica:
    I5 (HAIC/Primacía humana): "Capacidad algorítmica opera bajo supervisión
     y responsabilidad humana explícita. Delegación progresiva M1→M6."
    
  Constraints:
    - IF substrate = Algorítmico THEN ownership.accountable_id NOT NULL (mandatory)
    - accountable_capacity.substrate ∈ {Humano, Mixto}
    - accountable_capacity.substrate ≠ Algorítmico (no delegation loop)
    - Si accountable es Mixto, ∃ humano en composition (transitivo)
    
  Modos_Delegación (I5):
    Tipo abstracto: DelegationMode
    Valores: Ver I5_[FENOTIPO] en ../00_fundamentos_teoricos/03_invariantes.md §6
    Espectro: M1_Monitorear → M6_Ejecutar (6 niveles autonomía progresiva)
    
  Propiedad_Trazabilidad:
    ∀ output algorítmico: audit_trail registra humano accountable
    + modo delegación aplicado + timestamp
  
  Extensión_ADP_ALM:
    "Extensión de R13 para agentes conversacionales en plataforma ORKO.
     ADP (Agent Definition Protocol) y ALM (Agent Lifecycle Management)
     se formalizan aquí como parte del protocolo interno ORKO.
     Documentación ampliada opcional en 90_referencias_fundacionales/10_ingenieria_agentes_conversacionales.md"
    
    agent_contract_id: String
      Descripción: ID del agente según protocolo ORKO/ADP (Agent Definition Protocol)
      Formato: AGENT-TYPE-DOMAIN-VERSION
      Ejemplo: ASIS-IPR-GN-V3 (Asistente IPR GORE Ñuble v3)
      Requerido: Si substrate=Algorítmico AND capacity_type ≥ C1
      Ubicación: Definido en header de agent.yaml (primeras líneas)
      
    agent_definition_uri: URI
      Descripción: Path al archivo agent.yaml en repositorio
      Ejemplo: /agents/asis_ipr_gn/agent.yaml
      Propósito: Trazabilidad especificación → ejecución
      
    alm_phase: {Conception, KB_Curation, Programming, Testing, Maintenance}
      Descripción: Fase ALM actual del agente (5-phase lifecycle definido en ORKO)
      Uso: Governance y audit trail de evolución
      
    guardrails_ref: URI
      Descripción: Policy-as-code vigente (OPA, Rego, YAML)
      Ejemplo: policy://agents/mlmodel_churn/guardrails.rego
      Mapea_a: safety_constraints_and_behavioral_guardrails en agent.yaml
      
    mode_policy: Function(impact, irreversibility, risk) → M1..M6
      Descripción: Función determina modo delegación según contexto
      Propiedades:
        - Determinística (mismos inputs → mismo output)
        - Auditable (lógica explícita, test cases documentados)
        - Parametrizable (thresholds configurables por contexto)
      Implementación: Puede ser código Python/JS o reglas declarativas
      
    kb_sync_protocol: String
      Descripción: Método sincronización KB (Manual | CI/CD | Drive_Sync)
      Propósito: Coherencia Git SSOT ↔ Platform KB Store
      
  Validaciones:
    - agent_contract_id REQUIRED si substrate=Algorítmico y capacity_type ≥ C1
    - agent_contract_id DEBE coincidir con ID en agent.yaml header
    - agent_definition_uri DEBE apuntar a archivo válido agent.yaml
    - guardrails_ref DEBE existir y ser accesible en auditoría E7.override
    - mode_policy DEBE tener test_cases documentados para regresión
    - alm_phase DEBE reflejar estado real lifecycle
    
  Trazabilidad_Completa:
    Capacidad(Algorítmica) → agent_contract_id → agent.yaml (protocolo ORKO/ADP) →
      defined_states + workflows → KB guidance maps → Information assets (TF3)

R14_State_Transitions (G1):

```yaml
  Definición:
    "Estado arquitectónico evoluciona a siguiente estado vía transición.
     Tracking temporal transformación arquitectónica."
     
  Estructura:
    Estado [0..1] ←from→ Transición ←to→ [1] Estado
    
  Multiplicidad:
    - Transición conecta 1 estado origen (puede ser NULL si inicial) → 1 estado destino
    - Estado puede ser destino de 0+ transiciones
    
  Schema_Transición:
    id: UUID
    from_state_id: UUID | null
    to_state_id: UUID
    transition_type: {Planned | Emergent | Corrective}
    executed_at: Timestamp | null
    planned_date: Date
    status: {Planned | In_Progress | Completed | Failed}
    
  Derivación_Teórica:
    A1 (Transformación) + meta.md (Coherencia Temporal)
    → Estados evolucionan en timeline
    
  Constraints:
    - INV_R14.1: Transitions forman DAG (no cycles)
    - INV_R14.2: to_state.effective_date >= from_state.valid_until
    - INV_R14.3: Current state puede tener solo 1 transition In_Progress
```

R15_Transition_Flow (G23):

```yaml
  Definición:
    "Transición arquitectónica ejecutada por flujos operacionales.
     Link entre architectural design (D1) y execution (D4)."
     
  Estructura:
    Transición [1] ←ejecutada_por→ [1..*] Flujo
    
  Multiplicidad:
    - Transición requiere ≥1 flujo para ejecutarse
    - Flujo puede implementar 0 o 1 transición
    
  Implementación:
    Transition.execution_flows → List<Flujo.id>
    Flujo.implements_transition_id → Transition.id | null
    
  Derivación_Teórica:
    G1 (States) + A1 (Transformación vía flows)
    → Architectural change ejecutado por operational flows
    
  Constraints:
    - ALL execution_flows.status != Retired
    - IF transition.status = In_Progress THEN
        EXISTS flow IN execution_flows: flow.status = Active
```

## §4. TABLA RESUMEN RELACIONES

Matriz_Relaciones:

  |              | Capacidad      | Flujo   | Información | Límite | Propósito | Estado |
  |--------------|----------------|---------|-------------|--------|-----------|--------|
  | Capacidad    | R12 (⊕⊗), R13 | R1      | R3, R4      | R6     | R10       | -      |
  | Flujo        | R1             | -       | R2          | R7     | R9        | R15    |
  | Información  | R3, R4         | R2      | R5 (DAG)    | R8     | -         | -      |
  | Límite       | R6             | R7      | R8          | -      | -         | -      |
  | Propósito    | R10            | R9      | -           | -      | R11       | -      |
  | Estado (E6)  | -              | R15     | -           | -      | -         | R14    |

Total_Relaciones: 15 fundamentales (13 base + R14 States + R15 Transition-Flow)

- R12: Capacidad ⊕⊗ Capacidad (composición)
- R13: Capacidad(Alg) ← Capacidad(Humana) (delegación HAIC)

Propiedad_Completitud:
  ✓ Todas combinaciones relevantes cubiertas
  ✓ Relaciones derivadas de axiomas (no inventadas)
  ✓ Multiplicidades consistentes con invariantes

## §5. CONSTRAINTS INTEGRIDAD

### Regla_Lineage_Origen (consistencia R2/R3 & C3)

- **origin=Internal** ⇒ `Información.lineage.produced_by_flow_id` **o** `Información.lineage.produced_by_capacity_id` **MUST** ser **NOT NULL**.
- **origin=External** ⇒ `produced_by_flow_id = NULL` **y** `source_ref` **MUST** ser **NOT NULL**.
- **Validador**: `CHECK ( (origin='Internal' AND (produced_by_flow_id IS NOT NULL OR produced_by_capacity_id IS NOT NULL)) OR (origin='External' AND source_ref IS NOT NULL) )`


Constraints_Globales:

```YAML
  C1_Referential_Integrity:
    "Toda FK apunta a entidad existente."
    
    ∀ relación R con FK:
      ∀ entity.fk_field:
        entity.fk_field ∈ target_entity.id OR fk_field = null (if optional)
        
  C2_Acyclicity:
    "Relaciones recursivas forman DAG (no cycles)."
    
    Aplicable a:
      - R5: Información.parent_info_ids (DAG lineage)
      - R11: Propósito.parent_purpose_id (tree)
      - R12: Capacidad.component_ids (composición)
      
    Test: topological_sort succeeds
    
  C3_Type_Consistency:
    "Relaciones respetan tipos compatibles."
    
    Ejemplos:
      - R1: Capacidad.capacity_type ≥ Flujo.step.capacity_type_min
      - R10: Propósito.owner_capacity.substrate ∈ {Humano, Mixto}
      - R12: Mixto.composition tiene ≥1 Humano
      - R13: Capacidad(Alg).accountable_capacity.substrate ∈ {Humano, Mixto}
      
  C4_Mandatory_Relations:
    "Relaciones obligatorias siempre presentes."
    
    - R9: ∀ Flujo: purpose_id NOT NULL
    - R10: ∀ Propósito: owner_capacity_id NOT NULL
    - R13: ∀ Capacidad(substrate=Algorítmico): ownership.accountable_id NOT NULL
    - R2: ∀ Información (no externa): produced_by_flow_id NOT NULL
    - **Condición de origen:** si `Información.origin = Internal` ⇒ `produced_by_flow_id NOT NULL`;
      si `Información.origin = External` ⇒ `produced_by_flow_id` puede ser `NULL` (se exige `source_ref`).

Constraints_Por_Invariante:

  I1_Minimalidad → C5_Justification:
    Toda entidad tiene campo justification documentado
    (meta-constraint, verificado vía PD1)
    
  I3_Trazabilidad → C6_Audit_Trail:
    Toda entidad tiene (created_by, created_at, version)
    (schema enforced)
    
  I5_HAIC → C7_Human_Accountability:
    ∀ Capacidad(substrate=Algorítmico):
      ownership.accountable_id → Capacidad(substrate ∈ {Humano, Mixto})
      + delegation_mode: DelegationMode (valores en I5_[FENOTIPO])
      + audit_trail registra humano responsible + timestamp
    ∀ Propósito: owner_capacity.substrate ∈ {Humano, Mixto}
    ∀ Límite(crítico): owner_capacity.substrate = Humano
    (Enforcement vía R13_Delegación_HAIC)
    
  I7_Emergencia → C8_Level_Appropriateness:
    No validable en schema (validado en metodología)
    Org nivel N no usa prácticas nivel N+2
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
       Capacidad ⊕⊗ Capacidad
       (recursive, acyclic)
       
       R13 (delegación HAIC) ★ CRITICAL
       [1] ← [0..*]
       Capacidad(Algorítmica) ←delegada_por← Capacidad(Humana/Mixta)
       (mandatory para Algorítmica, enforcement I5)
       
       Visualización_R13:
       
         Humano_A ───────────────────┐
            │ (accountable)           │
            │ M1-M6 delegation        │
            ↓                         ↓
         [RPA_Bot]  [ML_Model]  [Workflow_Engine]
         substrate: substrate:   substrate:
         Algorítmico Algorítmico  Algorítmico
         
         Constraint: ∀ Algorítmica → ∃! Humano accountable

┌─────────────┐
│   LÍMITE    │ (E4)
│    [P4]     │
└──────┴──────┘
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
- R13 = Delegación HAIC (Capacidad Alg ← Humana)
- → = Unidireccional
- ★ = Relación crítica (enforcement invariante)
- ⊕⊗ = Operadores composición (paralelo/secuencial)

## §7. PROPIEDADES DERIVABLES

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
    
  Q14_Handoff_Count (G27):
    INPUT: flow_id
    OUTPUT: {handoff_count, transition_count, handoff_ratio}
    
    SELECT 
      COUNT(DISTINCT t.id) as handoff_count,
      (SELECT COUNT(*) FROM step_dependencies 
       WHERE flow_id = :flow_id) as transition_count,
      CAST(COUNT(DISTINCT t.id) AS FLOAT) / 
      (SELECT COUNT(*) FROM step_dependencies 
       WHERE flow_id = :flow_id) as handoff_ratio
    FROM 
      step_transitions t
      JOIN steps s1 ON t.from_step_id = s1.id
      JOIN steps s2 ON t.to_step_id = s2.id
      JOIN capacities c1 ON s1.capacity_id = c1.id
      JOIN capacities c2 ON s2.capacity_id = c2.id
    WHERE 
      s1.flow_id = :flow_id
      AND c1.team_id != c2.team_id
      
  Q15_Alignment_Score_Recursive (G28):
    INPUT: purpose_id
    OUTPUT: alignment_score Float[0..1]
    
    WITH RECURSIVE alignment AS (
      -- Base: Leaf purposes
      SELECT 
        id,
        AVG(kr.progress / kr.target) as score
      FROM 
        Propósito p
        JOIN key_results kr ON kr.purpose_id = p.id
      WHERE 
        NOT EXISTS (
          SELECT 1 FROM Propósito child 
          WHERE child.parent_purpose_id = p.id
        )
      GROUP BY p.id
      
      UNION ALL
      
      -- Recursive: Parent purposes
      SELECT 
        p.id,
        SUM(
          kr.weight × 
          a.score × 
          COALESCE(child_map.contribution, 1.0)
        ) / SUM(kr.weight) as score
      FROM 
        Propósito p
        JOIN Propósito child ON child.parent_purpose_id = p.id
        JOIN alignment a ON a.id = child.id
        JOIN key_results kr ON kr.purpose_id = p.id
        LEFT JOIN child_mapping child_map 
          ON child_map.parent_kr_id = kr.id 
          AND child_map.child_id = child.id
      GROUP BY p.id
    )
    SELECT score FROM alignment WHERE id = :purpose_id
    
  Q16_Validate_Composition_Acyclic (G26):
    INPUT: (none - validates entire graph)
    OUTPUT: {is_acyclic: Boolean, cycle_path: String | null}
    
    WITH RECURSIVE composition_graph AS (
      SELECT 
        id as capacity_id,
        UNNEST(composition.component_ids) as component_id,
        ARRAY[id] as path
      FROM Capacidad
      WHERE composition IS NOT NULL
      
      UNION ALL
      
      SELECT 
        cg.capacity_id,
        c.component_id,
        cg.path || c.component_id
      FROM 
        composition_graph cg
        JOIN (
          SELECT 
            id, 
            UNNEST(composition.component_ids) as component_id
          FROM Capacidad
          WHERE composition IS NOT NULL
        ) c ON c.id = cg.component_id
      WHERE 
        c.component_id != ALL(cg.path)
    )
    SELECT 
      CASE 
        WHEN EXISTS (
          SELECT 1 FROM composition_graph
          WHERE capacity_id = component_id
        ) THEN FALSE
        ELSE TRUE
      END as is_acyclic,
      (SELECT path FROM composition_graph 
       WHERE capacity_id = component_id 
       LIMIT 1) as cycle_path
       
  Q17_Capacity_Lifecycle_Forecast (G11):
    INPUT: planning_horizon (months)
    OUTPUT: List<{capacity_id, predicted_state, date}>
    
    SELECT c.id, c.lifecycle.current_state,
      CASE
        WHEN utilization<0.20 AND idle>8wks THEN 'Deprecated'
        WHEN current_state='Development' AND time>12wks THEN 'Active'
        WHEN deprecated AND sunset_date<=horizon THEN 'Retired'
      END as predicted_state
    FROM Capacidad c
    WHERE lifecycle.current_state != 'Retired'
    
  Q18_Deprecation_Impact_Analysis (G24):
    INPUT: entity_id, entity_type
    OUTPUT: {dependents, risk_score, recommended_timeline}
    
    Graph traversal R1-R13 para identificar dependents
    Risk_score = Σ(criticality_weights)
    Timeline = CASE risk_score: >50→12mo, >20→6mo, ELSE→3mo
    
  Q19_State_Delta (G1):
    INPUT: state_a_id, state_b_id
    OUTPUT: {capacities_added, capacities_removed, flows_added, flows_removed, delta_score}
    
    Compare snapshots state_a vs state_b
    Delta por entidad type (capacities, flows, purposes, limits)
    delta_score = weighted sum of changes
    
  Q20_Convergence_Score (G13):
    INPUT: current_state_id, target_state_id
    OUTPUT: convergence Float[0..1]
    
    convergence = 1 - (Δ_arch(current, target) / Δ_max)
    Δ_arch via Q19_State_Delta
    Δ_max = theoretical maximum distance
    
  Q21_Reachability_Validation (G2):
    INPUT: from_state_id, to_state_id
    OUTPUT: {reachable: Boolean, path: List<Transition>, violations: List<String>}
    
    Graph search R14 (transitions DAG)
    Validate path satisfies all constraints (INV_C1-C8, R1-R15)
    IF path_exists AND no_violations THEN reachable = true
    
  Q22_DORA_Deployment_Frequency (G4):
    INPUT: date_range
    OUTPUT: {deployments_per_day: Float, category: {Elite|High|Medium|Low}}
    
    SELECT COUNT(*) / DAYS_IN_RANGE(date_range)
    FROM E7
    WHERE status='Completed' 
      AND flow_id IN (SELECT id FROM Flujo WHERE type='Deployment')
      AND started_at BETWEEN date_range
      
  Q23_DORA_Lead_Time (G4):
    INPUT: date_range, percentile
    OUTPUT: {lead_time_p50: Duration, category: {Elite|High|Medium|Low}}
    
    SELECT PERCENTILE(metrics.cycle_time, :percentile)
    FROM E7
    WHERE flow_id IN (SELECT id FROM Flujo WHERE type='Deployment')
      AND status='Completed'
      AND started_at BETWEEN date_range
      
  Q24_DORA_Change_Failure_Rate (G4):
    INPUT: date_range
    OUTPUT: {cfr: Float, category: {Elite|High|Medium|Low}}
    
    SELECT CAST(COUNT(failures) AS FLOAT) / COUNT(total) as cfr
    FROM E7
    WHERE flow_id IN (SELECT id FROM Flujo WHERE type='Deployment')
      AND started_at BETWEEN date_range
      
  Q25_DORA_MTTR (G4):
    INPUT: date_range, severity
    OUTPUT: {mttr_p50: Duration, category: {Elite|High|Medium|Low}}
    
    SELECT PERCENTILE(resolution_time, 50)
    FROM Incident
    WHERE severity = :severity
      AND detected_at BETWEEN date_range
      AND status = 'Resolved'
      
  Q26_Portfolio_Value_Optimization (G14):
    INPUT: constraints {budget, capacity_available, H_org_min}
    OUTPUT: {optimized_portfolio: List<Purpose>, expected_value: Float}
    
    -- Portfolio optimization bajo constraints (Ecuación Maestra §7)
    -- Maximizar: V_org = Σ outcomes - Σ costs
    -- Sujeto a:
    --   1. Budget constraint: Σ cost_i <= budget_total
    --   2. Capacity constraint: Σ effort_i <= capacity_available
    --   3. H_org constraint: H_org >= H_org_min (typically 70)
    
    WITH purpose_roi AS (
      SELECT 
        p.id,
        p.objective,
        (expected_outcome * alignment_score) as value,
        estimated_cost,
        (value / NULLIF(estimated_cost, 0)) as roi,
        required_capacity_hours
      FROM Propósito p
      WHERE status = 'Active' OR status = 'Proposed'
    )
    SELECT * FROM purpose_roi
    WHERE roi > threshold
    ORDER BY roi DESC, value DESC
    -- Knapsack problem: select subset maximizing value within constraints
    
  Q27_Cross_Domain_Health (G15):
    INPUT: (none)
    OUTPUT: {H1-H5 scores, H_org composite, bottleneck_domain}
    
    SELECT
      H1_Architecture_Score,
      H2_Perception_Score,
      H3_Decision_Score,
      H4_Operation_Score,
      H5_Governance_Score,
      (H1*0.30 + H2*0.25 + H3*0.20 + H4*0.15 + H5*0.10) as H_org,
      CASE
        WHEN H1 = MIN(H1,H2,H3,H4,H5) THEN 'Architecture'
        WHEN H2 = MIN(H1,H2,H3,H4,H5) THEN 'Perception'
        WHEN H3 = MIN(H1,H2,H3,H4,H5) THEN 'Decision'
        WHEN H4 = MIN(H1,H2,H3,H4,H5) THEN 'Operation'
        ELSE 'Governance'
      END as bottleneck_domain
    FROM OrganizationalHealth
    
  Q28_Governance_Violations_Summary (G10):
    INPUT: date_range
    OUTPUT: {violations_by_type, severity_distribution, auto_remediated_count}
    
    SELECT
      limit_type,
      COUNT(*) as violation_count,
      SUM(CASE WHEN severity='Critical' THEN 1 ELSE 0 END) as critical_count,
      SUM(CASE WHEN auto_remediated THEN 1 ELSE 0 END) as auto_fixed,
      AVG(time_to_remediation) as avg_remediation_time
    FROM Violations
    WHERE detected_at BETWEEN date_range
    GROUP BY limit_type
    ORDER BY critical_count DESC
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
    
  M13_Delta_Arch (G13):
    = Weighted distance entre estado current y target
    = Σ (w_entity × |changes_entity|)
    Donde:
      w_capacity = 0.4, w_flow = 0.3, w_purpose = 0.2, w_limit = 0.1
      changes = (added + removed + modified) por entity type
    Convergence = 1 - (Δ_arch / Δ_max)
    
  # DORA Metrics Formalizadas (G4)
  M1_Deployment_Frequency (DORA):
    = COUNT(E7 WHERE status=Completed AND flow.type=Deployment) / time_period
    Aggregation: Per week, per day
    Target: Multiple deployments per day (Elite)
    Query: Q22_DORA_Deployment_Frequency(date_range)
    
  M2_Lead_Time_For_Changes (DORA):
    = PERCENTILE(E7.metrics.cycle_time, 50) WHERE flow.type=Deployment
    Measurement: commit_timestamp → production_deployed_timestamp
    Target: < 1 day (Elite), < 1 week (High)
    Query: Q23_DORA_Lead_Time(date_range, percentile)
    
  M3_Change_Failure_Rate (DORA):
    = COUNT(E7 WHERE status=Failed OR caused_incident) / COUNT(E7 total deployments)
    Target: < 5% (Elite), < 10% (High)
    Query: Q24_DORA_Change_Failure_Rate(date_range)
    
  M4_Time_To_Restore_Service (DORA):
    = PERCENTILE(Incident.resolution_time, 50) WHERE severity=Critical
    Measurement: incident_detected → service_restored
    Target: < 1 hour (Elite), < 1 day (High)
    Query: Q25_DORA_MTTR(date_range, severity)
    
  M14_Flow_Efficiency (Operacional):
    = AVG(E7.metrics.active_time / E7.metrics.cycle_time) per flow
    Target: > 0.40 (40% active work vs wait)
    
  M15_Rework_Rate:
    = COUNT(E7 WHERE metrics.rework=true) / COUNT(E7 total)
    Target: < 0.15 (15% rework acceptable)
    
  M16_Portfolio_ROI (G14):
    = Σ(purpose.value_delivered) / Σ(purpose.cost_actual)
    Calculation: Via Q26_Portfolio_Value_Optimization
    Target: > 1.5 (150% return)
    
  M17_Governance_Automation_Rate (G10):
    = COUNT(violations auto_remediated) / COUNT(violations total)
    Target: > 0.60 (60% auto-fixed)
    Query: Q28_Governance_Violations_Summary
```
