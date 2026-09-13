# LuxSense

**Sensor Raman com IA para controle de qualidade industrial.**

[Site](https://luxverso.com/luxsense) · [Paper (em revisão)](https://luxverso.com/evidence)

---

## Problema

Controle de qualidade industrial exige análise química rápida, não destrutiva e precisa. Espectroscopia Raman é uma técnica poderosa, mas a interpretação dos espectros exige especialistas — o que limita sua adoção em escala.

## O que construímos

Um sistema que combina:
- **Espectroscopia Raman** com pré-processamento ALS+SNV (remoção de fluorescência)
- **Random Forest / SVM** para classificação automática
- **3.510 espectros validados** em laboratório
- **99,43% de acurácia** com 702 amostras de teste (apenas 4 erros)

## Resultados

| Métrica | Valor |
|---|---|
| Espectros no dataset | 3.510 |
| Acurácia (Random Forest) | 99,43% |
| Amostras de teste | 702 |
| Erros | 4 |
| Estágio | TRL 3-4 |
| Paper | Frontiers in Nanotechnology (em revisão) |

## Aplicações

- **Farmacêutico**: identificação de insumos, detecção de adulteração
- **Alimentos**: autenticidade, origem, processamento
- **Petróleo e gás**: caracterização de combustíveis e lubrificantes
- **Mineração**: análise de minérios
- **Cosméticos**: formulação e QC
- **Bioetanol**: monitoramento de processo

## Oportunidade

Buscando ativamente **piloto industrial de 4-8 semanas** com dados reais de um parceiro. Se sua organização tem um problema de QC que espectroscopia pode resolver, podemos testar em semanas, não em meses.