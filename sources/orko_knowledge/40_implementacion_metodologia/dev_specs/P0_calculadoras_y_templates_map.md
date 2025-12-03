# P0-COMPLETE – Mapa calculadoras / templates → fases WSLC y playbooks

> Borrador P0 sobre ORKO v1.0.0. No cambia kernel, VOCAB, DEP_GRAPH, VG3, VG4 ni el contenido de las .xlsx.

## §0 Propósito

- **Qué busca:** Tener en un solo lugar una vista rápida de cómo se espera que se usen las calculadoras de
  `40_implementacion_metodologia/calculadoras/` (y algunos templates asociados) en decisiones WSLC y
  playbooks P01–P15 durante P0-COMPLETE.
- **Cómo se usa en P0:** Solo como mapa de trazabilidad e insumo para CAP-x futuros; no es contrato ni
  especificación canónica aún.

## §1 Calculadoras

- **health_score_calculator.xlsx**
  - Ruta: `40_implementacion_metodologia/calculadoras/health_score_calculator.xlsx`
  - Rol esperado: calcular `H_org` y componentes por dominio usando insumos de TF1/TF2/TF3 y métricas de
    sistema de trabajo.
  - Fases WSLC relacionadas: F1 (baseline de salud), F3 (insumo para decisión de trayectoria), F13
    (monitoring de salud en operación).
  - Playbooks relacionados (ejemplos): P01 (recuperación de baja salud), P02/P03 (alineamiento/foco),
    P15 (ajuste de cadencias según evolución de `H_org`).

- **context_decision_matrix.xlsx**
  - Ruta: `40_implementacion_metodologia/calculadoras/context_decision_matrix.xlsx`
  - Rol esperado: soportar `F3_trajectory_selection` recomendando `trajectory_selected`
    (`Survival`/`Minimal`/`Avanzada`) en función de `H_org`, tamaño, riesgo, presupuesto y horizonte.
  - Fases WSLC relacionadas: F1 (contexto e inputs), F3 (decisión de trayectoria).
  - Playbooks relacionados (ejemplos): P01 (selección de trayectoria en contexto crítico), P03
    (priorización de iniciativas según trayectoria), P15 (ajuste de cadencias según trayectoria).

- **convergence_tracker.xlsx**
  - Ruta: `40_implementacion_metodologia/calculadoras/convergence_tracker.xlsx`
  - Rol esperado: seguir convergencia entre `E6_current` y `E6_target` usando información de despliegue
    de capacidades/flows/info y evolución de `H_org`.
  - Fases WSLC relacionadas: F9/F18 (estado objetivo y convergencia), F13 (seguimiento de salud).
  - Playbooks relacionados (ejemplos): P07 (gestión de deuda de convergencia), P15 (cadencias adaptativas
    según grado de convergencia).

## §2 Templates (primer punteo)

- **Contexto / F1**
  - Artefactos típicos: `context.yaml`, plantillas de T01_context_assessment.
  - Relación con calculadoras: proveen los campos que luego alimentan `health_score_calculator` y
    `context_decision_matrix` (explícito en F1/F3).

- **Trayectoria / F3**
  - Artefactos típicos: `trajectory.md`, notas de decisión DMx.
  - Relación con calculadoras: consumen `H_org` y la recomendación de `context_decision_matrix` para
    fijar `trajectory_selected` y su justificación.

- **Operación / F13**
  - Artefactos típicos: registros de monitoreo de salud, tableros de operación.
  - Relación con calculadoras: consumen `health_score_calculator` y `convergence_tracker` para observar
    evolución de `H_org` y convergencia.
