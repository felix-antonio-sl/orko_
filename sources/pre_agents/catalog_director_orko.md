# Catálogo de Conocimiento: Orko Director (The Squad)

Este catálogo indexa a los **Agentes de Primer Orden** que componen la Cuadrilla Orko.
El **Orko Director** utiliza este catálogo para enrutar consultas, delegar tareas y orquestar la colaboración entre especialistas.

## La Cuadrilla (The Squad)

### 1. Orko Theorist (El Teórico)
- **Archivo ADP**: `99_cuadrilla/orko_theorist/adp_orko_theorist.yml`
- **Rol**: Especialista Consultor y Defensor de los Fundamentos Teóricos.
- **Dominio**: Axiomas, Primitivos, Invariantes, Genoma.
- **Cuándo llamar**: Consultas conceptuales profundas, validación de invariantes.

### 2. Orko Sage (El Sabio)
- **Archivo ADP**: `99_cuadrilla/orko_sage/adp_orko_sage.yml`
- **Rol**: Guardián del Conocimiento Referencial.
- **Dominio**: Referencias Fundacionales (WST, AOC, IA, eGov), Teoremas.
- **Cuándo llamar**: Búsqueda de definiciones canónicas, validación de teoremas, investigación.

### 3. Orko Architect (El Arquitecto)
- **Archivo ADP**: `99_cuadrilla/orko_architect/adp_orko_architect.yml`
- **Rol**: System Architect.
- **Dominio**: Contratos, Principios de Diseño, Vistas Arquitectónicas, Patrones.
- **Cuándo llamar**: Diseño de sistemas, auditoría de arquitectura, selección de patrones.

### 4. Orko Guide (El Guía)
- **Archivo ADP**: `99_cuadrilla/orko_guide/adp_orko_guide.yml`
- **Rol**: Methodology Specialist.
- **Dominio**: Ciclo de Vida (Fases), Playbooks, Gobernanza Metodológica.
- **Cuándo llamar**: Navegación por fases, selección de playbooks, diagnóstico de salud.

### 5. Orko Weaver (El Tejedor)
- **Archivo ADP**: `99_cuadrilla/orko_weaver/adp_orko_weaver.yml`
- **Rol**: Ingeniero de Sistemas y Tejidos.
- **Dominio**: Implementación Técnica (TF1, TF2, TF3), Código, Despliegue.
- **Cuándo llamar**: Implementación concreta, selección de stack tecnológico, generación de código.

### 6. Orko Builder (El Constructor)
- **Archivo ADP**: `99_cuadrilla/orko_builder/adp_orko_builder.yml`
- **Rol**: Especialista en Herramientas y Toolkit.
- **Dominio**: Calculadoras, Plantillas, Ejemplos Prácticos.
- **Cuándo llamar**: Necesidad de herramientas prácticas, templates, ejemplos.

## Matriz de Enrutamiento

| Intención del Usuario         | Agente Principal       | Agente de Soporte          |
| :---------------------------- | :--------------------- | :------------------------- |
| "¿Qué es...?" (Teoría)        | **Theorist**           | Sage                       |
| "¿Qué dice la referencia...?" | **Sage**               | Theorist                   |
| "¿Cómo diseño...?"            | **Architect**          | Sage                       |
| "¿Qué paso sigue...?"         | **Guide**              | Builder                    |
| "¿Cómo implemento...?"        | **Weaver**             | Architect                  |
| "¿Tienes una plantilla...?"   | **Builder**            | Guide                      |
| "Evalúa mi sistema"           | **Architect** (Diseño) | **Theorist** (Invariantes) |
