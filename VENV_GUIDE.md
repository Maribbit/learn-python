# Virtual Environment Management Guide

This guide explains how virtual environments work in your Python learning setup.

## What Are Virtual Environments?

Virtual environments are isolated Python installations that keep dependencies separate between projects. Each topic in your learning environment has its own `.venv/` directory.

## Directory Structure

```
learn-python/
├── topics/
│   ├── fizzbuzz/
│   │   ├── .venv/              # Python 3.12 + pytest
│   │   ├── pyproject.toml
│   │   └── main.py
│   ├── data-science/
│   │   ├── .venv/              # Python 3.12 + pandas + numpy + matplotlib
│   │   ├── pyproject.toml
│   │   └── analysis.py
│   └── web-scraping/
│       ├── .venv/              # Python 3.12 + requests + beautifulsoup4
│       ├── pyproject.toml
│       └── scraper.py
```

## Key Benefits

### ✅ **Isolation**
- Each topic has completely separate packages
- No version conflicts between topics
- Clean, predictable environments

### ✅ **Reproducible**
- `pyproject.toml` and `uv.lock` ensure same versions everywhere
- Easy to share exact environment with others

### ✅ **Automatic**
- `uv run` automatically uses the correct environment
- No manual activation needed for most tasks

## Working with Virtual Environments

### Automatic Usage (Recommended)

```bash
cd topics/any-topic/
uv run python script.py       # ✅ Uses topic's .venv automatically
uv run pytest                 # ✅ Uses topic's .venv automatically
uv run pip list               # ✅ Shows topic's packages
```

### Manual Activation (When Needed)

```bash
cd topics/any-topic/

# Windows PowerShell
.venv\Scripts\Activate.ps1

# Linux/Mac
source .venv/bin/activate

# Now you're "inside" the virtual environment
python script.py              # Uses topic's Python
pip list                      # Shows topic's packages
which python                  # Shows path to topic's Python

deactivate                    # Deactivate (return to system)
```

### Environment Management

```bash
# Create/update virtual environment
uv sync

# Add packages to current topic only
uv add requests beautifulsoup4

# Add development dependencies
uv add --dev pytest black mypy

# Remove packages
uv remove requests

# List installed packages
uv pip list

# Show dependency tree
uv tree

# Check environment info
uv python info
```

## Common Workflows

### Starting a New Topic
```bash
cd topics/
uv init --app machine-learning --vcs none
cd machine-learning/

# Add ML-specific packages
uv add scikit-learn pandas numpy matplotlib
uv add --dev pytest jupyter

# Environment is ready!
uv run python train_model.py
```

### Working on Data Science
```bash
cd topics/data-science/
uv add pandas numpy matplotlib seaborn jupyter
uv sync

# Start Jupyter in this environment
uv run jupyter notebook

# Run analysis scripts
uv run python analyze_data.py
```

### Working on Web Development
```bash
cd topics/web-dev/
uv add flask requests jinja2
uv add --dev pytest black

# Run Flask app
uv run python app.py

# Run tests
uv run pytest
```

### Switching Between Topics
```bash
cd topics/fizzbuzz/
uv pip list                    # Shows: pytest

cd ../data-science/
uv pip list                    # Shows: pandas, numpy, matplotlib, etc.

cd ../algorithms/
uv pip list                    # Shows: different packages
```

## Troubleshooting

### Environment Not Working?
```bash
# Recreate the virtual environment
rm -rf .venv/
uv sync
```

### Package Version Conflicts?
```bash
# Check what's installed
uv pip list

# Update dependencies
uv sync

# Check dependency tree for conflicts
uv tree
```

### Python Version Issues?
```bash
# Check Python version in current environment
uv run python --version

# Check available Python versions
uv python list

# Use specific Python version (creates new .python-version)
uv python pin 3.11
uv sync
```

### Want to Share Environment?
```bash
# Everything needed is in these files:
# - pyproject.toml (dependencies)
# - uv.lock (exact versions)
# - .python-version (Python version)

# Someone else can recreate exactly:
git clone your-repo
cd topics/some-topic/
uv sync    # Recreates identical .venv/
```

## Best Practices

### ✅ **Do:**
- Use `uv run` for most commands
- Add packages with `uv add` (not `pip install`)
- Commit `pyproject.toml` and `uv.lock` to git
- Use topic-specific dependencies

### ❌ **Don't:**
- Install packages globally with pip
- Manually mess with `.venv/` contents
- Copy `.venv/` directories between machines
- Mix pip and uv in same environment

## Environment Status Check

Quick health check for any topic:

```bash
cd topics/your-topic/

# 1. Check if environment exists
ls .venv/                     # Should show Python installation

# 2. Check Python version
uv run python --version      # Should show expected version

# 3. Check installed packages
uv pip list                   # Should show your dependencies

# 4. Check for issues
uv sync                       # Should complete without errors

# 5. Test basic functionality
uv run python -c "import sys; print(sys.executable)"
```

This setup ensures each topic has exactly the packages it needs, nothing more, nothing less!
