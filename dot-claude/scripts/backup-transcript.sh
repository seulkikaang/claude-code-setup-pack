#!/bin/bash
# backup-transcript.sh - PreCompact 훅
# compaction 전에 트랜스크립트를 백업

INPUT=$(cat)

# jq가 없으면 종료
if ! command -v jq &> /dev/null; then
  exit 0
fi

TRANSCRIPT_PATH=$(echo "$INPUT" | jq -r '.transcript_path // empty')

if [ -z "$TRANSCRIPT_PATH" ] || [ ! -f "$TRANSCRIPT_PATH" ]; then
  exit 0
fi

BACKUP_DIR="$HOME/.claude/transcript-backups"
mkdir -p "$BACKUP_DIR"

BACKUP_FILE="$BACKUP_DIR/backup-$(date +%Y%m%d-%H%M%S).jsonl"
cp "$TRANSCRIPT_PATH" "$BACKUP_FILE"

echo "트랜스크립트가 $BACKUP_FILE에 백업되었습니다."
