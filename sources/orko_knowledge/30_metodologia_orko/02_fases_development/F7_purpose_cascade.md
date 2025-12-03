# F7 – Purpose Cascade

## §0 FUNDAMENTO

```yaml
fase_id: F7
nombre_canonico: "Purpose Cascade"
vocabulos_referencia:
  wslc_phase: "VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F7"
  axiomas:
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A2_Proposito"
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A5_Cambio"
  primitivos:
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P5_Proposito"
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P1_Capacidad"
  invariantes:
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I3_Trazabilidad"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I5_HAIC"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I7_Coherencia"
  dominios:
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D1_Arquitectura"
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D3_Decision"
  metricas_canonicas:
    - "VOCABULARIO_CONTROLADO.layer_1.metricas_canonicas.H_org"
relacion_kernel:
  depende_de:
    - "F2"
    - "F3"
  prepara_a:
    - "F9"
    - "F11"
trayectorias_soportadas:
  - "Minimal"
  - "Avanzada"
estado_fundamento: "STABLE"
notas_fundamento: |
  F7 define la cascada de propósito (OKR L4→L3→L2) y su mecanismo de verificación.
  Entregables: okr_L4_refined, purpose_policy.yaml, okr_alignment_report.
  Requiere: TEMPLATE_PLAYBOOK.md y T07_okr_cascade.xlsx.
referencias_formales:
  - "SPEC_ARQUITECTURA_DEFINITIVA.§1.3.Purpose_Cascade"
```

---

## §1 INTERFAZ

```yaml
inputs:
  - id: "vision_statement"
    source: "F2.vision_statement"
    schema_ref: "T02_vision_statement.md"
    required: true
    description: "Narrativa de visión organizacional"
  
  - id: "okr_L4"
    source: "F2.okr_L4"
    schema_ref: "okr_schema.yaml"
    required: true
    description: "Objetivos organizacionales nivel 4 (3-8 OKRs)"
  
  - id: "trajectory_selected"
    source: "F3.trajectory_selected"
    required: true
    description: "Trayectoria define alcance cascade (L4→L3 o L4→L1)"

outputs:
  - id: "okr_cascade_L4_to_L1"
    artifact: "okr_cascade.yaml"
    schema_ref: "okr_cascade_schema.yaml"
    consumers: ["F9", "F11", "F13"]
    description: "Cascada OKR completa desde org (L4) hasta equipos (L1)"
    location: "artefactos/f7/"
  
  - id: "purpose_policy"
    artifact: "purpose_policy.yaml"
    consumers: ["F5", "F6", "F9"]
    description: "Políticas de alineamiento propósito-capacidad"
    location: "artefactos/f7/"
  
  - id: "alignment_matrix"
    artifact: "alignment_matrix.xlsx"
    consumers: ["F13", "P13"]
    description: "Matriz de alineamiento OKR×Capacidades×Flujos"
    template: "T07_okr_cascade.xlsx"
    location: "artefactos/f7/"

dependencies:
  reads_from: ["F2", "F3", "F4"]
  writes_to: ["F5", "F6", "F9", "F11"]
  informs: ["F13"]

acceptance_criteria:
  - criterion: "okr_cascade completa desde L4 hasta nivel requerido por trajectory"
    verification: |
      Minimal: L4→L3 (áreas)
      Avanzada: L4→L1 (equipos individuales)
    responsible: "Role_Captain"
  
  - criterion: "Cada OKR tiene owner HUMANO asignado (I5_HAIC)"
    verification: "automated (check okr_cascade.yaml field 'owner' != null AND owner.type == 'human')"
    responsible: "Role_HealthOwner"
    bloqueante: true
  
  - criterion: "Purpose_policy.yaml define criterios alignment capacity→okr"
    verification: "manual review"
    responsible: "Role_Architect"
  
  - criterion: "Alignment_matrix cubre top-10 capacidades críticas"
    verification: "count(capacities_mapped) >= 10"
    responsible: "Role_CapacityOwner"

templates:
  - T07_okr_cascade.xlsx

herramientas:
  - okr_alignment_calculator.xlsx (en /40_implementacion/calculadoras/)
```

---

## §2 DESCRIPCIÓN EJECUTIVA

F7 descompone la visión organizacional (F2) en objetivos cascadeados (OKR L4→L1) y define políticas de alineamiento entre propósito, capacidades y flujos.

**Actividades principales**:
1. Revisar F2.okr_L4 y F3.trajectory_selected
2. Facilitar sesión OKR cascade con líderes de área
3. Descomponer cada OKR L4 en OKRs L3 (áreas) y L2/L1 (equipos, si Avanzada)
4. Asignar owners HUMANOS a cada OKR (obligatorio I5_HAIC)
5. Crear purpose_policy.yaml con reglas alineamiento
6. Poblar alignment_matrix con mapeo OKR↔Capacidades

**Herramientas**:
- T07_okr_cascade.xlsx (template)
- okr_alignment_calculator.xlsx

**Duración estimada**: 1-2 días (sesiones facilitadas + documentación)

**Owner**: Role_Captain + líderes de área

**Nota**: F7 es crítico para I3 (Trazabilidad) - todo OKR debe ser trazable hasta F2.vision_statement.
