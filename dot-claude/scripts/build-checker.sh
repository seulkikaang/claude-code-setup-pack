#!/bin/bash
# build-checker.sh - Stop 훅
# 편집된 파일의 repo에서 빌드를 실행하여 에러 확인

LOG_DIR="$HOME/.claude/edit-logs"
LOG_FILE="$LOG_DIR/edits-$(date +%Y%m%d).log"

if [ ! -f "$LOG_FILE" ]; then
  exit 0
fi

# 최근 편집된 repo 목록 추출 (중복 제거)
REPOS=$(tail -50 "$LOG_FILE" | awk -F'|' '{print $2}' | tr -d ' ' | sort -u)
ERRORS=""

for REPO in $REPOS; do
  if [ "$REPO" = "unknown" ] || [ ! -d "$REPO" ]; then
    continue
  fi

  # package.json이 있으면 TypeScript 빌드 확인
  if [ -f "$REPO/tsconfig.json" ]; then
    BUILD_OUTPUT=$(cd "$REPO" && npx tsc --noEmit 2>&1)
    if [ $? -ne 0 ]; then
      ERROR_COUNT=$(echo "$BUILD_OUTPUT" | grep -c "error TS")
      if [ "$ERROR_COUNT" -gt 0 ]; then
        ERRORS="$ERRORS\n$(basename $REPO): $ERROR_COUNT TypeScript errors"
        if [ "$ERROR_COUNT" -lt 5 ]; then
          ERRORS="$ERRORS\n$BUILD_OUTPUT"
        else
          ERRORS="$ERRORS\n(에러가 5개 이상 - build-error-resolver 에이전트 실행을 권장합니다)"
        fi
      fi
    fi
  fi

  # Go 프로젝트 확인
  if [ -f "$REPO/go.mod" ]; then
    BUILD_OUTPUT=$(cd "$REPO" && go build ./... 2>&1)
    if [ $? -ne 0 ]; then
      ERRORS="$ERRORS\n$(basename $REPO): Go build errors\n$BUILD_OUTPUT"
    fi
  fi

  # Python 프로젝트 확인
  if [ -f "$REPO/pyproject.toml" ] || [ -f "$REPO/setup.py" ]; then
    if command -v ruff &> /dev/null; then
      LINT_OUTPUT=$(cd "$REPO" && ruff check . 2>&1)
      if [ $? -ne 0 ]; then
        ERRORS="$ERRORS\n$(basename $REPO): Python lint errors\n$LINT_OUTPUT"
      fi
    fi
  fi
done

if [ -n "$ERRORS" ]; then
  echo -e "빌드 에러 감지:$ERRORS"
  exit 0
fi
