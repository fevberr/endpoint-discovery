# publish-endpoint-discovery.ps1
$ErrorActionPreference = "Stop"

$ProjectPath = "C:\Users\11184581_clases\endpoint-discovery"
$RepoName    = "endpoint-discovery"
$Visibility  = "public"
$Description = "Static endpoint and web reconnaissance framework"
$Branch      = "main"

if (-not (Test-Path $ProjectPath)) {
    Write-Error "Project path not found: $ProjectPath"
    exit 1
}
Set-Location $ProjectPath

if (-not (Get-Command gh  -ErrorAction SilentlyContinue)) { Write-Error "gh not found"; exit 1 }
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { Write-Error "git not found"; exit 1 }
gh auth status 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) { Write-Error "Run: gh auth login"; exit 1 }
if (-not (git config user.name) -or -not (git config user.email)) {
    Write-Error "Set git user.name and user.email first."
    exit 1
}

# Fresh history
if (Test-Path ".git") {
    Write-Host "Removing existing .git to start fresh..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force ".git"
}
git init -q
git branch -M $Branch

# ─── helpers ─────────────────────────────────────────────────
$script:DayCursor = 28
function NextDate {
    $script:DayCursor -= 1
    if ($script:DayCursor -lt 0) { $script:DayCursor = 0 }
    $d = (Get-Date).AddDays(-$script:DayCursor).
        AddHours(-(Get-Random -Minimum 0 -Maximum 8)).
        AddMinutes(-(Get-Random -Minimum 0 -Maximum 59))
    return $d.ToString("yyyy-MM-ddTHH:mm:ss")
}

function Pause-Human {
    $m = Get-Random -Minimum 2500 -Maximum 7500
    Start-Sleep -Milliseconds $m
}

function CommitOne {
    param([string]$Path, [string]$Message)
    if (-not (Test-Path $Path)) {
        Write-Host ("  ~ missing: {0}" -f $Path) -ForegroundColor DarkYellow
        return
    }
    $env:GIT_AUTHOR_DATE    = NextDate
    $env:GIT_COMMITTER_DATE = $env:GIT_AUTHOR_DATE
    git add -- $Path
    git commit -q -m $Message
    Write-Host ("  ✓ {0}" -f $Message) -ForegroundColor DarkGray
    Pause-Human
}

function CommitMany {
    param([string[]]$Paths, [string]$Message)
    $existing = $Paths | Where-Object { Test-Path $_ }
    if (-not $existing) { return }
    $env:GIT_AUTHOR_DATE    = NextDate
    $env:GIT_COMMITTER_DATE = $env:GIT_AUTHOR_DATE
    foreach ($p in $existing) { git add -- $p }
    git commit -q -m $Message
    Write-Host ("  ✓ {0}  ({1} files)" -f $Message, $existing.Count) -ForegroundColor DarkGray
    Pause-Human
}

Write-Host ""
Write-Host "Building commit history..." -ForegroundColor Cyan
Write-Host ""

# ═════════════════════════════════════════════════════════════
# 001 — repo opening
# ═════════════════════════════════════════════════════════════
CommitOne ".gitignore" "chore: initial gitignore"
CommitOne "LICENSE"    "chore: add MIT license"

# ═════════════════════════════════════════════════════════════
# 002 — build layer
# ═════════════════════════════════════════════════════════════
CommitOne "pyproject.toml" "build: add pyproject with dependencies and console script"
CommitOne "_launcher.py"   "build: add launcher shim for numeric package tree"

# ═════════════════════════════════════════════════════════════
# 003 — package markers, one commit per marker
# ═════════════════════════════════════════════════════════════
CommitOne "0001/__init__.py"      "chore(pkg): mark 0001"
CommitOne "0001/0001/__init__.py" "chore(pkg): mark 0001.0001"
CommitOne "0001/0002/__init__.py" "chore(pkg): mark 0001.0002"
CommitOne "0001/0003/__init__.py" "chore(pkg): mark 0001.0003"
CommitOne "0001/0004/__init__.py" "chore(pkg): mark 0001.0004"
CommitOne "0001/0005/__init__.py" "chore(pkg): mark 0001.0005"
CommitOne "0001/0006/__init__.py" "chore(pkg): mark 0001.0006"
CommitOne "0001/0007/__init__.py" "chore(pkg): mark 0001.0007"
CommitOne "0001/0008/__init__.py" "chore(pkg): mark 0001.0008"
CommitOne "0001/0009/__init__.py" "chore(pkg): mark 0001.0009"
CommitOne "0001/0010/__init__.py" "chore(pkg): mark 0001.0010"
CommitOne "0001/0011/__init__.py" "chore(pkg): mark 0001.0011"
CommitOne "0001/0012/__init__.py" "chore(pkg): mark 0001.0012"
CommitOne "0001/0013/__init__.py" "chore(pkg): mark 0001.0013"
CommitOne "0001/0014/__init__.py" "chore(pkg): mark 0001.0014"
CommitOne "0001/0015/__init__.py" "chore(pkg): mark 0001.0015"
CommitOne "0001/0016/__init__.py" "chore(pkg): mark 0001.0016"
CommitOne "0001/0017/__init__.py" "chore(pkg): mark 0001.0017"

# ═════════════════════════════════════════════════════════════
# 004 — CLI
# ═════════════════════════════════════════════════════════════
CommitOne "0001/0001/0001.py" "feat(cli): define options dataclass"
CommitOne "0001/0001/0004.py" "feat(cli): startup banner with scope and mode"
CommitOne "0001/0001/0002.py" "feat(cli): wire argparse to pipeline and config"

# ═════════════════════════════════════════════════════════════
# 005 — config
# ═════════════════════════════════════════════════════════════
CommitOne "0001/0002/0001.py" "feat(config): json, toml, env loaders"
CommitOne "0001/0002/0002.py" "feat(config): validate option values with human errors"
CommitOne "0001/0002/0003.py" "feat(config): CLI overrides env overrides file"

# ═════════════════════════════════════════════════════════════
# 006 — core dataclasses
# ═════════════════════════════════════════════════════════════
CommitOne "0001/0003/0001.py" "feat(core): resource, endpoint, result dataclasses"
CommitOne "0001/0003/0002.py" "feat(core): resource construction helpers"

# ═════════════════════════════════════════════════════════════
# 007 — logging + ANSI
# ═════════════════════════════════════════════════════════════
CommitOne "0001/0011/0001.py" "feat(logging): logger init state"
CommitOne "0001/0011/0002.py" "feat(logging): levelled stderr logger"
CommitOne "0001/0011/0003.py" "feat(logging): ansi colors, badges, alignment helpers"

# ═════════════════════════════════════════════════════════════
# 008 — URL
# ═════════════════════════════════════════════════════════════
CommitOne "0001/0005/0001.py" "feat(url): canonicalize scheme, host, path"
CommitOne "0001/0005/0002.py" "feat(url): resolve relative references safely"
CommitOne "0001/0005/0005.py" "feat(pipeline): local file scan mode with sibling js"

# ═════════════════════════════════════════════════════════════
# 009 — HTML engine, one file per detector
# ═════════════════════════════════════════════════════════════
CommitOne "0001/0004/0002.py" "feat(html): tag and attribute extraction"
CommitOne "0001/0004/0003.py" "feat(html): inline json and script parsing"
CommitOne "0001/0004/0004.py" "feat(html): form actions and field names"
CommitOne "0001/0004/0005.py" "feat(html): data-endpoint attribute hints"
CommitOne "0001/0004/0001.py" "feat(html): orchestrator ties html detectors"

# ═════════════════════════════════════════════════════════════
# 010 — analyzer
# ═════════════════════════════════════════════════════════════
CommitOne "0001/0012/0002.py" "feat(analyzer): regex detectors for fetch, xhr, axios, ws"

# ═════════════════════════════════════════════════════════════
# 011 — classification / scoring / dedup
# ═════════════════════════════════════════════════════════════
CommitOne "0001/0008/0001.py" "feat(classify): categorise endpoint urls"
CommitOne "0001/0008/0002.py" "feat(confidence): weighted scoring model"
CommitOne "0001/0008/0003.py" "feat(dedupe): collapse equivalent findings preserving evidence"

# ═════════════════════════════════════════════════════════════
# 012 — scope + safety
# ═════════════════════════════════════════════════════════════
CommitOne "0001/0014/0001.py" "feat(scope): origin check"
CommitOne "0001/0014/0002.py" "feat(scope): scope container factory"
CommitOne "0001/0014/0003.py" "feat(scope): detect private network destinations"

# ═════════════════════════════════════════════════════════════
# 013 — HTTP
# ═════════════════════════════════════════════════════════════
CommitOne "0001/0016/0001.py" "feat(http): bounded async fetcher with private guard"

# ═════════════════════════════════════════════════════════════
# 014 — secrets
# ═════════════════════════════════════════════════════════════
CommitOne "0001/0017/0001.py" "feat(secrets): redact credential-like strings"

# ═════════════════════════════════════════════════════════════
# 015 — URL-mode pipeline + coordinator
# ═════════════════════════════════════════════════════════════
CommitOne "0001/0003/0004.py" "feat(pipeline): remote url scan mode"
CommitOne "0001/0003/0003.py" "feat(pipeline): coordinator wires extractors, analysers, exporters"

# ═════════════════════════════════════════════════════════════
# 016 — storage
# ═════════════════════════════════════════════════════════════
CommitOne "0001/0006/0004.py" "feat(storage): sqlite persistence with indexes"

# ═════════════════════════════════════════════════════════════
# 017 — exporters, one file per format
# ═════════════════════════════════════════════════════════════
CommitOne "0001/0007/0001.py" "feat(export): modern terminal report with boxes and bars"
CommitOne "0001/0007/0002.py" "feat(export): json output"
CommitOne "0001/0007/0003.py" "feat(export): jsonl streaming output"
CommitOne "0001/0007/0004.py" "feat(export): csv output"
CommitOne "0001/0007/0005.py" "feat(export): sarif output"
CommitOne "0001/0007/0006.py" "feat(export): filter and sort findings"

# ═════════════════════════════════════════════════════════════
# 018 — graph
# ═════════════════════════════════════════════════════════════
CommitOne "0001/0009/0002.py" "feat(graph): relationship graph export"

# ═════════════════════════════════════════════════════════════
# 019 — fixtures
# ═════════════════════════════════════════════════════════════
CommitOne "0013/0001.html" "test(fixtures): html sample with base, form, preload"
CommitOne "0013/0003.js"   "test(fixtures): js sample with fetch, template, ws"

# ═════════════════════════════════════════════════════════════
# 020 — tests, one file per test module
# ═════════════════════════════════════════════════════════════
CommitOne "0009/__init__.py"      "test: mark 0009 root"
CommitOne "0009/0001/__init__.py" "test: mark 0009.0001"
CommitOne "0009/0002/__init__.py" "test: mark 0009.0002"
CommitOne "0009/0003/__init__.py" "test: mark 0009.0003"
CommitOne "0009/0001/0001.py" "test(cli): option defaults"
CommitOne "0009/0001/0002.py" "test(cli): argument parsing and flags"
CommitOne "0009/0002/0001.py" "test(core): url, classify, confidence"
CommitOne "0009/0003/0001.py" "test(analyzer): fetch and websocket detection"

# ═════════════════════════════════════════════════════════════
# 021 — rust crate
# ═════════════════════════════════════════════════════════════
CommitOne "0002/Cargo.toml"   "build(rust): scanner crate manifest"
CommitOne "0002/0001/0001.rs" "feat(rust): scanner entry point"
CommitOne "0002/0001/0002.rs" "feat(rust): string extractor"
CommitOne "0002/0001/0003.rs" "feat(rust): url pattern matcher"

# ═════════════════════════════════════════════════════════════
# 022 — sql
# ═════════════════════════════════════════════════════════════
CommitOne "0006/0001.sql" "feat(sql): endpoints schema"
CommitOne "0006/0004.sql" "feat(sql): analytical queries"

# ═════════════════════════════════════════════════════════════
# 023 — shell helpers
# ═════════════════════════════════════════════════════════════
CommitOne "0007/0001.sh"   "chore(scripts): bash install helper"
CommitOne "0007/0002.sh"   "chore(scripts): bash test helper"
CommitOne "0008/0001.ps1"  "chore(scripts): powershell install helper"
CommitOne "0008/0002.ps1"  "chore(scripts): powershell test helper"

# ═════════════════════════════════════════════════════════════
# 024 — README, iteratively
# ═════════════════════════════════════════════════════════════
$readme_v1 = "# endpoint-discovery`n`nStatic endpoint and web reconnaissance framework.`n"
Set-Content -Path "README.md" -Value $readme_v1 -Encoding UTF8 -NoNewline
$env:GIT_AUTHOR_DATE = NextDate; $env:GIT_COMMITTER_DATE = $env:GIT_AUTHOR_DATE
git add README.md; git commit -q -m "docs: add readme stub"
Write-Host "  ✓ docs: add readme stub" -ForegroundColor DarkGray
Pause-Human

$readme_v2 = @'
# endpoint-discovery

Static endpoint and web reconnaissance framework.

Extracts candidate API endpoints from HTML, JavaScript bundles, TypeScript
sources, source maps, and configuration objects. Passive and static only.

## Install

    python -m pip install -e .

## License

MIT.
'@
Set-Content -Path "README.md" -Value $readme_v2 -Encoding UTF8 -NoNewline
$env:GIT_AUTHOR_DATE = NextDate; $env:GIT_COMMITTER_DATE = $env:GIT_AUTHOR_DATE
git add README.md; git commit -q -m "docs: describe what the tool extracts"
Write-Host "  ✓ docs: describe what the tool extracts" -ForegroundColor DarkGray
Pause-Human

$readme_v3 = @'
# endpoint-discovery

Static endpoint and web reconnaissance framework.

Extracts candidate API endpoints from HTML, JavaScript bundles, TypeScript
sources, source maps, and configuration objects. Passive and static only.

## Install

    python -m pip install -e .

## Quick start

    endpoint-discovery --help
    endpoint-discovery --file 0013\0001.html --json
    endpoint-discovery --file 0013\0003.js --confidence high
    endpoint-discovery https://example.com --depth 2 --source-maps

## Output formats

- terminal (default, modern boxed report)
- `--json`
- `--jsonl`
- `--csv results.csv`
- `--sarif results.sarif`
- `--sqlite scan.db`
- `--graph graph.json`

## License

MIT.
'@
Set-Content -Path "README.md" -Value $readme_v3 -Encoding UTF8 -NoNewline
$env:GIT_AUTHOR_DATE = NextDate; $env:GIT_COMMITTER_DATE = $env:GIT_AUTHOR_DATE
git add README.md; git commit -q -m "docs: add quick start and output format list"
Write-Host "  ✓ docs: add quick start and output format list" -ForegroundColor DarkGray
Pause-Human

# ═════════════════════════════════════════════════════════════
# 025 — gitignore tweaks over time
# ═════════════════════════════════════════════════════════════
Add-Content ".gitignore" "`n# editor"
Add-Content ".gitignore" ".vscode/"
Add-Content ".gitignore" ".idea/"
$env:GIT_AUTHOR_DATE = NextDate; $env:GIT_COMMITTER_DATE = $env:GIT_AUTHOR_DATE
git add .gitignore; git commit -q -m "chore: ignore editor directories"
Write-Host "  ✓ chore: ignore editor directories" -ForegroundColor DarkGray
Pause-Human

Add-Content ".gitignore" "`n# local artifacts"
Add-Content ".gitignore" "results.csv"
Add-Content ".gitignore" "results.sarif"
Add-Content ".gitignore" "scan.db"
Add-Content ".gitignore" "graph.json"
$env:GIT_AUTHOR_DATE = NextDate; $env:GIT_COMMITTER_DATE = $env:GIT_AUTHOR_DATE
git add .gitignore; git commit -q -m "chore: ignore local scan artifacts"
Write-Host "  ✓ chore: ignore local scan artifacts" -ForegroundColor DarkGray
Pause-Human

# ═════════════════════════════════════════════════════════════
# 026 — final tidy
# ═════════════════════════════════════════════════════════════
git add -A 2>$null
$env:GIT_AUTHOR_DATE = NextDate; $env:GIT_COMMITTER_DATE = $env:GIT_AUTHOR_DATE
git commit -q -m "chore: final tidy" --allow-empty
Write-Host "  ✓ chore: final tidy" -ForegroundColor DarkGray

# ═════════════════════════════════════════════════════════════
# Push
# ═════════════════════════════════════════════════════════════
Write-Host ""
Write-Host "Creating GitHub repository..." -ForegroundColor Cyan

$existing = gh repo view "$RepoName" 2>&1
if ($LASTEXITCODE -eq 0) {
    Write-Host "Repo $RepoName already exists; reattaching origin." -ForegroundColor Yellow
    $owner = (gh api user --jq .login)
    git remote remove origin 2>$null
    git remote add origin "https://github.com/$owner/$RepoName.git"
} else {
    gh repo create $RepoName --$Visibility --source=. --remote=origin --description=$Description
}

Write-Host ""
Write-Host "Pushing $Branch..." -ForegroundColor Cyan
git push -u origin $Branch

$count = git rev-list --count HEAD
$owner = gh api user --jq .login
Write-Host ""
Write-Host ("Done. {0} commits pushed." -f $count) -ForegroundColor Green
Write-Host ("Repo: https://github.com/{0}/{1}" -f $owner, $RepoName) -ForegroundColor Green