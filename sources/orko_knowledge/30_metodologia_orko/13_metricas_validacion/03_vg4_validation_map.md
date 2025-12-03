# 03_vg4_validation_map (draft)

## §0. Fundamento

- Invariantes: `I1`–`I8` (ver `VOCABULARIO_CONTROLADO.layer_0.invariantes` y `00_fundamentos_teoricos`).
- Health gates: `G1_H_org_Critico`, `G2_H_org_Bajo_Riesgo`, `G3_H_org_Bueno_Eficiencia_Baja`, `G4_Ready_For_Avanzada` (ver `02_health_gates.md`).
- Métricas canónicas: `H_org`, `eta_org`, `ROI_Habilitacion`.
- Trayectorias: `Survival`, `Minimal`, `Avanzada`.
- Governance: `01_team_structure_raci.md` (roles y RACI por gate).
- Decision support: `03_decision_matrix.md`.
 - Casos de ejemplo: 6 contextos completos en `40_implementacion_metodologia/ejemplos/*_completo` (startup, scaleup, enterprise, fintech, manufacturing, sector público).

Propósito: mapear, para cada invariante `I1`–`I8`, qué artefactos existentes sirven como evidencia operable para VG4, sin introducir nuevas métricas ni modificar el kernel (`VOCAB` + `DEPENDENCY_GRAPH`). Foco extra en `I3`, `I5`, `I6`, `I8` según CAP-12.

---

## §1. Mapa de evidencias por invariante

```yaml
vg4_validation_map:

  - invariante: "I1"
    prioridad_vg4: "media"
    descripcion_resumida: "Ver VOCAB/00_fundamentos_teoricos (invariante I1)."
    evidencias_principales:
      - tipo: "metodologia_core"
        artefactos:
          - "30_metodologia_orko/00_wip_desarrollo_metodologia/00_instrucciones_equipos_desarrollo.md"
          - "30_metodologia_orko/00_wip_desarrollo_metodologia/SPEC_ARQUITECTURA_DEFINITIVA.md"
      - tipo: "trazabilidad_dominios↔fases↔playbooks"
        artefactos:
          - "out/30_metodologia_orko.md"  # mapeo D1–D4 ↔ F1–F18 ↔ P01–P15
    gaps_v0_1:
      - "Aún no existe un checklist operativo por invariante; se espera refinar en sprints futuros."

  - invariante: "I2"
    prioridad_vg4: "media"
    descripcion_resumida: "Ver VOCAB/00_fundamentos_teoricos (invariante I2)."
    evidencias_principales:
      - tipo: "arquitectura_orko"
        artefactos:
          - "out/10_arquitectura_orko.md"
      - tipo: "tejidos"
        artefactos:
          - "out/20_tejidos.md"
    gaps_v0_1:
      - "Los 6 casos en 40_implementacion_metodologia/ejemplos muestran I2 en operación en contextos diversos; sigue pendiente sistematizar métricas cuantitativas específicas por caso."

  - invariante: "I3"
    prioridad_vg4: "alta"
    descripcion_resumida: "Trazabilidad extremo-a-extremo entre GENOME y FENOTIPO (IDs canónicos, DEP_GRAPH, VOCAB)."
    evidencias_principales:
      - tipo: "kernel_semantico"
        artefactos:
          - "40_implementacion_metodologia/dev_specs/VOCABULARIO_CONTROLADO.yaml"
          - "40_implementacion_metodologia/dev_specs/DEPENDENCY_GRAPH.yaml"
          - "40_implementacion_metodologia/dev_specs/dependency_closure_script.py"
          - "40_implementacion_metodologia/dev_specs/KERNEL_READINESS.md"
      - tipo: "health_gates_y_metricas"
        artefactos:
          - "30_metodologia_orko/13_metricas_validacion/02_health_gates.md"
      - tipo: "governance_y_trayectorias"
        artefactos:
          - "30_metodologia_orko/12_roles_governance/01_team_structure_raci.md"
          - "30_metodologia_orko/09_trayectorias/01_minimal_6_12_meses.md"
          - "30_metodologia_orko/09_trayectorias/02_avanzada_18_36_meses.md"
          - "30_metodologia_orko/09_trayectorias/04_survival_0_10K.md"
          - "30_metodologia_orko/09_trayectorias/03_decision_matrix.md"
      - tipo: "coordinacion"
        artefactos:
          - "30_metodologia_orko/00_wip_desarrollo_metodologia/board_coordinación.md"
    gaps_v0_1:
      - "Falta un procedimiento explícito de auditoría de trazabilidad (cómo revisar un caso concreto de inicio a fin)."

  - invariante: "I4"
    prioridad_vg4: "media"
    descripcion_resumida: "Ver VOCAB/00_fundamentos_teoricos (invariante I4)."
    evidencias_principales:
      - tipo: "fases_development_implementation"
        artefactos:
          - "30_metodologia_orko/02_fases_development/F4_capability_mapping.md"
          - "30_metodologia_orko/02_fases_development/F5_flow_design.md"
          - "30_metodologia_orko/02_fases_development/F6_information_architecture.md"
          - "30_metodologia_orko/03_fases_implementation/F10_quick_wins.md"
          - "30_metodologia_orko/03_fases_implementation/F11_fabric_deployment.md"
          - "30_metodologia_orko/03_fases_implementation/F12_state_transition.md"
      - tipo: "schemas"
        artefactos:
          - "40_implementacion_metodologia/dev_specs/schemas/compliance_framework_schema.yaml"
          - "40_implementacion_metodologia/dev_specs/schemas/context_pattern_schema.yaml"
    gaps_v0_1:
      - "Requiere vincular explícitamente estos artefactos con métricas de resultado en ejemplos concretos."

  - invariante: "I5"
    prioridad_vg4: "alta"
    descripcion_resumida: "Accountability humana clara en decisiones y ejecución (HAIC)."
    evidencias_principales:
      - tipo: "governance_roles"
        artefactos:
          - "30_metodologia_orko/12_roles_governance/01_team_structure_raci.md"
      - tipo: "health_gates"
        artefactos:
          - "30_metodologia_orko/13_metricas_validacion/02_health_gates.md"
      - tipo: "coordinacion"
        artefactos:
          - "30_metodologia_orko/00_wip_desarrollo_metodologia/board_coordinación.md"
    gaps_v0_1:
      - "Aún no hay plantillas de RACI por playbook ni registros de casos reales; se validará solo a nivel de diseño de roles/gates."

  - invariante: "I6"
    prioridad_vg4: "alta"
    descripcion_resumida: "Trajectory-awareness: decisiones y artefactos conscientes de la trayectoria activa y posibles cambios."
    evidencias_principales:
      - tipo: "trayectorias"
        artefactos:
          - "30_metodologia_orko/09_trayectorias/01_minimal_6_12_meses.md"
          - "30_metodologia_orko/09_trayectorias/02_avanzada_18_36_meses.md"
          - "30_metodologia_orko/09_trayectorias/04_survival_0_10K.md"
          - "30_metodologia_orko/09_trayectorias/03_decision_matrix.md"
      - tipo: "health_gates"
        artefactos:
          - "30_metodologia_orko/13_metricas_validacion/02_health_gates.md"
      - tipo: "playbooks"
        artefactos:
          - "30_metodologia_orko/06_playbooks_recovery/P01_low_h_org_recovery.md"
          - "30_metodologia_orko/06_playbooks_recovery/P02_handoff_reduction.md"
          - "30_metodologia_orko/06_playbooks_recovery/P03_okr_alignment.md"
          - "30_metodologia_orko/06_playbooks_recovery/P04_security_remediation.md"
          - "30_metodologia_orko/07_playbooks_transformation/P05_bounded_autonomy_m6.md"
    gaps_v0_1:
      - "Falta una guía explícita de cómo anotar el estado de trayectoria en artefactos operativos (ej. en casos o backlogs)."

  - invariante: "I7"
    prioridad_vg4: "media"
    descripcion_resumida: "Ver VOCAB/00_fundamentos_teoricos (invariante I7)."
    evidencias_principales:
      - tipo: "metodologia+tejidos"
        artefactos:
          - "out/30_metodologia_orko.md"
          - "out/20_tejidos.md"
    gaps_v0_1:
      - "Conectada conceptualmente a los 6 casos en 40_implementacion_metodologia/ejemplos; permanece pendiente definir métricas cuantitativas y checks específicos para I7 por caso."

  - invariante: "I8"
    prioridad_vg4: "alta"
    descripcion_resumida: "Consistencia temporal (lectura del tiempo y adaptación), ver VOCAB."
    evidencias_principales:
      - tipo: "fases_evolution+operation"
        artefactos:
          - "30_metodologia_orko/05_fases_evolution/README.md"
          - "30_metodologia_orko/02_fases_development/F6_information_architecture.md"
          - "30_metodologia_orko/03_fases_implementation/F10_quick_wins.md"
          - "30_metodologia_orko/03_fases_implementation/F11_fabric_deployment.md"
          - "30_metodologia_orko/03_fases_implementation/F12_state_transition.md"
          - "F15"  # cadencias
      - tipo: "health_gates_y_trayectorias"
        artefactos:
          - "30_metodologia_orko/13_metricas_validacion/02_health_gates.md"
          - "30_metodologia_orko/09_trayectorias/03_decision_matrix.md"
      - tipo: "coordinacion"
        artefactos:
          - "30_metodologia_orko/00_wip_desarrollo_metodologia/board_coordinación.md"
    gaps_v0_1:
      - "No se han definido aún KPIs temporales explícitos más allá de H_org/eta_org/ROI_Habilitacion; validación será cualitativa en SPRINT 1."
```

---

## §2. Uso del mapa en VG4 (v0.1)

- Este mapa sirve como índice: para cada invariante, qué artefactos revisar al hacer completitud de metodología (VG4) sin cambiar el kernel.
- Para SPRINT 1, la validación será principalmente **de diseño** (¿existen artefactos que soporten la invariante?) más que de datos empíricos.
- I3, I5, I6 e I8 tienen prioridad alta y deben recibir más atención en `17_validacion_final/01_validacion_trazabilidad_i1_i8.md`.

## §3. Puntos abiertos v0.1

- No se introducen nuevas métricas ni IDs; cualquier futura métrica adicional deberá añadirse primero a `VOCABULARIO_CONTROLADO`.
- Este mapa no pretende ser exhaustivo; se actualizará en sprints futuros cuando existan más ejemplos y casos (`40_implementacion_metodologia/ejemplos`).
- La conexión con checklists y scripts de validación automáticos se definirá después de probar el uso manual del mapa en al menos un caso de implementación completa.
