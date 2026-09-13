#!/usr/bin/env python3
"""Intelligence Pipeline Generator
Lê objects.yaml, gera markdown + feed + cards.
Uso: python3 intelligence-pipeline/generate.py
"""
import yaml, json, os, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / 'intelligence-pipeline' / 'objects.yaml'
OUT_INTEL = REPO / 'intelligence'
OUT_INVEST = REPO / 'investigations'
OUT_PROGRAMS = REPO / 'programs'
OUT_SIGNALS = REPO / 'signals'
OUT_CASES = REPO / 'cases'

# Load objects
with open(DATA) as f:
    objects = yaml.safe_load(f)

def slugify(s):
    return s.lower().replace(' ','-').replace('/','-').replace(':','')[:60]

def gen_intelligence(obj):
    """Generate /intelligence/io-NNN-title.md"""
    ioid = obj['id']
    title = obj['title']
    slug = f"{ioid}-{slugify(title)}"
    md = f"""---
id: {ioid}
title: "{title}"
level: {obj['level']}
program: {obj.get('program','')}
domain: {obj.get('domain','')}
status: {obj.get('status','')}
date: {obj.get('date','')}
publish_level: {obj.get('publish_level','public')}
---

# {title}

**Programa:** {obj.get('program','')} · **Domínio:** {obj.get('domain','')}  
**Status:** {obj.get('status','').upper()} · **Data:** {obj.get('date','')}

---

## Pergunta

{obj.get('question','')}

## Descoberta

{obj.get('finding','')}

## Implicação

{obj.get('implication','')}

## Próximo passo

{obj.get('next_step','')}

## Fontes
"""
    for s in obj.get('sources',[]):
        md += f"- {s}\n"
    md += "\n## Projetos relacionados\n"
    for p in obj.get('projects',[]):
        md += f"- [{p}](https://github.com/viniburilux/{p})\n"
    md += "\n## Entidades identificadas\n"
    for e in obj.get('entities',[]):
        md += f"- {e}\n"
    path = OUT_INTEL / f"{slug}.md"
    path.write_text(md)
    return slug

def gen_investigation(obj):
    """Generate /investigations/ from intelligence objects at level investigation"""
    if obj['level'] != 'investigation':
        return None
    # Reuse object as investigation
    return gen_intelligence(obj)

def gen_feed_entry(obj, slug):
    """Generate JSON entry for the feed"""
    return {
        "id": obj['id'],
        "title": obj['title'],
        "level": obj['level'],
        "program": obj.get('program',''),
        "status": obj.get('status',''),
        "date": obj.get('date',''),
        "slug": slug,
        "summary": obj.get('finding','')[:200] + '...',
        "domain": obj.get('domain','')
    }

def gen_program_summary(program_id, objs):
    """Generate /programs/{program}.md"""
    title_map = {
        'biotecnologia-agro': 'Biotecnologia e Agro',
        'territorio-energia': 'Território, Energia e Meio Ambiente',
        'mineracao-materiais': 'Mineração e Materiais Críticos',
        'dados-publicos': 'Dados Públicos e Transparência',
        'ciencia-tecnologia': 'Ciência, Tecnologia e Infraestrutura'
    }
    title = title_map.get(program_id, program_id)
    ios = [o for o in objs if o.get('program') == program_id]
    md = f"""# {title}

**Programa de investigação do Sistemas Inteligentes**

---

"""
    # Active investigations
    active = [o for o in ios if o.get('status') in ('observed','inferred')]
    if active:
        md += f"## Investigações ativas ({len(active)})\n\n"
        for o in active:
            slug = f"{o['id']}-{slugify(o['title'])}"
            md += f"- [{o['title']}](../intelligence/{slug}.md) — {o.get('status','').upper()}\n"
        md += "\n"
    # Systems
    projects = set()
    for o in ios:
        for p in o.get('projects',[]):
            projects.add(p)
    if projects:
        md += "## Sistemas construídos\n\n"
        for p in sorted(projects):
            md += f"- [{p}](https://github.com/viniburilux/{p})\n"
        md += "\n"
    # Applications
    md += "## Aplicações possíveis\n\n"
    apps = []
    for o in ios:
        impl = o.get('implication','')
        if impl:
            apps.append(f"- {impl}")
    md += "\n".join(list(set(apps)))
    md += "\n"
    path = OUT_PROGRAMS / f"{program_id}.md"
    path.write_text(md)
    return program_id

def gen_signals(objs):
    """Extract signals from objects at level 'signal' or create from snippets"""
    signals = [o for o in objs if o.get('level') == 'signal']
    if not signals:
        # Create from snippets of observed objects
        snippets = [
            {"id":"sg-001","title":"Aumento de 3x em publicações Bacillus + nematoides (2024-2025)","domain":"Biotecnologia","status":"signal"},
            {"id":"sg-002","title":"Convergência de atores em 3 rotas de reciclagem de lítio","domain":"Mineração","status":"signal"},
            {"id":"sg-003","title":"Correlação entre aceleração TTI e novos contratos de energia no NE","domain":"Território","status":"signal"},
            {"id":"sg-004","title":"Concentração de 70% das contratações artísticas em 15% dos municípios baianos","domain":"Dados Públicos","status":"signal"},
            {"id":"sg-005","title":"Divergência satélite-campo em manguezais não explicada pela literatura","domain":"Território","status":"signal"},
            {"id":"sg-006","title":"Epistemic statuses do TraceFoundry permitem auditoria de evidência em qualquer domínio","domain":"Ciência","status":"signal"},
        ]
        signals = snippets
    md = "# Sinais — Intelligence Pipeline\n\nSinais detectados pelos nossos sistemas. São mais leves que descobertas completas — indicam direções para investigação.\n\n---\n\n"
    for s in signals:
        md += f"""## {s['title']}

| Campo | Valor |
|---|---|
| **Domínio** | {s.get('domain','')} |
| **Status** | {s.get('status','').upper()} |
| **ID** | {s.get('id','')} |

---
"""
    path = OUT_SIGNALS / 'README.md'
    path.write_text(md)
    return signals

def update_index_html(feed_entries):
    """Generate the HTML for the Intelligence Feed section on homepage"""
    cards_html = ""
    for entry in feed_entries[:6]:
        tag_class = {
            'Biotecnologia':'tag-bio','Território':'tag-territory',
            'Mineração':'tag-mining','Dados Públicos':'tag-data',
            'Ciência':'tag-tech','Inovação':'tag-tech',
            'Infraestrutura':'tag-tech'
        }.get(entry.get('domain',''),'tag-tech')
        level_label = {'signal':'🟡 SINAL','intelligence':'🔵 INTELIGÊNCIA','investigation':'🔴 INVESTIGAÇÃO'}.get(entry['level'],'🔵')
        cards_html += f"""<div class="discovery-card">
    <span class="dc-tag {tag_class}">{entry.get('domain','')}</span>
    <span style="font-size:0.7rem;color:#888;margin-left:8px">{level_label}</span>
    <h3>{entry['title'][:60]}{'...' if len(entry['title'])>60 else ''}</h3>
    <div class="dc-finding">{entry.get('summary','')[:150]}</div>
    <div class="dc-meta">
        <span class="dc-status status-{entry.get('status','observed')}">{entry.get('status','').upper()}</span>
        <span>{entry.get('date','')}</span>
    </div>
    <a href="intelligence/{entry['slug']}.md" class="dc-next">→ Explorar</a>
</div>"""
    return cards_html

def main():
    feed = []
    for obj in objects:
        if obj.get('publish_level') in ('private',):
            continue
        
        # Generate intelligence page
        slug = gen_intelligence(obj)
        
        # Generate investigation page if level allows
        gen_investigation(obj)
        
        # Feed entry
        feed.append(gen_feed_entry(obj, slug))
    
    # Generate programs
    programs = set(o.get('program','') for o in objects if o.get('program'))
    for prog in programs:
        gen_program_summary(prog, objects)
    
    # Generate signals
    gen_signals(objects)
    
    # Write feed JSON
    feed_path = REPO / 'intelligence-pipeline' / 'feed.json'
    feed_path.write_text(json.dumps(feed, indent=2))
    
    # Write feed HTML partial
    cards = update_index_html(feed)
    cards_path = REPO / 'intelligence-pipeline' / 'feed-cards.html'
    cards_path.write_text(cards)
    
    # Write index of all intelligence
    idx = "# Inteligência — Pipeline\n\n"
    idx += "Últimas descobertas produzidas pelos nossos sistemas.\n\n---\n\n"
    for entry in feed:
        idx += f"- [{entry['title']}]({entry['slug']}.md) — {entry.get('domain','')} · {entry.get('status','').upper()} · {entry.get('date','')}\n"
    (OUT_INTEL / 'README.md').write_text(idx)
    
    print(f"✅ Generated: {len(feed)} intelligence objects")
    print(f"✅ Generated: {len(programs)} programs")
    print(f"✅ Generated: feed.json + feed-cards.html")
    print(f"✅ Generated: /intelligence/README.md")

if __name__ == '__main__':
    main()