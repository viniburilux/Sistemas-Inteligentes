# GhostWorks

**Motor de inteligência territorial semântica sobre embeddings de satélite.**

[Repositório](https://github.com/viniburilux/ghostworks) · [Atlas](https://github.com/viniburilux/ghostworks-atlas)

---

## Problema

Monitorar transformação territorial (mineração, expansão agrícola, urbanização, energia) exige análise de imagens de satélite de alta resolução, geralmente com custo proibitivo. Dados abertos (Landsat, Sentinel) existem, mas extrair deles sinais precoces de mudança é tecnicamente desafiador.

## O que construímos

Um motor que:

- Usa **embeddings AlphaEarth** (DeepMind) para representar o território em 64 dimensões
- Calcula o **índice TTI** (Transformação Territorial) como 1 − cosine similarity entre embeddings temporais
- Detecta **mudança precoce** sem supervisão humana
- Opera sob **orçamento zero** — só dados abertos e infraestrutura própria
- Serializa, versiona e permite consulta por região/fenômeno

## Resultados

- [TTI Brasil 2017-2024](https://github.com/viniburilux/TTI_Brazil_2017_2024): raster nacional 2km com 8 anos de série temporal
- [GhostWorks Atlas](https://github.com/viniburilux/ghostworks-atlas): 887 trajetórias de embeddings em 6 fenômenos (mina, garimpo, fronteira agrícola, petróleo, petroquímica, mar interior)
- Validação Sentinel-2 com 36 pontos (47-80% confirmação)
- **Achado contra-intuitivo**: Nordeste lidera transformação média, não Amazônia
- **Caso Remanso/BA**: detectado antes de aparecer em literatura
- Distribuição heavy-tailed: poucas regiões concentram a maior parte da transformação

## Reconhecimento externo

- Paper "Territorial Change Detection Under Zero-Budget Constraints" aceito no **IJCAI-ECAI 2026 / GlobalSouthAI** workshop
- [Manguezais SP](https://luxverso.com/Manguezais-Brasil/manguezais-sp): case completo com 4.000 pontos, 7 anos, 364 artigos cruzados

## Aplicações

- **Mineração**: detecção precoce de novas frentes
- **Energia**: mapeamento de expansão renovável no Nordeste
- **Meio ambiente**: monitoramento de manguezais, desmatamento, queimadas
- **Governo**: cruzamento com dados públicos (PNCP, FIRMS) para fiscalização