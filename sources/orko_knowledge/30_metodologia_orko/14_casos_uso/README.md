## 14_casos_uso – Casos y patrones de aplicación

Este directorio describe cómo se usan los **casos de ejemplo** y los **patrones de contexto** para aplicar la metodología ORKO en situaciones reales.

---

### §0 Relación con `40_implementacion_metodologia/ejemplos/`

- Los 6 casos `*_completo/` en `40_implementacion_metodologia/ejemplos/` (startup, scaleup, enterprise, fintech, manufacturing, sector público) son la **fuente principal de evidencia empírica** en ORKO v1.0.0.
- Cada caso incluye, al menos:
  - `context.yaml` – instancia del schema de contexto.
  - `trajectory.md` – trayectoria elegida (`Survival`/`Minimal`/`Avanzada`) y uso de `03_decision_matrix.md`.
  - `artefactos.md` – listado de fases, playbooks, templates y calculadoras utilizados.
- CAP-15 y CAP-17 usan estos casos para:
  - Verificar que la metodología es aplicable en contextos diversos.
  - Validar que no se introducen artefactos fuera de catálogo.
  - Evaluar invariantes I1–I8 en situaciones realistas.

---

### §1 Componentes de este directorio

- `context_pattern_schema.yaml`
  - Esquema (esqueleto en v1.0.0) para describir **patrones de contexto** reutilizables (por ejemplo, "startup tecnológica 50 personas", "gobierno regional").
  - No introduce nuevos contratos; se apoya en el schema de contexto ya utilizado en los casos de `40_implementacion_metodologia/ejemplos/`.

- `case_instances.yaml`
  - Archivo pensado para indexar instancias de casos contra patrones de contexto.
  - En v1.0.0 se considera un artefacto en estado MVO/esqueleto; la indexación efectiva se ilustra directamente en los casos `*_completo/`.

- `01_pattern_library.md`
- `02_lecciones_aprendidas.md`
  - Documentos destinados a recoger patrones y lecciones comunes extraídas de los casos.
  - En ORKO v1.0.0 funcionan principalmente como contenedores de notas y bocetos; la formalización de un catálogo completo de patrones queda en backlog post‑1.0.0.

---

### §2 Rol en VG4

- Este bloque ayuda a **cerrar la brecha** entre especificaciones teóricas y aplicación práctica:
  - Conecta `03_vg4_validation_map.md` y `01_validacion_trazabilidad_i1_i8.md` con ejemplos concretos.
  - Permite razonar sobre qué partes del diseño funcionan bien en distintos contextos y cuáles requieren ajustes.
- `validation_final_report.md` se apoya implícitamente en estos artefactos al sintetizar el estado de I1–I8; este README solo describe su rol y no introduce nuevos contratos.

