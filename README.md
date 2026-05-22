# Reproducible Analysis: DVC + Marimo

A multi-stage DVC pipeline that processes a raw events dataset, plus a Marimo notebook for visualization.

## Setup

```bash
uv sync
dvc repro
```

## Pipeline Stages

| Stage | Input | Output | Description |
|-------|-------|--------|-------------|
| `clean` | `data/raw/events.csv` | `data/clean/events.csv` | Drop invalid rows, normalize timestamps |
| `transform` | `data/clean/events.csv` | `data/transformed/events.csv` | Add `date` column |
| `features` | `data/transformed/events.csv` | `data/features/events.csv` | Add `duration_minutes` and `weekday` |

## Notebook

```bash
uv run marimo run notebooks/report.py
```
