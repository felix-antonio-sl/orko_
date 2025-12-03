# 02_health_gates (draft)

## §0. Fundamento

- Layer_0: Axiomas `A1`, `A4`, primitivos `P4`, invariantes `I3`, `I6`, `I8`.
- Layer_1: Métricas canónicas `H_org`, `eta_org`, `ROI_Habilitacion` (ver `VOCABULARIO_CONTROLADO.layer_1.metricas`).
- Layer_3: Fases `F1`, `F3`, `F13`, `F17` y playbooks `P01`–`P04`, `P09`, `P10`, `P11`, `P15` (ver `VOCABULARIO_CONTROLADO.layer_3`).
- Trayectorias: `Survival`, `Minimal`, `Avanzada` (ver `VOCABULARIO_CONTROLADO.layer_3.trayectorias`).

Propósito de este archivo:

- Definir health gates mínimos para guiar decisiones sobre activación de playbooks y ajustes de trayectoria.
- Asegurar que todas las referencias usen IDs canónicos desde `VOCABULARIO_CONTROLADO.yaml`.
- Alinear los gates con los triggers canónicos documentados en `40_implementacion_metodologia/dev_specs/playbooks_triggers_catalog.md` (v0.1).

---

## §1. Health gates (bosquejo SPRINT 1)

> Nota: Los valores numéricos de umbrales son propuestas iniciales **v0.1** para SPRINT 1 y pueden ajustarse en VG2–VG4.

```yaml
health_gates:

  - gate_id: "G1_H_org_Critico"
    descripcion: "H_org bajo umbral crítico: activar respuesta de recuperación inmediata."
    metric_ids:
      - "H_org"
    condicion:
      nivel: "RED"
      regla: "H_org < 60"  # umbral_critico_v0_1 (por debajo del umbral de recuperación de P01 ~70)
    fases_relacionadas:
      - "F13"   # Health Monitoring
      - "F14"   # Incident Response
    playbooks_triggered:
      - "P01"   # Low H_org Recovery
      - "P02"   # Handoff Reduction (si handoff_ratio contribuye a baja H_org)
      - "P15"   # Adaptive Cadence (ajuste de cadencias en crisis)
    trayectoria_recomendada:
      id: "Survival"
    notas:
      - "Cuando F13 detecta H_org < 60 en dos cortes consecutivos, escalar a F14 y ejecutar P01."
      - "Si el análisis de F5/F11 muestra handoff_ratio alto, incluir P02 en el plan de recuperación."

  - gate_id: "G2_H_org_Bajo_Riesgo"
    descripcion: "H_org en zona de riesgo pero no crítica; requiere recuperación estructurada."
    metric_ids:
      - "H_org"
    condicion:
      nivel: "YELLOW"
      regla: "60 <= H_org < 70"  # banda_riesgo_v0_1 asociada a activación estándar de P01/P09
    fases_relacionadas:
      - "F13"   # Health Monitoring
      - "F16"   # Learning Loops
      - "F17"   # Adaptation
    playbooks_triggered:
      - "P01"   # Low H_org Recovery (en modalidad parcial / focalizada)
      - "P09"   # Drift Detection Response
    trayectoria_recomendada:
      id: "Minimal"
    notas:
      - "F13 detecta tendencia descendente de H_org hacia < 70; activar P09 para analizar drift."
      - "Si el drift se confirma, ejecutar P01 focalizado en dominios con mayor contribución a la caída."

  - gate_id: "G3_H_org_Bueno_Eficiencia_Baja"
    descripcion: "H_org aceptable, pero eficiencia global y retorno de habilitación insuficientes."
    metric_ids:
      - "H_org"
      - "eta_org"
      - "ROI_Habilitacion"
    condicion:
      nivel: "YELLOW"
      regla: "H_org >= 70 AND (eta_org < 0.60 OR ROI_Habilitacion < 1.0)"  # umbral_madurez_minima_v0_1
    fases_relacionadas:
      - "F13"   # Health Monitoring
      - "F4"    # Capability Mapping
      - "F5"    # Flow Design
    playbooks_triggered:
      - "P10"   # Capacity Gap Resolution
      - "P11"   # Flow Optimization
      - "P03"   # OKR Alignment (si desalineación contribuye a bajo ROI_Habilitacion)
    trayectoria_recomendada:
      id: "Minimal"
    notas:
      - "Cuando H_org >= 70 pero eta_org y/o ROI_Habilitacion son bajos, la prioridad es optimizar capacidades (P10) y flujos (P11)."
      - "Si se detecta desalineamiento entre outcomes y esfuerzo (por ejemplo, eta_org por debajo de objetivos de trayectoria según F7/F9), considerar P03 para ajustar OKR."

  - gate_id: "G4_Ready_For_Avanzada"
    descripcion: "Organización con health y eficiencia suficientes para escalar hacia trayectoria Avanzada."
    metric_ids:
      - "H_org"
      - "eta_org"
      - "ROI_Habilitacion"
    condicion:
      nivel: "GREEN"
      regla: "H_org >= 70 AND eta_org >= 0.70 AND ROI_Habilitacion >= 1.2"  # umbral_listo_para_Avanzada_v0_1
    fases_relacionadas:
      - "F13"   # Health Monitoring
      - "F17"   # Adaptation
      - "F3"    # Trajectory Selection (re-evaluación)
    playbooks_triggered:
      - "P05"   # Bounded Autonomy M6
      - "P06"   # Pilot Transformation
      - "P07"   # Scale Transformation (según resultados de P06)
    trayectoria_recomendada:
      id: "Avanzada"
    notas:
      - "Cuando se cumplen simultáneamente los umbrales de H_org, eta_org y ROI_Habilitacion, F17 debe evaluar transición desde Minimal hacia Avanzada."
      - "P05 prepara HAIC (M1–M6); P06 y P07 ejecutan pilotos y escalamiento controlado."
```

---

## §2. Checklist de conformidad con VOCAB

- Todas las métricas usadas (`H_org`, `eta_org`, `ROI_Habilitacion`) provienen de `layer_1.metricas`.
- Todas las fases referenciadas (`F1`, `F3`, `F4`, `F5`, `F13`, `F16`, `F17`) corresponden a `layer_3.wslc_phases`.
- Todos los playbooks (`P01`–`P04`, `P09`, `P10`, `P11`, `P15`, `P03`, `P05`, `P06`, `P07`) corresponden a `layer_3.playbooks`.
- Las trayectorias (`Survival`, `Minimal`, `Avanzada`) corresponden a `layer_3.trayectorias`.

## §3. Puntos abiertos v0.1

- Los umbrales marcados con comentarios `*_v0_1` son propuestas iniciales para SPRINT 1.
- La calibración fina de `H_org`, `eta_org` y `ROI_Habilitacion` por trayectoria (objetivos por `Minimal`/`Avanzada`) queda abierta para etapas posteriores (VG2–VG4) usando datos empíricos.
- Se asume que futuros refinamientos de `VOCABULARIO_CONTROLADO.layer_1.metricas` podrán introducir métricas adicionales de dominio; este archivo deberá actualizarse para referenciar esos nuevos `metric_id` en lugar de crear métricas ad‑hoc.

