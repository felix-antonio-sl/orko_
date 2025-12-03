## 04_fases_operation – Bloque Operation (F13–F15)

Este directorio agrupa las fases de **Operation** del WSLC ORKO. Su función es operar el sistema de trabajo diseñado en Development (F4–F9) e implementado en Implementation (F10–F12), monitoreando la salud organizacional, respondiendo a incidentes y manteniendo la ejecución continua.

---

### §0 Propósito del bloque

- Mantener una **visión en tiempo casi real** del estado del sistema (`H_org`, `eta_org`, señales de riesgo) y de la ejecución de cambios.
- Coordinar la **respuesta a incidentes** que comprometen la estabilidad del sistema de trabajo (operacional, seguridad, cumplimiento, confianza).
- Asegurar que la ejecución diaria se mantiene **alineada** con el diseño objetivo (F9) y con las limitaciones de contexto (F1/F3/F8), sirviendo de puente hacia las fases de Evolution (F16–F18).

Este bloque se apoya en los contratos formales descritos en:

- `VOCABULARIO_CONTROLADO.yaml` (fase_id F13–F15, métricas canónicas, entidades como `H_org`).
- `DEPENDENCY_GRAPH.yaml` (relaciones `reads_from`/`writes_to` entre Operation, Development, Implementation y Evolution).
- `30_metodologia_orko/13_metricas_validacion/02_health_gates.md` (definición de G1–G4 y uso de métricas canónicas).

---

### §1 Fases incluidas

#### F13 – Health Monitoring

- Monitorea la **salud organizacional** (H_org y métricas relacionadas) y el desempeño del sistema de trabajo.
- Consume artefactos generados en F1/F4–F12 (contexto, capacidades, flujos, información, quick wins, despliegue de tejidos, planes de transición) y produce dashboards y señales de gates.
- Es la fase principal donde se evalúan y disparan los health gates G1–G4 descritos en `02_health_gates.md`.

#### F14 – Incident Response

- Coordina la **respuesta a incidentes** relevantes para el sistema ORKO: fallas operacionales críticas, incidentes de seguridad, desviaciones graves de diseño, incumplimientos regulatorios, etc.
- Utiliza playbooks de la familia Recovery/Operational (P01–P04, P10–P15) definidos en `06_playbooks_recovery/` y `08_playbooks_operational/`.
- Asegura que los incidentes quedan documentados y que se cierran bucles hacia F16/F17 (aprendizajes y ajustes de trayectoria).

#### F15 – Continuous Execution

- Se encarga de la **ejecución continua** del sistema de trabajo bajo los límites, capacidades y flujos diseñados.
- Orquesta el uso rutinario de playbooks, templates y calculadoras para mantener la operación dentro de las bandas definidas por los health gates.
- Provee insumos a F16/F17 sobre cómo se están usando los artefactos y qué fricciones o patrones emergen en la práctica.

---

### §2 Relación con trayectorias, health gates y casos

- **Trayectorias (`Survival`/`Minimal`/`Avanzada`):**
  - F13–F15 operan bajo la trayectoria elegida en F3, ajustando la agresividad de cambios y la tolerancia al riesgo.
  - En contextos `Survival`, el foco está en estabilizar H_org y reducir riesgo antes de aplicar cambios mayores.

- **Health gates (G1–G4):**
  - F13 evalúa continuamente las condiciones de G1–G4 y dispara playbooks adecuados (Recovery/Transformation/Operational) según `02_health_gates.md`.
  - F14 y F15 ejecutan y consolidan las respuestas asociadas a esos gates.

- **Casos de ejemplo:**
  - En casos como `startup_50p`, `scaleup_200p` y `gore_nuble`, Operation se refleja en los dashboards y decisiones descritas en `artefactos.md`, donde H_org y otros indicadores condicionan la activación de playbooks y ajustes de trayectoria.

---

### §3 Estado en ORKO v1.0.0

- Según `validation_final_report.md` (§2.3), el bloque Operation está **definido como contrato de diseño/operación** a nivel de fases WSLC y alineado con VOCAB/DEP_GRAPH y health gates.
- Algunas piezas (por ejemplo, contenido detallado de dashboards o runbooks de incidentes) se consideran aún en estado **MVO** y se tratan como backlog post‑1.0.0.
- Este README solo describe el rol del bloque y sus relaciones; cualquier cambio en métricas canónicas o contratos deberá entrar por nuevos CAP posteriores a la RELEASE.
