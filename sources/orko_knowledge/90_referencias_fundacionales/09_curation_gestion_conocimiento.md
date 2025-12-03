# Curación y Gestión de Conocimiento

**ID**: ORKO-REF-CGC-01  
**Fuentes**: STS (Structured Telegraphic Style), SFD (Structured Form Definition), KHM (Knowledge Hub Management)  
**Propósito**: Gobernar la curation de conocimiento como activo de software con ciclo de vida completo

---

## §1. FILOSOFÍA FUNDACIONAL

### 1.1 Principio Central: Conocimiento como Activo de Software

```
Conocimiento ≡ Software Code
- Versionado (Git)
- Ciclo de vida completo
- Quality control obligatorio
- Single source of truth
```

**Axioma de Refactoring**:

```
Curation ≠ Summarization
Curation = Format_Refactoring + Zero_Information_Loss
```

**Corolario**: Resumir = Error crítico que corrompe el activo

### 1.2 Los 5 Principios (Transversales a STS/SFD/KHM)

**P1. Fidelidad Absoluta**

```
∀artefacto_curado: Information(artefacto_curado) = Information(source)
```

Distillation transforma formato, NO omite contenido ("meat").

**P2. Source of Truth Autocontenida**

```
∀concepto: ∃!definición_en_artefacto
Referencias internas: Ref: ID_interno
Referencias externas: Solo contextuales (Ctx:)
```

**P3. Estructura = Significado**

- Jerarquía (headers), IDs, tablas, listas → Son "meat", no "fat"
- Prohibición: Markdown estilístico (bold, italics)

**P4. Densidad Máxima (Zero Fat)**

```
Densidad(artefacto) = Meat_tokens / Total_tokens → max
```

Eliminar verborrea; traducir matices a keywords explícitos

**P5. Invariancia de Lenguaje**

```
Control_Language (Keywords) = EN (fixed)
Content_Language (EssentialData) = Original_Language (preservado)
```

---

## §2. STS: STRUCTURED TELEGRAPHIC STYLE

### 2.1 Metáfora Conceptual

**Skeleton**: Estructura lógica (headers, IDs, tablas)  
**Meat**: Información esencial, datos, facts  
**Fat**: Verborrea sin valor informacional (eliminar)

### 2.2 Componentes Mandatorios

#### Control Metadata Block

```markdown
ID: ARTIFACT-DOMAIN-CONCEPT-NUM
Version: MAJOR.MINOR.PATCH (semver)
Status: Draft | Review | Published | Obsolete
Human-Creator: <initials>
Human-Editor: <initials>
Model-Collaborator: <model_name>
Creation-Date: YYYY-MM-DD
Modification-Date: YYYY-MM-DD
Source: <URI | description>
Ctx: <scope>
```

#### LLM Parsing Instructions

```
BEGIN_LLM_INSTRUCTIONS

You are consuming an STS artifact with absolute fidelity.
1. Core: Preserve meat+skeleton, ignore fat
2. Lexicon: Expand abbreviated keywords (Purp:→Purpose:, Req:→Requirement:, etc.)
3. Ref: Internal cross-references to ID: within THIS document only
4. Language: Keywords=EN, EssentialData=original language

END_LLM_INSTRUCTIONS
```

### 2.3 Lexicon Canónico (Consolidado)

| Abbr. | Keyword | Uso |
|-------|---------|-----|
| `Purp:` | Purpose | Propósito/intención |
| `Req:` | Requirement | Requisito/requerimiento |
| `Def:` | Definition | Definición formal |
| `Cpt:` | Concept | Concepto/idea |
| `Ctx:` | Context | Contexto/alcance |
| `Prohib:` | Prohibition | Prohibición |
| `Ref:` | Reference | Referencia interna a ID |
| `Ex:` | Example | Ejemplo |
| `Proc:` | Process | Proceso/serie de pasos |
| `Fnd:` | Foundation | Base/fundamento |
| `Mech:` | Mechanism | Mecanismo/cómo funciona |
| `Res:` | Result | Resultado/beneficio |
| `Just:` | Justification | Justificación/razón |
| `Warn:` | Warning | Advertencia/riesgo |
| `Cond:` | Condition | Condición/prerequisito |
| `Src:` | Source | Origen de información |

### 2.4 Micro-estructura: Línea Telegráfica

```
Keyword: EssentialData
```

**Proceso de Traducción de Intención**:

```
"No olvides..." → Req:
"Sería bueno considerar..." → Rec:
"Existe riesgo de..." → Warn:
```

### 2.5 Macro-estructura: Red de Conocimiento

**Jerarquía de Headers**: `#`, `##`, `###`  
**IDs Únicos**: `GROUP-SUBGROUP-CONCEPT-ID`  
**Cross-References**: `Ref: ID_interno`

**Teorema de Unicidad**:

```
∀concepto c: ∃!sección s: Define(s, c)
∀otra_mención: Ref: ID(s)
```

### 2.6 Embedded Blocks (Contenedores)

```markdown
BEGIN_EMBEDDED_BLOCK:: <TYPE> <BLOCK_ID>

[Contenido opaco al parser STS, gobernado por estándar externo]

END_EMBEDDED_BLOCK:: <BLOCK_ID>
```

**Uso**: SFD, scripts, diagramas Mermaid dentro de documento STS

---

## §3. SFD: STRUCTURED FORM DEFINITION

### 3.1 Rol y Relación con STS

**Definición**: SFD NO es estándar standalone; es formato de contenido especializado

**Requisito**: SFD DEBE estar encapsulado en `EMBEDDED_BLOCK` dentro de documento STS padre

### 3.2 Misión

Transcribir formularios con **fidelidad funcional**:

- Estructura completa
- Metadata
- Reglas de validación
- Lógica condicional

**Advertencia**: SFD ≠ resumen; SFD = re-arquitectura funcional en formato máquina

### 3.3 Arquitectura de Componentes

#### Form-Section

Header `###` que agrupa campos lógicamente

#### Form-Field

Unidad atómica bajo header `####`, definida por KeyTerms:

| KeyTerm | Mandatory | Definición |
|---------|-----------|------------|
| `ID:` | Sí | Identificador único (STS standard) |
| `Field-Label:` | Sí | Texto visible del campo |
| `Field-Type:` | Sí | Tipo de dato/control |
| `Field-Instr:` | No | Instrucciones para usuario |
| `Field-Constraint:` | No | Reglas de validación |
| `Field-Placeholder:` | No | Ejemplo en campo vacío |
| `Field-Option:` | Condicional | Opciones (Radio/Select/Checkbox-Group) |
| `Field-Logic:` | No | Visibilidad/requisitos condicionales |

### 3.4 Vocabulario Controlado: Field-Type

```
Text | TextArea | Number | Date | Checkbox | Checkbox-Group |
Radio | Select | File | Static-Text | Repeater
```

### 3.5 Mini-Lenguaje: Field-Constraint

```
Req: mandatory | optional
Max-Len: <n>
Min-Len: <n>
Max-Val: <n>
Min-Val: <n>
Format: email | url | YYYY-MM-DD
Pattern: <regex>
```

### 3.6 Ejemplo Canónico

```markdown
# Document: Risk Assessment Form
ID: PROJ-RISK-FORM-01
...

BEGIN_EMBEDDED_BLOCK:: SFD RISK-DECL-FORM-01

### Legal Compliance Section
ID: FORM-RISK-S1-LEGAL-01

#### Requires Legal Review
ID: FORM-RISK-F1-LEGALREV-01
Field-Label: "¿Requiere revisión legal?"
Field-Type: Checkbox
Field-Constraint: "Req: mandatory."

#### Justification
ID: FORM-RISK-F2-JUSTIFY-01
Field-Label: "Justificación"
Field-Type: TextArea
Field-Logic: "Cond: (Ref: FORM-RISK-F1-LEGALREV-01.Value == 'true') -> Req: mandatory."
Field-Constraint: "Req: mandatory. Max-Len: 500."

END_EMBEDDED_BLOCK:: RISK-DECL-FORM-01
```

---

## §4. KHM: KNOWLEDGE HUB MANAGEMENT

### 4.1 Arquitectura de Directorios (Mono-repo)

```
/knowledge/                  ← Artefactos curados y publicados
  /core/                     ← Conocimiento transversal
  /domains/{domain_name}/    ← Conocimiento específico dominio
  /catalog/                  ← Inventario maestro

/sources/                    ← Materiales crudos sin procesar

/staging/                    ← WIP transformación

/agents/                     ← Definiciones de agentes IA
  /{agent_name}/
    agent.yaml
```

### 4.2 Convención de Nomenclatura

```
{tipo}_{dominio}_{id-num}_{descripcion-corta}_{formato}.md
```

**Componentes**:

- `tipo`: `kb` (knowledge base) | `guide` (meta-documento)
- `dominio`: `core` | `gn` (GORE Ñuble) | ...
- `id-num`: 3 dígitos (001, 002, ...)
- `descripcion-corta`: 2-4 palabras kebab-case
- `formato`: `sts` | `sfd` (si es standalone, raro)

**Ejemplos**:

- `kb_gn_001_contexto-regional_sts.md`
- `guide_core_002_alm-master_sts.md`
- `kb_gn_005_formulario-postulacion_sts.md` (con bloque SFD embebido)

### 4.3 Knowledge Catalog

**Archivo maestro**: `knowledge/catalog/catalog_master_sts.md`

**Entrada por artefacto**:

```markdown
### kb_gn_001_contexto-regional_sts.md
ID: CATALOG-GN-KB-001
Purp: Proveer contexto fundamental de Región Ñuble.
Cpt: Skeleton.
  - "## 1. Datos Geográficos y Demográficos"
  - "## 2. Estructura Económica"
  - "## 3. Organización Política y Administrativa"
  - "## 4. Stakeholders Clave Regionales"
```

**Resultado**: Assessment rápido sin abrir archivo

### 4.4 Ciclo de Vida (6 fases)

**Fase 1: Sourcing** → Identificar/colocar material crudo en `/sources/`

**Fase 2: Staging & Transformation** → Copiar a `/staging/`, aplicar STS/SFD

**Fase 3: Audit** → Compliance checklist (100% pass obligatorio)

**Fase 4: Publishing** → Nomenclatura final, mover a `/knowledge/`, sync KB

**Fase 5: Registration** → Actualizar catalog con entrada nueva

**Fase 6: Maintenance** → Mini-ciclo: staging → audit → overwrite → sync

### 4.5 Prohibición: Branching para Configuraciones

**Anti-Pattern Crítico**:

```
✗ feature/agent-A-kb branch
✗ feature/agent-B-kb branch
→ Merge conflicts, duplicación, pérdida de SSOT
```

**Pattern Correcto: Composición Declarativa**:

```yaml
# agents/agent_A/agent.yaml
knowledge_base_interaction_and_governance_rules:
  usage_policy_and_source_management:
    source_files:
      - "knowledge/domains/gore_nuble/kb_gn_029_circular-33-general_sts.md"
```

```yaml
# agents/agent_B/agent.yaml
knowledge_base_interaction_and_governance_rules:
  usage_policy_and_source_management:
    source_files:
      - "knowledge/domains/gore_nuble/kb_gn_035_circular-33-especifica_sts.md"
```

**Resultado**: Git versiona ARCHIVOS, no CONFIGURACIONES

### 4.6 Conventional Commits para KB

```
kb(scope): subject

Ejemplos:
kb(gn_001): update regional context with 2024 census data
kb(core_002): fix typo in ALM Phase 3 description
```

---

## §5. METODOLOGÍA DE APLICACIÓN

### 5.1 STS: Ciclo Iterativo (4 fases)

**Fase 1: Arquitectura**

1. Analizar "meat" del source
2. Diseñar jerarquía de secciones
3. Asignar IDs únicos

**Fase 2: Población de Meat**

1. Eliminar "fat"
2. Convertir a `Keyword: EssentialData`
3. Preservar tablas/listas

**Fase 3: Sistema Nervioso**

1. Conectar nodos con `Ref:`
2. Principio SSOT

**Fase 4: Audit de Compliance**

- [ ] Metadata + LLM instructions completos
- [ ] IDs únicos y compliant
- [ ] Refs apuntan a IDs internos válidos
- [ ] Lexicon canónico usado correctamente
- [ ] Fidelidad absoluta (no summarization)
- [ ] Zero duplicación (Ref: usado)
- [ ] Invariancia lenguaje (EssentialData original)

### 5.2 SFD: Ciclo Especializado (5 fases)

**Fase 1: Deconstrucción** → Inventariar secciones/campos del form

**Fase 2: Transcripción** → Cada elemento → bloque Form-Field con lexicon SFD

**Fase 3: Ensamblaje** → Agrupar bajo Form-Section headers, IDs únicos

**Fase 4: Conexión** → Codificar dependencias con `Field-Logic:`

**Fase 5: Audit** → Checklist STS (hereda compliance)

### 5.3 KHM: Flujo Operacional

```
Source Material (PDF/docx/txt)
    ↓
[Staging] Apply STS/SFD refactoring
    ↓
[Audit] 100% compliance check
    ↓
[Publish] Final naming + move to /knowledge/ + KB sync
    ↓
[Register] Update catalog_master_sts.md
    ↓
[Maintain] Periodic updates via mini-cycle
```

---

## §6. ANTI-PATRONES CRÍTICOS

**AP1: Summarization**

```
✗ "Resumir el documento original"
✓ "Refactorizar formato preservando 100% información"
```

**AP2: Keywords Secuenciales**

```
✗ Req-1:, Req-2:, Act-A:, Act-B:
✓ Lista Markdown con mismo keyword:
  - Req: ...
  - Req: ...
```

**AP3: Ref: Externos**

```
✗ Ref: EXTERNAL-DOC-ID (apunta fuera del artefacto)
✓ Ctx: Basado en EXTERNAL-DOC (solo contextual)
```

**AP4: Git Branches para Configs**

```
✗ feature/agent-X-kb branch
✓ Composición en agent.yaml (source_files list)
```

**AP5: Stylistic Markdown en STS**

```
✗ **negrita**, *italics*
✓ Keywords explícitos: Warn:, Req:
```

---

## §7. INTEGRACIÓN CON ORKO

### Mapeo a Layers

**Layer 2 (Tejidos)**: TF4 (Knowledge Fabric)

- STS/SFD/KHM operacionalizan completamente TF4
- Curation pipeline desde source → staging → knowledge
- RAG optimizado (density principle)

**Layer 3 (Metodología)**: Playbooks de curation

- Fase específica: Knowledge Asset Management
- Integrada en ciclo ALM (ver 10_ingenieria_agentes_conversacionales.md)

**Layer 4 (Plataforma)**: CI/CD para KB

- Linters STS compliance
- Automated catalog updates
- KB sync protocols

### Contratos Canónicos (from SIGMA)

**ContratoDeConocimiento** (extendido con STS/SFD/KHM):

```yaml
type: knowledge_contract
collection: normativa_interna
authority: official_only
format: STS | SFD-embedded
doc_units: [expediente, documento, seccion, articulo]
metadata_min: [id_doc, tipo, emisor, fecha, vigencia, hash, acl]
naming_convention: {tipo}_{dominio}_{id}_{desc}_{formato}.md
lifecycle: [sourcing, staging, audit, publish, register, maintain]
indexing: {lexical: bm25, vector: embeddings, filters}
serving: {context_assembly, citation_policy: required_exact}
audit: {compliance_checklist: STS-PHASE4, snapshots: true}
```

---

## §8. TEOREMAS Y COROLARIOS

**Teorema de Fidelidad**:

```
∀s ∈ Sources, ∀a ∈ Artifacts:
  a = STS_Refactor(s) ⇒ Information(a) = Information(s)
```

**Teorema de Densidad**:

```
∀chunk ∈ RAG_Retrieval:
  Relevance(chunk) ∝ Density(chunk) × Self_Containment(chunk)
```

STS maximiza ambos factores.

**Teorema de Composición (KHM)**:

```
∀agent: KB(agent) = ⋃ {artifact_i ∈ source_files}
No branching required; composition = declarative list
```

**Corolario de Governance**:

```
Git versiona ARCHIVOS individuales (knowledge/*.md)
Agent configs componen SETS de archivos (agent.yaml)
→ Zero merge conflicts, SSOT preserved
```

---

## §9. MÉTRICAS DE CALIDAD

**M1. Fidelity Score**

```
Fidelity = |Information(curated)| / |Information(source)|
Target: 1.0 (100%)
```

**M2. Density Ratio**

```
Density = Meat_tokens / (Meat_tokens + Fat_tokens)
Target: > 0.9
```

**M3. Compliance Rate**

```
Compliance = Passed_checks / Total_checks (STS Phase 4)
Target: 1.0 (100% pass)
```

**M4. Reference Integrity**

```
Integrity = Valid_Refs / Total_Refs
Target: 1.0 (all Ref: point to valid internal IDs)
```

**M5. Catalog Coverage**

```
Coverage = Cataloged_artifacts / Published_artifacts
Target: 1.0 (every artifact has catalog entry)
```

---

## §10. HERRAMIENTAS Y AUTOMATIZACIÓN

### Linters y Validators

**STS Compliance Linter**:

- Check metadata completeness
- Validate ID format
- Verify Ref: integrity
- Detect sequenced keywords (AP2)
- Measure density ratio

**SFD Validator**:

- Check Field-Type vocabulary
- Validate Field-Constraint syntax
- Verify Field-Logic references

**KHM Naming Validator**:

- Regex: `^(kb|guide)_(core|[a-z]{2})_\d{3}_[a-z0-9-]{2,}_(sts|sfd)\.md$`
- Check domain exists in `/knowledge/domains/`

### CI/CD Pipeline

```yaml
on: [push, pull_request]
jobs:
  validate-knowledge:
    steps:
      - STS compliance check (all .md in /knowledge/)
      - Naming convention check
      - Catalog sync verification
      - Ref: integrity test
      - Density measurement (report only)
```

---

**Aplicación en ORKO**: Este marco operacionaliza completamente TF4 (Knowledge Fabric) del Layer 2, proveyendo los estándares, metodologías y governance para gestionar conocimiento como activo de software de alto valor, optimizado para RAG y consumo por agentes IA.
