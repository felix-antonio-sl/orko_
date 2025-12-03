# CHANGELOG – Implementación Metodología ORKO

Todas las fechas en UTC-3.

## [1.0.0] – 2025-11-17 – VG4 / CAP-14–CAP-19

**Contexto**

- `CAP-14` (E1) – Kernel semántico `v1.0.0-kernel` validado:
  - `VOCABULARIO_CONTROLADO.yaml` + `DEPENDENCY_GRAPH.yaml` consistentes según `dependency_closure_script.py`.
  - `validation_kernel_report.md`, `validation_expansion_report.md`, `VOCAB_v1.1.x_NOTAS.md` documentan el estado del kernel y de la expansión sin modificar el VOCAB.
- `CAP-15` (E2) – 6 casos completos en `ejemplos/*_completo` (`context`+`trajectory`+`artefactos`) usados como evidencia central de aplicación.
- `CAP-16` (E3) – Catálogo de playbooks P01–P15 y `playbook_instances.yaml` cerrado como contrato (VG3 estable).
- `CAP-17`/`CAP-19` (E4 + Capitán) – VG4 (I1–I8) auditado y sintetizado en `30_metodologia_orko/17_validacion_final/validation_final_report.md`.

**Alcance de ORKO v1.0.0 (implementación)**

- **Kernel y especificaciones**
  - Kernel semántico congelado en `VOCABULARIO_CONTROLADO.yaml` + `DEPENDENCY_GRAPH.yaml`.
  - Scripts y dev_specs en `dev_specs/` (`dependency_closure_script.py`, `CHECKLIST_VALIDACION.md`, schemas) usados como base de validación.

- **Calculadoras** (`calculadoras/`)
  - Se consolidan 6 calculadoras clave:
    - `budget_parametric_allocator.xlsx`
    - `context_decision_matrix.xlsx`
    - `convergence_tracker.xlsx`
    - `health_score_calculator.xlsx`
    - `regulatory_compliance_tracker.xlsx`
    - `roi_estimator.xlsx`
  - Estado 1.0.0: archivos presentes y cableados a fases/kernel (F1/F3/F7/F9/F13) según `PLAN_ETAPA_1_KERNEL.md` y `SPEC_ARQUITECTURA_DEFINITIVA.md`, pero en gran medida como **placeholders** (contenido interno a refinar en versiones posteriores).

- **Templates** (`templates/`)
  - Árbol T01–T20 organizado por categoría: `assessment/`, `planning/`, `execution/`, `evolution/`, `compliance/`, `context_specific/`.
  - T01 (`context_assessment`), T07 (`okr_cascade`) y T12 (`adr_template`) quedan anclados a fases kernel críticas (F1, F7, F9).

- **Casos de ejemplo** (`ejemplos/*_completo/`)
  - 6 casos completos (startup, scaleup, enterprise, fintech, manufacturing, sector público) con:
    - `context.yaml` conforme al schema de contexto.
    - `trajectory.md` ligado a `03_decision_matrix.md` + G1–G4.
    - `artefactos.md` referenciando fases WSLC, playbooks P01–P15, templates y calculadoras existentes.
  - Auditoría v0.1 más profunda sobre 3 casos (`01_startup_50p_completo`, `02_scaleup_200p_completo`, `06_gore_nuble_completo`) documentada en `validation_final_report.md` §2.5.

**Estado de invariantes I1–I8 (VG4)**

Según `30_metodologia_orko/17_validacion_final/validation_final_report.md` §3 (CAP-17/CAP-19), para ORKO v1.0.0:

- I3 (Trazabilidad extremo-a-extremo), I5 (Accountability humana) e I6 (Trajectory-awareness) quedan en estado **PASSED**.  
- I1 (Minimalidad), I2 (Ortogonalidad), I4 (Contratos y capas), I7 (Coherencia entre capas) e I8 (Consistencia temporal/adaptación) quedan en estado **CONDITIONAL**.

Los riesgos y trabajos pendientes asociados a estas invariantes `CONDITIONAL` están detallados en §5 de `validation_final_report.md` y constituyen el backlog principal post-1.0.0.

**Limitaciones conocidas (ver también `validation_final_report.md` §5)**

- Calculadoras: se valida solo presencia y wiring conceptual; las fórmulas/modelos internos deberán fortalecerse en versiones posteriores.
- Templates: el catálogo T01–T20 existe y se usa en casos, pero la documentación de uso detallado y la cobertura completa T01–T25 quedan como backlog.
- Casos: solo 3 de los 6 casos han sido auditados end-to-end en profundidad; los otros 3 se validan estructuralmente.

Para un resumen completo de la validación y de los gaps aceptados en ORKO v1.0.0, ver:

- `30_metodologia_orko/17_validacion_final/validation_final_report.md`

