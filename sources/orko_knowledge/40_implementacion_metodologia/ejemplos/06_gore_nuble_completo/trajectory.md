# trajectory – 06_gore_nuble_completo

## §0 CONTEXTO

- Contexto desde `context.yaml` (`gore_nuble_public_sector_minimal`): gobierno regional en sector público, tamaño ~300–600 personas, jurisdicción `cl`, financiado por `public_budget`.
- Alto componente de accountability pública, múltiples stakeholders y marcos formales de probidad/administración (sector público chileno).

## §1 TRAYECTORIA BASE (Minimal)

- **Trayectoria base:** `Minimal`.
- **Relación con `03_decision_matrix.md`:**
  - Se asume zona `DM2_G2_Minimal_Defensiva` y `DM3_G3_Minimal_Optimización` según variaciones de `H_org` y eficiencia en proyectos/programas.
  - `Survival` se reserva para casos de crisis política/operativa severa; `Avanzada` solo se consideraría en dominios muy maduros con alta capacidad de inversión y estabilidad.
- **Health gates relevantes:** G1–G4; con atención especial a G2/G3 como señales de riesgo reputacional u operativo.

## §2 DECISIONES F3/F17 (v0.1)

- **Selección inicial (`F3` – Trajectory Selection):**
  - `F3` documenta la elección de `Minimal` como trayectoria base, adecuada para consolidar prácticas de gestión, mejorar coordinación inter‑actor y elevar `H_org` en un horizonte 6–12 meses sin depender de grandes inversiones en TF.

- **Adaptación (`F17`) con decision_matrix + G1–G4:**
  - **Bajo `G2_H_org_Bajo_Riesgo` (`DM2`):**
    - Si `H_org` cae a banda G2 (por conflictos políticos, atrasos en ejecución presupuestaria, etc.), `F13` marca el gate.
    - `F17` ajusta el plan activando `P09` (Drift Detection) para entender fuentes de deterioro y `P01` focalizado en las unidades/ámbitos más afectados.
  - **Bajo `G3_H_org_Bueno_Eficiencia_Baja` (`DM3`):**
    - Cuando `H_org` es aceptable, pero la eficiencia en proyectos/programas o el `ROI_Habilitacion` en términos de impacto público es bajo, `F17` coordina ciclos de optimización usando P10/P11 y revisando alineamiento de objetivos mediante P03.
  - **Episodios `G1_H_org_Critico`:**
    - En casos de crisis severa (escándalos, fallas graves de ejecución, bloqueos políticos), `F13`/`F14` pueden recomendar trayectoria `Survival` (`04_survival_0_10K.md`) a corto plazo según `DM1`, con foco en estabilizar `H_org` y credibilidad.
    - `F17` documenta luego la transición de vuelta a `Minimal` según `DM5_Survival_Minimal_Fallback` cuando la situación se estabiliza.
  - **Uso eventual de `Avanzada`:**
    - Si en dominios específicos (p.ej. gestión de datos, planificación regional) se alcanza un estado cercano a G4 y existe capacidad de inversión y estabilidad política, `F17` puede proponer módulos de trabajo en modo `Avanzada` siguiendo la lógica de `DM4`, manteniendo el resto del contexto en `Minimal`.

