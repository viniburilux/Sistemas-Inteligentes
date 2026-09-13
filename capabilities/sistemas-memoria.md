# Sistemas de memória

**Memória operacional consultável com handoff entre agentes.**

---

## O que é

Sistemas que persistem e recuperam o estado de investigações anteriores, permitindo que um agente retome o trabalho de outro sem recomeçar do zero.

## Como funciona

1. Investigações produzem assets, evidências, capabilities e skills
2. LuxMemory indexa em JSONL + SQLite com schemas versionados
3. `consult_resume()` produz um `handoff_seed` com IDs de origem, próxima ação e fronteira
4. `retrieve()` busca grounded por tokens e hash embedding determinístico

## Componentes usados

- LuxMemory (core: retrieve.py, consult_resume.py, app.py, schemas)
- LuxOS (mapa de capacidades)
- Hermes Bridge (conexão entre agente e memória)

## Limitação atual

Os paths do LuxMemory estão hardcoded para `/home/ubuntu/luxmemory` — não são reproduzíveis sem ajuste de ambiente. Não há write-back live de novas investigações para a memória.

## Próximo passo

Validar a conexão entre ciclo de investigação e memória: web_search → EvidenceReference → Claim → LuxMemory write-back → consult_resume() no próximo ciclo.