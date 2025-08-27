# From-Proof-To-Measurement (Metrologia pre-submission package)

This repository contains:
- `paper.tex` — manuscript
- `IndisputableMonolith.lean` — Lean, sorry-free monolith with theorem hooks (T1–T8)
- `units.toml` — unit labels and optional anchor
- `display_calculator.py` — deterministic displays and pass/fail
- `versions.txt` — toolchain locks
- `Makefile` — deterministic PDF build

Build PDF:

    latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex

Compute displays and the pass/fail statistic:

    python3 display_calculator.py --units units.toml --print

