# VALIDACIÓN DE FUNDAMENTOS – CAP-22 CALCULADORAS

## §0 PROPÓSITO Y ALCANCE

**Objetivo:** Validar que las fórmulas y reglas de las tres calculadoras ORKO están correctamente derivadas del genoma (axiomas, primitivos, invariantes, tejidos, teoremas).

**Alcance CAP-22:**
- Validación teórica de `health_score_calculator`, `context_decision_matrix`, `convergence_tracker`
- Trazabilidad explícita: fórmula/regla → fuente genómica
- Clasificación de hallazgos por severidad

**Squad:** sq3 | **Mandato:** `20251118-1339-CAP22-MANDATO-sq3` | **Fecha:** 2025-11-18

---

## §1 METODOLOGÍA

### Criterios de validación

1. **Trazabilidad:** ¿Existe fuente explícita en genoma?
2. **Coherencia:** ¿Respeta significado ontológico de primitivos?
3. **Invariantes:** ¿No viola I1-I8?

### Clasificación
- ✅ VALIDADO
- ⚠️ ADVERTENCIA (supuestos fenotípicos)
- 🔴 BLOQUEANTE

### Fuentes consultadas
- `out/00_fundamentos_teoricos.md`, `out/20_tejidos.md`
- `30_metodologia_orko/09_trayectorias/03_decision_matrix.md`
- `VOCABULARIO_CONTROLADO.yaml`, `DEPENDENCY_GRAPH.yaml`

---

## §2 HEALTH_SCORE_CALCULATOR

### 2.1 Fórmula H_org

**Spec:** `H_org = w_A*A_Score + w_P*P_Score + w_D*D_Score`

| Elemento | Fuente | Estado |
|----------|--------|--------|
| H_org métrica canónica | Teorema T6 (`00_fundamentos` §4.3) | ✅ |
| Ecuación master V_org=f(H_org,η,ROI,t) | §7 Ecuación maestra | ✅ |
| Descomposición A/P/D | Derivación implícita P1-P5 | ⚠️¹ |
| TF1_Score en A_Score | TF1_Capacity (`20_tejidos`) | ✅ |
| TF2_Score en P_Score | TF2_Flow (`20_tejidos`) | ✅ |
| TF3_Score en D_Score | TF3_Information (`20_tejidos`) | ✅ |

**¹Nota:** A/P/D no explícita como teorema formal, pero coherente con A5→Alignment, P2+I4→Performance, P1+I3→Development.

**Conclusión M3.1:** ✅ **H_org VALIDADA** (advertencia documentada).

### 2.2 Bandas G1-G4

**Spec:** G1<0.35, G2[0.35-0.55), G3[0.55-0.75), G4≥0.75

| Elemento | Fuente | Estado |
|----------|--------|--------|
| Health gates existen | Invariante I6 | ✅ |
| 4 bandas diferenciadas | `02_health_gates.md` | ✅ |
| Umbrales numéricos | Parámetros fenotípicos | ⚠️ |

**Conclusión M3.1:** ✅ **Bandas VALIDADAS** como fenotipo de I6.

### 2.3 Invariantes

| Invariante | Cumple |
|------------|--------|
| I1 (Trazabilidad) | ✅ |
| I3 (No-regresión) | ✅ |
| I4 (Operabilidad) | ✅ |
| I6 (Health gates) | ✅ |
| I7 (Health monitoring) | ✅ |

---

## §3 CONTEXT_DECISION_MATRIX

### 3.1 Reglas DM1-DM5

| Regla | Lógica | Fuente | Estado |
|-------|--------|--------|--------|
| DM1 Crisis→Survival | H_org<floor OR risk=5 | I6, G1, T7 | ✅ |
| DM2 Budget→Survival | budget<threshold | A4, P4 (Límite) | ✅ |
| DM3 Madurez→Minimal | H_org<adv AND mat≤3 | P6 (WSLC), T7 | ✅ |
| DM4 Capacidad→Avanzada | H_org≥th AND budget OK | G4, I4 | ✅ |
| DM5 Default→Minimal | ELSE | T7, `03_decision_matrix` | ✅ |

**Coherencia G1-G4:**
- G1 → Survival (DM1) ✅
- G2 → Minimal defensiva (DM3) ✅
- G3 → Minimal optimización (DM3) ✅
- G4 → Avanzada (DM4) ✅

**Conclusión M3.2:** ✅ **DM1-DM5 VALIDADAS**.

### 3.2 Invariantes

| Invariante | Cumple |
|------------|--------|
| I1 (Trazabilidad) | ✅ |
| I6 (Health gates) | ✅ |
| I8 (Adaptabilidad) | ✅ |

---

## §4 CONVERGENCE_TRACKER

### 4.1 Métrica convergencia

**Spec:** 
```
Convergence_Score = Σ weight_i * (current_i/target_i)
Con: TF1, TF2, TF3, H_org (ratios cap en 1.0)
```

| Elemento | Fuente | Estado |
|----------|--------|--------|
| E6 (Architectural State) | Primitivo P5 (`20_tejidos` §7) | ✅ |
| Convergencia E6_cur→E6_tgt | Invariante I3 | ✅ |
| Descomp tejidos TF1/2/3 | `20_tejidos` | ✅ |
| H_org como dimensión | Ecuación master | ✅ |
| Pesos parametrizables | Fenotipo | ⚠️ |

**Conclusión M3.3:** ✅ **Convergence_Score VALIDADO**.

### 4.2 Estados

- "Converged" (≥0.85), "In Progress" ([0.50-0.85)), "Lagging" (<0.50)
- Threshold 0.85 es fenotípico ⚠️
- Distinción 3 estados coherente con I4 ✅

### 4.3 Invariantes

| Invariante | Cumple |
|------------|--------|
| I1 (Trazabilidad) | ✅ |
| I3 (No-regresión) | ✅ |
| I4 (Operabilidad) | ✅ |
| I8 (Adaptabilidad) | ✅ |

---

## §5 VALIDACIÓN CRUZADA

### 5.1 Flujo datos

```
F1 → health_score → decision_matrix → F4-9 (E6_tgt) → convergence
```

| Dependencia | Coherencia | Estado |
|-------------|------------|--------|
| H_org → trajectory | DM1-5 usan H_org | ✅ |
| trajectory → E6_target | T7 trayectorias | ✅ |
| E6_target → convergence | §4.1 validado | ✅ |

**Conclusión:** ✅ **Flujo coherente sin inconsistencias**.

### 5.2 DEPENDENCY_GRAPH

| Calculadora | Deps declaradas | Coherencia |
|-------------|----------------|------------|
| health_score | F1 → health | ✅ |
| trajectory | F1,health → F3 | ✅ |
| arch_state | F9 → E6_tgt | ✅ |

---

## §6 HALLAZGOS

### Bloqueantes: 🎉 **0**
### Críticos: 🎉 **0**

### Menores (3):

**H1:** Descomposición A/P/D no explícita en genoma
- Severidad: Menor
- Recomendación: Documentar post-1.0.0 como fenotipo válido

**H2:** Umbrales numéricos fenotípicos
- Afecta: G1-G4 (0.35/0.55/0.75), DM thresholds, convergence (0.85)
- Recomendación: Calibrar con casos 01/06, documentar como iniciales

**H3:** Pesos relativos fenotípicos
- Afecta: w_A/P/D, weight_TF1/2/3
- Recomendación: Mantener configurables en .xlsx

---

## §7 CONCLUSIONES

### Resumen ejecutivo

✅ **Las 3 calculadoras correctamente derivadas del genoma ORKO**.

| Calculadora | Trazabilidad | Invariantes | Bloqueantes | Estado |
|-------------|-------------|-------------|-------------|--------|
| health_score | ✅ T6,TF1/2/3,I6 | ✅ I1/3/4/6/7 | 0 | ✅ |
| decision_matrix | ✅ A4,P4/6,T7,I6 | ✅ I1/6/8 | 0 | ✅ |
| convergence | ✅ P5,I3,TF1/2/3 | ✅ I1/3/4/8 | 0 | ✅ |

**Hallazgos:** 0 bloqueantes, 0 críticos, 3 menores (advertencias)

**Conclusión M3.3:** Las calculadoras son **expresiones fenotípicas válidas** y pueden implementarse en .xlsx sin modificar kernel.

### Recomendaciones

**Para sq2 (implementación):**
1. Parámetros configurables en tabs "PARÁMETROS"
2. Documentar fuentes genómicas en metadata
3. Calibrar defaults con casos 01/06
4. Validaciones internas (suma pesos=1.0, etc.)

**Para sq1 (aplicación):**
1. Inputs trazables a artefactos reales
2. Documentar gaps de información
3. Verificar coherencia narrativa

**Para sq4 (guía):**
1. Explicitar separación genoma/fenotipo
2. Ejemplos de calibración por contexto
3. Incluir trazabilidad en casos

---

## §8 PRÓXIMOS PASOS

**Post-1.0.0:**
1. Formalizar A/P/D en genoma
2. Teorema T16 de convergencia
3. Sección parámetros fenotípicos en VOCAB

---

**Versión:** CAP-22 | **Estado:** M3.1-M3.3 completados | **Autor:** sq3
