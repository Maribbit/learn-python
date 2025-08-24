# Quick Setup Guide

## 1. Install uv
```powershell
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## 2. Try the example
```powershell
cd topics\fizzbuzz
uv sync
uv run python main.py
uv run pytest
```

## 3. Create new topics
1. Copy `pyproject.toml.template` to `topics\new-topic\pyproject.toml`
2. Update project name in `pyproject.toml`
3. Add your Python files
4. Run `uv sync` to set up the environment

That's it! Each topic has its own isolated Python environment.
