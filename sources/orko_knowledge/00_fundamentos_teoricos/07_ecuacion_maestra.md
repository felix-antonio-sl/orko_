# PARTE VII: ECUACIÓN MAESTRA

- [PARTE VII: ECUACIÓN MAESTRA](#parte-vii-ecuación-maestra)
  - [Ecuación maestra](#ecuación-maestra)
    - [§10. ECUACIÓN MAESTRA VALOR ORGANIZACIONAL](#10-ecuación-maestra-valor-organizacional)

> **Etiquetado Genoma/Fenotipo**: Este documento contiene [GENOMA] (ecuación formal V_org) y [FENOTIPO] (pesos, thresholds operativos). Ver §0.1 en 00_introduccion.md.

## Ecuación maestra

### §10. ECUACIÓN MAESTRA VALOR ORGANIZACIONAL

**[GENOMA]**

```yaml
Derivación_Formal_Desde_P5:

  Fundamentación:
    V_org NO es ecuación independiente.
    Deriva FORMALMENTE de P5 (Propósito) aplicado a portfolio WS.
    
  Dado: WS = (P1, P2, P3, P4, P5)
  Donde: P5 = Propósito(outcome, metrics[], parent_id)
  
  Entonces:
    outcome_value_ws = f(P5.metrics, P5.target_value)
    cost_ws = Σ (P1_capacity × tiempo × unit_cost)
    
    V_org(t) = Σ_ws∈Portfolio outcome_value_ws(t) - Σ_ws∈Portfolio cost_ws(t)
    
  Trazabilidad: V_org → P5 (primitivo) → A5 (axioma)

Definición_Valor_Org:

  V_org(t) = Σ_i outcome_bruto_i(t) - (Σ_i cost_producción_i(t) + Σ_j cost_habilitación_j(t))
  
  Donde:
    outcome_bruto_i(t): Valor bruto entregado flujo producción i
    cost_producción_i(t): Costos directos flujo producción i (capacidades, materiales)
    cost_habilitación_j(t): Costos flujos habilitación j (DevOps, HR, etc.)
  
  Nota_Contable:
    "Ecuación usa costeo completo (absorción). Outcomes son BRUTOS
     (revenue/valor percibido), costos incluyen producción + habilitación.
     f_evaluate mide CALIDAD/ADECUACIÓN, no financiamiento."
    
Descomposición_Outcome:

  outcome_i(t) = f_evaluate(output_i(t), propósito_i) × volume_i(t)
  
  Componentes:
    output_i(t): Información producida por flujo i
    propósito_i: Outcome deseado (P5)
    f_evaluate: Función evalúa CALIDAD output contra propósito (no financiera)
    volume_i(t): Throughput flujo (unidades/tiempo)
    
  Aclaración:
    f_evaluate retorna factor calidad (0.0 - 2.0+):
      < 1.0: Output no cumple propósito (degradación)
      = 1.0: Output cumple propósito exactamente
      > 1.0: Output excede propósito (valor premium)

## Integración AOC (Arquitectura Organizacional Cuántica)

**[GENOMA]** - Formulación Teórica

Se introduce proyección de invariantes Meyer (Coherencia, Resonancia, Flujo) sobre evaluación outcome:

```yaml
f_evaluate_enhanced(output, propósito, org_state) =
  f_evaluate_base(output, propósito) ×
  AOC_multiplier(org_state)
  
Donde:
  AOC_multiplier = w_coh·Coherencia(org) + w_res·Resonancia(org) + w_flu·Flujo(org)
  Constraint: w_coh + w_res + w_flu = 1
  
Invariantes_AOC_Teóricos:
  
  Coherencia_Meyer(org):
    Definición: Valor_entregado / Energía_total
    Donde: Energía = Esfuerzo + Fricción + Interferencia
    Propiedad: Coherencia ∈ [0, ∞), óptimo cuando interferencia→0
    Fundamentación: Meyer AOC (Ref: 90_referencias_fundacionales/02_...)
    
  Resonancia_Meyer(org):
    Definición: Profundidad_especialización × Amplitud_conexión
    Propiedad: Maximiza cuando especialización profunda + red amplia
    Fundamentación: Meyer principio especialización (P2)
    
  Flujo_Meyer(org):
    Definición: Tasa_creación_valor / (1 + Fricción_handoffs)
    Propiedad: Maximiza minimizando handoffs (transferencias valor)
    Fundamentación: Meyer principio flujo (invariante 3)
```

**[FENOTIPO]** - Configuración Operativa Recomendada

```yaml
Pesos_Sugeridos_Default:
  w_coh = 0.4  # Mayor peso coherencia (eliminar waste prioritario)
  w_res = 0.3  # Especialización + conexión
  w_flu = 0.3  # Minimizar handoffs
  
NOTA_Parametrización:
  Estos pesos son FENOTIPO (configurables según contexto).
  Ejemplo ajustes:
    - Org nueva (startup): w_flu = 0.5 (priorizar velocity)
    - Org madura: w_coh = 0.5 (priorizar eficiencia)
    - Org innovadora: w_res = 0.5 (priorizar especialización)
    
Operacionalización_Arquitectura:
  NOTA: La arquitectura ORKO (Layer 1) operacionaliza estos invariantes vía:
    - Principios PD-AOC-1 a PD-AOC-3 (derivan de esta teoría)
    - Métricas observables en dominios D1-D4
    - Ver post-lectura: ../10_arquitectura_orko/02_diseño.md
    
  Dirección dependencia: TEORÍA (aquí) → ARQUITECTURA (allá)
  NO al revés (Layer 0 es auto-contenido)
```
    
  Ejemplo:
    Flujo: OrderFulfillment
    output(Q1): 5000 orders entregados
    propósito: NPS > 70
    f_evaluate(orders, NPS=75) = 1.07 (7% sobre target)
    outcome = 5000 × 1.07 = 5350 "value units"
    
**[GENOMA]**

Descomposición_Cost:

  cost(t) = Σ_k (capacity_k × time_k(t) × unit_cost_k)
  
  Componentes:
    capacity_k: Capacidad usada en flujo (producción o habilitación)
    time_k(t): Tiempo uso en periodo t
    unit_cost_k: Costo unitario capacidad ($/hora)
    
  Ejemplos:
  
    A) Flujo_Producción: OrderFulfillment
       Capacidades: {SalesRep, WarehouseWorker, DeliveryTruck}
       time_use: {2h, 1h, 0.5h} × 5000 orders/trimestre
       unit_cost: {$40/h, $25/h, $60/h}
       cost_producción = (40×2 + 25×1 + 60×0.5) × 5000 = $682.5K
       
    B) Flujo_Habilitación: CI/CD_Pipeline
       Capacidades: {BuildServer, TestEnv, DeployService}
       time_use: {40h, 60h, 20h} × 100 pipelines/mes × 3 meses
       unit_cost: {$50/h, $100/h, $30/h}
       cost_habilitación = (50×40 + 100×60 + 30×20) × 300 = $2.58M

**[GENOMA]** - Métricas Formales Derivadas

Métricas_Derivadas:

  Eficiencia_Global:
    η_org(t) = V_org(t) / Total_Capacity_Cost(t)
    
    Target: η > 1.5
      Cada $1 habilitación genera $1.5 producción
      
  ROI_Habilitación:
    ROI_j = ΔOutcome_habilitado / Cost_j
    
    Ejemplo:
      CI/CD permite 10x más deploys
      Deploys generan features más rápido
      Features generan $5M incrementales
      CI/CD cuesta $860K/mes × 12 = $10M/año
      ROI = $5M / $10M = 0.5 (Break‑even: depende de periodicidad. Si CAPEX único $10M y beneficio $5M/año ⇒ ≈ año 2; si OPEX $10M/año vs beneficio $5M/año ⇒ no hay break‑even en régimen estacionario
      
  Value_Flow_Velocity:
    VFV = Σ outcome_i / Σ cycle_time_i
    
    Mide: Valor entregado por unidad tiempo
    Target: Maximizar sosteniblemente

**[GENOMA]** - Formulación Optimización

Optimización_Portfolio:

  Problema:
    max V_org(t)
    
    Subject to:
      Σ capacity_allocated ≤ capacity_available
      cost_total ≤ budget
      H_org(t) ≥ H_min (salud mínima preservar sostenibilidad)
      
  Donde:
    H_org: Health organizacional (función D1-D4, definida en 05_dominios.md)
    H_min: Threshold mínimo (FENOTIPO, típicamente 70)
    
**[FENOTIPO]** - Heurísticas Solución
      
Heurísticas_Recomendadas:
  
  Priorización:
    - RICE (Reach × Impact × Confidence / Effort)
    - WSJF (Weighted Shortest Job First)
    
  Asignación:
    - Capacidades a flujos con mayor ROI incremental
    - Constraint: Preservar H_org ≥ H_min
    
  Balanceo_Producción_Habilitación:
    Heurística: 70% capacidad producción, 30% habilitación
    
    NOTA: Este ratio es FENOTIPO (configurable).
    Ajustes contextuales:
      - Org legacy: 60/40 (más investment modernización)
      - Org greenfield: 80/20 (menos habilitación inicial)
      - Org escala: 65/35 (más platform investment)
    
**[GENOMA]** - Invariante Health-Value

Invariante_Health_Value:

  IF H_org < H_min THEN ∂V_org/∂t < 0 (degradación futura)
  
  Demostración:
    H_org bajo → Debt acumulado alto
    Debt alto → Velocity decae (fricción aumenta)
    Velocity baja → V_org/t decrece
  
  Justificación:
    Salud baja → debt acumula → velocity decae
    Mejor: Invertir en health antes que nuevas features
```

**[FENOTIPO]** - Threshold H_min

```yaml
H_min_Default: 70
  Interpretación: 70% health mínimo para transformaciones seguras
  
Ajustes_Contextuales:
  - Org estable, low-risk: H_min = 60 (más permisivo)
  - Org crítica, high-stakes: H_min = 80 (más conservador)
  - Org startup, high-growth: H_min = 50 (tolerancia deuda técnica)
```

> **Resumen Genoma/Fenotipo**: V_org es ecuación formal (genoma). Pesos AOC, ratios 70/30, thresholds H_min son configuraciones operativas (fenotipo) que respetan la forma teórica.