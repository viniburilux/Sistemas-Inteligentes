#!/usr/bin/env python3
"""Run the generator - no pip needed."""
import sys
sys.path.insert(0, '/home/vinicius/.local/lib/python3.*/site-packages')
import yaml, json, os
from pathlib import Path

REPO = Path('/home/vinicius/Sistemas-Inteligentes')
DATA = REPO / 'intelligence-pipeline' / 'objects.yaml'
OUT_INTEL = REPO / 'intelligence'
OUT_PROGRAMS = REPO / 'programs'
OUT_SIGNALS = REPO / 'signals'

with open(DATA) as f:
    objects = yaml.safe_load(f)

def slugify(s):
    return s.lower().replace(' ','-').replace('/','-').replace(':','')[:60]

program_titles = {
    'biotecnologia-agro': 'Biotecnologia e Agro',
    'territorio-energia': 'Território, Energia e Meio Ambiente',
    'mineracao-materiais': 'Mineração e Materiais Críticos',
    'dados-publicos': 'Dados Públicos e Transparência',
    'ciencia-tecnologia': 'Ciência, Tecnologia e Infraestrutura'
}

tag_classes = {
    'Biotecnologia / Agro':'tag-bio','Território / Sensoriamento Remoto':'tag-territory',
    'Território / Mineração / Energia':'tag-territory','Mineração / Materiais Críticos':'tag-mining',
    'Sensoriamento / Controle de Qualidade':'tag-tech','Meio Ambiente / Território':'tag-territory',
    'Dados Públicos / Transparência':'tag-data','Neurociência / Ciência':'tag-tech',
    'Inovação / Oportunidades':'tag-tech','Representação de Conhecimento':'tag-tech',
    'Infraestrutura de Investigação':'tag-tech','Mineração':'tag-mining',
    'Indústria / Mineração / Energia':'tag-mining','Metodologia de Investigação':'tag-tech',
    'Dados Públicos':'tag-data'
}

# Generate intelligence pages
feed = []
for obj in objects:
    if obj.get('publish_level') == 'private':
        continue
    
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
    
    (OUT_INTEL / f"{slug}.md").write_text(md)
    
    feed.append({
        "id": ioid, "title": title, "level": obj['level'],
        "program": obj.get('program',''), "status": obj.get('status',''),
        "date": obj.get('date',''), "slug": slug,
        "summary": obj.get('finding','')[:200],
        "domain": obj.get('domain',''),
        "tag_class": tag_classes.get(obj.get('domain',''),'tag-tech')
    })

# Generate programs
programs = set(o.get('program','') for o in objects if o.get('program'))
for prog in programs:
    title = program_titles.get(prog, prog)
    ios = [o for o in objects if o.get('program') == prog and o.get('publish_level') != 'private']
    
    md = f"# {title}\n\n**Programa de investigação do Sistemas Inteligentes**\n\n---\n\n"
    active = [o for o in ios if o.get('status') in ('observed','inferred')]
    
    if active:
        md += f"## Investigações ativas ({len(active)})\n\n"
        for o in active:
            s = f"{o['id']}-{slugify(o['title'])}"
            md += f"- [{o['title']}](../intelligence/{s}.md) — {o.get('status','').upper()}\n"
        md += "\n"
    
    projects = set()
    for o in ios:
        for p in o.get('projects',[]):
            projects.add(p)
    if projects:
        md += "## Sistemas construídos\n\n"
        for p in sorted(projects):
            md += f"- [{p}](https://github.com/viniburilux/{p})\n"
        md += "\n"
    
    md += "## Aplicações possíveis\n\n"
    apps = []
    for o in ios:
        impl = o.get('implication','')
        if impl:
            apps.append(f"- {impl}")
    md += "\n".join(list(set(apps))) + "\n"
    
    (OUT_PROGRAMS / f"{prog}.md").write_text(md)

# Generate signals
signals = """# Sinais

Sinais detectados pelos nossos sistemas. Mais leves que descobertas completas — indicam direções para investigação.

---

- **sg-001** — Aumento de 3x em publicações Bacillus + nematoides (2024-2025) · Biotecnologia
- **sg-002** — Convergência de atores em 3 rotas de reciclagem de lítio · Mineração
- **sg-003** — Correlação entre aceleração TTI e novos contratos de energia no NE · Território
- **sg-004** — Concentração de 70% das contratações artísticas em 15% dos municípios baianos · Dados Públicos
- **sg-005** — Divergência satélite-campo em manguezais não explicada pela literatura · Território
- **sg-006** — Epistemic statuses do TraceFoundry permitem auditoria em qualquer domínio · Ciência
"""
(OUT_SIGNALS / 'README.md').write_text(signals)

# Write feed JSON
feed_data = {
    "generated": "2026-09-13",
    "total": len(feed),
    "entries": feed
}
(REPO / 'intelligence-pipeline' / 'feed.json').write_text(json.dumps(feed_data, indent=2))

# Write intelligence index
idx = "# Inteligência — Pipeline\n\nÚltimas descobertas produzidas pelos nossos sistemas.\n\n---\n\n"
for e in feed:
    idx += f"- [{e['title']}]({e['slug']}.md) — {e.get('domain','')} · {e.get('status','').upper()} · {e.get('date','')}\n"
(OUT_INTEL / 'README.md').write_text(idx)

print(f"✅ Generated: {len(feed)} intelligence objects")
print(f"✅ Generated: {len(programs)} programs")
print(f"✅ Generated: signals")
print(f"✅ Generated: feed.json")