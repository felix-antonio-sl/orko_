# ORKO: Organizational Knowledge Ontology

> **v1.0.0 - "Complexity, Tamed."**

[![KODA Compliant](https://img.shields.io/badge/KODA-1.0.0-blue)](https://github.com/felix-antonio-sl/koda_)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🚀 ¿Eres un Usuario Final?

Si buscas usar ORKO para transformar tu organización **AHORA MISMO**, ignora el resto de este repositorio y ve directo a:

👉 **[ORKO_Toolkit_v1.0.0/](ORKO_Toolkit_v1.0.0/)**

Allí encontrarás:
1. **Guía de Inicio:** `00_COMIENCE_AQUI.md` 
2. **Herramientas:** Calculadoras y Excel listos para usar.
3. **Kits:** Paquetes de acción según tu nivel de salud (`Survival`, `Minimal`, `Advanced`).

---

## 📚 KODA Knowledge Base

Este repositorio es un **namespace KODA-compliant** que contiene conocimiento estructurado y agentes IA para transformación organizacional.

### URN Namespace
```
urn:knowledge:orko:{domain}:{artifact}:{version}
```

### Estructura KODA
```
orko/
├── .knowledge-resolver.yml    # Configuración de federación KODA
├── catalog/
│   └── catalog_master_orko.yml  # Inventario de artefactos
├── knowledge/
│   ├── core/                  # Layers 0-2: Fundamentos, Arquitectura, Tejidos
│   └── domains/
│       ├── metodologia/       # Layer 3: Fases, Playbooks
│       └── implementacion/    # Layer 4: Toolkit specs
├── agents/
│   └── arquitecto-orko/       # Agente experto ORKO
├── schemas/                   # JSON Schemas (futuro)
├── sources/                   # Materiales fuente
└── staging/                   # Work in progress
```

---

## 🏗️ Arquitectura de Capas ORKO

| Layer | Nombre | Contenido | Estado |
|-------|--------|-----------|--------|
| **0** | Fundamentos Teóricos | Genoma: Primitivos (P1-P5), Invariantes (I1-I8), Teoremas | ✅ Estable |
| **1** | Arquitectura | Contratos, relaciones, PD1-PD76 | ✅ Estable |
| **2** | Tejidos | TF1-TF3 - Instanciación de primitivos | ✅ Definido |
| **3** | Metodología | Fases, Playbooks, Templates | ✅ Completo |
| **4** | Implementación | Scripts, generadores, specs | ✅ Funcional |
| **5** | Producto (Toolkit) | Entregable compilado | ✅ Released |

---

## 🤖 Agentes ORKO

### Arquitecto ORKO
```yaml
URN: urn:knowledge:orko:agents:arquitecto-orko:1.0.0
```
Agente experto en transformación organizacional usando metodología ORKO. Domina:
- Diagnóstico de salud organizacional
- Selección de playbooks (Survival/Minimal/Advanced)
- Aplicación de primitivos e invariantes
- Guía de implementación de tejidos tecnológicos

---

## 🛠️ Desarrollo y Contribución

### Generación de Artefactos
```bash
cd 40_implementacion_metodologia/dev_specs
source .venv_cap22/bin/activate
python scripts/generate_calculadoras_cap22.py
```

### Principios de Contribución
1. **Minimalidad:** No agregues nada que no sea estrictamente necesario.
2. **Trazabilidad:** Todo cambio en el Toolkit debe tener un origen en el Genoma.
3. **Honestidad:** Si algo es un borrador, márcalo como "WIP".

### Validación KODA
```bash
# Desde el directorio koda
cd ../koda
./scripts/koda-health.sh ../orko
```

---

## 🔗 Federación KODA

Este namespace está federado con:
- **koda** (upstream): Framework base
- Otros namespaces pueden referenciar artefactos ORKO vía URN

### Ejemplo de Referencia Cross-Repo
```yaml
dependencies:
  requires:
    - urn: "urn:knowledge:orko:core:fundamentos:1.0.0"
      reason: "ORKO primitives for organizational modeling"
```

---

## 📄 Licencia

© 2025 ORKO Project. Licensed under [MIT](LICENSE).

---

*Parte del ecosistema [KODA Framework](https://github.com/felix-antonio-sl/koda_) — Knowledge-Oriented Design Architecture*
