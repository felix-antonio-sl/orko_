# P0-COMPLETE – Propuesta de backlog CAP-x post-1.0.0

> Borrador sq4/E4 para P0-COMPLETE (ORKO v1.0.0). Basado en `validation_final_report.md` §5 y mandato CAP-P0-DEC-01.

## §0 Propósito

- **Qué busca:** Sintetizar 2-3 CAP-x priorizados para post-1.0.0 que atiendan los gaps más críticos
  identificados en `validation_final_report.md` §5 (G1-G7) y alineados con el trabajo iniciado por
  sq1, sq2, sq3 en P0-COMPLETE.
- **Criterios de priorización:**
  - Atienden los ejes del mandato M4.2.c: (i) consolidación F1/F3, (ii) calculadoras H_org/trayectoria/convergencia,
    (iii) refuerzo §0 FUNDAMENTO en fases CONDITIONAL.
  - Maximizan impacto en invariantes I1-I8 que están CONDITIONAL.
  - Aprovechan el trabajo ya iniciado por sq1/sq2/sq3 durante P0.

## §1 Gaps del §5 (resumen)

Según `validation_final_report.md` §5, los gaps conocidos son:

- **G1**: §0 FUNDAMENTO incompleto en 10/18 fases (F1, F3, F7, F9, F13-F18) – afecta I1/I3/I4/I7.
- **G2**: Coverage VOCAB Layer 0-3 vs docs/playbooks/trayectorias – afecta I1/I2/I7.
- **G3**: Profundidad en templates y calculadoras (contenido esquelético) – afecta I1/I4/I7/I8.
- **G4**: Auditorías end-to-end por caso (solo 3/6 casos auditados en profundidad) – afecta I2/I3/I4/I6/I7/I8.
- **G5**: Métricas y validación empírica (falta datos operativos) – afecta I2/I4/I7/I8.
- **G6**: RACI por playbook y anotación de trayectoria/tiempo – afecta I5/I6/I8.
- **G7**: Automatización parcial de auditorías – afecta I3/I8.

## §2 Propuesta de CAP-x priorizados

### CAP-22: Calculadoras H_org / Trayectoria / Convergencia

- **Objetivo:**
  - Transformar las calculadoras `health_score_calculator.xlsx`, `context_decision_matrix.xlsx` y
    `convergence_tracker.xlsx` de placeholders controlados a herramientas ejecutables y trazables.
- **Alcance:**
  - Implementar especificaciones textuales diseñadas en P0 (trabajo de sq2).
  - Definir fórmulas operativas para H_org (descomposición A/P/D, contribución TF1/TF2/TF3) alineadas con
    `out/00_fundamentos_teoricos.md` y `out/20_tejidos.md`.
  - Formalizar reglas de decisión DM1-DMx para `context_decision_matrix` coherentes con G1-G4 y F3.
  - Diseñar métrica de convergencia E6_current→E6_target para `convergence_tracker` (F9/F18).
  - Aplicar estas calculadoras a los casos `01_startup_50p_completo` y `06_gore_nuble_completo` como
    validación mínima.
- **Impacto en gaps:**
  - Aborda directamente **G3** (profundidad en calculadoras).
  - Contribuye a **G4** (auditorías end-to-end por caso, al aplicar calculadoras a 01/06).
  - Establece base para **G5** (métricas empíricas futuras).
- **Impacto en invariantes:**
  - Mejora I1 (trazabilidad kernel-fenotipos), I4 (operacionalidad), I7 (salud), I8 (adaptabilidad).
- **Relación con P0:**
  - Aprovecha el trabajo de sq2 (especificaciones textuales) y el mapa de sq4
    (`P0_calculadoras_y_templates_map.md`).
- **Entregables mínimos:**
  - Especificaciones formales en `dev_specs/` (esquemas de hojas, fórmulas, parámetros).
  - Actualización de los 3 archivos .xlsx con contenido operativo (o versiones nuevas si es necesario).
  - Aplicación documentada en `01_startup_50p_completo/artefactos.md` y
    `06_gore_nuble_completo/artefactos.md`.
  - Micro-guía de uso de las calculadoras para contextos típicos.

---

### CAP-23: Consolidación F1/F3 y §0 FUNDAMENTO en Initiation

- **Objetivo:**
  - Cerrar el gap de F1 (Context Assessment) y F3 (Trajectory Selection) completando sus contratos
    (§0 FUNDAMENTO, §1 INTERFAZ) y aplicándolos explícitamente a casos guía.
- **Alcance:**
  - Redactar §0 FUNDAMENTO y §1 INTERFAZ de `F1_context_assessment.md` y `F3_trajectory_selection.md`
    siguiendo el patrón de F2/F4-F6/F8 (trabajo iniciado por sq1).
  - Aplicar F1/F3 a `01_startup_50p_completo` y `06_gore_nuble_completo`: explicitar en `context.yaml`
    y `trajectory.md` cómo se instancian los artefactos F1/F3 y cómo se usa `context_decision_matrix`.
  - Producir resumen por caso: inputs F1, decisión F3, bandas G1-G4 aplicadas, vínculo con H_org.
- **Impacto en gaps:**
  - Aborda **G1** (§0 FUNDAMENTO incompleto) específicamente para F1 y F3.
  - Contribuye a **G4** (auditorías end-to-end) al hacer explícita la aplicación de F1/F3 en casos.
- **Impacto en invariantes:**
  - Mejora I1 (trazabilidad), I2 (consistencia interna), I3 (coherencia), I6 (convergencia).
- **Relación con P0:**
  - Aprovecha el trabajo de sq1 (borradores de §0/§1 para F1/F3) y de sq3 (micro-template de §0
    FUNDAMENTO).
- **Entregables mínimos:**
  - `F1_context_assessment.md` y `F3_trajectory_selection.md` con §0 y §1 completos.
  - `context.yaml` y `trajectory.md` actualizados en casos 01/06 con trazabilidad explícita a F1/F3.
  - Resumen por caso en `artefactos.md` o documento nuevo: flujo contexto→trayectoria→health.

---

### CAP-24: Refuerzo §0 FUNDAMENTO en Operation/Evolution (F13-F18)

- **Objetivo:**
  - Completar §0 FUNDAMENTO en las fases del bloque Operation (F13-F15) y Evolution (F16-F18) para
    llevarlas de estado CONDITIONAL a un estándar cercano a PASSED.
- **Alcance:**
  - Aplicar el micro-template de §0 FUNDAMENTO diseñado por sq3 a F13-F18.
  - Explicitar axiomas, primitivos, invariantes, dominios y su relación con VOCAB/DEP_GRAPH.
  - Marcar como CONDITIONAL cualquier parte que dependa de backlog futuro (ej. métricas empíricas de G5).
  - Registrar [OUTCOME] por fase intervenida en el board.
- **Impacto en gaps:**
  - Aborda **G1** (§0 FUNDAMENTO incompleto) específicamente para 6 fases (F13-F18).
  - Contribuye a **G2** (coverage VOCAB) al hacer explícitas las referencias a VOCAB en estas fases.
- **Impacto en invariantes:**
  - Mejora I1 (trazabilidad), I3 (coherencia), I4 (operacionalidad), I7 (salud).
- **Relación con P0:**
  - Aprovecha el micro-template de sq3 y el mandato M2.1-M2.3 para F1/F3/F13 (extendiendo a F14-F18).
- **Entregables mínimos:**
  - §0 FUNDAMENTO completo en `30_metodologia_orko/04_fases_operation/F13-F15` y
    `30_metodologia_orko/05_fases_evolution/F16-F18`.
  - Micro-template de §0 FUNDAMENTO documentado en `dev_specs/` o en `GUIA_AUTOR_CONTENIDO.md`.
  - [OUTCOME] por fase en el board trazando fuentes usadas (VOCAB, DEP_GRAPH, fundamentos).

---

## §3 Criterios de decisión para el Capitán

- **Si se prefiere impacto inmediato en operacionalidad:** Priorizar **CAP-22** (calculadoras) como primer
  CAP post-1.0.0, luego CAP-23, luego CAP-24.
- **Si se prefiere consolidar contratos antes de herramientas:** Priorizar **CAP-23** (F1/F3), luego
  CAP-24 (fundamentos), luego CAP-22 (calculadoras).
- **Si se prefiere barrido transversal de fundamentos:** Fusionar CAP-23 y CAP-24 en un único CAP de
  §0 FUNDAMENTO para todas las fases CONDITIONAL (F1, F3, F7, F9, F13-F18).

## §4 Gaps NO priorizados en esta propuesta

Los siguientes gaps quedan fuera del alcance de los CAP-x propuestos, pero se recomienda abordarlos en
una segunda ola post-1.0.0:

- **G2** (coverage VOCAB Layer 0-3): requiere diseño de auditoría sistemática, podría ser CAP-25 o
  parte de CAP-24 si se extiende.
- **G4** (auditorías end-to-end en los 6 casos): parcialmente cubierto por CAP-22 y CAP-23, pero
  faltaría procedimiento estándar y aplicación a los 3 casos restantes (`02_scaleup_200p_completo`,
  `03_enterprise_2000p_completo`, otros).
- **G5** (métricas y validación empírica): requiere datos operativos y promoción de métricas candidatas
  a VOCAB v1.1.x; fuera del alcance inmediato post-1.0.0.
- **G6** (RACI por playbook): diseño de plantillas RACI fino; podría ser CAP-26.
- **G7** (automatización de auditorías): scripts/checklists semi-automatizados; podría ser CAP-27 o
  trabajo continuo de E4.

---

## §5 Recomendación de sq4/E4

**Proponer al Capitán que abra CAP-22, CAP-23 y CAP-24 como siguiente conjunto de CAP-x post-1.0.0**,
priorizando el orden según el criterio de §3. Estos 3 CAP-x cierran los ejes más críticos del mandato
M4.2.c y aprovechan el trabajo ya iniciado por sq1, sq2, sq3 durante P0-COMPLETE, manteniendo el
kernel/VOCAB/DEP_GRAPH/VG3/VG4 intocados según CAP-21.
