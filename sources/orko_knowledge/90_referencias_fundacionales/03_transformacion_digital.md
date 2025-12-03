# Marco de Transformación Digital

**ID**: ORKO-REF-TD-01  
**Fuentes**: Kelly Unified Framework, Alter DTPM  

---

## §1. INVARIANTES FUNDAMENTALES (Kelly)

### Los 8 Invariantes que Atraviesan Todos los Dominios

1. **Team-Centricity**: Equipo = unidad fundamental de producción
2. **Value-Driven**: Beneficio negocio como único criterio
3. **Flow Optimization**: Flujo continuo > grandes lotes
4. **Quality = Speed**: Calidad alta reduce tiempo y costo
5. **Emergence > Planning**: Estrategia emergente > plan rígido
6. **Devolved Authority**: Autoridad al equipo, accountability por valor
7. **Small Batches**: Deseconomías de escala favorecen lo pequeño
8. **Purpose Over Profit**: Propósito superior como motor sostenible

---

## §2. MODELO ORGANIZACIONAL

### Software as Asset (SaaA)

**Principio**: Software = activo que genera valor, NO costo a minimizar

**Decay Management**:

```
Software sin inversión continua → decay inevitable
Respuesta: Funding continuo basado en valor histórico
```

### Equipos Estables y Amoeba Lifecycle

```
MVT (2-3) → Growth → Steady (7±2) → Split (>12) → 2 New Teams
                                  ↓
                              Shrink/Merge (si decline)
```

**Benefits**:

- Data para forecasting (velocity estable)
- Incentivo a optimizar (cosecha beneficios)
- Camaraderie y knowledge retention
- Ownership y pride

### Continuous Governance

**Modelo VC/Real Options**:

- Portfolio equipos-como-startups
- Funding en tranches condicionales
- Gobernanza retrospectiva: ¿Qué HA SIDO entregado?
- Opciones: Continue | Increase | Reduce | Close

**Budgeting**: `Budget = Team Burn Rate × Período`

---

## §3. SISTEMA DE DIRECCIÓN (OKRs)

### Purpose Hierarchy

```
Organization Purpose (BHAG/MTP)
    ↓
Team Purpose
    ↓
Quarterly OKRs (hypothesis)
    ↓
Sprint Work
```

### OKR Mechanics

**Structure**:

- **Objective**: Outcome valioso (no output)
- **Key Results**: 3-4 tests medibles
- **Cadence**: Quarterly (12 semanas)

**Nature**: Test-driven management (acceptance criteria del quarter)

**Ground Rules**:

- Team-set (bottom-up)
- Limited number (3-4 max)
- Prioritized (orden absoluto)
- NOT money (purpose beyond profit)
- Avoid planning by OKR (outcomes, not actions)

### OKR-Driven Execution

**Planning Integration**:

```
Long-term: Strategy/Roadmap
Mid-term (OKRs): Planning glue ⭐
Short-term: Sprint planning
```

**Backlog Relationship** (Option B preferred):

- OKRs first → throw away backlog
- Cada sprint: "¿Cómo avanzar OKRs?" (blank sheet)
- Backlog = ideas, not commitments

---

## §4. CAPTURA DE VALOR (User Stories)

### Story Essence

**Format**: `As a <role> I want <capability> So that <benefit>`

**Core Attributes**:

- Lightweight (bajo costo upfront)
- Easy to comprehend
- Easy to share (rompe barrera técnico/negocio)

**Nature**:

- Placeholder for conversation (NOT requirement completo)
- Token for work (prioritize, split, refine)
- Transitory by design

### Golden Rules

**Rule 1: Beneficial** - Business value statement required

**Rule 2: Small** - Target: <2 semanas (<10 workdays)

**Tension**: Benefit → larger; Small → smaller

### Value Techniques

**Estimation over Analysis**: Shark Tank, planning poker

**Value Before Effort**: Secuencia correcta evita anchoring bias

**Cost of Delay**: Time-value profiles, priorizar alto CoD

**ROI Maximization**: Early releases → earlier benefit → higher ROI

---

## §5. MÉTODO OPERACIONAL (Xanpan)

### Core Principles

**P1: Iterations** - 2 semanas default, 1 común

**P2: Flow to Team** - Team estable, work fluye A equipo

**P3: Quality is Free** - Dial quality UP para ir fast

**P4: Visualize** - Boards, burn-down, CFD

### Board Mechanics

```
Pending → Current (WIP) → Completed
```

**Card Colors**:

- Blue: Development stories (business value)
- White: Tasks (technical work)
- Red: Bugs
- Yellow: Unplanned work
- Green: Process improvement

### Xanpan Deviations from Scrum

1. **Carry-over allowed** (mejora flow)
2. **No commitment** (probabilistic delivery)
3. **Unplanned work** (yellow cards aceptados)

### Planning Meeting

**Players**: PO (prepared), Creators, Facilitator

**Process**:

1. PO presenta prioritized blues
2. Team breaks down to white tasks
3. Planning poker estimates
4. Track against velocity
5. Repeat hasta capacidad

**Velocity**: Rolling average last 4-5 sprints, team-specific currency

---

## §6. INTEGRACIÓN VERTICAL

### From Strategy to Code

```
Organization Purpose & Strategy
    ↓ Strategic Intent
Team Purpose
    ↓ Quarterly Hypothesis
OKRs
    ↓ Story Machine
User Stories (Epic → Story → Task)
    ↓ Specifications
Acceptance Criteria → Tests
    ↓ TDD
Code + Automated Tests
    ↓ CI/CD
Working Software
    ↓ Governance Review
Value Delivered → Feedback Loop
```

### Feedback Loops

**Strategic** (Quarterly): OKR review, governance review

**Tactical** (Sprint): Retrospective, demo, tests

**Operational** (Daily): Stand-up, CI build, pair programming

---

## §7. TRANSFORMACIÓN DIGITAL (Alter DTPM)

### Definiciones

**Digital Transformation**:

```
DT = enterprise-level transformation donde
     IT-related changes → strategically significant changes
     en mission-critical WSs
```

**DT Initiative**: Initiation/oversight/management de proyectos DT desde inception hasta completion

### DT Phases (5-phase WSLC variation)

1. **Impetus**: Reconocimiento de challenges
2. **Transformational Vision**: Management vision para outcomes
3. **Resource Acquisition**: Crear/obtener recursos necesarios
4. **Implementation**: Cambios WS para lograr vision
5. **Operation & Maintenance**: Operar/soportar WSs transformados

### Recursos para el Cambio (5 categorías)

**Momentum (tangible)**:

```
Estado actual WS + proyectos ongoing
Alineación con schedule y vision
```

**Capabilities (tangible)**:

```
SW development/implementation
Financial capabilities
Trustworthy leadership/org change
```

**Forces (WS-wide)**:

```
Cohesive, Innovative (aligned)
Disruptive (entropy-like), Inertial
Forces-at-distance (economics, regulation, tech change)
```

**Drivers & Impediments (WS elements)**:

```
Factores por elemento (customers, products, processes,
participants, information, technologies, environment,
infrastructure, strategies)
```

**Catalysts (micro-dynamics)**:

```
Needing: Necesidad percibida para goals
Understanding: Comprensión de benefits
Liking: Preferencia afectiva
```

### Resource Favorability

```
Favorability = likelihood recursos contribuyan positiva/negativamente
Escala: extremely unfavorable ← → extremely favorable
```

### DTPM Model Statement

```
Favorability(5 categorías) → jointly contribute to:
  - Degree of Completion
  - Business Success

Estados/favorability varían over time debido a:
  - DT project adjustments
  - WS changes
  - Environmental shifts
```

---

## §8. PROHIBICIONES EXPLÍCITAS

1. NO proyectos en orgs digitales (equipos continuos SÍ)
2. NO commitment en sprints (probabilidad SÍ)
3. NO cascading OKRs top-down
4. NO OKRs vinculados a bonus
5. NO estimates en horas (puntos abstractos SÍ)
6. NO "casi done" (binario: done o not-done)
7. NO detailed upfront planning
8. NO disbanding teams post-"proyecto"
9. NO separation planean vs ejecutan
10. NO gold-plating bajo excusa calidad

---

## §9. PRINCIPIOS DE COHERENCIA

**PC1: Fractal Consistency** - Pattern se repite en todas escalas

**PC2: Flow Optimization** - Decisión unificadora: ¿Mejora o degrada flujo?

**PC3: Value Maximization** - Criterio único: ¿Maximiza valor entregado?

**PC4: Quality Enables Speed** - High quality = High speed

**PC5: Purpose Over Prescription** - Team ownership de proceso

---

**Aplicación en ORKO**: Fundamenta Layer 3 (Metodología) con playbooks operacionales y ciclos de entrega. Integra con Layer 1 (contratos) y Layer 2 (tejidos).
