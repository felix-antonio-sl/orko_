# F2 – Vision Definition

## §0 FUNDAMENTO

```yaml
fase_id: F2
nombre_canonico: "Vision Definition"
vocabulos_referencia:
  wslc_phase: "VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F2"
  axiomas:
    - "VOCABULARIO_CONTROLADO.layer_0.axiomas.A2_Proposito"
  primitivos:
    - "VOCABULARIO_CONTROLADO.layer_0.primitivos.P5_Proposito"
  invariantes:
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I3_Trazabilidad"
    - "VOCABULARIO_CONTROLADO.layer_0.invariantes.I5_HAIC"
  dominios:
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D1_Arquitectura"
    - "VOCABULARIO_CONTROLADO.layer_1.dominios.D3_Decision"
relacion_kernel:
  depende_de:
    - "F1"
    - "F3"
  prepara_a:
    - "F7"
    - "F9"
trayectorias_soportadas:
  - "Minimal"
  - "Avanzada"
  - "Survival"
```

## §1 INTERFAZ

```yaml
inputs:
  - id: "F1.context_profile_36_params"
    fuente: "F1"
  - id: "F1.h_org_baseline"
    fuente: "F1"
  - id: "F3.trajectory_selected"
    fuente: "F3"
  - id: "F3.timeline_commitment"
    fuente: "F3"
  - id: "F3.budget_allocation"
    fuente: "F3"
  - id: "F7.okr_L4"
    fuente: "F7"
outputs:
  - id: "vision_statement"
    archivo: "vision_statement.md"
    descripcion: "Narrativa de vision ligada a F2 (Vision Definition)"
  - id: "vision_constraints"
    archivo: "vision_constraints.yaml"
    descripcion: "Conjunto de limites macro modelados con P4_Limite"
  - id: "okr_L4"
    descripcion: "OKR de nivel organizacional consumidos por F7 y F9"
  - id: "okr_L4_refined"
    descripcion: "Version refinada de okr_L4 cuando aplique"
  - id: "north_star"
    descripcion: "Declaracion North Star alineada a F2 y F9"
  - id: "north_star_metrics"
    descripcion: "Conjunto de metricas asociadas a north_star"
dependencies:
  reads_from:
    - "F1"
    - "F3"
    - "F7"
  writes_to:
    - "F3"
    - "F7"
    - "F9"

acceptance_criteria:
  - criterion: "vision_statement.md completo con secciones: contexto, ambición, constraints, horizonte temporal"
    verification: "manual"
    responsible: "Role_Captain"
  
  - criterion: "okr_L4.yaml con 3-8 objetivos (según trajectory)"
    verification: "automated (count okrs)"
    responsible: "Role_Captain"
    
  - criterion: "vision_constraints.yaml alineado con F3.trajectory_selected"
    verification: "compatibility_score >= 0.80 (ver F2_F3_convergence_protocol.md)"
    responsible: "Role_TrajectoryOwner"
    
  - criterion: "Sponsor_L1_Human aprueba vision_statement"
    verification: "firma sponsor_approval en artefacto"
    responsible: "Sponsor_L1_Human"
    bloqueante: true

protocol_ref:
  convergencia_f2_f3: "01_fases_initiation/F2_F3_convergence_protocol.md"
  descripcion: "F2 y F3 tienen dependencia circular resuelta por protocolo iterativo"

templates:
  - T02_vision_statement.md
  - T07_okr_cascade.xlsx (para okr_L4)
```

---

## §2 DESCRIPCIÓN EJECT

F2 transforma el perfil de contexto (F1) en una **declaración de visión** que articula propósito, ambición y límites de la organización bajo la restricción de la trayectoria seleccionada (F3).

**Actividades principales**:
1. Revisar F1.context_profile y F3.trajectory_selected
2. Facilitar sesión vision workshop con stakeholders clave
3. Redactar vision_statement.md (narrativa inspiracional + pragmática)
4. Derivar okr_L4 (objetivos organizacionales nivel 4)
5. Documentar vision_constraints explícitos
6. Validar con F3 que vision es compatible con trajectory (ver protocolo convergencia)

**Herramientas**:
- Template T02_vision_statement.md
- OKR cascade worksheet (T07)
- F2_F3_convergence_protocol.md (gestión circularidad)

**Duración estimada**: 4-6 horas (sin iteraciones), 1-2 días (con iteraciones F2↔F3)

**Owner**: Role_Captain + Sponsor_L1_Human
