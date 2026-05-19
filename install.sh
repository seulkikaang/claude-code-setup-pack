#!/bin/bash
# Claude Code 글로벌 설정 설치 스크립트 (macOS / Linux)
# 사용법: bash install.sh

set -e

CLAUDE_DIR="$HOME/.claude"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SOURCE_DIR="$SCRIPT_DIR/dot-claude"

echo ""
echo "============================================"
echo "  Claude Code 글로벌 설정 설치"
echo "============================================"
echo ""

# 0. jq 설치 확인
if ! command -v jq &> /dev/null; then
  echo "[사전] jq가 설치되어 있지 않습니다. 설치 중..."
  if command -v brew &> /dev/null; then
    brew install jq
  elif command -v apt-get &> /dev/null; then
    sudo apt-get install -y jq
  else
    echo "  jq를 수동으로 설치해주세요: https://jqlang.github.io/jq/download/"
  fi
fi

# 1. 기존 설정 백업
if [ -d "$CLAUDE_DIR" ]; then
  BACKUP_DIR="$CLAUDE_DIR-backup-$(date +%Y%m%d-%H%M%S)"
  echo "[1/8] 기존 설정을 백업합니다: $BACKUP_DIR"
  cp -r "$CLAUDE_DIR" "$BACKUP_DIR"
else
  echo "[1/8] 기존 설정 없음 - 새로 생성합니다"
  mkdir -p "$CLAUDE_DIR"
fi

# 2. CLAUDE.md
echo "[2/8] CLAUDE.md를 복사합니다..."
cp "$SOURCE_DIR/CLAUDE.md" "$CLAUDE_DIR/CLAUDE.md"

# 3. settings.json 병합
echo "[3/8] settings.json을 설정합니다..."
if [ -f "$CLAUDE_DIR/settings.json" ] && command -v python3 &> /dev/null; then
  python3 -c "
import json
with open('$CLAUDE_DIR/settings.json') as f: existing = json.load(f)
with open('$SOURCE_DIR/settings.json') as f: new = json.load(f)
merged = {**new}
if 'enabledPlugins' in existing:
    merged['enabledPlugins'] = {**new.get('enabledPlugins', {}), **existing['enabledPlugins']}
if 'env' in existing:
    merged_env = {**new.get('env', {}), **existing.get('env', {})}
    merged['env'] = merged_env
with open('$CLAUDE_DIR/settings.json', 'w') as f:
    json.dump(merged, f, indent=2, ensure_ascii=False)
print('  -> 기존 설정과 병합 완료')
" 2>/dev/null || cp "$SOURCE_DIR/settings.json" "$CLAUDE_DIR/settings.json"
else
  cp "$SOURCE_DIR/settings.json" "$CLAUDE_DIR/settings.json"
fi

# 4. 스크립트
echo "[4/8] 훅 스크립트를 설치합니다..."
mkdir -p "$CLAUDE_DIR/scripts"
cp "$SOURCE_DIR/scripts/"*.sh "$CLAUDE_DIR/scripts/"
chmod +x "$CLAUDE_DIR/scripts/"*.sh
echo "  -> $(ls "$SOURCE_DIR/scripts/"*.sh | wc -l | tr -d ' ')개 스크립트"

# 5. 슬래시 명령어
echo "[5/8] 슬래시 명령어를 설치합니다..."
mkdir -p "$CLAUDE_DIR/commands"
cp "$SOURCE_DIR/commands/"*.md "$CLAUDE_DIR/commands/" 2>/dev/null || true
cp "$SOURCE_DIR/commands/"*.toml "$CLAUDE_DIR/commands/" 2>/dev/null || true
echo "  -> $(ls "$SOURCE_DIR/commands/"*.md "$SOURCE_DIR/commands/"*.toml 2>/dev/null | wc -l | tr -d ' ')개 명령어"

# 6. 규칙
echo "[6/8] 코딩 규칙을 설치합니다..."
mkdir -p "$CLAUDE_DIR/rules"
cp -r "$SOURCE_DIR/rules/"* "$CLAUDE_DIR/rules/"
echo "  -> $(find "$SOURCE_DIR/rules" -name '*.md' | wc -l | tr -d ' ')개 규칙 파일"

# 7. 스킬
echo "[7/8] 스킬을 설치합니다..."
if [ -d "$SOURCE_DIR/skills" ]; then
  mkdir -p "$CLAUDE_DIR/skills"
  cp -r "$SOURCE_DIR/skills/"* "$CLAUDE_DIR/skills/"
  echo "  -> $(ls -d "$SOURCE_DIR/skills/"*/ 2>/dev/null | wc -l | tr -d ' ')개 스킬"
fi

# 8. 에이전트
echo "[8/8] 에이전트를 설치합니다..."
if [ -d "$SOURCE_DIR/agents" ]; then
  mkdir -p "$CLAUDE_DIR/agents"
  cp "$SOURCE_DIR/agents/"*.md "$CLAUDE_DIR/agents/" 2>/dev/null || true
  echo "  -> $(ls "$SOURCE_DIR/agents/"*.md 2>/dev/null | wc -l | tr -d ' ')개 에이전트"
fi

mkdir -p "$CLAUDE_DIR/edit-logs"

echo ""
echo "============================================"
echo "  설치 완료!"
echo "============================================"
echo ""
echo "다음 단계:"
echo "1. Claude Code 앱에서 플러그인 설치 (필요시):"
echo "   /install-plugin Notion"
echo "   /install-plugin playwright"
echo "2. (선택) ~/.claude/settings.json 의 GEMINI_API_KEY 채우기"
echo "3. Claude Code 재시작"
echo ""
