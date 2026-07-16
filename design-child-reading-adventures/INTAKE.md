# Design Child Reading Adventures Intake

## Skill Type

Complex Atomic Skill. It owns one stable outcome: turn grounded books into age-appropriate, child-led reading adventures at the depth requested by the user.

## Purpose

Help a parent, educator, or responsible adult transform supplied titles or text into reading ideas, a structured plan, or a coordinated plan and child-facing handbook without inventing book content or turning reading into adult-managed homework.

## Primary Users

- Parents and caregivers designing independent reading experiences.
- Educators creating optional, child-owned book activities.
- Designers producing printable or digital reading-adventure handbooks.

## Core Use Cases

1. Generate a small set of grounded reading-play ideas.
2. Design an adult-facing multi-book reading route and cadence.
3. Produce a coordinated reading plan and reusable child-facing adventure handbook.
4. Provide a provisional genre-level design when edition-specific evidence is unavailable.

## Not in Scope

- Teaching or grading through compulsory worksheets.
- Guaranteeing learning, intelligence, comprehension, or long-term outcomes.
- Reconstructing copyrighted books or using unauthorized copies.
- Inventing page, plot, chapter, character, quotation, or edition details.
- Requiring continuous adult questioning, scheduling, signatures, or performance monitoring.
- Replacing professional advice for developmental, accessibility, or safeguarding needs.

## Inputs

Use supplied context first and scale intake to the output mode.

- Always useful: age/grade, independent-reading level, preferred formats, and one or two desired effects.
- Required for individualized plans/full handbooks: identifying book material, available weeks/session length, and requested output format.
- Optional: interests, dislikes, preferred creation methods, sensitivities, accessibility needs, and topics to avoid.

## Outputs

Choose the smallest sufficient mode:

1. `ideas`: bounded activity ideas; no full route or handbook.
2. `plan`: adult-facing design brief, content basis, diagnosis, route, activities, independence audit, and adjustment rules.
3. `full`: the complete adult-facing plan plus a coordinated child-facing adventure handbook; when files are requested, deliver them as two separate artifacts unless the user explicitly asks for one combined file.

## Frequency / Reuse Value

Evidence gating, activity mechanics, agency checks, and handbook architecture repeat across different children, editions, genres, collections, and formats.

## Testability and Benchmarkability

Use fixed prompts for mode routing, intake, grounding, pagination, quota calculations, safety/privacy, and child agency. Score required criteria and automatic failures under `EVAL.md`.

## Decision

Create as a governed Atomic Skill candidate. Do not merge into a manager or MetaSkill.
