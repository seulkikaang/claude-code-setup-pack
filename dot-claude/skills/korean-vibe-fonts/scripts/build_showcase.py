#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[1]
CORE_CATALOG = BASE_DIR / "references" / "font_catalog.json"
ARCHIVE_CATALOG = BASE_DIR / "references" / "fonts_archive_commercial.json"
DECISION_GUIDE = BASE_DIR / "references" / "font_decision_guide.json"
SHOWCASE = BASE_DIR / "showcase.html"
INDEX = BASE_DIR / "index.html"

CATEGORY_LABELS = {
    "curated": "큐레이션 핵심",
    "baemin-food": "배민·푸드",
    "ui-sans": "UI 기본 산스",
    "headline-campaign": "캠페인·헤드라인",
    "editorial-serif": "에디토리얼·부리",
    "handwriting": "손글씨·포인트",
    "retro-pixel": "레트로·픽셀",
    "institution-local": "기관·로컬 브랜드",
    "experimental": "실험적·장식",
}

SAMPLES = {
    "curated": "고민 없이 중간",
    "baemin-food": "맛있게 흔들리는 제목",
    "ui-sans": "차분한 화면 설계",
    "headline-campaign": "오늘만 크게 외치기",
    "editorial-serif": "문장에 남는 온기",
    "handwriting": "손끝으로 남긴 말",
    "retro-pixel": "오래된 화면의 맛",
    "institution-local": "믿음직한 안내문",
    "experimental": "낯선 리듬의 포인트",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def family_of(font: dict[str, Any]) -> str:
    app = font.get("application", {})
    return (
        app.get("heading_family")
        or app.get("body_family")
        or app.get("code_family")
        or "sans-serif"
    )


def item_from_core(font: dict[str, Any]) -> dict[str, Any]:
    category = "curated"
    return {
        "id": font["id"],
        "name": font["name"],
        "family": family_of(font),
        "stylesheet": font.get("stylesheet_url"),
        "styleTag": font.get("integration", {}).get("style_tag"),
        "category": category,
        "categoryLabel": CATEGORY_LABELS[category],
        "provider": font.get("provider", ""),
        "sample": SAMPLES[category],
        "isCore": True,
    }


def item_from_archive(font: dict[str, Any]) -> dict[str, Any]:
    category = font.get("category") or "experimental"
    return {
        "id": font["id"],
        "name": font["name"],
        "family": family_of(font),
        "stylesheet": font.get("stylesheet_url"),
        "styleTag": None,
        "category": category,
        "categoryLabel": CATEGORY_LABELS.get(category, CATEGORY_LABELS["experimental"]),
        "provider": font.get("repo") or "fonts-archive",
        "sample": SAMPLES.get(category, SAMPLES["experimental"]),
        "isCore": False,
    }


def build_items() -> tuple[list[dict[str, Any]], dict[str, Any], dict[str, Any]]:
    core = load_json(CORE_CATALOG)["fonts"]
    archive_doc = load_json(ARCHIVE_CATALOG)
    guide = load_json(DECISION_GUIDE)
    items = [item_from_core(font) for font in core]
    items.extend(item_from_archive(font) for font in archive_doc["fonts"])
    return items, archive_doc, guide


def style_block() -> str:
    return r"""
:root{--paper:#f6f1e7;--ink:#151719;--muted:#697078;--line:rgba(21,23,25,.13);--accent:#c25d4a;--blue:#526f9d;--green:#5b8c68;--gold:#bf934a;--teal:#4d918d;--ui:ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Apple SD Gothic Neo","Malgun Gothic",sans-serif}*{box-sizing:border-box}html,body{margin:0;min-height:100%}body{color:var(--ink);background:#d7d9d1;font-family:var(--ui)}body:before{position:fixed;inset:0;pointer-events:none;background:linear-gradient(rgba(21,23,25,.038) 1px,transparent 1px),linear-gradient(90deg,rgba(21,23,25,.038) 1px,transparent 1px);background-size:34px 34px;content:""}.shell{width:min(100% - 32px,1720px);margin:24px auto;border:1px solid rgba(21,23,25,.17);border-radius:12px;background:linear-gradient(180deg,#fbf8ef,var(--paper));box-shadow:0 24px 70px rgba(21,23,25,.15);overflow:hidden}header{display:grid;grid-template-columns:minmax(0,1fr) minmax(280px,540px);gap:28px;align-items:end;padding:clamp(28px,4vw,62px) clamp(22px,4vw,64px) 24px;border-bottom:1px solid var(--line)}.eyebrow{margin:0 0 10px;color:var(--muted);font-size:13px;font-weight:820}h1{margin:0;max-width:820px;font-size:clamp(42px,5.8vw,92px);line-height:.92;letter-spacing:0}.summary{margin:0;color:#2f3439;font-size:clamp(15px,1.18vw,21px);font-weight:720;line-height:1.45;word-break:keep-all}.layout{display:grid;grid-template-columns:300px minmax(0,1fr);min-height:760px}aside{padding:22px;border-right:1px solid var(--line);background:rgba(255,255,255,.34)}.search{width:100%;height:42px;border:1px solid var(--line);border-radius:8px;padding:0 12px;background:rgba(255,255,255,.66);color:var(--ink);font:760 14px var(--ui);outline:none}.search:focus{border-color:rgba(194,93,74,.6);box-shadow:0 0 0 3px rgba(194,93,74,.12)}.sideTitle{margin:18px 0 9px;color:#2f3439;font-size:11px;font-weight:900;letter-spacing:0}.tabs,.scenarioList{display:grid;gap:8px}.tab,.scenario{display:grid;grid-template-columns:1fr auto;align-items:center;gap:10px;width:100%;border:1px solid transparent;border-radius:8px;padding:10px 11px;background:transparent;color:#373c42;font:800 13px var(--ui);text-align:left;cursor:pointer;transition:transform .28s cubic-bezier(.2,.8,.2,1),background .28s cubic-bezier(.2,.8,.2,1),border-color .28s cubic-bezier(.2,.8,.2,1)}.scenario{grid-template-columns:1fr;font-size:12px;padding:9px 10px}.tab:hover,.scenario:hover{transform:translateY(-1px);background:rgba(255,255,255,.48);border-color:var(--line)}.tab[aria-selected=true],.scenario[aria-selected=true]{background:#151719;color:#fff8ec;border-color:#151719}.count{opacity:.68;font-variant-numeric:tabular-nums}.metaBox{margin-top:18px;padding-top:16px;border-top:1px solid var(--line);color:var(--muted);font-size:12px;font-weight:720;line-height:1.5}main{min-width:0;padding:22px}.bar{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:16px;align-items:end;margin-bottom:14px}h2{margin:0;font-size:clamp(28px,2.8vw,50px);line-height:1;letter-spacing:0}.resultMeta{color:var(--muted);font-size:13px;font-weight:800}.guide{display:none;margin-bottom:16px;border:1px solid var(--line);border-radius:8px;background:rgba(255,255,255,.48);overflow:hidden}.guide.visible{display:grid;grid-template-columns:1.1fr .9fr}.guideMain{padding:16px 18px}.guideMeta{padding:16px 18px;border-left:1px solid var(--line);background:rgba(255,255,255,.38)}.tone{margin:0 0 7px;color:var(--accent);font-size:12px;font-weight:900}.best{margin:0;color:#2f3439;font-size:15px;font-weight:760;line-height:1.45;word-break:keep-all}.roles{display:grid;gap:7px;margin-top:10px}.role{display:grid;grid-template-columns:52px 1fr;gap:8px;color:#33383d;font-size:12px;font-weight:820}.role span:first-child{color:var(--muted)}.avoid{margin:10px 0 0;color:var(--muted);font-size:12px;font-weight:720;line-height:1.45}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(188px,1fr));gap:10px}.card{position:relative;min-height:132px;display:grid;grid-template-rows:auto 1fr auto;gap:10px;padding:13px 14px 12px;overflow:hidden;border:1px solid var(--line);border-radius:8px;background:rgba(255,255,255,.55)}.card:before{position:absolute;inset:0 auto 0 0;width:5px;background:var(--swatch,var(--accent));content:""}.card.baemin-food{--swatch:var(--accent)}.card.ui-sans{--swatch:var(--blue)}.card.headline-campaign{--swatch:#b64f4b}.card.editorial-serif{--swatch:#78649b}.card.handwriting{--swatch:var(--gold)}.card.retro-pixel{--swatch:#6e6253}.card.institution-local{--swatch:var(--green)}.card.experimental{--swatch:var(--teal)}.card.curated{--swatch:#30353a}.card.scenarioPick{background:rgba(255,255,255,.68)}.topline{display:flex;justify-content:space-between;gap:10px;color:var(--muted);font:850 11px/1.15 var(--ui)}.repo{max-width:58%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;text-align:right}.sample{align-self:center;font-size:clamp(22px,1.65vw,34px);line-height:1.08;letter-spacing:0;word-break:keep-all}.name{min-width:0;color:#30353a;font:800 12px/1.25 var(--ui);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.empty{padding:56px;border:1px solid var(--line);border-radius:8px;background:rgba(255,255,255,.48);color:var(--muted);font-weight:800}@media(max-width:920px){.shell{width:min(100% - 20px,760px);margin:10px auto}header{grid-template-columns:1fr;padding:26px 18px 18px}.layout{grid-template-columns:1fr}aside{border-right:0;border-bottom:1px solid var(--line)}.tabs{grid-template-columns:repeat(2,minmax(0,1fr))}main{padding:16px}.bar{grid-template-columns:1fr}.guide.visible{grid-template-columns:1fr}.guideMeta{border-left:0;border-top:1px solid var(--line)}}
"""


def script_block(fonts: list[dict[str, Any]], categories: list[dict[str, Any]], scenarios: list[dict[str, Any]]) -> str:
    data = json.dumps(fonts, ensure_ascii=False, indent=2)
    cats = json.dumps(categories, ensure_ascii=False, indent=2)
    scens = json.dumps(scenarios, ensure_ascii=False, indent=2)
    return f"""
const FONT_DATA={data};const CATEGORIES={cats};const SCENARIOS={scens};
const loadedSheets=new Set();const loadedStyles=new Set();let activeCategory='curated';let activeScenario=null;
const tabs=document.getElementById('tabs'),scenarioList=document.getElementById('scenarioList'),grid=document.getElementById('grid'),title=document.getElementById('categoryTitle'),meta=document.getElementById('resultMeta'),search=document.getElementById('search'),guide=document.getElementById('guide');
function loadFont(font){{if(font.styleTag&&!loadedStyles.has(font.id)){{const tpl=document.createElement('template');tpl.innerHTML=font.styleTag.trim();document.head.append(...tpl.content.childNodes);loadedStyles.add(font.id)}}if(font.stylesheet&&!loadedSheets.has(font.stylesheet)){{const link=document.createElement('link');link.rel='stylesheet';link.href=font.stylesheet;link.type='text/css';document.head.appendChild(link);loadedSheets.add(font.stylesheet)}}}}
function esc(v){{return String(v??'').replace(/[&<>"]/g,function(c){{return {{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]}})}}
function renderTabs(){{tabs.innerHTML=CATEGORIES.map(function(cat){{return '<button class="tab" type="button" data-category="'+cat.id+'" aria-selected="'+(!activeScenario&&cat.id===activeCategory)+'"><span>'+cat.label+'</span><span class="count">'+cat.count+'</span></button>'}}).join('')}}
function renderScenarios(){{scenarioList.innerHTML=SCENARIOS.map(function(s){{return '<button class="scenario" type="button" data-scenario="'+s.id+'" aria-selected="'+(activeScenario&&activeScenario.id===s.id)+'">'+esc(s.label)+'</button>'}}).join('')}}
function byId(id){{return FONT_DATA.find(function(font){{return font.id===id}})}}
function filteredFonts(){{const q=search.value.trim().toLowerCase();if(activeScenario&&!q){{return activeScenario.font_ids.map(byId).filter(Boolean).map(function(font){{return Object.assign({{}},font,{{scenarioSample:activeScenario.sample}})}})}}return FONT_DATA.filter(function(font){{const inCategory=q||font.category===activeCategory;const hay=(font.name+' '+font.provider+' '+font.categoryLabel+' '+font.sample).toLowerCase();return inCategory&&(!q||hay.indexOf(q)!==-1)}})}}
function roleName(id){{if(!activeScenario)return '';if(id===activeScenario.body)return 'body';if(id===activeScenario.heading)return 'heading';if(id===activeScenario.code)return 'code';return 'candidate'}}
function renderGuide(){{if(!activeScenario||search.value.trim()){{guide.className='guide';guide.innerHTML='';return}}guide.className='guide visible';guide.innerHTML='<div class="guideMain"><p class="tone">'+esc(activeScenario.tone)+'</p><p class="best">'+esc(activeScenario.best_when)+'</p><p class="avoid">'+esc(activeScenario.avoid)+'</p></div><div class="guideMeta"><div class="roles"><div class="role"><span>body</span><strong>'+esc(byId(activeScenario.body)?.name||'-')+'</strong></div><div class="role"><span>heading</span><strong>'+esc(byId(activeScenario.heading)?.name||'-')+'</strong></div><div class="role"><span>code</span><strong>'+esc(byId(activeScenario.code)?.name||'-')+'</strong></div></div></div>'}}
function render(){{renderTabs();renderScenarios();renderGuide();const fonts=filteredFonts();const category=CATEGORIES.find(function(cat){{return cat.id===activeCategory}});title.textContent=search.value.trim()?'검색 결과':(activeScenario?activeScenario.label:category.label);meta.textContent=fonts.length+' fonts';fonts.slice(0,180).forEach(loadFont);if(!fonts.length){{grid.innerHTML='<div class="empty">조건에 맞는 폰트가 없습니다.</div>';return}}grid.innerHTML=fonts.slice(0,180).map(function(font,index){{const role=roleName(font.id);const label=role?role:font.provider;return '<article class="card '+font.category+(activeScenario?' scenarioPick':'')+'"><div class="topline"><span>'+String(index+1).padStart(2,'0')+'</span><span class="repo">'+esc(label)+'</span></div><div class="sample" data-font-index="'+index+'">'+esc(font.scenarioSample||font.sample)+'</div><div class="name" title="'+esc(font.name)+'">'+esc(font.name)+'</div></article>'}}).join('');grid.querySelectorAll('.sample').forEach(function(node){{const font=fonts[Number(node.dataset.fontIndex)];if(font)node.style.fontFamily=font.family}});if(fonts.length>180){{grid.insertAdjacentHTML('beforeend','<div class="empty">'+(fonts.length-180)+'개가 더 있습니다. 검색어나 카테고리로 좁혀 보세요.</div>')}}}}
tabs.addEventListener('click',function(event){{const button=event.target.closest('button[data-category]');if(!button)return;activeCategory=button.dataset.category;activeScenario=null;search.value='';render()}});
scenarioList.addEventListener('click',function(event){{const button=event.target.closest('button[data-scenario]');if(!button)return;activeScenario=SCENARIOS.find(function(s){{return s.id===button.dataset.scenario}});search.value='';render()}});
search.addEventListener('input',function(){{activeScenario=null;render()}});
render();
"""


def main() -> None:
    items, archive_doc, guide = build_items()
    counts = {category: sum(1 for font in items if font["category"] == category) for category in CATEGORY_LABELS}
    categories = [
        {"id": category, "label": label, "count": counts.get(category, 0)}
        for category, label in CATEGORY_LABELS.items()
    ]
    html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Korean Vibe Fonts Decision Showcase</title>
  <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin="anonymous">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <style>{style_block()}</style>
</head>
<body>
  <div class="shell">
    <header>
      <div>
        <p class="eyebrow">Korean Vibe Fonts / decision guide + fonts-archive</p>
        <h1>상황별로 고르는<br>상업용 한글 웹폰트</h1>
      </div>
      <p class="summary">먼저 상황을 고르면 body, heading, code 역할별 추천이 좁혀집니다. 더 넓게 보고 싶을 때는 느낌 카테고리나 검색을 쓰세요.</p>
    </header>
    <div class="layout">
      <aside>
        <input id="search" class="search" type="search" placeholder="폰트명, repo, 느낌 검색" autocomplete="off">
        <p class="sideTitle">상황별 추천</p>
        <nav id="scenarioList" class="scenarioList" aria-label="Font decision scenarios"></nav>
        <p class="sideTitle">느낌 카테고리</p>
        <nav id="tabs" class="tabs" aria-label="Font categories"></nav>
        <div class="metaBox"><strong>{len(items)}</strong>개 표시 가능<br>상황 프리셋 {len(guide["scenarios"])}개<br>fonts-archive 스캔 {archive_doc["total_repositories_scanned"]}개 중 {archive_doc["included_count"]}개 포함<br>조건부/비상업/불명확 {archive_doc["excluded_count"]}개 제외</div>
      </aside>
      <main>
        <div class="bar"><h2 id="categoryTitle">큐레이션 핵심</h2><div id="resultMeta" class="resultMeta"></div></div>
        <section id="guide" class="guide" aria-live="polite"></section>
        <section id="grid" class="grid" aria-live="polite"></section>
      </main>
    </div>
  </div>
  <script>{script_block(items, categories, guide["scenarios"])}</script>
</body>
</html>
"""
    SHOWCASE.write_text(html, encoding="utf-8")
    INDEX.write_text(html, encoding="utf-8")
    print(
        f"Wrote {SHOWCASE} and {INDEX} with "
        f"{len(items)} fonts and {len(guide['scenarios'])} scenarios."
    )


if __name__ == "__main__":
    main()
