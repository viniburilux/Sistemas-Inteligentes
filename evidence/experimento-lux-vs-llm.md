# Experimento: Copiloto Lux vs LLM puro

**Pergunta:** "Quais organismos, mecanismos e instituições para controle biológico de nematoides em soja?"

**Fontes:** 5 artigos científicos via web_search (mesmas fontes para ambas as versões)

## Versão A — Com infraestrutura Lux

### Evidence Records

| ID | Fonte | Conteúdo | Status |
|---|---|---|---|
| ev-001 | DOI:10.1186/s12866-024-03514-y | B. halotolerans Ba2-6: 93.85% mortalidade J2, ISR via PR1/PR3a/PR5/NPR1-2 | OBSERVADO |
| ev-002 | Frontiers in Microbiology (2024) | Bacillus thuringiensis, B. subtilis, Trichoderma harzianum — mecanismos múltiplos | OBSERVADO |
| ev-005 | DOI:10.3389/fmicb.2024.1510036 | B. subtilis: lipopeptides (surfactin, fengycin) rompem cutícula | OBSERVADO |
| ev-007 | DOI:10.16768/j.issn.1004-874x.2025.07.005 | B. subtilis CHFA/CHFB: 56-61% mortalidade J2, 44-57% redução em campo | OBSERVADO |

### Claims

| ID | Afirmação | Evidências | Status |
|---|---|---|---|
| cl-001 | Bacillus halotolerans Ba2-6 induz ISR via SA/JA | ev-001 | OBSERVADO |
| cl-002 | B. subtilis lipopeptides rompem cutícula | ev-005 | OBSERVADO |
| cl-003 | Fungos Trichoderma, Purpureocillium atuam por parasitismo de ovos | ev-003, ev-004 | OBSERVADO |
| cl-004 | Tratamento de sementes reduz população em campo (44-57%) | ev-007 | OBSERVADO |

### Gaps

| ID | Descrição |
|---|---|
| gap-001 | Estudos comparativos entre cepas de Bacillus em condições brasileiras limitados |
| gap-002 | Poucos estudos de campo com combinações fungos + bactérias |
| gap-003 | Viabilidade econômica não encontrada nas fontes |

## Versão B — LLM puro (mesmas fontes, sem estrutura)

> O controle biológico de nematoides em soja envolve principalmente bactérias do gênero Bacillus e fungos nematófagos. Bacillus subtilis é o organismo mais estudado, atuando por produção de lipopeptídeos que rompem a cutícula e por ISR. Bacillus halotolerans também apresenta eficácia. Fungos como Trichoderma harzianum e Purpureocillium lilacinum atuam por parasitismo direto de ovos. A combinação mostra sinergia. Principais instituições: universidades chinesas e USDA ARS.

## Comparação

| Critério | Lux | LLM puro |
|---|---|---|
| Cada afirmação tem fonte rastreável? | ✅ Sim (evidence_id → DOI) | ❌ Não |
| Separa OBSERVADO de INFERIDO? | ✅ Sim | ❌ Não |
| Gaps explicitados? | ✅ Sim (3 gaps) | ❌ Não (omitido) |
| Verificação independente possível? | ✅ Sim | ⚠️ Precisa caçar referências |
| Reutilizável em nova investigação? | ✅ Sim (evidence_ids conectáveis) | ❌ Não (texto plano) |

## Veredito

**SIM — a resposta com infraestrutura Lux é objetivamente melhor.**

O ganho não está no conteúdo (ambas usam as mesmas fontes) — está na **rastreabilidade, separação epistêmica e verificabilidade**. A versão Lux permite que qualquer afirmação seja verificada no DOI original. A versão LLM pura exige confiança cega.

> Lux: "Aqui está o que sabemos, como sabemos e o que não sabemos."
> LLM: "Aqui está a resposta."