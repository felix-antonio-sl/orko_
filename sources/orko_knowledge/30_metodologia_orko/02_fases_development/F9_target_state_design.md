# F9 – Target State Design

## §0 FUNDAMENTO

```yaml
fase_id: F9
nombre_canonico: "Target State Design"
vocabulos_referencia:
  wslc_phase: "VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F9"
  axiomas:
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A1_Organizacion"
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A4_Contexto"
  primitivos:
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P2_Flujo"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P1_Capacidad"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P3_Informacion"
  invariantes:
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I4_Clasificacion_Contextual"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I7_Coherencia"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I8_Adaptacion_Contextual"
  dominios:
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D1_Arquitectura"
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D4_Operacion"
  metricas_canonicas:
    - "VOCABULARIO_CONTROLADO.layer_1.metricas_canonicas.H_org"
relacion_kernel:
  depende_de:
    - "F3"
    - "F4"
    - "F5"
  prepara_a:
    - "F10"
    - "F11"
trayectorias_soportadas:
  - "Minimal"
  - "Avanzada"
estado_fundamento: "STABLE"
notas_fundamento: |
  F9 produce E6_target (target architectural state) y target patterns de TF1/TF2/TF3.
  Entregables: F9.target_state.yaml, e6_target_schema.json, target_components.drawio
  Metodología: use TEMPLATE_FASE_WSLC.md y DEPENDENCY_GRAPH para trazabilidad.
referencias_formales:
  - "SPEC_ARQUITECTURA_DEFINITIVA.§1.4.Target_State_Design"
```

---

## §1 INTERFAZ

```yaml
inputs:
  - id: "capacity_inventory"
    source: "F4.capacity_inventory"
    schema_ref: "TF1.CapacityInventory"
    required: true
    description: "Inventario completo de capacidades target"
  
  - id: "flow_maps"
    source: "F5.flow_maps"
    schema_ref: "TF2.FlowMap"
    required: true
    description: "Mapas de flujo diseñados"
  
  - id: "information_architecture"
    source: "F6.information_architecture"
    schema_ref: "TF3.InfoArchitecture"
    required: true
    description: "Arquitectura de información y datos"
  
  - id: "okr_cascade"
    source: "F7.okr_cascade_L4_to_L1"
    required: true
    description: "OKRs cascadeados para alinear target state"
  
  - id: "limits_catalog"
    source: "F8.limits_catalog"
    schema_ref: "P4_Limite"
    required: true
    description: "Catálogo de límites operacionales"
  
  - id: "trajectory_selected"
    source: "F3.trajectory_selected"
    required: true
    description: "Trayectoria define alcance target state"

outputs:
  - id: "e6_target"
    artifact: "e6_target.yaml"
    schema_ref: "E6_ArchitecturalState (ver /10_arquitectura_orko/)"
    consumers: ["F10", "F11", "F12", "F18"]
    description: "Estado arquitectónico objetivo con TF1/TF2/TF3 integrados"
    location: "artefactos/f9/"
  
  - id: "target_diagrams"
    artifact: "target_diagrams.drawio"
    consumers: ["F11", "F12"]
    description: "Diagramas visuales de target state (C4, flow, data)"
    location: "artefactos/f9/"
  
  - id: "target_schemas"
    artifact: "target_schemas.yaml"
    consumers: ["F11", "F12"]
    description: "Schemas y contratos de componentes target"
    location: "artefactos/f9/"
  
  - id: "gap_analysis_current_to_target"
    artifact: "gap_analysis.yaml"
    consumers: ["F10", "F11"]
    description: "Análisis de gaps entre E6_current (F1) y E6_target"
    location: "artefactos/f9/"

dependencies:
  reads_from: ["F3", "F4", "F5", "F6", "F7", "F8"]
  writes_to: ["F10", "F11", "F12"]
  validates_with: ["F18"]

acceptance_criteria:
  - criterion: "E6_target.yaml completo con componentes TF1/TF2/TF3"
    verification: |
      Validar schema E6_ArchitecturalState:
      - TF1_capacities: lista completa
      - TF2_flows: mapeados a capacidades
      - TF3_data: linked a flujos
    responsible: "Role_Architect"
    bloqueante: true
  
  - criterion: "Target_diagrams incluye al menos: C4 context, flow map, data lineage"
    verification: "manual review (3 diagramas mínimos)"
    responsible: "Role_Architect"
  
  - criterion: "Gap_analysis identifica top-10 gaps críticos"
    verification: "count(gaps_críticos) >= 10"
    responsible: "Role_Architect"
  
  - criterion: "Target state alineado con OKR cascade de F7"
    verification: "manual validation: cada OKR L3 tiene componente target"
    responsible: "Role_Captain"

templates:
  - target_state_template.yaml
  - C4_diagrams_template.drawio

herramientas:
  - gap_analysis_calculator.xlsx (en /40_implementacion/calculadoras/)
```

---

## §2 DESCRIPCIÓN EJECUTIVA

F9 sintetiza los diseños de F4-F8 en un **estado arquitectónico objetivo (E6_target)** que integra capacidades (TF1), flujos (TF2) e información (TF3) bajo restricciones de F8 y alineado con propósito de F7.

**Actividades principales**:
1. Consolidar outputs de F4, F5, F6, F7, F8
2. Diseñar E6_target con componentes TF1/TF2/TF3 integrados
3. Crear diagramas arquitectónicos (C4, flujos, datos)
4. Analizar gaps: E6_current (de F1) → E6_target
5. Priorizar gaps críticos para F10 (Quick Wins)

**Herramientas**:
- drawio para diagramas
- E6_ArchitecturalState schema
- gap_analysis_calculator.xlsx

**Duración estimada**: 2-3 días (sesiones diseño + documentación)

**Owner**: Role_Architect + Role_Captain

**Nota crítica**: E6_target es referencia para F18 (Convergence Check) - debe ser preciso y medible.
