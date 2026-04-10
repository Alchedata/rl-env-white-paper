# The Environment Layer: Building Infrastructure for Agentic AI Training

This repository contains the LaTeX source for an arXiv white paper by Fei Wang, Eric Wang, and Salon Ren at Alchedata AI.

The paper surveys the environment layer for agentic AI training, including POMDP framing, environment frameworks, synthetic environment generation, credit assignment algorithms, evaluation methodology, and the sim-to-real gap.

## Repository Layout

- `main.tex`: LaTeX entry point, preamble, title, abstract, and bibliography wiring.
- `content_fixed.tex`: Main paper body and the primary file to edit for content changes.
- `content_backup.tex`: Backup copy of the paper body.
- `references.bib`: Bibliography database.
- `figures/`: Paper figures and figure notes.
- `sections/`: Section-by-section Markdown drafts and working notes.
- `rebuttal_plan.md`: Reviewer feedback and revision plan.
- `CLAUDE.md`: Repository-specific working guidance.

## Build

Preferred:

```bash
latexmk -pdf main.tex
```

Manual LaTeX build:

```bash
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

If bibliography references need to be regenerated:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Editing Workflow

- Edit `content_fixed.tex` for body content changes.
- Only modify `main.tex` for preamble, metadata, package, or global document configuration changes.
- Use `figures/` assets by filename only because `\graphicspath{{figures/}}` is already configured.
- Treat `sections/*.md` as drafts and notes; they do not compile into the PDF.

## Core Concepts Covered

- `EQF`: Environment Quality Framework across fidelity, diversity, and verifiability.
- `CLASSic`: Production-readiness lens spanning cost, latency, accuracy, security, and stability.
- `CLEAR`: Cost-normalized evaluation framing.
- `ExpA`: Expanded action space for language, routing, and environment actions.
- `USI`: User-Sim Index for measuring sim-to-real quality.

## Output

The main compiled artifact is `main.pdf`.