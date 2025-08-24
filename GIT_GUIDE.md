# Git Guide for Python Learning Environment

This repository uses git for version control to track your learning progress across different Python topics.

## Initial Setup

Repository is already initialized with:
- ✅ `.gitignore` - Excludes virtual environments, cache files, etc.
- ✅ `.gitconfig` - Local git settings for this project

## Basic Git Workflow

### 1. Check Status
```bash
git status
```
Shows what files have changed.

### 2. Stage Changes
```bash
# Stage all changes
git add .

# Stage specific files
git add topics/fizzbuzz/main.py
```

### 3. Commit Changes
```bash
git commit -m "Add fizzbuzz implementation"
```

### 4. View History
```bash
git log --oneline
```

## Recommended Workflow for Learning

### When Starting a New Topic:
```bash
# Create and switch to a new branch
git checkout -b topic/new-topic-name

# Initialize the topic using uv
cd topics/
uv init --app new-topic-name --vcs none
cd new-topic-name/
uv add --dev pytest
uv sync

# Work on your code...
# When ready to save progress:
git add .
git commit -m "Initial implementation of new-topic-name"
```

### When Completing a Topic:
```bash
# Switch back to main branch
git checkout main

# Merge your topic branch
git merge topic/new-topic-name

# Optional: Delete the topic branch
git branch -d topic/new-topic-name
```

### Save Progress Regularly:
```bash
# Quick save of current work
git add .
git commit -m "WIP: working on algorithm optimization"
```

## Useful Git Commands

| Command | Description |
|---------|-------------|
| `git status` | Show current state |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Commit with message |
| `git log --oneline` | Show commit history |
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes |
| `git checkout <branch>` | Switch branches |
| `git branch` | List all branches |
| `git branch <name>` | Create new branch |

## Branch Strategy

- **`main`**: Stable, completed topics
- **`topic/<name>`**: Work-in-progress branches for each topic
- **`experiment/<name>`**: For trying different approaches

## Example Learning Session

```bash
# Start learning recursion
git checkout -b topic/recursion

# Initialize the topic with uv
cd topics/
uv init --app recursion --vcs none
cd recursion/
uv add --dev pytest
uv sync

# Code, test, repeat...
# Save progress frequently
git add .
git commit -m "Add basic recursive factorial"

# Continue working...
git add .
git commit -m "Add recursive fibonacci with memoization"

# When satisfied with the topic
git checkout main
git merge topic/recursion
git branch -d topic/recursion
```

## Tips

1. **Commit often** - Small, frequent commits are better than large ones
2. **Use descriptive messages** - "Add bubble sort algorithm" vs "update code"
3. **One topic per branch** - Keep different learning topics separate
4. **Review your progress** - Use `git log` to see your learning journey

## Troubleshooting

### Undo last commit (keep changes):
```bash
git reset --soft HEAD~1
```

### Discard all uncommitted changes:
```bash
git reset --hard HEAD
```

### Switch branches with uncommitted changes:
```bash
git stash
git checkout <branch>
git stash pop
```
