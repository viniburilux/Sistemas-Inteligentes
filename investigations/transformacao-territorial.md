# Investigação: Transformação territorial no Brasil

**Tema:** Território / Mineração / Energia  
**Status:** OBSERVADO  
**Data:** Setembro 2026

---

## Pergunta

Onde o território brasileiro está mudando mais rapidamente e quais fenômenos estão associados a essa transformação?

## Sinal

Dados de satélite abertos (Sentinel-2, Landsat) processados via embeddings AlphaEarth revelam padrões de transformação que não aparecem em monitoramento tradicional.

## Descoberta

### TTI Brasil 2017-2024

O Índice de Transformação Territorial (1 − cosine similarity de embeddings AlphaEarth de 64 dimensões) foi calculado para todo o território brasileiro em resolução de 2km:

| Achado | Detalhe |
|---|---|
| **Nordeste lidera** | Transformação média mais alta, não a Amazônia (contra-intuitivo) |
| **Caso Remanso/BA** | Detectado por satélite antes de aparecer em qualquer literatura |
| **Distribuição heavy-tailed** | 10% das regiões concentram 70% da mudança |
| **Validação** | Sentinel-2 confirmou 47-80% dos pontos detectados |

### GhostWorks Atlas — 887 trajetórias

6 fenômenos monitorados (2018-2024):
- **Mineração**: Carajás — transformação contínua e previsível
- **Garimpo**: Yanomami — mudança irregular e sazonal
- **Fronteira agrícola**: MATOPIBA — expansão acelerada pós-2020
- **Petróleo**: Permian Flaring — o fenômeno mais distinto dinamicamente
- **Indústria**: Camaçari — transformação estável, baixa variação
- **Mar interior**: Aral Sea — colapso e estabilização

## Implicação

O monitoramento por embeddings de satélite detecta transformação precoce onde métodos convencionais (NDVI, mudança de uso) falham. Aplicável a:
- **Mineração**: detecção de novas frentes antes do licenciamento
- **Energia**: mapeamento de expansão renovável no Nordeste
- **Meio ambiente**: queimadas, desmatamento, manguezais
- **Governo**: cruzamento com contratos PNCP e fiscalização

## Próximo passo

Integrar TTI com dados de contratação pública (PNCP) para detectar correlações entre transformação territorial e gasto público.

## Proveniência

- Dataset CC-BY 4.0: github.com/viniburilux/TTI_Brazil_2017_2024
- Paper aceito: IJCAI-ECAI 2026 / GlobalSouthAI
- Notebook Colab reproduzível no Earth Engine