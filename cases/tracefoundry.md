# TraceFoundry

**Infraestrutura pública de investigação baseada em evidência.**

[Repositório](https://github.com/viniburilux/TraceFoundry) · [LuxVerso](https://luxverso.com)

---

## Problema

Investigação científica e tecnológica exige consulta a múltiplas fontes (literatura, patentes, datasets), cada uma com formato, qualidade e acesso diferentes. Sem uma estrutura comum de evidência, cada descoberta fica isolada e não reutilizável.

## O que construímos

Uma infraestrutura modular com:

- **Adapters reais**: DANDI (neurociência), Zenodo, OpenAlex (ciência aberta), PatentsView (patentes)
- **Contratos canônicos**: `EvidenceReference`, `Claim`, `EvidenceGap`, `ResearchMove` — tipos de dados que modelam a investigação
- **Estados epistêmicos**: observado, inferido, hipótese, insuficiente, bloqueado, rejeitado, contradito
- **Manifests versionados**: cada consulta é rastreável por hash
- **Seleção explicável**: critérios de relevância documentados e auditáveis
- **Testes offline + live**: fixtures com dados reais e modo metadata-only para APIs

## Resultados

- 4+ adapters funcionais para APIs científicas
- Schemas e contratos reutilizáveis em múltiplos domínios
- Benchmarks cross-domain (organoid, mangrove, lithium, mineral recovery)
- Playbooks de claim-audit e scientific staging
- Integração com LuxMemory e Hermes Bridge

## Aplicação

TraceFoundry é a **camada de confiança** do ecossistema. Qualquer investigação que precisa rastrear evidência até a fonte usa esses contratos. Funciona independente do domínio — o mesmo adapter OpenAlex serve para biotecnologia, mineração ou ciência de materiais.

## Evidência

- Repositório público com código, testes, fixtures e schemas
- Licença MIT
- Integração documentada com Lux-Radar, Inteligência Biotecnológica e Organoid Intelligence

## Próximo passo

Conectar os contratos de evidência a um ciclo de investigação automatizado — onde uma pergunta gera busca, que gera evidência, que gera claim, que persiste em memória.