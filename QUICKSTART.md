# Quick Setup Guide

## 1. Install Prerequisites
```powershell
# Install uv (Python package manager)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Install git (if not already installed)
winget install Git.Git
```

## 2. Try the example
```powershell
cd topics\fizzbuzz
uv sync
uv run python main.py
uv run pytest
```

## 3. Check git setup
```powershell
git status
git log --oneline
```

## 4. Create new topics
1. Copy `pyproject.toml.template` to `topics\new-topic\pyproject.toml`
2. Update project name in `pyproject.toml`
3. Add your Python files
4. Run `uv sync` to set up the environment
5. Use git to track your progress:
   ```powershell
   git add .
   git commit -m "Add new-topic implementation"
   ```

## 📚 More Help
- **Complete setup**: See `README.md`
- **Git workflow**: See `GIT_GUIDE.md`

That's it! Each topic has its own isolated Python environment and git tracks your learning progress.
