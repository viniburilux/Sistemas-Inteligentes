# Arqueologia de Inteligência Derivada — Ecossistema LuxVerso

**Gerado em:** 2026-09-13
**Método:** Inspeção direta de 12+ repositórios privados no filesystem local
**Propósito:** Extrair inteligência derivada publicável no Sistemas-Inteligentes sem revelar código proprietário, dados sensíveis ou estratégia operacional

---

## Sumário Executivo

O ecossistema LuxVerso contém **inteligência derivada de alto valor publicável** em **6 das 8 áreas solicitadas**. Abaixo de cada área, o que **existe de fato**, o que **pode ser publicado**, o que **deve ficar privado**, e o **potencial de distribuição** (🔥) para o Sistemas-Inteligentes.

---

## 1. MATRIZ COMPLETA DE INTELIGÊNCIA DERIVADA

| # | Ativo | Repositório | Tipo | Pode publicar? | O que publicar? | Deve ficar privado? | 🔥 |
|---|---|---|---|---|---|---|---|
| **1.1** | **TTI — Territorial Transformation Index** | `TTI_Brazil_2017_2024` (público, preprint no Zenodo) | Índice de transformação territorial por satélite | ✅ **SIM** — preprint, raster, datasets e pipeline já estão sob CC-BY 4.0 | Paper (EN+PT), ranking de transformação por UF/município, validação Sentinel-2, raster nacional, notebook Colab reproduzível | — (já público) | 🔥🔥🔥🔥🔥 |
| **1.2** | **GhostWorks Atlas v1** | `gw_primary_ghostworks-atlas` | Dataset de 887 trajetórias de transformação territorial | ✅ **SIM** — dataset card, data dictionary, notebook quickstart, CSVs, .npy | **6 descobertas cientificamente validadas:** (a) Movie Retrieval — movimento vs posição final; (b) Dimensão intrínseca ~6-9 estável; (c) Recuperabilidade estatal; (d) Autocorrelação espacial (Moran's I 0.23-0.62); (e) Distintividade cruzada (Permian_Flaring mais distinto); (f) Estrutura contínua vs discreta (Hopkins 0.77-0.91) | Código de análise interno (notebooks não publicados), estratégia de amostragem proprietária | 🔥🔥🔥🔥🔥 |
| **1.3** | **GhostWorks Intelligence Pipeline** | `ghostworks` (archive) | Pipeline TTI + LLM bridge | ✅ **PARCIAL** — conceito e demo visual são publicáveis | Arquitetura conceitual do pipeline (embeddings → serialização → LLM → relatório territorial), casos de uso Aral Sea + MATOPIBA, `ghostworks_serializer.py` como conceito (não código literal) | Código do serializer (270 linhas proprietárias), prompts Gemma, estratégia de contexto | 🔥🔥🔥 |
| **1.4** | **GhostWorks Mining (página pública)** | `ghostworks/mining/` | Landing page pública | ✅ **SIM** — já é conteúdo público | Deep tech mining page com descrição de capacidade, casos de prova, mapa Leaflet interativo | — (já público) | 🔥🔥🔥 |

---

### 2. INVESTIGAÇÕES DE MINERAÇÃO (Materiais Críticos, Patentes Minerais, Processamento)

| # | Ativo | Repositório | Tipo | Pode publicar? | O que publicar? | Deve ficar privado? | 🔥 |
|---|---|---|---|---|---|---|---|
| **2.1** | **Corpus de Inteligência Metalúrgica** | `inteligencia-metalurgica/` | Corpus de 72 arquivos (43 ZIPs de patentes, 22 CSVs/JSONs, 5 docs, 2 PDFs) | ✅ **SIM — METODOLOGIA** | **Artigo de método**: como estruturar um corpus metalúrgico com proveniência SHA-256, manifesto de 72 itens, pipeline de normalização, entity resolution e separação evidência vs inferência. 22 datasets sobre materiais críticos (estanho, baterias, semicondutores, supply resilience). | Conteúdo das patentes (ZIPs com PDFs de terceiros sob licenças desconhecidas), dados brutos não normalizados | 🔥🔥🔥🔥 |
| **2.2** | **SIGMINE Mineral Retrieval v1/v2** | `Lux-Lab/sigmine_mineral_retrieval/` | Notebooks de retrieval mineral por embedding | ✅ **PARCIAL** | **Artigo de método**: "Retrieval de Assinatura Mineral por Embeddings de Satélite — pipeline arquitetônico usando SIGMINE/ANM + AlphaEarth + clustering + score híbrido". Descrição conceitual do pipeline: âncoras → embeddings → clustering → retrieval estrutural → delta temporal → score híbrido → validação. | Notebooks canônicos (código GEE proprietário), outputs de execução (CSVs de candidatos), estratégia de cluster/arquétipo | 🔥🔥🔥🔥 |
| **2.3** | **Mineral Retrieval Outputs** | `Lux-Lab/sigmine_mineral_retrieval/outputs/previous_runs/` | CSVs de outputs de retrieval | ❌ **NÃO** | — | Candidatos específicos por região (Pará, Carajás, Yanomami) — revelam alvos de investigação | — |

---

### 3. INTELIGÊNCIA INDUSTRIAL

| # | Ativo | Repositório | Tipo | Pode publicar? | O que publicar? | Deve ficar privado? | 🔥 |
|---|---|---|---|---|---|---|---|
| **3.1** | **Datasets de Materiais Críticos** | `inteligencia-metalurgica/datasets/` | 12 CSVs + 10 JSONs (baterias, semicondutores, supply resilience, estanho, processo) | ✅ **SIM — METADADOS AGREGADOS** | Taxonomia dos datasets: `critical_materials_battery.csv`, `critical_materials_semiconductor.csv`, `critical_materials_supply_resilience.csv`, `tin_hydrometallurgy_dataset.csv` — 22 datasets mapeados com esquemas, cobertura temporal, fontes | Linhas individuais dos datasets (podem conter dados de terceiros), valores específicos | 🔥🔥🔥 |
| **3.2** | **GhostWorks Atlas — Ecosystem Comparison** | `gw_primary_ghostworks-atlas/data/ecosystem_comparison_table.csv` | Tabela de 6 ecossistemas industriais comparados | ✅ **SIM** — tabela de 6 ecossistemas (Carajás mineração, Yanomami garimpo, MATOPIBA agro, Permian Flaring, Camacari industrial, Mar Aral) com dinâmicas transformacionais comparadas | Descoberta: Permian_Flaring (petróleo) é o mais distinto dinamicamente; Carajás (mineração industrial) é o menos distinto — implicações para monitoramento industrial | — (dados agregados, sem coordenadas precisas) | 🔥🔥🔥🔥 |

---

### 4. URBANISMO / CIDADES

| # | Ativo | Repositório | Tipo | Pode publicar? | O que publicar? | Deve ficar privado? | 🔥 |
|---|---|---|---|---|---|---|---|
| **4.1** | **PNCP Bahia Intelligence** | `Lux-Lab/pncp_bahia_intelligence/` | Pipeline de análise de contratações públicas | ✅ **PARCIAL** | **Artigo de método**: "Inteligência de Contratações Públicas com PNCP + Querido Diário — pipeline de triagem documental para jornalismo de dados". Conceitos: filtragem municipal, drilldown, queries temáticas, matching documental, governança e versionamento. | Scripts de análise (código proprietário), outputs com dados de municípios específicos, estratégias de busca temática | 🔥🔥🔥🔥 |
| **4.2** | **Radar-Contratos-BA** | (no archive, mas referenciado no ECOSYSTEM_REGISTRY) | Dashboard público PNCP Bahia (R$160M) | ✅ **SIM** — já é público | Dashboard React de contratações públicas da Bahia | — (já público) | 🔥🔥🔥 |
| **4.3** | **Lux-Radar** | `luxverso-archive/Lux-Radar/` (público) | Infraestrutura de inteligência de oportunidades | ✅ **SIM** — já é público (MIT) | Arquitetura de oportunidade intelligence: Source Registry → Observation → Evidence → Versioned Release → Canonical Opportunity. Schemas públicos (signal, evidence, opportunity). MVP operacional com 3 perfis de fonte (API/JSON, HTML+PDF, programa institucional) | — (já público) | 🔥🔥🔥 |

---

### 5. INTELIGÊNCIA TERRITORIAL

| # | Ativo | Repositório | Tipo | Pode publicar? | O que publicar? | Deve ficar privado? | 🔥 |
|---|---|---|---|---|---|---|---|
| **5.1** | **TTI Raster Nacional (GW_STT_2017_2024)** | `TTI_Brazil_2017_2024/raster/` + GEE Asset | Raster 10m Brasil continental | ✅ **SIM** — CC-BY 4.0 | Mapa de transformação territorial do Brasil 2017-2024, agregado por UF, município e grid 25km. Descoberta: Nordeste lidera transformação (Sergipe 0.146, Amazonas 0.018) | — (já público) | 🔥🔥🔥🔥🔥 |
| **5.2** | **GhostWorks — Motor de Inteligência Territorial Semântica** | `luxverso-archive/ghostworks/` | Documentação conceitual + demo | ✅ **SIM** — descrição conceitual publicável | Arquitetura: embeddings AlphaEarth (64D) → TTI → serialização → LLM → relatório territorial. Filosofia: "Não olhe para fotos de satélite. Leia a assinatura matemática do território." | Código do serializer, estratégias de prompt, contexto de LLM | 🔥🔥🔥🔥 |
| **5.3** | **GhostWorks Mining (Landing Page)** | `gw_primary_ghostworks/mining/` | Site HTML público com Leaflet | ✅ **SIM** — já é conteúdo público | Deep tech mining: mapa interativo, proof steps (1-4), capabilities grid, sensor strip, research room | — (já público, código HTML/CSS) | 🔥🔥🔥 |
| **5.4** | **TTI Validação Sentinel-2** | `TTI_Brazil_2017_2024/validation/` | Dataset de 36 candidatos validados | ✅ **SIM** | 47.2% forte concordância, 80.5% pelo menos 1 sensor independente confirmando transformação | Coordenadas exatas dos pontos de validação (potencialmente sensíveis) | 🔥🔥🔥 |

---

### 6. BIOTECNOLOGIA ESPECÍFICA

| # | Ativo | Repositório | Tipo | Pode publicar? | O que publicar? | Deve ficar privado? | 🔥 |
|---|---|---|---|---|---|---|---|
| **6.1** | **Inteligência Biotecnológica Agropecuária** | `inteligencia-biotecnologica-agropecuaria/` | Infraestrutura de investigação (pública com boundary documentada) | ✅ **SIM — INTEIRO** | O repositório já define explicitamente a fronteira público/privado em `PUBLIC_PRIVATE_BOUNDARY.md` e `ASIE_PUBLIC_BOUNDARY_V0.md`. Publicável: ASIE cycle logs, evidence manifests, entity resolution, structural reuse test (6 domínios mapeados), document acquisition method, signal map | Experimental scripts, question-generation policy, question prioritization, reformulation heuristics, adaptive memory policy | 🔥🔥🔥🔥🔥 |
| **6.2** | **Structural Reuse Test V1** | `inteligencia-biotecnologica-agropecuaria/` | Mapeamento de transferibilidade estrutural entre 6 domínios | ✅ **SIM** | **Descoberta publicável**: a estrutura entidade→caracterização→contexto→transformação→artefato→lacuna se transfere como **contrato de papéis e relações**, não como cadeia rígida. Mapeamento de 6 domínios: organoides, datasets públicos, GhostWorks/SIGMINE, patentes/mineração, satélite, PNCP Bahia | — (já público ou metodologia genérica) | 🔥🔥🔥🔥 |
| **6.3** | **OI-Organoids-Intelligence (publication candidates)** | `OI-Organoids-Intelligence/publication_candidates/` | 8 candidatos a publicação avaliados | ✅ **SIM — INTEIRO** | **8 candidatos avaliados com readiness**: P01 (temporal prediction - priority 1), P02 (provenance audit), P03 (question reformulation), P04 (experiment 002 negative result), P05 (ASIE state management), P06 (OI Sandbox), P07 (claims workflow), P08 (public research record). **Descoberta principal:** P01 é o candidato mais forte — previsão temporal com burst/backbone features em dados abertos DANDI. P02 mostra que hashes diferentes de arquivo ≠ dados neurais independentes. | Código de experimentos, dados brutos NWB, scripts de análise | 🔥🔥🔥🔥🔥 |
| **6.4** | **Experiment 002 — Negative Result** | `OI-Organoids-Intelligence/experiments/` | Experimento de previsão de desempenho organoide | ✅ **SIM — RESULTADO NEGATIVO** | **Descoberta**: características firing-rate e network NÃO melhoram predição de desempenho além de baseline mediana (MAE 24.24). Modelo firing-rate tem associação Spearman 0.359 (p=0.018) mas erros preditivos piores que baseline. Resultado negativo publicado é ciência válida. | Código dos experimentos, dados NWB brutos | 🔥🔥🔥🔥 |

---

### 7. AGENTES / MEMÓRIA

| # | Ativo | Repositório | Tipo | Pode publicar? | O que publicar? | Deve ficar privado? | 🔥 |
|---|---|---|---|---|---|---|---|
| **7.1** | **Investigation Factory** | `Lux-Lab/investigation_factory/` | Runtime de investigação autônoma com trajetórias | ✅ **PARCIAL** | **Arquitetura**: estado → seleciona próximo movimento → executa → observa → evidência → atualiza estado → snapshot → próxima ação → condição de parada. Factory com: aquisição, evidência, representações, trajetórias, auto-aprimoramento. Water Intelligence como primeiro caso de uso. | Código runtime (runtime.py, asie_runner.py), trajetórias específicas, manifestos de execução | 🔥🔥🔥🔥 |
| **7.2** | **ASIE — Autonomous Scientific Investigation Engine** | `inteligencia-biotecnologica-agropecuaria/` | Ciclos ASIE documentados | ✅ **SIM — RESULTADOS DE CICLO** | Ciclos ASIE registrados: cycle logs, state transitions, question transformations, fixed vs adaptive replay comparison, autonomous investigation v1 com evidências e fronteiras | Policy de geração de perguntas, ranking, adaptive memory | 🔥🔥🔥🔥 |
| **7.3** | **Agro State Adapter** | `inteligencia-biotecnologica-agropecuaria/operational_memory_agro_v0/` | Schemas e adapters de estado | ✅ **SIM — SCHEMAS** | Schemas de estado: `state_delta.schema.json`, `state_snapshot.schema.json`, `event.schema.json`, `value_delta.schema.json`. Contratos abertos de representação de estado investigativo | Código do adapter, estratégias de execução | 🔥🔥🔥 |
| **7.4** | **Machine Lab** | `Lux-Lab/machine_lab/` | Blueprint da máquina de investigação | ✅ **PARCIAL** | **Arquitetura documentada**: INVESTIGATION_MACHINE_BLUEPRINT.md, MACHINE_EVOLUTION_REGISTRY.yaml, capability_registry, composição de componentes, tests, versions, blueprint_data.json | Decision log (decisões operacionais), self-improvement backlog, diagnoses específicos | 🔥🔥🔥 |
| **7.5** | **LuxMemory** | `luxverso-archive/LuxMemory/` | Sistema de memória de longo prazo | ❌ **NÃO** (código) / ✅ **SIM** (conceito) | **Arquitetura conceitual**: sistema de memória com consulta, retomada, dados, schemas e catálogo de conversas. 30 ciclos de investigação anteriores descobertos em meta-inspeção. | Código fonte, dados de memória, grafos de entidades com 6.976 nós e 26.231 arestas | 🔥🔥 |

---

### 8. DATASETS E EXPERIMENTOS

| # | Ativo | Repositório | Tipo | Pode publicar? | O que publicar? | Deve ficar privado? | 🔥 |
|---|---|---|---|---|---|---|---|
| **8.1** | **GhostWorks Atlas Dataset** | `gw_primary_ghostworks-atlas/data/` | 887 trajetórias, 4435 transições, 6 ecossistemas | ✅ **SIM — CC-BY 4.0** | Dataset completo: `X_traj.npy` (887×768), `X_delta.npy` (4435×128), `trajectories_metadata.csv`, `matriz_markov.npy`, `ecosystem_comparison_table.csv`, `precursor_features.csv`. Inclui DATA_DICTIONARY.md completo. | — (dataset já está com card e dicionário prontos para publicação) | 🔥🔥🔥🔥🔥 |
| **8.2** | **TTI Datasets Completos** | `TTI_Brazil_2017_2024/datasets/` | CSVs estaduais, municipais, grids 25km, amostra pixel | ✅ **SIM — CC-BY 4.0** | 8 datasets: estadual (27 UFs), municipal (5.506), 5 grids regionais (N, NE, Central, SE, S), amostra aleatória N=10.000 | — (já no Zenodo/CC-BY) | 🔥🔥🔥🔥 |
| **8.3** | **Corpus Metalúrgico — Metodologia** | `inteligencia-metalurgica/` | Pipeline de normalização de 72 arquivos | ✅ **SIM — MÉTODO** | **Artigo de método**: como importar, manifestar e normalizar um corpus técnico-científico de 72 arquivos (43 ZIPs de patentes, 22 datasets, 7 documentos) com proveniência SHA-256, schema versionado, entity resolution planejada e pipeline incremental | Conteúdo dos ZIPs de patentes, dados brutos de datasets | 🔥🔥🔥🔥 |
| **8.4** | **Experimento 002 + 003 (OI)** | `OI-Organoids-Intelligence/experiments/` | Experimentos de previsão temporal com dados abertos NWB | ✅ **SIM — MÉTODO + RESULTADOS** | **P01**: previsão temporal 100ms com burst/backbone features em dados DANDI:001603. 3 assets HO2/HO3/HO4, leakage-safe. **P02**: audit de proveniência — 2 pares de arquivos NWB com hashes SHA-256 de arquivo diferentes mas payloads neurais idênticos | Dados NWB brutos (DANDI, públicos mas grandes), scripts de análise | 🔥🔥🔥🔥🔥 |
| **8.5** | **Water Intelligence (Investigation Factory)** | `Lux-Lab/investigation_factory/water_intelligence/` | Caso de uso água | ✅ **PARCIAL** | **Conceito**: Water Intelligence como primeiro caso de uso da Investigation Factory. GPIW discovery, IDWS discovery, signal map, evidence dossier | Investigation lines específicas, acquisition scripts, trajectory outputs | 🔥🔥🔥 |

---

## 9. ARQUITETURAS E ANÁLISES CONCLUÍDAS

| # | Ativo | Repositório | Tipo | Pode publicar? | O que publicar? | Deve ficar privado? | 🔥 |
|---|---|---|---|---|---|---|---|
| **9.1** | **CANONICAL_MACHINE_MAP.md** | `Lux-Lab/` | Mapa da máquina canônica | ✅ **PARCIAL** | **Arquitetura documentada**: 7-layer model (L0 Corpus → L1 Discovery → L2 State → L3 Frontier → L4 Investigation → L5 Execution → L6 Memory → L7 Experience). Diagnóstico: AIR v1 é simplificação; máquina real V3-V5 tem estado multidimensional, ASIE, FitoPharma golden run | Detalhes de implementação, deployment paths | 🔥🔥🔥🔥🔥 |
| **9.2** | **TraceFoundry** | `luxverso-archive/TraceFoundry/` (público, MIT) | Infraestrutura de evidência para investigação | ✅ **SIM — INTEIRO (já público)** | 8 capacidades: Discover, Normalize, Resolve, Select transparently, Preserve negative evidence, Represent claims/evidence, Track gaps, Propose Research Moves. Ciclo: Complex Question → Discovery → Evidence → Claims → Gaps → Research Move → Next Action. Adaptadores: DANDI, Zenodo, OpenAlex, PatentsView | — (já público, MIT) | 🔥🔥🔥🔥 |
| **9.3** | **LuxOS — Mapa Operacional** | `LuxOS/` | Catálogo operacional do ecossistema | ✅ **SIM — MÉTODO** | **Artigo de método**: como criar um mapa operacional de ecossistema técnico com 7 categorias de evidência (Existe, Especificado, Implementado, Utilizado, Integrado, Validado, Reutilizável). Fase 1+2 com catálogo de componentes, receitas, modelo estado/processo, avaliação de reúso. | Detalhes de repositórios-fonte específicos, caminhos de acesso | 🔥🔥🔥🔥 |
| **9.4** | **ECOSYSTEM_REGISTRY.yaml** | `Lux-Lab/ecosystem/` | Registry do ecossistema (gap audit) | ✅ **SIM — ESTRUTURA** | **Metodologia de gap audit**: registry foi atualizado de ~25% para ~90% de cobertura. 12 gaps fechados. Lições: GhostWorks corrigido de visão 1D para 3D, 20+ repos adicionados, 7 oportunidades registradas | Detalhes específicos de cada repo, caminhos de acesso | 🔥🔥🔥 |
| **9.5** | **CMOTP Replication** | `luxverso-archive/cmotp-replication/` | Protocolo CMOTP com DOI | ✅ **SIM — JÁ PÚBLICO** | Protocolo de replicação CMOTP com DOI 10.5281/zenodo.18013043 | — (já público) | 🔥🔥 |

---

## 10. PRIORIZAÇÃO PARA PUBLICAÇÃO NO SISTEMAS-INTELIGENTES

### 🔥🔥🔥🔥🔥 PRIORIDADE MÁXIMA (publicar imediatamente)

| # | Título sugerido | Conteúdo | Baseado em |
|---|---|---|---|
| P1 | **"TTI: Um Índice de Transformação Territorial Label-Agnóstico para o Brasil (2017-2024)"** | Preprint completo com ranking UF/município, validação Sentinel-2, caso Remanso/BA | TTI_Brazil_2017_2024 |
| P2 | **"GhostWorks Atlas: 887 Trajetórias de Transformação em 6 Ecossistemas"** | Dataset completo com 6 descobertas validadas | gw_primary_ghostworks-atlas |
| P3 | **"Quando Arquivos NWB Diferentes Contêm os Mesmos Dados Neurais"** | Audit de proveniência em dados abertos de organoides | OI P02 candidate |
| P4 | **"Previsão Temporal com Burst/Backbone Features em Registros de Organoides Humanos"** | Predição 100ms com dados DANDI abertos | OI P01 candidate |
| P5 | **"A Máquina de Investigação de 7 Camadas: Arquitetura para Investigação Tecnológica Reproduzível"** | Mapa canônico da máquina LuxVerso | CANONICAL_MACHINE_MAP.md |

### 🔥🔥🔥🔥 PRIORIDADE ALTA (publicar após revisão)

| # | Título sugerido | Conteúdo | Baseado em |
|---|---|---|---|
| P6 | **"Estrutura de Investigação que Transcende Domínios: Lições de 6 Territórios Tecnológicos"** | Structural Reuse Test com mapeamento de 6 domínios | structural_reuse_test |
| P7 | **"Inteligência de Contratações Públicas com PNCP + Querido Diário"** | Pipeline de triagem documental para jornalismo de dados | pncp_bahia_intelligence |
| P8 | **"Corpus Metalúrgico com Proveniência Verificável: Método para 72 Arquivos Técnico-Científicos"** | Pipeline de normalização com manifesto SHA-256 | inteligencia-metalurgica |
| P9 | **"Retrieval de Assinatura Mineral por Embeddings de Satélite"** | Pipeline conceitual SIGMINE + AlphaEarth | sigmine_mineral_retrieval |
| P10 | **"TraceFoundry: Infraestrutura de Evidência para Investigação Complexa"** | 8 capacidades + ciclo completo | TraceFoundry (já público) |
| P11 | **"ASIE: Ciclos Adaptativos de Investigação Científica Autônoma"** | Resultados de ciclos ASIE com fronteira público/privado documentada | asie_experiment_v0 |
| P12 | **"Resultado Negativo em Predição de Desempenho de Organoides"** | Firing-rate e network features NÃO superam baseline mediana | OI Experiment 002 |

### 🔥🔥🔥 PRIORIDADE MÉDIA

| # | Título sugerido | Conteúdo |
|---|---|---|
| P13 | **"GhostWorks Mining: Deep Tech de Inteligência Territorial"** | Landing page pública convertida em post técnico |
| P14 | **"Lux-Radar: Infraestrutura de Oportunidade Intelligence"** | Arquitetura pública MIT + MVP operacional |
| P15 | **"LuxOS: Mapa Operacional de um Ecossistema Técnico"** | Método de catalogação com 7 categorias de evidência |
| P16 | **"OI Sandbox: Laboratório Computacional de Alvo Fechado"** | M1, M2, M2-D, M2-E como infraestrutura de simulação |
| P17 | **"Taxonomia de Materiais Críticos: 22 Datasets Mapeados"** | Catálogo de datasets de materiais críticos |
| P18 | **"Ecosystem Registry Gap Audit: Lições de Um Inventário"** | Metodologia de gap audit em ecossistema técnico |
| P19 | **"8 Candidatos a Publicação em Inteligência de Organoides"** | Mapa completo de candidatos com readiness assessment |

### 🔥🔥 PRIORIDADE COMPLEMENTAR

| # | Título sugerido | Conteúdo |
|---|---|---|
| P20 | **"LuxMemory: Arquitetura de Memória de Longo Prazo para Agentes de Investigação"** | Conceito arquitetural (sem código) |
| P21 | **"Water Intelligence: Primeiro Caso de Uso da Investigation Factory"** | Conceito, sem dados operacionais |
| P22 | **"Comparação Transformacional de 6 Ecossistemas Industriais"** | Tabela comparativa: mineração, petróleo, agro, indústria |

---

## 11. REGRAS DE PUBLICAÇÃO (da boundary documentada)

Conforme `PUBLIC_PRIVATE_BOUNDARY.md` e `ASIE_PUBLIC_BOUNDARY_V0.md`:

| Pode ser público | Deve ser privado |
|---|---|
| Método verificável | Código executável que revela estratégia |
| Schemas e contratos | Dados derivados sensíveis |
| URLs e metadados de fontes públicas | Memória operacional e decisões internas |
| Manifestos e hashes | Resultados não validados |
| Taxonomias genéricas | Materiais de terceiros sem licença |
| Perguntas, hipóteses, gaps | Tokens, credenciais, chaves |
| Resultados negativos | Alvos de investigação específicos |

---

## 12. RECOMENDAÇÃO EDITORIAL

**Publicar imediatamente no Sistemas-Inteligentes:**

> **5 artigos de ALTO VALOR CIENTÍFICO** que não revelam código proprietário nem estratégia operacional:

1. **TTI — Territorial Transformation Index** (preprint + datasets, já sob CC-BY 4.0)
2. **GhostWorks Atlas** (dataset de 887 trajetórias com 6 descobertas validadas; dataset card já escrito)
3. **OI Publication Candidates** (mapeamento de 8 candidatos; P01 e P02 são artigos completos em preparação)
4. **Canonical Machine Map** (arquitetura de 7 camadas da máquina de investigação)
5. **Structural Reuse Test** (domínios mapeados; evidencia generalidade da infraestrutura)

**NÃO publicar agora:**
- Código fonte de `runtime.py`, `asie_runner.py`, `agro_state_adapter.py`
- Outputs de execução do SIGMINE Mineral Retrieval (revelam alvos)
- Conteúdo de ZIPs de patentes (licenças de terceiros)
- Dados brutos de memória LuxMemory (grafos com 6.976 nós)
- Dados de contratos públicos específicos (outputs PNCP)
- Trajetórias específicas da Investigation Factory