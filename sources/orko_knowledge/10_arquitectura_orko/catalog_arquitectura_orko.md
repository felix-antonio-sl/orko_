# Catálogo de Conocimiento: Arquitectura Orko

Este catálogo indexa los recursos fundamentales para el Agente Arquitecto de Orko.
Estos documentos definen la capa lógica del sistema, incluyendo contratos, principios, relaciones y patrones.

## Fuentes Primarias (Nivel 1: Normativo)

### 1. Introducción y Visión General
- **Archivo**: `00_introduccion.md`
- **Propósito**: Provee la visión global de la arquitectura, su estructura modular y la trazabilidad vertical.
- **Uso**: Contexto general y navegación inicial.

### 2. Contratos Canónicos (C1-C5)
- **Archivo**: `01_contratos.md`
- **Propósito**: Define formalmente los primitivos del sistema (Capacidad, Flujo, Activo, etc.) y sus esquemas de datos obligatorios.
- **Uso**: Validación de estructuras de datos y cumplimiento de invariantes de tipo.

### 3. Principios de Diseño (PD1-PD76)
- **Archivo**: `02_diseño.md`
- **Propósito**: Establece las reglas de diseño (Genoma y Fenotipo) que deben regir cualquier implementación Orko.
- **Uso**: Auditoría de diseños y justificación de decisiones arquitectónicas.

### 4. Modelo Relacional (R1-R15)
- **Archivo**: `03_relaciones.md`
- **Propósito**: Especifica las relaciones permitidas entre entidades, sus multiplicidades y restricciones (ej. HAIC).
- **Uso**: Validación de grafos de conocimiento y estructuras organizacionales.

### 5. Vistas Arquitectónicas (D1-D4)
- **Archivo**: `04_vistas.md`
- **Propósito**: Define las proyecciones estándar para visualizar el sistema (Estructural, Comportamiento, etc.).
- **Uso**: Generación de diagramas y artefactos visuales.

### 6. Patrones y Anti-Patrones
- **Archivo**: `05_patrones.md`
- **Propósito**: Cataloga soluciones probadas para problemas comunes y advertencias sobre malas prácticas.
- **Uso**: Recomendación de soluciones constructivas y refactorización.
