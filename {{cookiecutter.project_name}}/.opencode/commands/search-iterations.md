---
allowed-tools: Bash(git tag:*), Bash(git grep:*), Bash(git show:*)
description: Search through iteration history for a keyword. Searches tag messages and iteration files across all archived iterations.
argument-hint: <keyword>
---

# Search Iterations

Search through iteration git history for specific keywords or topics.

## Validation

```bash
if [ -z "$1" ]; then
    echo "   Error: Search keyword required"
    echo ""
    echo "Usage: /search-iterations <keyword>"
    echo ""
    echo "Examples:"
    echo "  /search-iterations GPU"
    echo "  /search-iterations 'error handling'"
    echo "  /search-iterations performance"
    exit 1
fi
```

## Execution

```bash
KEYWORD="$1"
echo "   Searching for: '$KEYWORD'"
echo ""

# Search in tag messages
echo "=== Tag Messages ==="
git tag -l "iter-*" --sort=-creatordate | while read tag; do
    TAG_MSG=$(git tag -l --format='%(contents)' "$tag")
    if echo "$TAG_MSG" | grep -qi "$KEYWORD"; then
        TAG_DATE=$(git log -1 --format=%ai "$tag" | cut -d' ' -f1)
        echo "   $tag ($TAG_DATE)"
        echo "   $TAG_MSG"
        echo ""
    fi
done

# Search in iteration files across all tags
echo "=== Iteration Files ==="
git tag -l "iter-*" --sort=-creatordate | while read tag; do
    # Search in files under iterations/ for this tag
    RESULTS=$(git grep -i "$KEYWORD" "$tag" -- 'iterations/*' 2>/dev/null || true)

    if [ -n "$RESULTS" ]; then
        TAG_DATE=$(git log -1 --format=%ai "$tag" | cut -d' ' -f1)
        echo "   $tag ($TAG_DATE)"
        echo "$RESULTS" | head -n 5 | sed 's/^/   /'
        echo ""
    fi
done

echo "   To view full iteration: /show-iteration <tag-name>"
```

## Usage Examples

```bash
# Search for GPU-related iterations
/search-iterations GPU

# Search for error handling discussions
/search-iterations "error handling"

# Search for performance work
/search-iterations performance

# Search for CUDA mentions
/search-iterations CUDA
```

## Output Format

```
   Searching for: 'GPU'

=== Tag Messages ===
   iter-gpu-acceleration (2025-10-20)
   GPU acceleration complete - 3x speedup achieved

   iter-gpu-spike (2025-09-28)
   Failed GPU spike - CUDA incompatibility found

=== Iteration Files ===
   iter-gpu-acceleration (2025-10-20)
   iterations/iter-gpu-acceleration/planning.md: - Implement GPU kernel for matrix ops
   iterations/iter-gpu-acceleration/retrospective.md: GPU acceleration successful...

   iter-gpu-spike (2025-09-28)
   iterations/iter-gpu-spike/spike-results.md: CUDA version conflict...
```
