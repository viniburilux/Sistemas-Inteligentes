# Inteligência territorial

**Detecção precoce de transformação via embeddings de satélite com validação independente.**

---

## O que é

Capacidade de monitorar transformação territorial (mineração, agricultura, urbanização, energia) usando embeddings de satélite de código aberto, sem depender de imagens de alta resolução pagas.

## Como funciona

1. Embeddings AlphaEarth (64-dim) extraídos de imagens Sentinel-2/Landsat
2. Índice TTI = 1 − cosine similarity entre embeddings de anos consecutivos
3. Identificação de regiões com aceleração ou desaceleração de mudança
4. Validação com imagens de alta resolução e cruzamento com dados auxiliares

## Componentes usados

- [TTI Brasil 2017-2024](https://github.com/viniburilux/TTI_Brazil_2017_2024): índice nacional
- [GhostWorks Atlas](https://github.com/viniburilux/ghostworks-atlas): 887 trajetórias
- [Manguezais SP](https://luxverso.com/Manguezais-Brasil/manguezais-sp): case completo

## Evidência

- Paper aceito no IJCAI-ECAI 2026 (GlobalSouthAI)
- Validação Sentinel-2 com 36 pontos (47-80% confirmação)
- Notebook Colab reproduzível no Earth Engine
- Dataset público CC-BY 4.0

## Aplicações

- **Mineração**: detecção precoce de novas frentes
- **Energia**: monitoramento de expansão renovável
- **Meio ambiente**: queimadas, desmatamento, manguezais
- **Governo**: cruzamento com dados de contratos e fiscalização