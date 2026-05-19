#!/bin/bash
# error-handling-reminder.sh - Stop 훅
# 편집된 파일에서 위험 패턴 감지 시 리마인더 출력

LOG_DIR="$HOME/.claude/edit-logs"
LOG_FILE="$LOG_DIR/edits-$(date +%Y%m%d).log"

if [ ! -f "$LOG_FILE" ]; then
  exit 0
fi

RECENT_FILES=$(tail -20 "$LOG_FILE" | awk -F'|' '{print $3}' | tr -d ' ')
RISKY_FILES=0

for FILE in $RECENT_FILES; do
  if [ ! -f "$FILE" ]; then
    continue
  fi

  # 위험 패턴 감지
  if grep -q -E '(try\s*\{|catch\s*\(|async\s|await\s|\.query\(|\.execute\(|fetch\()' "$FILE" 2>/dev/null; then
    RISKY_FILES=$((RISKY_FILES + 1))
  fi
done

if [ "$RISKY_FILES" -gt 0 ]; then
  echo ""
  echo "에러 처리 자체 점검:"
  echo "  $RISKY_FILES개 파일에서 위험 패턴 감지"
  echo "  - catch 블록에 적절한 에러 로깅이 있는가?"
  echo "  - async 함수에 에러 처리가 되어 있는가?"
  echo "  - DB 호출이 try-catch로 감싸져 있는가?"
fi
