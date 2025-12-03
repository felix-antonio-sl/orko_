# 15_instrumentacion – Métricas, efectividad y auditorías

Este directorio describe la **instrumentación** necesaria para observar el comportamiento de la metodología ORKO en práctica: cómo se miden adopción, efectividad y coherencia, y cómo se conectan esas observaciones con health gates y decisiones de evolución.

## §0 Relación con métricas y health gates

- Las métricas canónicas (por ejemplo `H_org`, `eta_org`, `ROI_Habilitacion`) se definen en `VOCABULARIO_CONTROLADO.yaml` y se usan en los health gates G1–G4 (`13_metricas_validacion/02_health_gates.md`).
- Este bloque **no introduce métricas nuevas**: cualquier métrica adicional debe tratarse como candidata y documentarse en `VOCAB_v1.1.x_NOTAS.md` antes de convertirse en canónica en futuras versiones.
- La instrumentación se entiende como el conjunto de **métodos, pipelines y dashboards** que capturan y exponen estas métricas para soportar decisiones de playbooks, trayectorias y evolución (F13–F18).

## §1 Componentes de este directorio

- `01_metricas_adopcion_metodologia.md`
  - Espacio para describir cómo se mide la **adopción** de la metodología (por ejemplo, uso efectivo de fases, playbooks, templates) usando métricas existentes o derivadas.
  - En ORKO v1.0.0 se considera un esqueleto; las aproximaciones concretas se ilustran a través de los casos y de las calculadoras en `40_implementacion_metodologia/calculadoras/`.

- `02_efectividad_metodologia.md`
  - Documento pensado para capturar cómo se evalúa la **efectividad** de la metodología (mejoras en H_org, eficiencia, cumplimiento de objetivos).
  - Conecta con los resultados reportados en `validation_final_report.md` y con las métricas definidas en `13_metricas_validacion/`.

- `03_auditorias_coherencia.md`
  - Diseñado para describir auditorías de **coherencia** entre capas: si las decisiones de fases, playbooks, casos y artefactos respetan el kernel y los contratos.
  - Relacionado con las auditorías descritas en `validation_final_report.md` (§2.1–§2.5) y con herramientas como `dependency_closure_script.py`.

En v1.0.0, estos documentos funcionan principalmente como **marcos de referencia**: indican qué tipos de instrumentación son relevantes sin especificar aún todos los detalles de implementación técnica.

## §2 Conexión con calculadoras y dashboards

- Las calculadoras en `40_implementacion_metodologia/calculadoras/` (p.ej. `context_decision_matrix.xlsx`, `convergence_tracker.xlsx`, `health_score_calculator.xlsx`) aportan artefactos de análisis que pueden alimentar la instrumentación descrita aquí.
- Los futuros dashboards y reportes se documentan en `13_metricas_validacion/03_dashboards_reporting.md` (esqueleto), que debe mantenerse alineado con este bloque.
- Cualquier expansión significativa de instrumentación (nuevas métricas, pipelines o dashboards canónicos) deberá entrar como parte del backlog post‑1.0.0 y seguir el proceso señalado en `KERNEL_READINESS.md` y `VOCAB_v1.1.x_NOTAS.md`.

