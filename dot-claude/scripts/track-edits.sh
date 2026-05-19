#!/bin/bash
# track-edits.sh - PostToolUse 훅
# 편집된 파일과 해당 repo를 기록

INPUT=$(cat)

# jq가 없으면 종료
if ! command -v jq &> /dev/null; then
  exit 0
fi

FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // .tool_input.path // empty')

if [ -z "$FILE_PATH" ]; then
  exit 0
fi

LOG_DIR="$HOME/.claude/edit-logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/edits-$(date +%Y%m%d).log"

# 파일이 속한 repo 판별
REPO_DIR=$(cd "$(dirname "$FILE_PATH")" 2>/dev/null && git rev-parse --show-toplevel 2>/dev/null || echo "unknown")

echo "$(date +%H:%M:%S) | $REPO_DIR | $FILE_PATH" >> "$LOG_FILE"
