# VOCAB_v1.1.x_NOTAS (draft)

> Documento de notas internas para futuras extensiones del vocabulario.
> No modifica el contrato actual `v1.0.0-kernel`; sirve como backlog conceptual.

## §0. Propósito y alcance

- Registrar **métricas y entidades candidatas** que hoy se usan en:
  - Arquitectura (`10_arquitectura_orko/`)
  - Fases WSLC (`30_metodologia_orko/`)
  - Playbooks / health gates / casos (`playbooks_triggers_catalog`, `02_health_gates`, `ejemplos/*`)
- Ningún elemento aquí listado es **canónico** todavía.
- Cualquier promoción a canónico deberá pasar por:
  - Actualización de `VOCABULARIO_CONTROLADO.yaml`.
  - Ejecución de `dependency_closure_script.py`.
  - Notas de cambio en el changelog del VOCAB.

## §1. Métricas candidatas

### 1.1. `handoff_ratio`

- **Uso observado:**
  - Arquitectura de flujos (`10_arquitectura_orko/01_contratos.md`, `02_diseño.md`, `03_relaciones.md`, `04_vistas.md`, `05_patrones.md`).
  - Fase `F5_flow_design` (`30_metodologia_orko/02_fases_development/F5_flow_design.md`) como output.
  - Planes de expansión y quick wins (`PLAN_ETAPA_2_EXPANSION.md`, `PLAN_ETAPA_3_PLAYBOOKS.md`).
  - Health gates y playbooks de remediación (contexto de P02, G1/G2, etc.).

- **Intención semántica:**
  - Fracción de transiciones entre pasos de flujo que implican handoff relevante (cross-team, cambio de ownership).
  - Indicador de fricción estructural en flujos.

- **Notas para diseño formal (v1.1.x):**
  - Probable ubicación: `VOCAB.layer_1.metricas.handoff_ratio`.
  - Requiere definir:
    - Dominio de valores: `Float[0..1]`.
    - Esquema de cálculo estándar (ya bosquejado en `10_arquitectura_orko`).
    - Umbrales típicos (ej. `<0.20` como target, `>0.30` como alerta).

### 1.2. `cycle_time` / `cycle_time_baseline`

- **Uso observado:**
  - Diseño de flujos (F5) y quick wins (F10) en planes y docs de fase.
  - Métrica operativa en vistas de arquitectura y ejemplos.

- **Intención semántica:**
  - Tiempo total de ciclo de un flujo (desde start hasta done), por flujo crítico.

- **Notas:**
  - Candidata natural a métrica de soporte para `eta_org`.
  - Probable definición en términos de distribuciones/percentiles en lugar de valor único.

### 1.3. `flow_efficiency` / `efficiency`

- **Uso observado:**
  - Contratos de capacidad/flujo en `10_arquitectura_orko`.
  - Planes de expansión y quick wins.

- **Intención semántica:**
  - Relación entre tiempo de valor agregado y tiempo total de ciclo.

- **Relación con métricas canónicas:**
  - Podría actuar como métrica derivada de soporte para `eta_org`.

### 1.4. `okr_alignment_score` / `alignment_score`

- **Uso observado:**
  - Documentos de planificación (`PLAN_ETAPA_1_KERNEL.md`) y guías de playbooks (P03, P05–P07) como señal de desalineamiento.

- **Intención semántica:**
  - Medir cuán alineados están los OKR entre niveles (L1–L4) con el propósito y la trayectoria actual.

- **Notas:**
  - Requiere un modelo explícito de scoring (escala, inputs, método).
  - Probable anclaje en F2/F7.

### 1.5. `capacity_gap_index`

- **Uso observado:**
  - Referencias en board/checklists como métrica candidata asociada a P10 (Capacity Gap Resolution) y F4/F10.

- **Intención semántica:**
  - Índice agregado de severidad de gaps de capacidad (skills, FTE, plataforma) frente a objetivos.

- **Notas:**
  - Requiere definición formal de composición (ponderación por dominio/tipo de capacidad).

### 1.6. `tf3_data_quality_score`

- **Uso observado:**
  - Referencias como candidata en contexto de TF3 e incidentes de datos.

- **Intención semántica:**
  - Cuantificar la calidad de datos en el tejido de información (completitud, consistencia, frescura, etc.).

- **Notas:**
  - Anclaje natural en TF3 y fases `F6`, `F13`, P12.

## §2. Entidades/contratos candidatos

### 2.1. `context_pattern` / `context_instance`

- **Artefactos actuales:**
  - `context_pattern_schema.yaml`
  - `ejemplos/*/context.yaml`

- **Situación actual:**
  - Se usan como schemas/instancias en implementación, pero aún no aparecen como entidades formales en `VOCAB.layer_1`.

- **Propuesta v1.1.x (a discutir):**
  - Introducir una entidad canónica asociada a contexto (por ejemplo `E8_ContextProfile` o similar) o aclarar que `context_pattern` es solo un schema de implementación, no un nuevo primitivo/entidad.

### 2.2. `compliance_framework`

- **Artefactos actuales:**
  - `compliance_framework_schema.yaml`

- **Situación actual:**
  - Actúa como contrato auxiliar para F8/F11/F12, pero no está reflejado explícitamente en VOCAB.

- **Notas:**
  - Analizar si corresponde modelarlo como entidad derivada de `P4_Limite` (familia de constraints) en lugar de introducir un nuevo primitivo.

## §3. Reglas de juego para promover elementos a canónicos

1. **Evidencia de uso:**
   - La métrica/entidad debe aparecer en casos reales (`40_implementacion_metodologia/ejemplos`) y/o en playbooks/health gates como pieza central, no solo decorativa.

2. **Definición operativa clara:**
   - Dominio de valores, método de cálculo, fuentes de datos.
   - Relación explícita con métricas canónicas (`H_org`, `eta_org`, `ROI_Habilitacion`).

3. **Compatibilidad con el kernel:**
   - No violar invariantes ni duplicar conceptos ya cubiertos por A/P/I/D/F.

4. **Proceso de cambio controlado:**
   - Propuesta → revisión por E1 + Capitán → actualización de VOCAB + DEP_GRAPH → ejecución de `dependency_closure_script.py` → actualización de changelog.

## §4. Estado actual

- Para RELEASE `1.0.0`, **ningún** elemento de este archivo es canónico.
- Este documento sirve como backlog y registro de decisiones previas (por ejemplo, la evaluación de candidatas mencionada en eventos del `board_coordinación` bajo `CAP-02` y `CAP-14`).

