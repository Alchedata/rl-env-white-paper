# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

An arXiv white paper on **"The Environment Layer: Building Infrastructure for Agentic AI Training"** by Fei Wang, Eric Wang, and Salon Ren (Alchedata AI). The paper surveys RL environments for agentic AI, covering POMDP theory, environment frameworks, synthetic data generation, credit assignment algorithms, and the sim-to-real gap.

## Build Commands

Compile the PDF (run twice for correct TOC/references):
```bash
cd /Users/fei/.openclaw/workspace/rl-paper
pdflatex main.tex && pdflatex main.tex
```

For bibliography:
```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Or using latexmk (preferred if available):
```bash
latexmk -pdf main.tex
```

## Document Structure

```
main.tex             # Entry point: preamble, title, abstract, TOC, \input{content_fixed}
content_fixed.tex    # All section content (the main body to edit)
content_backup.tex   # Backup of previous content version
references.bib       # Bibliography (natbib/plainnat style)
arxiv.sty            # arXiv style file
figures/             # PNG figures (fig1–fig9, named *_gemini.png for AI-generated ones)
sections/            # Markdown drafts of each section (01–11), used as reference/notes
```

**Editing rule**: body content lives in `content_fixed.tex`. `main.tex` is only touched for preamble, packages, or metadata changes.

## Key Paper Concepts

- **EQF (Environment Quality Framework)**: 3-axis evaluation: Fidelity, Diversity, Verifiability
- **CLASSic**: Production readiness framework: Cost, Latency, Accuracy, Security, Stability
- **CLEAR**: Cost-normalized accuracy (CNA) framework
- **ExpA**: Expanded Action Space — decouples language, routing, and environment actions
- **USI (User-Sim Index)**: Metric for sim-to-real gap (~76 for LLMs vs ~93 for humans)

## Current State / Active Work

- `rebuttal_plan.md` — reviewer feedback with 6 actionable directions; priority is **experiments (Option 1) + EQF quantification (Option 2)**
- Figures 1 and 9 use TikZ (in `content_fixed.tex`); others are PNG files in `figures/`
- The `sections/*.md` files are working notes / markdown drafts; they do not get compiled

## LaTeX Conventions

- Document class: `\documentclass{article}` with `arxiv.sty`
- Citations: `\citet{}` / `\citep{}` (natbib), bibliography style `plainnat`
- Figures: `\graphicspath{{figures/}}` — always reference files by name without path prefix
- Wide tables: wrap with `\resizebox{\textwidth}{!}{...}` if overflowing
- No `\section` prefixes in section titles (e.g., not "Section 4: Frameworks")
