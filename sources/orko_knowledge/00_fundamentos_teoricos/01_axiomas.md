# ORKO: FUNDAMENTOS TEÓRICOS

- [ORKO: FUNDAMENTOS TEÓRICOS](#orko-fundamentos-teóricos)
  - [PARTE I: AXIOMAS IRREDUCIBLES](#parte-i-axiomas-irreducibles)
    - [§1. INTRODUCCIÓN ONTOLÓGICA](#1-introducción-ontológica)
    - [§2. LOS CINCO AXIOMAS FUNDAMENTALES](#2-los-cinco-axiomas-fundamentales)
    - [§3. VALIDACIÓN DE AXIOMAS](#3-validación-de-axiomas)

## PARTE I: AXIOMAS IRREDUCIBLES

### §1. INTRODUCCIÓN ONTOLÓGICA

**Objetivo:** Definir axiomas que NO pueden reducirse más, desde los cuales todo lo demás deriva.

**Método:** Análisis categorial + verificación empírica contra fuentes + síntesis refundacional.

### §2. LOS CINCO AXIOMAS FUNDAMENTALES

```yaml
AXIOMA_A1_Existencia_Transformación:
  Enunciado: 
    "En todo sistema organizacional existe transformación: 
     algo cambia de estado S₁ a estado S₂"
  
  Justificación_Irreducibilidad:
    - Sin transformación, sistema es estático (fuera de alcance)
    - Organización = sistema que transforma inputs en outputs
    - No derivable de otro concepto más fundamental
    
  Fundamentación_Teórica:
    - Alter WST: "Work system transforma inputs en outputs para customers"
    - TSTI: "Act(ividades) = transformaciones que producen outputs"
    - Meyer: "Flujo de valor = propagación transformaciones"
    
  Primitivo_Derivado: FLUJO
  
  Propiedad_Medible:
    - Transformación tiene duración T
    - Transformación tiene costo C
    - Transformación tiene calidad Q


AXIOMA_A2_Existencia_Capacidad:
  Enunciado:
    "Existe capacidad que efectúa transformación. 
     Transformación no ocurre espontáneamente"
  
  Justificación_Irreducibilidad:
    - Transformación requiere agente causal
    - Capacidad = potencial de transformar
    - No reducible a transformación misma
    
  Fundamentación_Teórica:
    - Alter WST: "Participants (humanos) + Technologies (artefactos)"
    - TSTI: "Participants = H ∪ AA (humanos + agentes algorítmicos)"
    - Meyer: "Capacidad = recursos + competencias + autoridad"
    
  Primitivo_Derivado: CAPACIDAD
  
  Distinción_Crítica:
    Capacidad ≠ Actor
    - "Actor" conflates sustrato (quién) con capacidad (qué puede hacer)
    - "Capacidad" separa nivel cognitivo de sustrato físico
    
  Propiedad_Medible:
    - Capacidad tiene throughput (unidades/tiempo)
    - Capacidad tiene latencia (tiempo respuesta)
    - Capacidad tiene disponibilidad (0-1)


AXIOMA_A3_Existencia_Información:
  Enunciado:
    "Existe estructura portadora de significado que coordina transformaciones"
  
  Justificación_Irreducibilidad:
    - Sin información, no hay coordinación entre capacidades
    - Sin información, no hay memoria del sistema
    - Información irreducible a capacidad o transformación
    
  Fundamentación_Teórica:
    - Alter WST: "Information = datos + contexto usado/producido por WS"
    - TSTI: "Knowledge Objects = información estructurada y accesible"
    - Shannon: "Información reduce incertidumbre"
    
  Primitivo_Derivado: INFORMACIÓN
  
  Unificación_Conceptual:
    Dato, Señal, Estado son SUBTIPOS de Información:
    - Dato = Información(type=Persistente)
    - Señal = Información(type=Transitoria, trigger=true)
    - Estado = Información(type=Agregada, timestamp=T)
    
  Propiedad_Medible:
    - Información tiene volumen (bytes)
    - Información tiene freshness (age desde timestamp)
    - Información tiene calidad (completitud, exactitud)


AXIOMA_A4_Existencia_Restricción:
  Enunciado:
    "No todo es posible en todo momento. 
     Existen restricciones que acotan espacio de posibilidades"
  
  Justificación_Irreducibilidad:
    - Sin restricciones, espacio infinito (no operable)
    - Restricciones emergen de: física, regulación, recursos, economía
    - No derivable de otros axiomas
    
  Fundamentación_Teórica:
    - Alter WST: "Environment impone constraints al WS"
    - TSTI: "Límites físicos, organizacionales, económicos"
    - Meyer: "Anti-interferencia = límites que preservan coherencia"
    
  Primitivo_Derivado: LÍMITE
  
  Propiedad_Medible:
    - Límite tiene severidad (info, warning, error, critical)
    - Límite tiene cobertura (% sistema afectado)
    - Límite tiene violaciones (count, frecuencia)


AXIOMA_A5_Existencia_Intencionalidad:
  Enunciado:
    "Transformación organizacional tiene propósito: 
     existe outcome deseado que direcciona acción"
  
  Justificación_Irreducibilidad:
    - Sin propósito, transformación es movimiento browniano
    - Propósito = criterio evaluación éxito
    - No reducible a transformación (el PARA QUÉ vs el QUÉ)
    
  Fundamentación_Teórica:
    - Alter WST: "Value producido para Customers"
    - TSTI: "Evaluation = criterios objetivo/subjetivo de éxito"
    - Kelly: "Outcomes > Outputs - propósito más importante que actividad"
    
  Primitivo_Derivado: PROPÓSITO
  
  Propiedad_Medible:
    - Propósito tiene target_value
    - Propósito tiene current_value
    - Propósito tiene progress = current/target
```

### §3. VALIDACIÓN DE AXIOMAS

```yaml
Test_Irreducibilidad:
  Pregunta: "¿Puede axioma X derivarse de axiomas Y, Z?"
  
  A1 (Transformación):
    ¿Derivable de A2-A5? NO
    - A2 (Capacidad) sin transformación = potencial no usado
    - A3 (Información) sin transformación = datos estáticos
    - A4 (Límite) sin transformación = restricción sin sujeto
    - A5 (Propósito) sin transformación = intención sin acción
    ✓ Irreducible
    
  A2 (Capacidad):
    ¿Derivable de A1, A3-A5? NO
    - A1 (Transformación) no explica QUÉ la causa
    - A3 (Información) no transforma por sí misma
    - A4 (Límite) solo restringe, no habilita
    - A5 (Propósito) solo direcciona, no ejecuta
    ✓ Irreducible
    
  A3 (Información):
    ¿Derivable de A1, A2, A4, A5? NO
    - A1+A2 pueden transformar sin coordinación (caos)
    - Sin A3, no hay memoria ni estado
    ✓ Irreducible
    
  A4 (Límite):
    ¿Derivable de A1-A3, A5? NO
    - A1-A3 no imponen restricciones inherentes
    - A5 direcciona pero no restringe
    ✓ Irreducible
    
  A5 (Propósito):
    ¿Derivable de A1-A4? NO
    - A1-A4 describen mecánica, no teleología
    - Transformación sin propósito = eficiente pero sin sentido
    ✓ Irreducible

Test_Suficiencia:
  Pregunta: "¿Falta algún axioma fundamental?"
  
  Candidatos_Descartados:
    
    "Tiempo":
      ¿Es axioma separado? NO
      - Tiempo es propiedad de transformación (A1)
      - timestamp es propiedad de información (A3)
      - NO requiere axioma separado
      
    "Espacio":
      ¿Es axioma separado? NO
      - Espacio es un tipo de límite (A4: físico)
      - NO fundamental para organizaciones (son redes, no físicas)
      
    "Identidad":
      ¿Es axioma separado? NO
      - Identidad de capacidad/información es propiedad, no axioma
      - Trazabilidad derivable de A3 (información identifica origen)
      
  Conclusión: A1-A5 son necesarios y suficientes ✓

Test_Consistencia:
  Pregunta: "¿Algún axioma contradice otro?"
  
  Análisis_Par_a_Par:
    A1 ⊥ A2-A5: Transformación compatible con capacidad, información, límite, propósito ✓
    A2 ⊥ A3-A5: Capacidad compatible con información, límite, propósito ✓
    A3 ⊥ A4-A5: Información compatible con límite, propósito ✓
    A4 ⊥ A5: Límite compatible con propósito (restringe medio, no fin) ✓
    
  Conclusión: Sistema axiomático consistente ✓
```
