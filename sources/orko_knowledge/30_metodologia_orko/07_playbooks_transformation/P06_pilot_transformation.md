
# P06_pilot_transformation

**Tipo:** Playbook Transformation  
**ID:** P06  
**Trigger:** Decisión de ejecutar piloto de transformación para mejorar `H_org`/`eta_org` en dominio acotado  
**Estimación Ejecución:** `P4W`

---

## §0. FUNDAMENTO

**Layer 0:** `A1`, `A3`, `A5`, `P1`, `P2`, `P5`, `I3`, `I6`  
**Layer 1:** `D1`, `D2`, `D4`, `E6`, `E7`  
**Layer 2:** `TF1`, `TF2`

**Justificación:** Cuando la organización necesita mejorar `H_org` y `eta_org` pero aún no es seguro escalar cambios a todo el sistema, P06 define cómo ejecutar un piloto controlado en dominios acotados, orquestando capacidades (`P1`) y flujos (`P2`) alineados al propósito (`P5`) y preservando trazabilidad (`I3`) y aprendizaje adaptativo (`I6`).

---

## §1. INTERFAZ

### Trigger Conditions

```yaml
triggers:
  - condition: "Trayectoria Minimal/Avanzada decide ejecutar piloto en dominio específico"
    metric: "H_org"
    threshold: "mejora_objetivo"
    source: "F3.trayectoria_decision"
  - condition: "Gap de eficiencia identificado en F9/F11 con H_org aceptable"
    metric: "eta_org"
    threshold: "por_debajo_target"
    source: "F13.eta_org_dashboard"
```

### Outputs

```yaml
outputs:
  - report: "P06_pilot_transformation_report.md"
    consumers: ["F9", "F11", "F15", "F16", "F17", "E4_governance"]
  - artifact: "pilot_transformation_plan.yaml"
    consumers: ["F11", "F15", "P07", "trayectorias.Minimal", "trayectorias.Avanzada"]
```

### Casos típicos

- **CT1 – Piloto Avanzada (G4 activo):** G4 (`Ready_For_Avanzada`) se cumple y se decide un piloto limitado en uno o dos dominios críticos antes de escalar (P07).  
- **CT2 – Piloto de recuperación de eficiencia:** tras P10/P11, se usa P06 para probar combinaciones de cambios de capacidad/flujo en un dominio antes de extenderlas.  
- **CT3 – Piloto de contexto nuevo:** entrada a un nuevo mercado/unidad donde se requiere validar impacto en `H_org`/`eta_org` con bajo riesgo.

### Inputs adicionales

- `F4/F5` – mapas de capacidades y flujos objetivo.  
- `F9` – arquitectura objetivo del dominio piloto.  
- `F13` – series históricas de `H_org`, `eta_org`, `ROI_Habilitacion` del dominio.  
- `F16` – hipótesis y aprendizajes previos relevantes (learning_loops_log).

### Riesgos y mitigación

- **R1 – Piloto mal acotado:** el dominio piloto es demasiado amplio y el impacto negativo en `H_org` sería alto si falla.  
  - Mitigación: usar `03_decision_matrix.md` y G4 para acotar alcance y revisar runway/budget.  
- **R2 – Falta de trazabilidad:** cambios del piloto no quedan reflejados en F16/F17, dificultando evaluar `eta_org`/`ROI_Habilitacion`.  
  - Mitigación: exigir registro en `learning_loops_log` y vincular outputs de P06 a recomendaciones de trayectoria.


---

## §2. EJECUCIÓN
**Pasos**: 1) Seleccionar dominio piloto acotado, 2) Diseñar intervención, 3) Ejecutar piloto (2-4 semanas), 4) Evaluar resultados, 5) Decidir escala

---

## §3. RACI
```yaml
raci:
  responsible: ["Transformation_Lead", "Pilot_Team_Lead"]
  accountable: "Role_Captain"
  consulted: ["Role_Architect", "Role_HealthOwner"]
  informed: ["Sponsor_L1_Human", "Steering_Committee"]
```
