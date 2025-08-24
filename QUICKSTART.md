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
uv sync                    # Creates .venv/ and installs dependencies
uv run python main.py     # Runs in fizzbuzz's virtual environment
uv run pytest             # Runs tests in fizzbuzz's virtual environment
```

## 3. Understanding Virtual Environments
Each topic gets its own `.venv/` directory:
- ✅ **Isolated**: fizzbuzz and algorithms have separate Python environments
- ✅ **Automatic**: `uv run` always uses the correct environment
- ✅ **Clean**: No global package conflicts

```powershell
# Check what's installed in current topic
uv pip list

# Manually activate environment (optional)
uv shell
python main.py    # Now using topic's environment
exit              # Deactivate
```

## 3. Check git setup
```powershell
git status
git log --oneline
```

## 4. Create new topics

### Easy way with `uv init`:
```powershell
cd topics
uv init --app new-topic --vcs none    # Creates project structure
cd new-topic
uv add --dev pytest                   # Add testing to THIS topic only
uv sync                               # Create .venv/ for THIS topic
```

### Manual way:
1. Copy `pyproject.toml.template` to `topics\new-topic\pyproject.toml`
2. Update project name in `pyproject.toml`
3. Add your Python files
4. Run `uv sync` to create `.venv/` for this topic

### Each topic is independent:
```powershell
cd topics\data-science
uv add pandas numpy matplotlib    # Only added to data-science topic

cd ..\algorithms  
uv pip list                      # Won't show pandas/numpy/matplotlib
```

### Track progress:
```powershell
git add .
git commit -m "Add new-topic implementation"
```

## 📚 More Help
- **Complete setup**: See `README.md`
- **Git workflow**: See `GIT_GUIDE.md`

That's it! Each topic has its own isolated Python environment and git tracks your learning progress.
