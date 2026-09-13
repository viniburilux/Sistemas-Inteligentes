# Lux-Radar

**Motor de opportunity intelligence com pipeline semanal automatizado.**

[Repositório](https://github.com/viniburilux/Lux-Radar) · [Site](https://viniburilux.github.io/Lux-Radar/)

---

## Problema

Oportunidades de financiamento, editais e chamadas estão dispersas em dezenas de fontes públicas (Transferegov, FAPESB, BNDES, Finep). Acompanhá-las manualmente é inviável. Perder uma chamada relevante pode custar meses de oportunidade.

## O que construímos

Um motor que:

- **Coleta** fontes de oportunidade de forma declarada (config/sources.json)
- **Observa** mudanças e novas publicações
- **Estrutura** em observations, evidence, opportunities e signals
- **Versiona** releases semanais automaticamente (GitHub Actions)
- **Publica** como JSON/CSV navegáveis

## Resultados

- Pipeline rodando semanalmente desde o MVP
- Fontes reais: Transferegov, FAPESB, BNDES/Floresta Viva
- Schemas versionados e reutilizáveis
- Relação documentada com TraceFoundry (compatibilidade de contratos)

## Aplicações

- **P&D**: radar de editais para laboratórios e institutos
- **Startups**: identificação de chamadas de inovação
- **Governo**: mapeamento de oportunidades de financiamento por região/tema
- **IPT Open**: scouting de deeptechs e parcerias institucionais