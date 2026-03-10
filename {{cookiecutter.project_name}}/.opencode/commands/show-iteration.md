---
allowed-tools: Bash(git show:*), Bash(git tag:*)
description: Show detailed information from a specific iteration by tag name. Displays planning, retrospective, and key files from an archived iteration.
argument-hint: <tag-name>
---

# Show Iteration Details

Display detailed information from an archived iteration.

## Validation

Check if tag name is provided:

```bash
if [ -z "$1" ]; then
    echo "   Error: Tag name required"
    echo ""
    echo "Usage: /show-iteration <tag-name>"
    echo ""
    echo "Example: /show-iteration iter-007"
    echo ""
    echo "   Use /display-recent-tags to see available tags"
    exit 1
fi
```

Check if tag exists:

```bash
if ! git tag -l "$1" | grep -q "$1"; then
    echo "   Error: Tag '$1' not found"
    echo ""
    echo "Available iteration tags:"
    git tag -l "iter-*" --sort=-creatordate | head -n 10
    exit 1
fi
```

## Execution

```bash
TAG=$1
echo "=== Iteration: $TAG ==="
echo ""

# Show tag annotation
echo "   Tag Message:"
git tag -l --format='%(contents)' "$TAG"
echo ""

# Show commit info
echo "   Date:"
git log -1 --format="%ai" "$TAG"
echo ""

# Try to find and show iteration directory contents
ITER_PATTERN="iterations/${TAG}"

# List files in iteration directory
echo "   Iteration Files:"
git ls-tree -r --name-only "$TAG" | grep "^iterations/${TAG}" | sed 's/^/  /'
echo ""

# Show retrospective if exists
echo "   Retrospective:"
RETRO_FILE=$(git ls-tree -r --name-only "$TAG" | grep "iterations/${TAG}.*retrospective.md" | head -n 1)
if [ -n "$RETRO_FILE" ]; then
    git show "$TAG:$RETRO_FILE"
else
    echo "  (No retrospective found)"
fi
echo ""

# Show planning if exists
echo "   Planning:"
PLAN_FILE=$(git ls-tree -r --name-only "$TAG" | grep "iterations/${TAG}.*planning.md" | head -n 1)
if [ -n "$PLAN_FILE" ]; then
    git show "$TAG:$PLAN_FILE" | head -n 30
    echo "  ..."
else
    echo "  (No planning found)"
fi
echo ""

echo "   To see specific file: git show $TAG:path/to/file"
echo "   To restore iteration: git checkout $TAG -- iterations/"
```

## Usage Examples

```bash
# View type system refactor iteration
/show-iteration iter-type-system

# View GPU acceleration iteration
/show-iteration iter-gpu-acceleration
```

## Output Format

```
=== Iteration: iter-type-system ===

   Tag Message:
Type system refactor using traits - cleaner API

   Date:
2025-10-12 14:23:45 +0900

   Iteration Files:
  iterations/iter-type-system/planning.md
  iterations/iter-type-system/retrospective.md
  ...

   Retrospective:
# Retrospective: Type System Refactor
...
```
