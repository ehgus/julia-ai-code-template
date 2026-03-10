---
allowed-tools: Bash(git add:*), Bash(git commit:*), Bash(git tag:*), Bash(ls:*), Bash(cat:*), Bash(date:*)
description: Complete the current iteration by committing files, creating a git tag, and prompting for PROGRESS.md update. Use descriptive iteration names like 'iter-gpu-acceleration' or 'iter-data-validation'.
argument-hint: <iteration-name> <summary>
---

# Complete Iteration

Automates the iteration completion workflow: commit, tag, and prepare for PROGRESS.md update.

**Naming Convention:** Use descriptive names like `iter-gpu-acceleration`, `iter-error-handling`, not sequential numbers.

## Validation

```bash
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "   Error: Iteration name and summary required"
    echo ""
    echo "Usage: /complete-iteration <iteration-name> <summary>"
    echo ""
    echo "Examples:"
    echo "  /complete-iteration iter-gpu-acceleration 'GPU support complete'"
    echo "  /complete-iteration iter-data-validation 'Input validation with 95% coverage'"
    echo "  /complete-iteration iter-error-messages 'Improved user-facing errors'"
    echo ""
    echo "   Use descriptive names (iter-FEATURE) not numbers (iter-001)"
    exit 1
fi
```

## Execution

```bash
ITER_NAME="$1"
SUMMARY="$2"
ITER_DIR="iterations/${ITER_NAME}"

# Check if iteration directory exists
if [ ! -d "$ITER_DIR" ]; then
    echo "   Error: Iteration directory not found: $ITER_DIR"
    echo ""
    echo "Available iterations:"
    ls -d iterations/*/ 2>/dev/null | sed 's|iterations/||' | sed 's|/||'
    exit 1
fi

echo "=== Completing Iteration: $ITER_NAME ==="
echo ""

# Show what will be committed
echo "   Files to commit:"
ls -la "$ITER_DIR" | tail -n +4 | awk '{print "  " $9}'
echo ""

# Check if retrospective exists
if [ ! -f "$ITER_DIR/retrospective.md" ]; then
    echo "   Warning: No retrospective.md found"
    echo "   Consider creating one before completing the iteration"
    echo ""
    read -p "Continue anyway? (y/N): " confirm
    if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
        echo "Aborted."
        exit 1
    fi
fi

# Stage iteration directory
echo "   Staging files..."
git add "$ITER_DIR/"

# Commit
COMMIT_MSG="${ITER_NAME}: ${SUMMARY}

   Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

echo "   Creating commit..."
git commit -m "$COMMIT_MSG"

# Create tag
echo "    Creating tag..."
git tag -a "$ITER_NAME" -m "$SUMMARY"

echo ""
echo "   Iteration completed!"
echo ""
echo "   Tag: $ITER_NAME"
echo "   Summary: $SUMMARY"
echo ""

# Show reminder for PROGRESS.md
echo "=== Next Steps ==="
echo ""
echo "1. Update PROGRESS.md:"
echo "   - Add to 'Recently Completed' with date: $(date +%Y-%m-%d)"
echo "   - Add key outcomes/decisions to 'Key Decisions Log'"
echo "   - Update 'Current Iteration' section to next iteration"
echo ""
echo "2. Start next iteration:"
echo "   - Create new iteration directory from 'Next Iteration' backlog"
echo "   - Update PROGRESS.md 'Current Iteration' section"
echo "   - Create planning.md with specific tasks for this iteration"
echo ""
echo "3. Optional: Archive old iterations if workspace is cluttered"
echo "   - Keep last 3-10 iterations"
echo "   - Delete older ones: rm -rf iterations/iter-XXX/"
echo "   - They're preserved in git: git show $ITER_NAME:..."
echo ""

# Show retrospective summary if exists
if [ -f "$ITER_DIR/retrospective.md" ]; then
    echo "   Retrospective Summary:"
    head -n 10 "$ITER_DIR/retrospective.md" | sed 's/^/   /'
    echo ""
fi

echo "   View this iteration later: /show-iteration $ITER_NAME"
echo "   View recent work: /display-recent-tags"
```

## Usage Examples

```bash
# Complete GPU acceleration iteration
/complete-iteration iter-gpu-acceleration "GPU support complete"

# Complete validation iteration
/complete-iteration iter-data-validation "Input validation with 95% coverage"

# Complete error handling iteration
/complete-iteration iter-error-messages "Improved user-facing error messages"
```

## Output Format

```
=== Completing Iteration: iter-gpu-acceleration ===

   Files to commit:
  planning.md
  test-failures.md
  implementation.md
  refactor-notes.md
  retrospective.md

   Staging files...
   Creating commit...
    Creating tag...

   Iteration completed!

   Tag: iter-gpu-acceleration
   Summary: GPU support complete

=== Next Steps ===

1. Update PROGRESS.md:
   - Add to 'Recently Completed' with date and outcomes
   - Add key decisions to 'Key Decisions Log'
   - Update 'Current Iteration' to next iteration
   ...
```
