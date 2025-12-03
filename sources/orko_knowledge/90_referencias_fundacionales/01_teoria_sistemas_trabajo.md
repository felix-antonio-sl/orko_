# Teoría de Sistemas de Trabajo

**ID**: ORKO-REF-TST-01  
**Versión**: 1.1.0  
**Última actualización**: 2025-01-13  
**Changelog 1.1.0**: Agregado §9 (Extensión e-Government, Axioma A10 Valor Dual)  
**Fuentes**: Alter WST (2013), TSTI Axiomática  

---

## §1. PRIMITIVO BASE

### Sistema de Trabajo (9-tupla)

```
WS := ⟨P, A, I, T, V, C, E, S, R⟩

P: Participantes (H ∪ AA)
A: Actividades/Procesos
I: Información
T: Tecnologías
V: Valor (productos/servicios)
C: Clientes
E: Entorno
S: Estrategias
R: Recursos compartidos
```

**Definición**: Sistema donde participantes humanos/máquinas realizan trabajo usando información, tecnología y recursos para producir productos/servicios para clientes.

---

## §2. AXIOMAS FUNDAMENTALES

**A1. Existencia**: `∀Contexto_Org: ∃WS`

**A2. Transformación**: `∀WS: ∃φ: (P × A × I × T) → V`

**A3. Entrega**: `∀WS: ∃ψ: V → C`

**A4. Restricción**: `∀WS: φ opera bajo (E, S, R)`

**A5. Agencia Dual**: `P = H ∪ AA` (humanos ∪ agentes algorítmicos)

**A6. Ciclo Cognitivo**: `∀WS: SENSE → DECIDE → EXECUTE`

**A7. No Optimalidad**: No existe configuración óptima para todos los criterios simultáneamente

**A8. Incompletitud**: Todo diseño genera comportamientos emergentes no especificados

**A9. Cambio Dual**: `Evolución = Planificado ⊕ Emergente`

---

## §3. TAXONOMÍA

### Clasificación por Agencia

- **WS_Sociotécnico**: `H ≠ ∅` (al menos un humano)
- **WS_Automatizado**: `H = ∅ ∧ AA ≠ ∅` (solo agentes)
- **Sistema de Información**: `IS ⊂ WS` donde actividades son operaciones informacionales
- **CHS**: Sistema ciber-humano con interacción consciente H-AA

---

## §4. CICLO DE VIDA (WSLC)

```
Operación ⟷ (Iniciación → Desarrollo → Implementación) ⟷ Operación
```

**Dinámica de Workarounds**:

```
Improvisación → Bricolage → Aprendizaje → Proyecto_Formal → Método_Sistemático
```

**Teorema**: `Frecuencia(Workarounds) ∝ Gap(Diseño, Necesidad)`

---

## §5. TEORÍA DE USO (ISUT)

### Roles IS (6 tipos)

- R1: Monitorear
- R2: Proveer información
- R3: Habilitar capacidades
- R4: Controlar
- R5: Co-producir
- R6: Ejecutar

### Facetas de Trabajo (18)

Decisión, Comunicación, Procesamiento, Pensamiento, Representación, Provisión Info, Conocimiento, Aprendizaje, Planificación, Control, Improvisación, Coordinación, Trabajo Físico, Soporte, Interacción Social, Servicio, Creación Valor, Seguridad

### Tensor de Uso

```
Uso_Efectivo(IS, WS) = ∑(i,j) Rol_i × Faceta_j × Contexto
AR: R × F → {NR, Bajo, Medio, Alto, Crítico}
Dimensionalidad = 6 × 18 = 108 vectores
```

---

## §6. SUPERPOSICIÓN IS-WS

```
Tipo 1: [IS]─interface─[WS]     (Simple)
Tipo 2: [IS]∩ε[WS]               (Mínima)
Tipo 3: [IS ∩∩ WS]               (Sustancial)
Tipo 4: [IS ⊂ WS]                (Completa)
```

**Teorema**: `Complejidad_Coordinación ∝ Grado_Superposición`

---

## §7. ECUACIÓN MAESTRA

```
Valor(WS) = F(
  Alineación_Interna(P, A, I, T, V, C),
  Distribución_SADE(H, AA),
  Tensor_AR(R × F),
  Balance_Criterios(Eval),
  Conjunto_Patrones(Patterns),
  Acceso_KO
) bajo restricciones(E, S, R, Path_Dependency)
```

---

## §8. METATEOREMAS

**Consistencia**: TSTI no contiene contradicciones derivables

**Decidibilidad**: Toda proposición sobre WS específico es decidible en tiempo finito

**Completitud**: Framework describe completamente cualquier WS

**Minimalidad**: No se pueden eliminar axiomas sin pérdida de cobertura

**Ortogonalidad**: Dimensiones {SADE, AR, Eval, WSLC, Patterns} son independientes

---

## §9. EXTENSIÓN PARA CONTEXTO E-GOVERNMENT

### Axioma A10. Valor Dual en Sector Público

```
∀WS_eGov: V = V_transaccional ⊕ V_societal

V_transaccional: Valor entregado a stakeholder directo (ciudadano, empresa)
V_societal: Valor entregado a sociedad como bien colectivo
```

**Justificación Irreducibilidad**:

- Sin V_societal, eGov = empresa privada (fuera de alcance público)
- Ethos público requiere maximizar ambos (no solo transaccional)
- No derivable de A1-A9 (sector privado válido sin V_societal)

**Fundamentación Teórica**:

- Alter eGovWSF: "Valor para la sociedad" como elemento distintivo
- Bannister & Connolly: Taxonomía valores públicos (deber, servicio, sociedad)
- Hood: Ideales de gestión pública (profesionalismo, eficiencia, servicio, engagement)

### Formalización V_societal

**Modelo Bannister & Connolly (3 dimensiones)**:

```
V_societal := w₁·V_deber + w₂·V_servicio + w₃·V_sociedad

V_deber := {
  Accountability: Responsabilidad por decisiones y recursos
  Transparency: Visibilidad procesos y datos
}

V_servicio := {
  Efficiency: Costo-efectividad recursos públicos
  Effectiveness: Logro objetivos declarados
  Responsiveness: Capacidad respuesta a necesidades
}

V_sociedad := {
  Justice: Trato justo bajo ley
  Equality: Igualdad acceso servicios
  Equity: Distribución justa recursos considerando necesidades
}

Restricción: w₁ + w₂ + w₃ = 1 (pesos contextuales)
```

### Teorema Conservación Valor Público

```
∀WS_eGov: Maximizar V_transaccional SIN considerar V_societal →
           Violación ethos público (Ref: Doc 05 §2)

Corolario: ∃configuraciones donde V_transaccional ↑ pero V_societal ↓
           (Ejemplo: Automatización que excluye ciudadanos sin acceso digital)
```

### Función de Evaluación Dual

```
Valor_Total(WS_eGov) = α·V_transaccional + β·V_societal

α, β: Pesos políticos (varían por jurisdicción y régimen)

Restricciones obligatorias:
  β > 0 (siempre considerar valor societal)
  V_societal ≥ V_min (umbral legal/ético)
  ∀stakeholder ∈ Ciudadanía: V_accesible(stakeholder) > 0 (inclusión)
```

### Integración con Ecuación Maestra (§7)

**Ecuación extendida para eGov**:

```
Valor(WS_eGov) = F(
  Alineación_Interna(P, A, I, T, V_transaccional, V_societal, C),
  Distribución_SADE(H, AA),
  Tensor_AR(R × F),
  Balance_Criterios(Eval),
  Conjunto_Patrones(Patterns),
  Acceso_KO,
  Valores_Públicos(Accountability, Transparency, Equity)
) bajo restricciones(
  E, S, R, Path_Dependency,
  Leyes_Regulaciones,  ← Nuevo (Ref: Doc 05 §4)
  Ethos_Público         ← Nuevo (Ref: Doc 05 §2)
)
```

### Aplicación en Diseño eGov

**Tensiones Típicas**:

```
Efficiency ↔ Equity
  (Automatizar vs Inclusión digital)

Responsiveness ↔ Due_Process
  (Rapidez vs Garantías legales)

Innovation ↔ Stability
  (Transformación vs Continuidad servicio)

Centralization ↔ Local_Autonomy
  (Estándares nacionales vs Adaptación regional)
```

**Regla de Resolución**:

```
∀tensión: Resolver vía pesos (α, β) explícitos + V_min obligatorio
NO existe solución óptima universal (Axioma A7 aplica)
```

### Derivación hacia ORKO

**Primitivo P5 (Propósito)**:

```
∀WS_eGov: Purpose := {
  target_value_transaccional: Métrica tradicional (tiempo, costo, calidad)
  target_value_societal: Métrica valor público (8 dimensiones Bannister)
  legal_basis_refs: URI[] (leyes que fundamentan propósito)
  public_value_weights: {w₁, w₂, w₃}
}
```

**Contrato C5 (Propósito) extendido**:

- Campo `public_value` (ya aplicado en PR-05) ahora deriva formalmente de A10
- Campo `legal_basis_refs` deriva de restricción Leyes_Regulaciones

---

**Aplicación en ORKO**: Esta teoría provee los primitivos (P1-P5) y axiomas (A1-A10) del Layer 0, fundamentando toda la arquitectura. La extensión eGov (§9) fundamenta formalmente el diseño para sector público.
