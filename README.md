# Python Learning Environment

A structured environment for learning Python topics, each with isolated virtual environments using `uv` and version control with `git`.

## Prerequisites

**Install `uv` (Python package manager):**
```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or via pip
pip install uv
```

**Install `git` (if not already installed):**
- Download from [git-scm.com](https://git-scm.com/)
- Or via package manager: `winget install Git.Git`

## Quick Start

1. Navigate to any topic directory (e.g., `topics/fizzbuzz`)
2. Run `uv sync` to create virtual environment and install dependencies
3. Run `uv run python main.py` to execute the code
4. Run `uv run pytest` to run tests (if available)

## Virtual Environment Management

Each topic has its own isolated virtual environment in `.venv/`:

```
topics/
├── fizzbuzz/
│   ├── .venv/          # Isolated Python environment for fizzbuzz
│   ├── pyproject.toml
│   └── main.py
├── algorithms/
│   ├── .venv/          # Separate environment for algorithms
│   ├── pyproject.toml
│   └── main.py
```

### Working with Virtual Environments

**Automatic (Recommended):**
```bash
cd topics/your-topic/
uv run python script.py    # Runs in topic's .venv automatically
uv run pytest            # Runs tests in topic's .venv
```

**Manual Activation:**
```bash
cd topics/your-topic/
uv shell                 # Activate the virtual environment
python script.py         # Now using topic's Python/packages
exit                     # Deactivate (or just close terminal)
```

**Environment Status:**
```bash
uv sync                  # Create/update .venv based on pyproject.toml
uv pip list             # Show installed packages in current topic
uv tree                 # Show dependency tree
```

## Structure

```
topics/
├── fizzbuzz/           # Example: FizzBuzz problem
│   ├── pyproject.toml  # Project config & dependencies
│   ├── main.py         # Main implementation
│   └── README.md       # Topic-specific instructions
└── [new-topic]/        # Add more topics here
```

## Adding New Topics

### Option 1: Use `uv init` (Recommended)
```bash
cd topics/
uv init --app new-topic --vcs none
cd new-topic/
uv add --dev pytest  # Add testing support
```

### Option 2: Manual Setup
1. Create a new directory under `topics/`
2. Copy `pyproject.toml` template from existing topic
3. Update the project name in `pyproject.toml`
4. Add your Python files and README

### Track with Git
```bash
git add .
git commit -m "Add new-topic implementation"
```

## Documentation

- 📖 **`README.md`** - This file (main guide)
- 🚀 **`QUICKSTART.md`** - Quick setup instructions  
- 📋 **`GIT_GUIDE.md`** - Complete git workflow guide
- 🔧 **`UV_INIT_GUIDE.md`** - Why we use `uv init --vcs none`
- 🐍 **`VENV_GUIDE.md`** - Virtual environment management explained

## Commands Cheat Sheet

### uv (Python Environment)
- `uv sync` - Create/update virtual environment
- `uv add <package>` - Add dependency to current topic
- `uv remove <package>` - Remove dependency from current topic
- `uv run <command>` - Run command in virtual environment
- `uv shell` - Activate virtual environment shell
- `uv pip list` - Show installed packages in current topic
- `uv tree` - Show dependency tree for current topic

### Git (Version Control)
- `git add .` - Stage all changes
- `git commit -m "message"` - Commit changes
- `git status` - Check repository status
- `git log --oneline` - View commit history
- `git branch <name>` - Create new branch
- `git checkout <branch>` - Switch branch
