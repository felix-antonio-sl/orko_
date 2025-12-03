# trajectory – 05_manufacturing_800p_completo

## §0 CONTEXTO

- Contexto desde `context.yaml` (`manufacturing_800p_minimal`): empresa de manufactura ~800 personas, `private_company`, jurisdicción principal `eu`, fuerte peso de operaciones y cadena de suministro.
- Riesgo operacional moderado‑alto por dependencias físicas y de proveedores; presión por estabilidad, eficiencia y cumplimiento.

## §1 TRAYECTORIA BASE (Minimal)

- **Trayectoria base:** `Minimal`.
- **Relación con `03_decision_matrix.md`:**
  - Escenario predominante previsto: `DM3_G3_Minimal_Optimización` (H_org en verde, eficiencia/ROI de habilitación por debajo del potencial) aplicado a plantas, logística y soporte.
  - `DM2_G2_Minimal_Defensiva` se usa cuando `H_org` cae a banda G2 por incidentes operacionales o problemas de seguridad.
- **Health gates relevantes:** G1–G4, con foco particular en G2/G3 para operaciones; G1 como señal de crisis severa y G4 como horizonte de posible transición a `Avanzada` en dominios específicos.

## §2 DECISIONES F3/F17 (v0.1)

- **Selección inicial (`F3` – Trajectory Selection):**
  - `F3` documenta la elección de `Minimal` como trayectoria base para consolidar prácticas, estabilizar `H_org` y mejorar eficiencia antes de desplegar programas de transformación más intensos.

- **Adaptación (`F17`) con decision_matrix + G1–G4:**
  - **Bajo `G3_H_org_Bueno_Eficiencia_Baja` (`DM3`):**
    - `F13` detecta que `H_org` es aceptable, pero `eta_org`/`ROI_Habilitacion` son bajos.
    - `F17` prioriza iteraciones sobre capacidades críticas (mantenimiento, logística, calidad) y flujos (cadena de suministro, planificación) usando P10/P11, y P03 cuando hay desalineamiento de objetivos.
  - **Bajo `G2_H_org_Bajo_Riesgo` (`DM2`):**
    - Caídas hacia banda G2 se abordan con P09 (análisis de drift) y P01 focalizado (recuperación de H_org), manteniendo `Minimal` mientras sea viable.
  - **Episodios `G1_H_org_Critico`:**
    - Crisis severas (paros de planta, incidentes repetidos graves) pueden requerir activar trayectoria `Survival` (`04_survival_0_10K.md`) a corto plazo según `DM1`.
    - `F17` gestiona luego la reentrada a `Minimal` siguiendo `DM5_Survival_Minimal_Fallback` cuando H_org se estabiliza en G2/G3.
  - **Evolución hacia `Avanzada`:**
    - Para dominios muy maduros y con inversión suficiente, si se cumple G4, `F17` puede proponer para esos dominios un paso a `Avanzada` (p.ej. despliegue intensivo de tejidos digitales) siguiendo la lógica de `DM4`, manteniendo al resto de la organización en `Minimal`.

