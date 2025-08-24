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

1. Create a new directory under `topics/`
2. Copy `pyproject.toml` template from existing topic
3. Update the project name in `pyproject.toml`
4. Add your Python files and README
5. Use git to track your progress (see `GIT_GUIDE.md`)

## Documentation

- 📖 **`README.md`** - This file (main guide)
- 🚀 **`QUICKSTART.md`** - Quick setup instructions
- 📋 **`GIT_GUIDE.md`** - Complete git workflow guide

## Commands Cheat Sheet

### uv (Python Environment)
- `uv sync` - Create/update virtual environment
- `uv add <package>` - Add dependency
- `uv run <command>` - Run command in virtual environment
- `uv shell` - Activate virtual environment shell

### Git (Version Control)
- `git add .` - Stage all changes
- `git commit -m "message"` - Commit changes
- `git status` - Check repository status
- `git log --oneline` - View commit history
- `git branch <name>` - Create new branch
- `git checkout <branch>` - Switch branch
