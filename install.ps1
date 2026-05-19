# Claude Code 글로벌 설정 설치 스크립트 (Windows PowerShell)
# 사용법: powershell -ExecutionPolicy Bypass -File install.ps1

$ErrorActionPreference = "Stop"

$ClaudeDir = Join-Path $env:USERPROFILE ".claude"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$SourceDir = Join-Path $ScriptDir "dot-claude"

Write-Host ""
Write-Host "============================================"
Write-Host "  Claude Code 글로벌 설정 설치"
Write-Host "============================================"
Write-Host ""

# 1. 백업
if (Test-Path $ClaudeDir) {
    $BackupDir = "$ClaudeDir-backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
    Write-Host "[1/8] 기존 설정을 백업합니다: $BackupDir"
    Copy-Item -Recurse -Force $ClaudeDir $BackupDir
} else {
    Write-Host "[1/8] 기존 설정 없음 - 새로 생성합니다"
    New-Item -ItemType Directory -Force -Path $ClaudeDir | Out-Null
}

# 2. CLAUDE.md
Write-Host "[2/8] CLAUDE.md를 복사합니다..."
Copy-Item -Force (Join-Path $SourceDir "CLAUDE.md") (Join-Path $ClaudeDir "CLAUDE.md")

# 3. settings.json
Write-Host "[3/8] settings.json을 설정합니다..."
$SettingsPath = Join-Path $ClaudeDir "settings.json"
$NewSettingsPath = Join-Path $SourceDir "settings.json"

if (Test-Path $SettingsPath) {
    try {
        $existing = Get-Content $SettingsPath -Raw | ConvertFrom-Json
        $new = Get-Content $NewSettingsPath -Raw | ConvertFrom-Json
        if ($existing.enabledPlugins) {
            $mergedPlugins = @{}
            $new.enabledPlugins.PSObject.Properties | ForEach-Object { $mergedPlugins[$_.Name] = $_.Value }
            $existing.enabledPlugins.PSObject.Properties | ForEach-Object { $mergedPlugins[$_.Name] = $_.Value }
            $new.enabledPlugins = [PSCustomObject]$mergedPlugins
        }
        $new | ConvertTo-Json -Depth 10 | Set-Content -Encoding UTF8 $SettingsPath
        Write-Host "  -> 기존 설정과 병합 완료"
    } catch {
        Copy-Item -Force $NewSettingsPath $SettingsPath
    }
} else {
    Copy-Item -Force $NewSettingsPath $SettingsPath
}

# 4. 스크립트
Write-Host "[4/8] 훅 스크립트를 설치합니다..."
$ScriptsDir = Join-Path $ClaudeDir "scripts"
New-Item -ItemType Directory -Force -Path $ScriptsDir | Out-Null
Copy-Item -Force (Join-Path $SourceDir "scripts\*.sh") $ScriptsDir
$scriptCount = (Get-ChildItem (Join-Path $SourceDir "scripts\*.sh")).Count
Write-Host "  -> ${scriptCount}개 스크립트"

# 5. 슬래시 명령어
Write-Host "[5/8] 슬래시 명령어를 설치합니다..."
$CommandsDir = Join-Path $ClaudeDir "commands"
New-Item -ItemType Directory -Force -Path $CommandsDir | Out-Null
Copy-Item -Force (Join-Path $SourceDir "commands\*.md") $CommandsDir -ErrorAction SilentlyContinue
Copy-Item -Force (Join-Path $SourceDir "commands\*.toml") $CommandsDir -ErrorAction SilentlyContinue
$cmdCount = (Get-ChildItem (Join-Path $SourceDir "commands") -Include "*.md","*.toml" -Recurse).Count
Write-Host "  -> ${cmdCount}개 명령어"

# 6. 규칙
Write-Host "[6/8] 코딩 규칙을 설치합니다..."
$RulesDir = Join-Path $ClaudeDir "rules"
New-Item -ItemType Directory -Force -Path $RulesDir | Out-Null
Copy-Item -Recurse -Force (Join-Path $SourceDir "rules\*") $RulesDir
$ruleCount = (Get-ChildItem (Join-Path $SourceDir "rules") -Include "*.md" -Recurse).Count
Write-Host "  -> ${ruleCount}개 규칙 파일"

# 7. 스킬
Write-Host "[7/8] 스킬을 설치합니다..."
$SkillsSourceDir = Join-Path $SourceDir "skills"
if (Test-Path $SkillsSourceDir) {
    $SkillsDir = Join-Path $ClaudeDir "skills"
    New-Item -ItemType Directory -Force -Path $SkillsDir | Out-Null
    Copy-Item -Recurse -Force (Join-Path $SkillsSourceDir "*") $SkillsDir
    $skillCount = (Get-ChildItem $SkillsSourceDir -Directory).Count
    Write-Host "  -> ${skillCount}개 스킬"
}

# 8. 에이전트
Write-Host "[8/8] 에이전트를 설치합니다..."
$AgentsSourceDir = Join-Path $SourceDir "agents"
if (Test-Path $AgentsSourceDir) {
    $AgentsDir = Join-Path $ClaudeDir "agents"
    New-Item -ItemType Directory -Force -Path $AgentsDir | Out-Null
    Copy-Item -Force (Join-Path $AgentsSourceDir "*.md") $AgentsDir -ErrorAction SilentlyContinue
    $agentCount = (Get-ChildItem (Join-Path $AgentsSourceDir "*.md")).Count
    Write-Host "  -> ${agentCount}개 에이전트"
}

New-Item -ItemType Directory -Force -Path (Join-Path $ClaudeDir "edit-logs") | Out-Null

Write-Host ""
Write-Host "============================================"
Write-Host "  설치 완료!"
Write-Host "============================================"
Write-Host ""
Write-Host "다음 단계:"
Write-Host "1. Claude Code 앱에서 플러그인 설치 (필요시):"
Write-Host "   /install-plugin Notion"
Write-Host "   /install-plugin playwright"
Write-Host "2. (선택) ~/.claude/settings.json 의 GEMINI_API_KEY 채우기"
Write-Host "3. Claude Code 재시작"
Write-Host ""
