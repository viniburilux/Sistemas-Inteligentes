# Agentes de investigação

**Sistemas multiagente com capacidades catalogadas, playbooks operacionais e integração com memória persistente.**

---

## O que é

Agentes que recebem uma pergunta, consultam fontes, estruturam evidência, produzem inteligência e registram o processo — tudo usando componentes existentes do ecossistema.

## Capacidades dos agentes

- **Descoberta**: web_search, OpenAlex, PatentsView, DANDI
- **Estruturação**: contratos TraceFoundry (EvidenceReference, Claim)
- **Proveniência**: versionamento por hash, estados epistêmicos
- **Memória**: consulta e retomada via LuxMemory
- **Handoff**: retomada de investigação por outro agente

## Hermes Bridge

A [luxverso-hermes-bridge](https://github.com/viniburilux/luxverso-hermes-bridge) materializa a conexão entre agente e ecossistema:
- Registry de 21 capabilities com evidência em código
- 3 playbooks reais (investigate-new-domain, repository-archaeology, data-source-discovery)
- Skill opportunity-router
- Cliente LuxMemory

## Evidência de funcionamento

[Experimento Lux vs LLM](https://github.com/viniburilux/Sistemas-Inteligentes/blob/main/evidence/experimento-lux-vs-llm.md): um agente usando a infraestrutura Lux respondeu a mesma pergunta (nematoides em soja) com rastreabilidade, separação epistêmica e gaps declarados — a versão LLM pura respondeu sem proveniência.

## Próximo passo

Completar o ciclo: pergunta → descoberta → evidência → memória → handoff. Validar se as interfaces existentes se conectam antes de construir qualquer nova capacidade.