# HOWTO_VOCABULARIO_OROKO

## 1. Propósito de este documento

Este HOWTO define **cómo usar el `VOCABULARIO_CONTROLADO.yaml`** desde los equipos 2–3–4 para evitar ambigüedades.

- **Fuente de verdad semántica:** `40_implementacion_metodologia/dev_specs/VOCABULARIO_CONTROLADO.yaml`.
- **Regla de oro:** *ningún término nuevo se usa en docs sin pasar por VOCAB*.
- **Tiempo de lectura objetivo:** 5–10 minutos.

---

## 2. Cómo referenciar términos (contrato obligatorio)

### 2.1. Siempre usar el **id canónico**, no el alias

En cualquier artefacto (fase, esquema, playbook, métrica, README):

- **Obligatorio:** usar el `id` definido en VOCAB (`A1`, `P1_Capacidad`, `F3`, `P01`, `H_org`, etc.).
- **Opcional:** puedes añadir el nombre descriptivo entre paréntesis la primera vez.

Ejemplos:

- `F3 (Trajectory Selection)` en vez de “fase de selección de ruta”.
- `P01 (playbook de recuperación de contexto)` en vez de “playbook para reactivar contexto”.
- `H_org (health organizacional)` en vez de “salud de la organización”.

### 2.2. Patrones recomendados en texto

- Primera aparición:
  - `F3 (Trajectory Selection, ver VOCABULARIO_CONTROLADO.layer_3.wslc_phases.F3)`
- Siguientes menciones:
  - Solo `F3`.

- Primera aparición de playbook:
  - `P01 (ver VOCABULARIO_CONTROLADO.layer_3.playbooks.P01)`
- Siguientes menciones:
  - Solo `P01`.

- Métricas:
  - `H_org` siempre con subíndice explícito (`_org`).

---

## 3. Ejemplos por tipo de artefacto

### 3.1. Ejemplo para fase (F3_trajectory_selection)

En `F3_trajectory_selection.md` y artefactos relacionados:

- Cuando describas la fase:
  - "Esta fase corresponde a **F3** en el VOCAB (Trajectory Selection)."
- Cuando referencies otras fases:
  - "F3 depende de **F1** (Context Assessment) y alimenta a **F7** (Purpose Cascade) y **F9** (Target State Design)."
- En esquemas o YAML asociados:
  - `phase_id: F3`

### 3.2. Ejemplo para playbook (P01_reactivar_contexto)

En el playbook de reactivación de contexto (P01):

- Encabezado del doc:
  - `id: P01`
  - `nombre_canonico: "Playbook reactivación de contexto"` (o el nombre que defina el VOCAB).
- Cuando lo llame otra fase/playbook:
  - "Si `H_org` cae bajo el umbral X, ejecutar **P01** según el `VOCABULARIO_CONTROLADO.layer_3.playbooks.P01`."
- En esquemas (Equipo 2):
  - `playbook_id: P01`

### 3.3. Ejemplo para métrica (H_org)

En cualquier doc de métricas, governance o dashboards:

- Definir siempre:
  - `metric_id: H_org`
  - `nombre: "Health organizacional"`
  - Referencia: `VOCABULARIO_CONTROLADO.layer_1.metricas.H_org`.
- En texto:
  - "El objetivo de F13 es elevar **H_org** desde 45→70 en 12 meses."

---

## 4. Qué puedes (y no puedes) inventar

### 4.1. Permitido sin cambios en VOCAB

Puedes **crear libremente** dentro de los contornos ya definidos en el VOCAB, por ejemplo:

- Nuevos ejemplos, casos de uso y escenarios dentro de fases o playbooks.
- Nuevos campos en plantillas **siempre que** usen ids canónicos para referencias (`phase_id`, `playbook_id`, `metric_id`).
- ASCII/diagramas, notas operativas, checklists que solo consuman términos existentes.

### 4.2. No permitido sin pasar por VOCAB (bloqueado)

No se puede:

- Inventar nuevos **ids** (`F19`, `P16`, `NuevaMetricX`, `NuevoDominioY`).
- Usar términos ambiguos/prohibidos definidos en `terminos_prohibidos` (por ejemplo, “recurso”, “gente”, “proyecto transformación”) en lugar de los términos canónicos.
- Crear métricas ad‑hoc sin registrarlas como métricas formales en `layer_1.metricas`.

Si necesitas algo nuevo, sigue el proceso del punto 5.

---

## 5. Proceso para proponer nuevos términos

Cuando un equipo detecte que **falta un término** (nueva métrica, nuevo playbook, nueva fase, nuevo tejido, etc.):

1. **No lo inventes en silencio.** Usa un nombre de trabajo claro pero márcalo como "propuesta" en el doc.
2. Anuncia en el canal acordado (ej. `#orko-core`) indicando al menos:
   - Tipo de término propuesto (p.ej. "nueva métrica", "nuevo playbook").
   - Propuesta de `id` (ej: `M_new`, `P16`) y nombre descriptivo.
   - Justificación (por qué no basta con los términos existentes).
   - Referencias a las fases/playbooks donde se usaría.
3. El Equipo 1 evalúa y, si se aprueba:
   - Se agrega el término al `VOCABULARIO_CONTROLADO.yaml`.
   - Se actualiza `metadata.statistics` y el `changelog`.
4. **Solo después de que aparezca en VOCAB** el término se considera canónico para todos los equipos.

---

## 6. Checklist rápido para equipos 2–3–4

Antes de dar por terminado un artefacto nuevo (fase, schema, playbook, métrica, template):

- [ ] Cada referencia a fases usa `F1`–`F18` (no nombres libres).
- [ ] Cada referencia a playbooks usa `P01`–`P15`.
- [ ] Cada referencia a métricas usa su `id` canónico (`H_org`, `eta_org`, etc.).
- [ ] No se usan términos en la lista `terminos_prohibidos` sin reemplazo canónico.
- [ ] Si surgió un término nuevo, hay registro de propuesta a Equipo 1 y está documentado el estado (pendiente/aprobado).

Con esto, el contrato semántico queda **congelado y explícito** para uso por los equipos 2–3–4.
