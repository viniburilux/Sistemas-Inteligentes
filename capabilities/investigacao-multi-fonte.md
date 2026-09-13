# Investigação multi-fonte

**Consulta simultânea a literatura, patentes, datasets públicos e APIs científicas, com evidência rastreável.**

---

## O que é

Capacidade de consultar múltiplas fontes heterogêneas em uma mesma investigação, estruturar os resultados em contratos de evidência unificados e preservar a proveniência de cada descoberta.

## Como funciona

1. Uma pergunta é formulada
2. Adaptadores específicos consultam cada fonte (OpenAlex, PatentsView, DANDI, web_search)
3. Resultados são normalizados em `EvidenceReference` (fonte, URI, observado_at, metadata_only)
4. Evidências são organizadas em `Claim` com status epistêmico
5. Gaps e contradições são explicitamente registrados

## Componentes usados

- TraceFoundry (contratos e adaptadores)
- web_search (descoberta pública)
- LuxMemory (persistência e consulta)

## Por que isso importa

Sem estrutura de evidência, cada consulta é um evento isolado e não reutilizável. Com os contratos, qualquer descoberta pode ser:
- verificada (tem DOI/URI)
- classificada (observado vs inferido)
- revisitada (persiste em memória)
- combinada (outra investigação pode usar a mesma evidência)

## Evidência de funcionamento

[Experimento](https://github.com/viniburilux/Sistemas-Inteligentes/blob/main/evidence/experimento-lux-vs-llm.md): mesma pergunta sobre controle biológico de nematoides em soja, mesmas 5 fontes web_search. Resposta com infraestrutura Lux tem rastreabilidade, separação epistêmica e gaps declarados — a resposta LLM pura não.