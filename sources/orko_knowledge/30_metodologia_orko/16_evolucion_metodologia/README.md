# 16_evolucion_metodologia – Evolución post‑1.0.0

## Propósito del bloque

- Explicar **cómo se espera que la metodología ORKO evolucione después de la RELEASE 1.0.0**, sin romper el kernel ni los contratos congelados.  
- Conectar el estado actual documentado en `17_validacion_final/validation_final_report.md` (§3–§5) con un backlog estructurado de mejoras futuras.

 Este bloque **no introduce cambios efectivos** en el kernel ni en VG3/VG4; sirve como guía para futuros CAP y versiones (por ejemplo, `VOCAB v1.1.x`).

## Fuentes principales para la evolución

- `40_implementacion_metodologia/dev_specs/KERNEL_READINESS.md`  
  - Define qué está congelado en `v1.0.0-kernel` (IDs A*/P*/I*/D*/F*, P01–P15, trayectorias, métricas canónicas `H_org`, `eta_org`, `ROI_Habilitacion`).  
  - Cualquier cambio futuro que toque estos elementos debe respetar la política de cambio controlado descrita ahí.

- `40_implementacion_metodologia/dev_specs/VOCAB_v1.1.x_NOTAS.md`  
  - Backlog de métricas y entidades candidatas (por ejemplo `handoff_ratio`, `capacity_gap_index`, `context_pattern`, `compliance_framework`).  
  - Ninguna de estas candidatas es canónica en 1.0.0; este archivo guía futuras extensiones de VOCAB y DEP_GRAPH.

- `30_metodologia_orko/17_validacion_final/validation_final_report.md`  
  - §3 sintetiza el estado de las invariantes I1–I8 (`PASSED`/`CONDITIONAL`) para ORKO v1.0.0.  
  - §5 lista gaps aceptados como backlog post‑1.0.0 (por ejemplo, enriquecimiento de §0 FUNDAMENTO en fases `CONDITIONAL`, profundización de templates/calculadoras, auditorías adicionales por caso).

## Ejes de evolución esperada

- **Eje 1 – VOCAB y métricas**  
  - Consolidar métricas candidatas de `VOCAB_v1.1.x_NOTAS.md` que demuestren uso consistente en casos, playbooks y health gates.  
  - Cuando una métrica/entidad se promueva a canónica, actualizar `VOCABULARIO_CONTROLADO.yaml`, `DEPENDENCY_GRAPH.yaml` y ejecutar `dependency_closure_script.py`, siguiendo el proceso de cambio controlado.

- **Eje 2 – Cobertura de §0 FUNDAMENTO e invariantes**  
  - Completar y profundizar `§0 FUNDAMENTO` en fases WSLC hoy marcadas como `CONDITIONAL` en `validation_final_report.md` §2.3.  
  - Fortalecer evidencias para invariantes I1–I8 donde el estado actual es `CONDITIONAL`, usando nuevos casos, datos operativos y mejoras en documentación.

- **Eje 3 – Templates, calculadoras y casos**  
  - Extender la profundidad de contenido en `40_implementacion_metodologia/templates/` y `40_implementacion_metodologia/calculadoras/` (sin romper contratos existentes).  
  - Aumentar la cobertura y detalle narrativo de los casos en `40_implementacion_metodologia/ejemplos/*_completo/`, manteniendo la coherencia con el kernel, los playbooks y los health gates.

- **Eje 4 – Playbooks, trayectorias y governance**  
  - Después de la RELEASE 1.0.0, abrir nuevos CAP específicos (por ejemplo, para profundizar secciones avanzadas de P01–P15, o para iterar sobre triggers y umbrales usando datos empíricos), siempre partiendo del estado congelado descrito en CAP‑16/CAP‑18.  
  - Ajustar trayectorias y decision_matrix solo mediante nuevos CAP y versiones de VOCAB/DEP_GRAPH, manteniendo trazabilidad en el `board_coordinación.md`.

## Uso de este bloque en futuros CAP

- Este directorio funciona como **punto de partida** para futuros CAP orientados a evolución metodológica (post‑1.0.0).  
- Cada nuevo CAP debería:
  - referenciar explícitamente qué parte del backlog de `validation_final_report.md` §5 aborda,  
  - declarar el impacto esperado sobre VOCAB/DEP_GRAPH, fases, playbooks o tejidos, y  
  - documentar sus resultados aquí, manteniendo alineación con `KERNEL_READINESS.md` y las reglas de cambio controlado.
