---
allowed-tools: Bash(git tag:*), Bash(git show:*)
description: Display recent iteration git tags with summaries. Use this to see what work has been completed recently.
argument-hint: [number_of_tags]
---

# Display Recent Iteration Tags

This command shows recent iteration tags with their commit messages and dates.

## Execution

```bash
# Get number of tags to display (default: 5)
NUM_TAGS=${1:-5}

echo "=== Recent $NUM_TAGS Iterations ==="
echo ""

# Get recent tags matching iter-* pattern, sorted by date
git tag -l "iter-*" --sort=-creatordate | head -n $NUM_TAGS | while read tag; do
    # Get tag annotation message
    TAG_MSG=$(git tag -l --format='%(contents)' "$tag")
    # Get tag date
    TAG_DATE=$(git log -1 --format=%ai "$tag" | cut -d' ' -f1)
    # Get files in iteration directory from that tag
    ITER_DIR="iterations/${tag}*"

    echo "   $tag ($TAG_DATE)"
    echo "   $TAG_MSG"

    # Try to show retrospective summary (first 3 lines)
    RETRO=$(git show "$tag:iterations/${tag}-"*/retrospective.md 2>/dev/null | head -n 5 | tail -n 3)
    if [ -n "$RETRO" ]; then
        echo "   Summary: $RETRO" | head -c 200
        echo "..."
    fi
    echo ""
done

echo ""
echo "   To see full details: /show-iteration <tag-name>"
echo "   To search iterations: /search-iterations <keyword>"
```

## Usage Examples

```bash
# Show last 5 iterations (default)
/display-recent-tags

# Show last 10 iterations
/display-recent-tags 10

# Show all iterations
/display-recent-tags 1000
```

## Output Format

```
=== Recent 5 Iterations ===

   iter-data-validation (2025-10-18)
   Input validation feature complete - 95% coverage

   iter-performance-opt (2025-10-15)
   Performance optimization - 2.5x speedup achieved

   iter-type-system (2025-10-12)
   Type system refactor using traits
```
