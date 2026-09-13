# Arquitetura

**Como os sistemas inteligentes funcionam por dentro.**

---

## Visão geral

```
PERGUNTA
   ↓
DESCOBERTA (web_search, OpenAlex, PatentsView, DANDI, satélite)
   ↓
REPRESENTAÇÃO (grafos, séries temporais, redes, trajetórias)
   ↓
INVESTIGAÇÃO (evidência, proveniência, estados epistêmicos)
   ↓
SÍNTESE (inteligência acionável)
   ↓
AÇÃO (decisão, oportunidade, próximo passo)
```

## Componentes do ecossistema

| Camada | Componente | Função |
|---|---|---|
| **Mapa operacional** | [LuxOS](https://github.com/viniburilux/LuxOS) | Catálogo de capacidades, recipes, mapa de navegação |
| **Contratos de evidência** | [TraceFoundry](https://github.com/viniburilux/TraceFoundry) | EvidenceReference, Claim, estados epistêmicos, adapters |
| **Memória** | LuxMemory | Consulta, retomada, handoff entre agentes |
| **Descoberta** | web_search, OpenAlex, PatentsView, DANDI | Fontes públicas e científicas |
| **Território** | GhostWorks, TTI | Embeddings de satélite, detecção de transformação |
| **Oportunidades** | Lux-Radar | Captura e estruturação de editais e chamadas |
| **Agentes** | Hermes Bridge | Orquestração, capabilities catalogadas, playbooks |
| **Representação** | R0-R6 | Grafos, séries temporais, redes de atores e citações |

## Princípios

1. **Proveniência primeiro** — toda informação tem fonte rastreável
2. **Separação epistêmica** — observado ≠ inferido ≠ hipótese
3. **Gaps declarados** — o que não se sabe é tão importante quanto o que se sabe
4. **Reutilização transversal** — mesma capacidade funciona em domínios diferentes
5. **Público ≠ privado** — inteligência derivada é pública; dados e código sensíveis não

## Status atual

O ecossistema tem componentes funcionais e testados. O próximo passo é validar a **composição** entre eles — provar que um ciclo completo (pergunta → descoberta → evidência → memória) funciona de ponta a ponta usando apenas as interfaces existentes.

[Relatório completo de auditoria disponível no LuxOS](https://github.com/viniburilux/LuxOS)