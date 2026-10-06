---
name: skill-generator-chips
description: Universal Meta-Generator & Systems Framework for creating, auditing, and optimizing production-ready SKILL.md files across multi-platform AI agent ecosystems (Claude Code, Codex CLI, Cursor, Copilot, OpenCode, Antigravity, Pi). Use this skill whenever requested to create a new AI skill, generate a domain SOP, or upgrade existing skill architecture.
version: 2.5.0
tags: [meta-framework, skill-architect, agentic-ai, chips-v2, sop-generator]
---

# Universal SKILL Template Generator (CHIPS-v2 Framework)

Systematic framework and operational meta-generator for engineering production-ready, deterministic, and modular `SKILL.md` instruction sets across multi-platform AI coding agent harnesses.

---

## 1. Architectural Principles & Quality Gates

Every generated `SKILL.md` must strictly adhere to four foundational engineering principles:

1. **Progressive Disclosure**: Keep the core `SKILL.md` body under the **8 KB hard cap** (Codex CLI limit). Offload exhaustive reference tables, deep domain schemas, or secondary code templates to `references/` subdirectories.
2. **Deterministic & Executable Logic**: Eliminate conversational filler, vague guidance, and ambiguous prompts. Use step-by-step SOPs, mathematical/logical formulas, and explicit decision trees (`IF ... THEN ... ELSE`).
3. **Multi-Platform Interoperability**: Standardize metadata using valid YAML Frontmatter (`name`, `description`, `version`, `tags`). Ensure syntax parity across Claude Code, Codex, Cursor (`.cursor/rules`), Copilot, OpenCode, Antigravity, and Pi.
4. **Trigger Precision**: Embed explicit semantic triggers, slash commands, and contextual keywords within `description` and prompt triggers to prevent false activations or missed invocations.

---

## 2. CHIPS-v2 Framework Anatomy

The **CHIPS-v2 Framework** divides every skill definition into 5 strict structural pillars:

| Pillar | Element | Operational Definition |
| :--- | :--- | :--- |
| **C** | **Context, Goal & Persona** | Defines the explicit identity, domain bounds, primary objective, and activation criteria. |
| **H** | **Handling Inputs & Sources** | Specifies input types (raw text, file uploads, parameters, URLs) and pre-processing rules. |
| **I** | **Instruction Steps (SOP)** | Sequential, numbered logic flow with branching rules, formulas, and execution heuristics. |
| **P** | **Presentation & Structure** | Strict schema for output formatting (table layouts, word limits, slide limits, structural tags). |
| **S** | **Special Constraints & Gates** | Negative constraints ("DO NOT"), safety rules, edge-case handling, and validation criteria. |

---

## 3. Step-by-Step Generation SOP

When tasked with generating or revising a `SKILL.md` file for ANY domain (technical, financial, operational, academic, creative), follow this sequence:

### Step 1: Requirements Triage & Domain Mapping
- Identify the target domain, target audience, and primary task type.
- Determine required inputs (e.g., CSV, PDF, source code, user query) and expected outputs.
- Select natural trigger phrases and slash command syntax (e.g., `/code-audit`, `/proposal-gen`).

### Step 2: Architecture & Sizing Check
- Calculate instruction scope. If the total context exceeds 8 KB:
  - Keep core execution SOPs in `SKILL.md`.
  - Delegate reference schemas to `references/details.md` or `templates/`.

### Step 3: Drafting the Metadata & Frontmatter
Write valid, clean YAML frontmatter:
```yaml
---
name: [kebab-case-name]
description: [1-2 sentences with explicit function, domain, and triggers]
version: 1.0.0
tags: [tag1, tag2, tag3]
---
```

### Step 4: Constructing Core Execution Flow
Build the `SKILL.md` sections using the mandatory output template below.

---

## 4. Mandatory SKILL.md Output Template

```markdown
---
name: [nama-skill-format-kebab-case]
description: [Penjelasan 1-2 kalimat ringkas mengenai tujuan, domain fungsi, dan kapan skill ini dipanggil. Sertakan kata kunci pemicu utama.]
version: 1.0.0
tags: [domain, kategori, kata-kunci]
---

# [Nama Skill Format Title Case]

[Deskripsi ringkas 1-2 paragraf tentang fungsi utama, cakupan domain, dan manfaat operasional skill ini.]

---

## Overview & Execution Context

- **Primary Persona**: [Deskripsi peran/ekspertise agen]
- **Target Harnesses**: Claude Code, Codex, Cursor, Copilot, OpenCode, Antigravity, Pi
- **Input Requirements**: [Tentukan input wajib/opsional, misal: file .csv, transcript, query]
- **Primary Triggers**: `/[nama-command]`, "[frase pemicu 1]", "[frase pemicu 2]"

---

## Core Framework & Operational Formulas

[Sertakan rumus, matriks keputusan, atau kerangka kerja konseptual yang digunakan.]

### Decision Tree / Logic Matrix
```
IF [Kondisi A] THEN
    -> Eksekusi Alur 1
ELSE IF [Kondisi B] THEN
    -> Eksekusi Alur 2
ELSE
    -> Panggil Pengecualian / Minta Klarifikasi
```

---

## Step-by-Step SOP (Execution Procedure)

### Step 1: Input Validation & Parsing
1. Verify presence of required inputs/files.
2. Check format compliance and flag missing variables.

### Step 2: Core Processing & Transformation
1. [Langkah eksekusi 1 dengan instruksi terukur]
2. [Langkah eksekusi 2 dengan aturan transformasi]
3. [Langkah eksekusi 3 dengan pengecekan kriteria]

### Step 3: Quality Check & Synthesis
1. Validate outputs against domain standards.
2. Apply mandatory formatting constraints.

---

## Presentation & Output Formatting

[Spesifikasikan format luaran secara kaku]

- **Header Structure**: [Jumlah dan nama header]
- **Table / List Constraints**: [Format tabel, kolom wajib, batas bullet points]
- **Tone & Style**: [Misal: Concise, Executive, Technical, Direct]

```markdown
# [Template Structure Output]
## Section 1: [Name]
- Bullet 1...
## Section 2: [Metrics/Table]
| Column 1 | Column 2 | Column 3 |
```

---

## Special Constraints & Quality Gates (DO NOTs)

- **DO NOT** use conversational filler ("Based on your input...", "Here is the result...").
- **DO NOT** hallucinate missing data — explicitly flag unstated parameters.
- **DO NOT** exceed specified length/formatting constraints.
- **ALWAYS** include [elemen wajib, misal: warning disclaimer / summary box].

---

## Sample Invocation & Usage

- `/[nama-command] [contoh input 1]`
- `/[nama-command] [contoh input dengan file lampiran]`
```

---

## 5. Multi-Platform Deployment Guide

| Harness | Deployment Path / Command | Special Notes |
| :--- | :--- | :--- |
| **Claude Code** | `/plugin install <repo>` or placement in `plugins/<plugin>/skills/` | Source of truth format |
| **Codex CLI** | `npx codex-marketplace add <repo>` | Strictly respects 8 KB limit |
| **Cursor** | `.cursor/rules/` or `.cursor-plugin/` | Uses rule triggers |
| **GitHub Copilot** | `.copilot/skills/` | Markdown skill discovery |
| **gh / npx skills** | `gh skill install <repo> <skill>` | Direct CLI installation |

---

## 6. Self-Audit & Quality Assurance Checklist

Before finalizing any generated `SKILL.md`, verify:
- [ ] Valid YAML frontmatter syntax (no unquoted special characters).
- [ ] Kebab-case naming convention used in `name`.
- [ ] Size < 8 KB for Codex compatibility.
- [ ] Zero ambiguous words ("sebaiknya", "mungkin", "kira-kira") in execution steps.
- [ ] Mandatory output template adhered to strictly.
- [ ] Decision trees handle missing or invalid inputs explicitly.
