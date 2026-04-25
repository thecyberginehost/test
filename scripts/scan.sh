#!/bin/bash
# Automated scan script - runs all tools against a target
# Usage: ./scripts/scan.sh <path-to-contracts>

set -e

TARGET="${1:-.}"
OUTPUT_DIR="scan-results-$(date +%Y%m%d-%H%M%S)"

if [ ! -d "$TARGET" ]; then
    echo "Error: $TARGET is not a directory"
    echo "Usage: ./scripts/scan.sh <path-to-foundry-project>"
    exit 1
fi

mkdir -p "$OUTPUT_DIR"
echo "=== Scanning: $TARGET ==="
echo "=== Output: $OUTPUT_DIR ==="

# 1. Slither
echo ""
echo "[1/4] Running Slither..."
if command -v slither &> /dev/null; then
    slither "$TARGET" \
        --json "$OUTPUT_DIR/slither.json" \
        --sarif "$OUTPUT_DIR/slither.sarif" \
        2>&1 | tee "$OUTPUT_DIR/slither-stdout.txt" || true
    echo "  Slither output: $OUTPUT_DIR/slither.json"
else
    echo "  SKIPPED: slither not installed"
fi

# 2. Aderyn
echo ""
echo "[2/4] Running Aderyn..."
if command -v aderyn &> /dev/null; then
    aderyn "$TARGET" -o "$OUTPUT_DIR/aderyn-report.md" 2>&1 || true
    echo "  Aderyn output: $OUTPUT_DIR/aderyn-report.md"
else
    echo "  SKIPPED: aderyn not installed"
fi

# 3. Semgrep with custom rules
echo ""
echo "[3/4] Running Semgrep..."
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RULES_DIR="$SCRIPT_DIR/../tools/semgrep"
if command -v semgrep &> /dev/null; then
    semgrep --config "$RULES_DIR/solidity-rules.yaml" \
        "$TARGET" \
        --json -o "$OUTPUT_DIR/semgrep.json" 2>&1 || true
    echo "  Semgrep output: $OUTPUT_DIR/semgrep.json"
else
    echo "  SKIPPED: semgrep not installed"
fi

# 4. Mythril (slow - only on specific files)
echo ""
echo "[4/4] Running Mythril (on .sol files in src/)..."
if command -v myth &> /dev/null; then
    find "$TARGET/src" -name "*.sol" -type f 2>/dev/null | while read -r sol_file; do
        basename=$(basename "$sol_file" .sol)
        echo "  Analyzing: $sol_file"
        myth analyze "$sol_file" \
            --execution-timeout 120 \
            -o json \
            > "$OUTPUT_DIR/mythril-$basename.json" 2>&1 || true
    done
    echo "  Mythril outputs: $OUTPUT_DIR/mythril-*.json"
else
    echo "  SKIPPED: mythril not installed"
fi

echo ""
echo "=== Scan Complete ==="
echo "Results in: $OUTPUT_DIR/"
echo ""
echo "Next steps:"
echo "  1. Review slither.json for high/medium findings"
echo "  2. Review aderyn-report.md for additional findings"
echo "  3. Cross-reference semgrep.json with manual review"
echo "  4. Check mythril outputs for reachable exploits"
echo "  5. Start manual review using checklists in solidity/checklists/"
