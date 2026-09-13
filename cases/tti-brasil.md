# TTI Brasil 2017-2024

**Índice de Transformação Territorial — um mapa nacional de mudança.**

[Repositório](https://github.com/viniburilux/TTI_Brazil_2017_2024) · [Notebook Colab](https://github.com/viniburilux/TTI_Brazil_2017_2024)

---

## Problema

Transformação territorial (mineração, agricultura, urbanização, energia) é monitorada por satélites de alta resolução com custo proibitivo. Dados abertos existem, mas extrair deles sinais precoces de mudança é tecnicamente complexo.

## O que construímos

Um índice nacional que:
- Usa **embeddings AlphaEarth** (64 dimensões) de imagens Sentinel-2/Landsat
- Calcula **TTI = 1 − cosine similarity** entre embeddings de anos consecutivos
- Gera um raster nacional de 2km de resolução (2017-2024)
- Opera com **custo computacional zero** (só dados abertos + Colab)

## Resultados

- Raster nacional disponível (CC-BY 4.0)
- Notebook Colab reproduzível no Earth Engine
- Validação Sentinel-2 com 36 pontos: **47-80% de confirmação**
- **Achado contra-intuitivo**: Nordeste lidera transformação média, não Amazônia
- **Caso Remanso/BA**: transformação detectada antes de aparecer em literatura
- Distribuição **heavy-tailed**: poucas regiões concentram a maior parte da mudança

## Reconhecimento

- Preprint disponível
- Base para paper aceito no IJCAI-ECAI 2026 (GlobalSouthAI)
- Dataset em Zenodo (em preparação)

## Aplicações

- Monitoramento de impacto de mineração e energia
- Detecção precoce de desmatamento e queimadas
- Planejamento territorial e ambiental
- Cruzamento com dados socioeconômicos e fiscais