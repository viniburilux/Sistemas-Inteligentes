# Proveniência e evidência

**Contratos canônicos com 7 estados epistêmicos, versionamento por hash e cadeia auditável.**

---

## O que é

Um sistema de contratos que modela o processo de investigação — de onde veio cada informação, como foi classificada e qual seu nível de confiança — independente do domínio ou da fonte.

## Os contratos

| Contrato | O que representa |
|---|---|
| `EvidenceReference` | Uma observação de fonte: artigo, dataset, API, patente — com URI, timestamp e metadata |
| `Claim` | Uma afirmação derivada da evidência — com status epistêmico |
| `EvidenceGap` | O que não foi encontrado — tão importante quanto o que foi |
| `ResearchMove` | A ação de investigação que conecta estado anterior ao posterior |

## Estados epistêmicos

| Status | Significado |
|---|---|
| `observed` | Diretamente extraído da fonte |
| `inferred` | Derivado de observações |
| `hypothesis` | Proposição não testada |
| `insufficient` | Evidência fraca demais para concluir |
| `blocked` | Não é possível investigar (acesso, método) |
| `rejected` | Testado e refutado |
| `contradicted` | Evidências conflitantes |

## Por que isso importa

Sem separação epistêmica, toda informação parece igualmente válida. Com os estados:
- O que é observado pode ser verificado (DOI, URI)
- O que é inferido é marcado como tal (não tratado como fato)
- Gaps são declarados (não omitidos)
- Contradições são registradas (não escondidas)

## Evidência de funcionamento

Os contratos foram testados em:
- [Investigações científicas](https://github.com/viniburilux/organoid-intelligence) (organoides, DANDI)
- [Inteligência biotecnológica](https://github.com/viniburilux/inteligencia-biotecnologica-agropecuaria) (763 obras, 2.680 atores)
- [Experimento Lux vs LLM](https://github.com/viniburilux/Sistemas-Inteligentes/blob/main/evidence/experimento-lux-vs-llm.md) (prova que resposta com infraestrutura é objetivamente melhor)