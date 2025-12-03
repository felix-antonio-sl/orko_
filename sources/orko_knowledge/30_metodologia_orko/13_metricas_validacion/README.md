# 13 – Métricas y validación (VG4)

## §0. Propósito del bloque

- Este bloque recoge los artefactos de **métricas, health gates y validación** usados para evaluar la metodología ORKO.
- Es la cara documental de VG4: conecta métricas canónicas, casos y auditorías con la decisión de RELEASE 1.0.0.

## §1. Componentes principales

- `02_health_gates.md`
  - Define los **health gates G1–G4** y cómo se usan `H_org`, `eta_org` y `ROI_Habilitacion` para disparar decisiones (playbooks, cambios de trayectoria, bloqueos).
  - Es el contrato principal de gating para ORKO v1.0.0.

- `03_vg4_validation_map.md`
  - Mapa de evidencias de VG4 por invariante I1–I8.
  - Explica cómo se combinan GENOME/VOCAB, DEP_GRAPH, fases, playbooks y casos para validar cada invariante.

- `01_kpis_por_trayectoria.md` (esqueleto)
  - Espacio para describir KPIs sugeridos por trayectoria (Survival/Minimal/Avanzada), sin introducir nuevas métricas canónicas.

- `03_dashboards_reporting.md` (esqueleto)
  - Espacio para describir dashboards y reportes que consumen las métricas definidas en health gates y casos.

- `30_metodologia_orko/17_validacion_final/validation_final_report.md`
  - Reporte de validación final que resume CAP-14–CAP-19 y sintetiza el estado de I1–I8 y la recomendación de RELEASE.

## §2. Relación con casos y playbooks

- Los 6 casos de `40_implementacion_metodologia/ejemplos/*_completo` sirven como **evidencia cualitativa** del comportamiento de métricas y gates.
- `02_health_gates.md` y `03_vg4_validation_map.md` documentan cómo estos casos ejercitan G1–G4 y playbooks P01–P15.
- `playbook_instances.yaml` usa únicamente métricas canónicas como entrada (`metricas_canonicas`), en coherencia con este bloque.

## §3. Lineamientos para ORKO v1.0.0

- Las únicas métricas canónicas en esta versión son las definidas en `VOCABULARIO_CONTROLADO.yaml` (incluyendo `H_org`, `eta_org`, `ROI_Habilitacion`).
- Cualquier métrica adicional debe tratarse como **candidata** (documentada en `VOCAB_v1.1.x_NOTAS.md`) y no puede usarse como `metric_id` en contratos hasta una futura versión.
- Este bloque describe cómo se usan las métricas actuales para validar la metodología; no introduce nuevas métricas canónicas.
