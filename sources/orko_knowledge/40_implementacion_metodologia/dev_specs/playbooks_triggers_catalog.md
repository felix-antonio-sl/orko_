# Catálogo de Triggers e Incidentes – Playbooks ORKO (v0.1)

> Fuente de verdad semántica: `VOCABULARIO_CONTROLADO.yaml` (ver HOWTO_VOCABULARIO_OROKO).
>
> Alcance v0.1: catalogar **triggers** y **tipos de incidente/gap** para playbooks `P01`–`P15`,
> usando **solo métricas canónicas** de `layer_1.metricas` y referenciando fases WSLC `F14`–`F18`
> y entidades `E6`/`E7` cuando corresponda.

---

## 1. Métricas canónicas disponibles para triggers

Según `VOCABULARIO_CONTROLADO.layer_1.metricas`:

- `H_org`  
  - Health organizacional integrada sobre dominios `D1`–`D4`.  
  - Fuente oficial: `00_fundamentos_teoricos/05_dominios.md`.
- `eta_org`  
  - Eficiencia global derivada de la ecuación maestra de valor organizacional `V_org`.  
  - Fuente oficial: `00_fundamentos_teoricos/07_ecuacion_maestra.md`.
- `ROI_Habilitacion`  
  - Retorno de inversión de flujos/capacidades de habilitación.  
  - Fuente oficial: `00_fundamentos_teoricos/07_ecuacion_maestra.md`.

**Regla v0.1:**

- Cada trigger de este catálogo referencia **al menos una** de estas métricas (campo `metricas_canonicas`).  
- Otras señales (drift, handoffs, conflictos, etc.) se describen como **incidentes** apoyados en fases/entidades canónicas (`F*`, `P*`, `E6`, `E7`),
  no como métricas nuevas.

---

## 2. Triggers por playbook (P01–P15)

Vista resumen de cómo cada playbook se engancha a métricas canónicas y artefactos WSLC.

| Playbook | metricas_canonicas | Condición/trigger canónico (resumen) | Fases WSLC relacionadas | Entidades relacionadas |
|---------|---------------------|--------------------------------------|-------------------------|------------------------|
| `P01` Low H_org Recovery | `H_org` | Activar cuando `H_org` cae por debajo de un **umbral de recuperación** acordado (ej. 70) y el descenso está confirmado por `F13` (Health Monitoring). | `F13` (sensing), `F14` (ejecución incidente), `F16` (post‑mortem), `F17` (ajuste trayectoria) | Impacto sobre `E6` (estado arquitectónico actual) |
| `P02` Handoff Reduction | `H_org`, `ROI_Habilitacion` | Activar cuando hay deterioro de `H_org` o `ROI_Habilitacion` atribuible a ineficiencias de flujo identificadas en `F5`/`F11` (exceso de handoffs en `E7_FlowExecution`). | `F5`, `F11`, `F13`, `F14`, `F16` | `E7` (instancias de flujo con altos handoffs) |
| `P03` OKR Alignment | `H_org`, `eta_org` | Activar cuando `H_org` y/o `eta_org` se encuentran por debajo de objetivos a pesar de tener propósito definido (`F7`) y arquitectura objetivo (`F9`), indicando desalineamiento entre OKR y ejecución. | `F7`, `F9`, `F13`, `F16`, `F17` | `E6` (target vs current), outputs de trayectorias |
| `P04` Security Remediation | `H_org`, `ROI_Habilitacion` | Activar ante incidentes de seguridad o gaps de cumplimiento detectados en `F8`/tejidos TF1–TF3, cuando estos impactan o amenazan `H_org` o `ROI_Habilitacion`. | `F8`, `F11`, `F13`, `F14`, `F16` | `E6` (estado con riesgo), activos de información TF3 |
| `P05` Bounded Autonomy M6 | `eta_org`, `ROI_Habilitacion` | Activar cuando `H_org` es suficiente para soportar mayor autonomía, y se busca incrementar `eta_org`/`ROI_Habilitacion` mediante modos de delegación `M1`–`M6` (en especial `M6`). | `F3` (trayectoria), `F7`, `F11`, `F15`, `F17` | Capacidades `P1_Capacidad` orquestadas en `E7` |
| `P06` Pilot Transformation | `H_org`, `eta_org`, `ROI_Habilitacion` | Activar cuando se decide ejecutar un **piloto** controlado de transformación para mejorar `H_org`/`eta_org` en un dominio acotado, previo a escala total. | `F3`, `F9`, `F11`, `F15`, `F16` | `E6` (estado intermedio de dominio piloto), `E7` |
| `P07` Scale Transformation | `H_org`, `eta_org`, `ROI_Habilitacion` | Activar cuando un piloto (P06) demuestra mejoras sostenidas en `H_org`/`eta_org` y se decide escalar a más unidades o dominios. | `F9`, `F11`, `F12`, `F15`, `F17` | `E6` (target ampliado), `E7` |
| `P08` Optimization Sustain | `H_org`, `eta_org`, `ROI_Habilitacion` | Activar cuando la transformación ya fue escalada y se requiere sostener/optimizar `H_org`/`eta_org` evitando regresión o drift operativo. | `F13`, `F15`, `F16`, `F18` | `E6` (current vs target), `E7` (métricas de ejecución) |
| `P09` Drift Detection Response | `H_org`, `eta_org` | Activar ante drifts detectados por `F13` (por ejemplo, degradación de `H_org`/`eta_org` respecto a valores esperados por trayectoria) que requieren análisis y contención específica. | `F13`, `F14`, `F16`, `F17` | `E6` (desalineamiento target), `E7` (historial de ejecución) |
| `P10` Capacity Gap Resolution | `H_org`, `eta_org`, `ROI_Habilitacion` | Activar cuando análisis de capacidades (`F4`) muestra gaps críticos que explican baja `H_org`/`eta_org` o bajo `ROI_Habilitacion` en dominios clave. | `F4`, `F10`, `F13`, `F17` | Inventario de capacidades (`P1_Capacidad`), `E6` |
| `P11` Flow Optimization | `eta_org`, `ROI_Habilitacion` | Activar cuando la eficiencia de flujos (`eta_org`, `ROI_Habilitacion`) se degrada y los cuellos de botella pueden localizarse en flujos específicos (`E7_FlowExecution`). | `F5`, `F11`, `F13`, `F16` | `E7` (flujos con tiempos/carga anómalos) |
| `P12` Data Quality Recovery | `H_org`, `eta_org`, `ROI_Habilitacion` | Activar cuando problemas de calidad de datos (en TF3/F6) afectan métricas de resultado reflejadas en `H_org`, `eta_org` o `ROI_Habilitacion`. | `F6`, `F11`, `F13`, `F16` | Activos `C3_Informacion` en TF3, `E6` |
| `P13` Political Alignment | `H_org` | Activar cuando conflictos entre stakeholders o decisiones políticas degradan `H_org` sin causas técnicas evidentes, requiriendo alineamiento político/organizacional. | `F1`, `F3`, `F7`, `F13`, `F17` | Trayectorias (`Minimal`, `Avanzada`, `Survival`), `E6` |
| `P14` Client Expectation Management | `H_org`, `eta_org`, `ROI_Habilitacion` | Activar cuando hay brecha entre expectativas de clientes y resultados percibidos, reflejada en `H_org`/`eta_org`/`ROI_Habilitacion` asociados a dominios cliente. | `F1`, `F3`, `F13`, `F16` | Casos en `case_instances.yaml`, `E6` |
| `P15` Adaptive Cadence | `H_org` | Activar cuando cambios de contexto (crisis/hypergrowth, ver trayectorias y contexto) ponen en riesgo `H_org` y obligan a ajustar cadencias de trabajo (`F15`). | `F3`, `F13`, `F15`, `F17` | Trayectorias (`Survival`, `Minimal`, `Avanzada`), `E6` |

**Nota:** Los umbrales concretos (ej. `H_org < 70`) y fórmulas operacionales derivadas se definen en artefactos de implementación (`40_implementacion_metodologia/`),
pero este catálogo fija qué **métricas canónicas** participan en cada trigger y qué fases/entidades las consumen.

---

## 3. Tipos de incidente/gap y su anclaje WSLC/E6/E7

Esta sección clasifica incidentes/gaps que aparecen recurrentemente en la Etapa 3, enlazándolos con fases WSLC, entidades arquitectónicas
y playbooks relevantes.

| Tipo de incidente/gap (descripción) | Fases WSLC relevantes | Entidades/primitivos clave | Playbooks asociados |
|-------------------------------------|------------------------|----------------------------|---------------------|
| **Caída crítica de health organizacional** (descenso brusco/sostenido de `H_org` respecto a baseline y objetivos) | `F13`, `F14`, `F16`, `F17` | `H_org`, `E6_ArchitecturalState` | `P01`, `P09`, `P08` |
| **Ineficiencias de flujo y handoffs excesivos** (flujos con muchos traspasos y fricción) | `F5`, `F11`, `F13`, `F14` | `P2_Flujo`, `E7_FlowExecution` | `P02`, `P11` |
| **Desalineamiento de propósito/OKR entre niveles** (propósito bien definido pero ejecución no convergente) | `F2`, `F3`, `F7`, `F9`, `F13`, `F17` | `P5_Proposito`, `E6_ArchitecturalState` | `P03`, `P05`, `P06`, `P07` |
| **Incidente de seguridad o gap de cumplimiento** (riesgos regulatorios/técnicos relevantes) | `F8`, `F11`, `F13`, `F14` | `P4_Limite`, activos `C3_Informacion` (TF3) | `P04`, `P12` |
| **Drift arquitectónico/operativo** (estado actual se aleja de `E6` target) | `F9`, `F12`, `F13`, `F16`, `F18` | `E6_ArchitecturalState`, `E7_FlowExecution` | `P09`, `P08` |
| **Gaps críticos de capacidad** (skills/FTE/plataforma insuficientes para objetivos) | `F4`, `F10`, `F13`, `F17` | `P1_Capacidad`, `C1_Capacidad` | `P10`, `P05` |
| **Problemas de calidad de datos** (datos incompletos, inconsistentes o obsoletos que afectan decisiones) | `F6`, `F11`, `F13` | `P3_Informacion`, `C3_Informacion`, TF3 | `P12`, `P09` |
| **Conflictos políticos y de stakeholders** (bloqueos no técnicos) | `F1`, `F3`, `F7`, `F13`, `F17` | Trayectorias (`Minimal`, `Avanzada`, `Survival`), roles en `12_roles_governance` | `P13` |
| **Desajuste de expectativas de clientes** (gap entre promesa y entrega) | `F1`, `F3`, `F13`, `F16` | Casos en `14_casos_uso`, trayectorias | `P14` |
| **Cambio abrupto de contexto (crisis/hypergrowth)** | `F1`, `F3`, `F13`, `F15`, `F17` | Contexto en `context_pattern_schema`/`case_instances`, trayectorias | `P15`, `P01`, `P02` |

En todos los casos, las **métricas numéricas** usadas para monitorear y tomar decisión (
`H_org`, `eta_org`, `ROI_Habilitacion`) son las definidas en el VOCAB.
Otros términos de dominio (drift, handoff, conflicto político, etc.) se apoyan en fases, contratos y entidades ya definidos (`F*`, `P*`, `E6`, `E7`, `C1`–`C5`).

---

## 4. DoD – Catálogo de triggers normalizado (v0.1)

Este archivo cumple los siguientes criterios para SPRINT 1:

- [x] Cada trigger de playbook hace referencia explícita a **métricas canónicas** de `VOCABULARIO_CONTROLADO.layer_1.metricas`.
- [x] No se introducen **nuevas métricas** fuera del VOCAB (solo se usan `H_org`, `eta_org`, `ROI_Habilitacion`).
- [x] Cada tipo de incidente/gap referencia al menos una fase WSLC (`F14`–`F18` cuando aplica) y, si corresponde, `E6` y/o `E7`.
- [x] Fases y playbooks se refieren únicamente por sus IDs canónicos (`F1`–`F18`, `P01`–`P15`).
- [x] El documento sigue los patrones de referencia definidos en `HOWTO_VOCABULARIO_OROKO`.
