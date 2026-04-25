#!/bin/bash
# Generate a new audit report from template
# Usage: ./scripts/report.sh <project-name>

PROJECT="${1:-unnamed-project}"
DATE=$(date +%Y-%m-%d)
FILENAME="reports/${DATE}-${PROJECT}.md"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE="$SCRIPT_DIR/../templates/audit-notes.md"

if [ ! -f "$TEMPLATE" ]; then
    echo "Error: Template not found at $TEMPLATE"
    exit 1
fi

mkdir -p reports

if [ -f "$FILENAME" ]; then
    echo "Report already exists: $FILENAME"
    exit 1
fi

# Copy template and fill in basics
sed "s/\[Name\]/$PROJECT/g; s/\[YYYY-MM-DD\]/$DATE/g" "$TEMPLATE" > "$FILENAME"

echo "Created: $FILENAME"
echo "Open it and start filling in your findings."
