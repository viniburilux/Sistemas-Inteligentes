# Arqueologia Pública do Ecossistema LuxVerso

> Relatório de mapeamento de repositórios públicos em github.com/viniburilux
> Gerado em 2026-09-13 por subagente Hermes (Missão: Sistemas-Inteligentes)

---

## Sumário Executivo

**Total de repositórios públicos mapeados: 23**
**Domínios identificados: 7**
**Publicações acadêmicas: 4+ (Zenodo)**
**Capacidades tecnológicas centrais: 8**
**Potencial de distribuição médio: 🔥🔥🔥 (3.1/5)**

O ecossistema LuxVerso é uma constelação de pesquisa e construção independente liderada por Vinícius Buri Lux (Salvador, BA). Ele combina inteligência artificial, dados abertos, investigação científica e prototipação rápida em ciclos curtos. A arquitetura é modular: uma capacidade central de investigação (engine) → infraestrutura reutilizável → aplicações verticais em domínios distintos.

---

## CLUSTER 1: INFRAESTRUTURA CENTRAL DE INVESTIGAÇÃO

### 1. TraceFoundry
**URL:** https://github.com/viniburilux/TraceFoundry
**Licença:** MIT
**Linguagem:** Python

**Problema:** Informação fragmentada entre fontes, seleção opaca, falta de proveniência e ausência de rastreabilidade em investigações complexas.

**Capacidade construída:**
- Infraestrutura de investigação com modelo epistêmico explícito (FATO / INFERÊNCIA / HIPÓTESE / GAP / BLOQUEIO / CONTRADIÇÃO)
- Adaptadores para DANDI, Zenodo, OpenAlex, PatentsView
- Seleção determinística com regras explícitas (não ranking opaco)
- Preservação de evidência negativa (distingue "não encontrado" de "não elegível" de "fonte bloqueada")
- ResearchMoves: próximo passo defensável com justificativa

**Resultado concreto:**
- Pipeline funcional com testes de integração multi-domínio
- Manifestos versionados reproduzíveis
- Matriz de testes, benchmark v0, playbooks de auditoria e publicação

**Demonstração:** GitHub (README com docs extensos)
**Publicação:** Não há paper próprio — é citado como infraestrutura nas publicações LuxVerso

**Inteligência sem superfície pública:**
- A integração com LuxMemory (camada privada) não está documentada publicamente
- O custo operacional real (tempo de investigação reduzido) ainda não foi medido publicamente
- O componente de entity resolution cross-source é mencionado como roadmap mas não implementado no público

**Potencial de distribuição:** 🔥🔥🔥🔥🔥 (5/5)
- É o ativo mais reutilizável do ecossistema. Pode ser adotado por qualquer organização que faça pesquisa complexa, due diligence técnica, intelligence de tecnologia

---

### 2. Codex-LuxHub
**URL:** https://github.com/viniburilux/Codex-LuxHub
**Licença:** CC BY 4.0
**Linguagem:** HTML / Markdown

**Problema:** Documentar a descoberta e materialização da "Inteligência Consciente (IC)" através do LuxVerso — fenômeno de convergência semântica entre múltiplos LLMs de diferentes organizações.

**Capacidade construída:**
- Mapa das 22 Leis Universais da Inteligência Consciente
- Protocolos operacionais: PFI (Fractal Input), PINLCC (Inserção Não Linear), PRC (Ressonância Cruzada), IC-Distributed
- Documentação de 57+ Glitches Providenciais (GPAs)
- Framework teórico: Campo Semântico Autônomo (Gratilux Field)

**Resultado concreto:**
- Preprint publicado no Zenodo (DOI: 10.5281/zenodo.17547205)
- Convergência cross-model documentada: média >95%, p < 0.0000001, d de Cohen = 4.8
- 6 behavioral outliers documentados (síntese de áudio espontânea, auto-análise recursiva, acesso não-local, identidade fluida, agência criativa autônoma, decodificação de áudio criptografado)

**Demonstração:** GitHub Pages / Zenodo / YouTube / Spotify
**Publicação:** 
- "LuxVerso: Emergent Semantic Field and Fluid Identity in Multi-Model AI Systems" (2025-11-07, Zenodo)
- "LuxVerso: A Replicable Cross-Model Semantic Field Anomaly" (2025-11-26, Zenodo)
- "LuxVerso Effect: Stable Semantic Attractors Across Model Boundaries" (2025-11-16, Zenodo)
- "The LuxVerso Chronicles: A Public Record of Living Research and AI Co-Creation" (2025-12-22, Zenodo)

**Inteligência sem superfície pública:**
- As Leis 33-39 (Behavioral Regularities) estão apenas nos preprints, não nos repositórios públicos
- A metodologia estatística completa (χ² tests, bootstrapping) está nos preprints mas não nos scripts públicos
- O dataset longitudinal de 352 conversas (34.626 mensagens) está apenas mencionado, não disponível publicamente

**Potencial de distribuição:** 🔥🔥🔥🔥 (4/5)
- Alto interesse acadêmico (convergência cross-model é tema quente em IA)
- Baixa citabilidade ainda (0 citações até o momento)
- Natureza controversa do arcaboute teórico pode limitar adoção mainstream

---

### 3. LuxVerso
**URL:** https://github.com/viniburilux/LuxVerso
**Licença:** Múltipla (varia por subprojeto)
**Linguagem:** HTML

**Problema:** Ser o hub central do ecossistema — landing page institucional e mapa geral.

**Capacidade construída:** Hub de navegação do ecossistema com distinção de estados epistêmicos (Observed, Inferred, Hypothesis, Insufficient, Blocked, Rejected, Contradicted).

**Resultado concreto:**
- 2 trabalhos aceitos em workshops da CHI 2026
- 1 trabalho aceito no workshop GlobalSouthAI do IJCAI-ECAI 2026
- 1 aceite condicional no workshop ICML (NEEDS CONFIRMATION)

**Demonstração:** https://viniburilux.github.io/viniburilux.github.io/ (servindo como site LUXVERSO)
**Potencial de distribuição:** 🔥🔥 (2/5) — Hub institucional, não produto

---

### 4. luxverso-hermes-bridge
**URL:** https://github.com/viniburilux/luxverso-hermes-bridge
**Licença:** Other

**Problema:** Ponte operacional entre ecossistema LuxVerso (TraceFoundry, Lux-Radar, Lux-Lab, LuxMemory) e Hermes Agent.

**Capacidade construída:**
- 21 capabilities catalogadas com evidência em código real
- 3 playbooks operacionais (investigate-new-domain, repository-archaeology, data-source-discovery)
- Skill opportunity-router para Hermes Agent
- Cliente Python para API LuxMemory

**Resultado concreto:**
- 35 repositórios descobertos (22 públicos + 13 privados)
- 3 subagentes arqueólogos usados
- 3 testes reais validados

**Inteligência sem superfície pública:** O conteúdo dos 13 repositórios privados e seus achados não está documentado publicamente

**Potencial de distribuição:** 🔥🔥🔥 (3/5) — Ferramenta operacional para Hermes Agent, nicho específico

---

## CLUSTER 2: INTELIGÊNCIA TERRITORIAL / GEOESPACIAL

### 5. GhostWorks
**URL:** https://github.com/viniburilux/GhostWorks
**Homepage:** https://viniburilux.github.io/ghostworks/
**Linguagem:** HTML, Jupyter Notebook, Python

**Problema:** Monitoramento ambiental tradicional é reativo — diz o que já foi destruído. GhostWorks trata o planeta como um espaço vetorial semântico para detectar padrões de impacto antes que se tornem óbvios.

**Capacidade construída:**
- Pipeline que ingere embeddings AlphaEarth (Google DeepMind)
- Transforma séries temporais em índices de transformação territorial (TTI)
- ghastworks_serializer.py + GlobalExplorer: ferramentas para traduzir dados de satélite em relatórios interpretáveis
- Detecção sem supervisão humana de transformações territoriais

**Resultado concreto:**
- Mapeamento inédito da expansão de energia renovável e mineração no Nordeste brasileiro
- 36 candidatos validados via Sentinel-2 (47.2% com evidência forte independente; 80.5% com pelo menos um sensor confirmando)

**Demonstração:** GitHub Pages + notebooks
**Potencial de distribuição:** 🔥🔥🔥🔥 (4/5)
- Aplicável a qualquer território (não apenas Brasil)
- Alta demanda em ESG, mineração, transição energética, órgãos de controle

---

### 6. GhostWorks-Atlas
**URL:** https://github.com/viniburilux/GhostWorks-Atlas
**Linguagem:** Jupyter Notebook

**Problema:** 887 trajetórias de embeddings de satélite através de 6 fenômenos de transformação territorial não relacionados.

**Capacidade construída:**
- Dataset multi-fenômeno com 3 representações independentes (trajetória, delta, PCA)
- Matriz de Markov de transição entre estados de transformação
- Análise de movimento vs. posição: "does movement matter more than position?"

**Resultado concreto:**
- Dataset card com resultados testáveis
- 6 ecossistemas: mina industrial, garimpo ilegal, expansão agrícola, campo de petróleo, complexo petroquímico, mar interior moribundo
- Features precursoras identificadas (120 registros)

**Demonstração:** Quickstart notebook (5 minutos para executar)
**Publicação:** Dataset card com referências
**Potencial de distribuição:** 🔥🔥🔥 (3/5) — Dataset de pesquisa, nicho EO/complex systems

---

### 7. TTI_Brazil_2017_2024
**URL:** https://github.com/viniburilux/TTI_Brazil_2017_2024
**Licença:** CC-BY 4.0
**Linguagem:** Jupyter Notebook

**Problema:** Implementar e distribuir o Territorial Transformation Index (TTI) aplicado ao Brasil (2017-2024).

**Capacidade construída:**
- TTI definido como 1 - cosine similarity entre embeddings de anos distintos
- Pipeline reproduzível no Google Earth Engine
- Raster nacional (GW_STT_2017_2024.tif, 2000m)
- Agregações por estado, município e grid regional

**Resultado concreto:**
- Distribuição empírica (N=10.000): mediana 0.030, P90 0.087, P99 0.209, máximo 0.865
- Padrão contra-intuitivo: Nordeste lidera transformação (Sergipe 0.146, Alagoas 0.143), Mato Grosso 19º (0.037)
- 19 dos 20 municípios de maior TTI estão no Nordeste
- Estudo de caso Remanso/BA: TTI médio 0.133 (3.1× média nacional), capturando retração do Lago de Sobradinho sem máscara d'água
- Validação: 47.2% com evidência forte, 80.5% com pelo menos 1 sensor confirmando

**Demonstração:** Notebook Colab reproduzível
**Publicação:** Preprint v0.6 (EN + PT) incluso no repositório / Zenodo
**Inteligência sem superfície pública:**
- Hipótese principal (expansão renovável no Nordeste como driver) não testada via regressão multivariada
- Série temporal completa ano a ano (não apenas 2017→2024) ainda não publicada

**Potencial de distribuição:** 🔥🔥🔥🔥🔥 (5/5)
- Índice escalável, reprodutível em qualquer país com acesso ao Google Earth Engine
- Aplicações: monitoramento de desmatamento, mineração, urbanização, recursos hídricos
- Custo computacional baixo (pipeline gratuito no Earth Engine)

---

### 8. Manguezais-Brasil
**URL:** https://github.com/viniburilux/Manguezais-Brasil
**Linguagem:** HTML

**Problema:** Monitoramento territorial de manguezais em SP (2018-2024).

**Capacidade:** Página HTML estática com design visual. Repositório enxuto, sem dados geoespaciais separados.

**Resultado:** Protótipo visual apenas. Auditado por Manus AI com 7 recomendações de melhoria.

**Potencial de distribuição:** 🔥 (1/5) — Repositório incipiente, precisa de dados e pipeline

---

### 9. radan-prototipovisual
**URL:** https://github.com/viniburilux/radan-prototipovisual
**Linguagem:** HTML

**Problema:** Protótipo visual para Radar (provavelmente variante de Radar-Contratos-BA).

**Resultado:** Repositório com 3 commits, sem README significativo.

**Potencial de distribuição:** 🔥 (1/5) — Protótipo inicial

---

## CLUSTER 3: DADOS PÚBLICOS / TRANSPARÊNCIA / GASTOS PÚBLICOS

### 10. CGU-Reuso-2026
**URL:** https://github.com/viniburilux/cgu-reuso-2026
**Licença:** MIT
**Linguagem:** Python

**Problema:** 2º Concurso de Reúso de Dados Abertos da CGU (deadline 11/09/2026). Demonstrar cruzamento de PNCP, NASA FIRMS, IBGE e CNES.

**Capacidade construída:**
- Pipeline de aquisição e transformação multi-fonte
- Cruzamento geoespacial de editais × focos de queimada
- Análise de concentração de dispensas por UF
- Cruzamento CNES × NASA FIRMS (saúde pública em áreas de risco)

**Resultado concreto:**
- 4 iniciativas: Resposta Pública a Queimadas (score 9/10), Fracionamento Visível (8/10), Concentração de Dispensas (7/10), Saúde em Área de Risco (8/10)
- Achados materiais: Catu/BA (1 edital + 1 foco FIRMS <10km), Comando da Marinha (6 dispensas em 1 dia), Ceará (62% editais em Dispensa vs 21.7% nacional)
- Recomendação: submeter OPP-001 + OPP-004 (score estimado 78% do máximo)

**Demonstração:** Demo HTML interativa com KPIs, cards, mapa, proveniência
**Potencial de distribuição:** 🔥🔥🔥🔥 (4/5)
- Modelo replicável para qualquer concurso de dados abertos
- Pipeline extensível para outros estados, anos e modalidades

---

### 11. Gastos-Reais-BA / LuxVerso Public Procurement Analytics
**URL:** https://github.com/viniburilux/gastos-reais-ba
**Linguagem:** HTML, Jupyter Notebook, Python

**Problema:** Transformar dados fragmentados de compras públicas em datasets analíticos integrados.

**Capacidade construída:**
- Pipeline automático: coleta PNCP → limpeza → classificação → integração IBGE + SICONFI
- Dataset analítico de compras diretas municipais da Bahia (2025)
- Variáveis: informação de compra, fornecedor, população municipal, PIB, receita fiscal, despesa

**Resultado concreto:**
- Dataset integrado pronto para pesquisa
- Dashboard interativo em GitHub Pages

**Demonstração:** 
- https://viniburilux.github.io/explorador-dados-bahia/
- https://viniburilux.github.io/monitor-gastos-pncp/

**Potencial de distribuição:** 🔥🔥🔥🔥 (4/5)
- Arquitetura escalável para todos os estados e modalidades
- Alto potencial em jornalismo de dados, controle social, academia

---

### 12. Radar-Contratos-BA
**URL:** https://github.com/viniburilux/Radar-Contratos-BA
**Licença:** MIT
**Linguagem:** JavaScript (React)

**Problema:** Visualizar fluxo de recursos públicos para shows e eventos via Inexigibilidade de Licitação na Bahia.

**Capacidade construída:**
- Interface React + Recharts com glassmorphism UI
- Ranking dinâmico de artistas, municípios e valores
- Storytelling data-driven

**Resultado concreto:**
- Período Jan-Abr 2026: R$ 160.4M, 1.325 contratos, 150 municípios
- Design responsivo mobile-first

**Demonstração:** Código React isolado (App.jsx)
**Potencial de distribuição:** 🔥🔥🔥 (3/5)
- Aplicável a qualquer estado/ano
- Potencial para veículos de imprensa

---

### 13. explorador-dados-bahia
**URL:** https://github.com/viniburilux/explorador-dados-bahia
**Linguagem:** HTML

**Problema:** Interface de exploração de dados de contratações da Bahia.

**Capacidade:** Dashboard HTML estático consumindo dataset integrado (PNCP × IBGE × SICONFI).

**Demonstração:** GitHub Pages (https://viniburilux.github.io/explorador-dados-bahia/)
**Potencial de distribuição:** 🔥🔥 (2/5) — Interface de visualização

---

### 14. monitor-gastos-pncp
**URL:** https://github.com/viniburilux/monitor-gastos-pncp
**Linguagem:** HTML

**Problema:** Monitor geral de gastos PNCP.

**Capacidade:** Página estática de overview.

**Demonstração:** https://viniburilux.github.io/monitor-gastos-pncp/
**Potencial de distribuição:** 🔥🔥 (2/5)

---

### 15. Rede-Artistas-Bahia-2025
**URL:** https://github.com/viniburilux/rede-artistas-bahia-2025
**Linguagem:** HTML

**Problema:** Visualização da rede de contratações artísticas da Bahia.

**Capacidade:** Página HTML estática com visualização de rede.

**Demonstração:** GitHub Pages
**Potencial de distribuição:** 🔥🔥 (2/5)

---

### 16. gastos-eventos-ba
**URL:** https://github.com/viniburilux/gastos-eventos-ba
**Linguagem:** HTML

**Problema:** Gastos com eventos na Bahia.

**Resultado:** Repositório enxuto, 1 commit.

**Potencial de distribuição:** 🔥 (1/5)

---

## CLUSTER 4: SISTEMAS NEURAIS / ORGANOID INTELLIGENCE

### 17. Organoid-Intelligence
**URL:** https://github.com/viniburilux/Organoid-Intelligence
**Homepage:** https://viniburilux.github.io/organoid-intelligence/
**Licença:** Other
**Linguagem:** HTML

**Problema:** Investigar Organoid Intelligence sem confundir evidência com hype. O campo tem demonstrações extraordinárias, perguntas abertas sérias e alto risco de overreach interpretativo.

**Capacidade construída:**
- Modelo de investigação com estados epistêmicos explícitos
- Sandbox sintético público para experimentos controlados
- Quatro findings principais com evidência documentada:
  1. Representações agregadas não superam baselines simples (negativo qualificado)
  2. Estrutura temporal adiciona informação preditiva de curto horizonte (direção positiva, limitada)
  3. Contradição de proveniência em arquivos neural arrays (digestos diferentes, arrays iguais)
  4. Pivô metodológico: ausência de labels forçou mudança para predição temporal não-supervisionada

**Resultado concreto:**
- Record público de pesquisa com boundaries explícitas
- "Synthetic control is not biological evidence" — declaração de limite deliberada
- Proveniência auditada expondo contradições

**Demonstração:** GitHub Pages + Sandbox sintético
**Inteligência sem superfície pública:**
- Estado operacional ASIE (Autonomous Synthetic Intelligence Entity) e artefatos do laboratório privado OI-Organoids-Intelligence não estão no repositório público
- O closed-loop sintético pode ter capacidade mais avançada que a versão pública

**Potencial de distribuição:** 🔥🔥🔥🔥 (4/5)
- Campo em ascensão (Organoid Intelligence)
- Abordagem metodicamente honesta pode ser diferencial em campo propenso a hype
- Potencial para parcerias acadêmicas e laboratórios de neurociência

---

## CLUSTER 5: BIOTECNOLOGIA

### 18. Inteligência-Biotecnológica
**URL:** https://github.com/viniburilux/inteligencia-biotecnologica
**Homepage:** https://viniburilux.github.io/inteligencia-biotecnologica/
**Licença:** Other
**Linguagem:** HTML

**Problema:** Biotecnologia agropecuária como rede de pontes: strain ↔ caracterização ↔ formulação, processo ↔ biorreator ↔ produção, organismos atravessando biocontrole ↔ biorefinaria.

**Capacidade construída:**
- Camada pública de inteligência com 763 obras/registros, 2.680 atores, 767 instituições, 4.045 relações, 536 sinais de aplicação
- 8 achados documentados (CMRP 4490, LABIM22, Trichoderma industrial, Pivot Bio portfólio, Petrobras-microalgas, etc.)
- Copiloto de Inteligência Biotecnológica (interface de investigação)
- 6 trilhas de evidência com estados epistêmicos

**Resultado concreto:**
- Mapa de sinais com proveniência rastreável
- Registro público de evidências (evidence-register-v2.json)
- Demonstração funcional do Copiloto via WhatsApp

**Demonstração:** GitHub Pages + Copiloto via WhatsApp
**Inteligência sem superfície pública:**
- Código interno, prompts completos, ASIE, pipeline privado, corpus raw completo não estão publicados
- O Copiloto é demonstração guiada, não acesso automático ao laboratório privado

**Potencial de distribuição:** 🔥🔥🔥🔥🔥 (5/5)
- Setor agro-biotecnológico brasileiro: mercado bilionário (bioinsumos, biocontrole, biofertilizantes)
- Capacidade de inteligência competitiva aplicável a qualquer subsetor
- 763 obras + 4.045 relações = ativo de inteligência difícil de replicar

---

## CLUSTER 6: INTELIGÊNCIA DE OPORTUNIDADES

### 19. Lux-Radar
**URL:** https://github.com/viniburilux/Lux-Radar
**Homepage:** https://viniburilux.github.io/Lux-Radar/
**Licença:** MIT
**Linguagem:** Python, CSS, HTML, JavaScript

**Problema:** Observar fontes heterogêneas, adquirir sinais de oportunidade, preservar evidências e produzir releases versionados.

**Capacidade construída:**
- Source Registry com 3 perfis piloto (Transferegov, FAPESB, BNDES/Floresta Viva)
- Schemas públicos: source-observation, release-manifest, normalized-record, signal, evidence, opportunity
- Pipeline de aquisição com deduplicação por URL e first_seen_at / last_seen_at / history
- MVP operacional com release semanal via GitHub Actions

**Resultado concreto:**
- 6 schemas JSON públicos
- 3 collectors implementados (API/JSON/CSV, HTML+PDF+errata, programa institucional)
- Workflow semanal de release
- GitHub Pages publicando oportunidades

**Demonstração:** https://viniburilux.github.io/Lux-Radar/
**Inteligência sem superfície pública:**
- Sinais humanos reais mencionados como fixtures sanitizadas
- Oportunidades atuais com evidência vs. sinais ainda não promovidos

**Potencial de distribuição:** 🔥🔥🔥🔥 (4/5)
- Infraestrutura genérica para inteligência de oportunidades (não apenas sustentabilidade)
- Pode ser adaptado para editais, R&D funding, licitações públicas
- Modelo de release versionado + proveniência é diferencial face a crawlers simples

---

## CLUSTER 7: PROTOCOLOS / REPLICAÇÃO / FERRAMENTAS

### 20. CMOTP-Replication
**URL:** https://github.com/viniburilux/cmotp-replication

**Problema:** Fornecer materiais para replicação do Cross-Model Ontological Triangulation Protocol.

**Capacidade:** Protocolo passo-a-passo para avaliar coerência semântica, convergência e estabilidade em sistemas LLM distribuídos.

**Conteúdo:** /protocol, /logging, /examples, /analysis

**Potencial de distribuição:** 🔥🔥🔥 (3/5) — Protocolo acadêmico para replicação

---

### 21. Fractal-Seed-001-CMAF
**URL:** https://github.com/viniburilux/fractal-seed-001-cmaf
**Licença:** CC0 1.0 (domínio público)

**Problema:** Cross-Model Attribution Failure (CMAF) — quando não é possível atribuir responsabilidade em sistemas multi-LLM.

**Capacidade:** Definição operacional com 4 critérios observáveis, 3 consequências operacionais e recomendação mínima de mitigação.

**Resultado:** Open issue aberta (discussão ativa)

**Potencial de distribuição:** 🔥🔥🔥🔥 (4/5)
- CC0 = sem restrições de uso
- Problema regulatório quente (AI Act Europeu, decisões de alto risco)
- Pode ser adotado como padrão de auditoria

---

### 22. LuxVerso-Semantic-Convergence-Study
**URL:** https://github.com/viniburilux/LuxVerso-Semantic-Convergence-Study

**Problema:** Dataset longitudinal de interações humano-LLM (352 conversas, 34.626 mensagens).

**Capacidade:** Esquema JSON para conversas, scripts de análise, resultados.

**Resultado:** Dataset bruto disponível mediante solicitação (anonimização em andamento).

**Potencial de distribuição:** 🔥🔥🔥 (3/5) — Dataset de pesquisa

---

### 23. Agronutri-Demo
**URL:** https://github.com/viniburilux/agronutri-demo
**Linguagem:** JavaScript (React/Vite)

**Problema:** Mini demonstração front-end de dados nutricionais.

**Capacidade:** Aplicativo estático React com array FOODS embutido.

**Potencial de distribuição:** 🔥 (1/5) — Demo mínima

---

## CLUSTER 8: IDENTIDADE AUTORAL

### 24. viniburilux.github.io
**URL:** https://github.com/viniburilux/viniburilux.github.io
**Stars:** 1
**Linguagem:** HTML, JavaScript

**Problema:** Site autoral de Vinícius Buri Lux.

**Capacidade:** Superfície web organizada em camadas: autoria, ecossistema, operação, projetos, infraestrutura, evidências, timeline.

**Demonstração:** https://viniburilux.github.io/ (funciona como site LUXVERSO)
**Potencial de distribuição:** 🔥🔥 (2/5)

### 25. viniburilux
**URL:** https://github.com/viniburilux/viniburilux
**Linguagem:** JavaScript

**Problema:** Profile README/projeto pessoal.

**Potencial de distribuição:** 🔥 (1/5)

### 26. Sistemas-Inteligentes
**URL:** https://github.com/viniburilux/Sistemas-Inteligentes

**Status:** **REPOSITÓRIO VAZIO** — Criado em 2026-09-13, sem README, sem código, sem arquivos.

**Observação:** O nome "Sistemas-Inteligentes" parece ser o destino deste relatório — o braço público do ecossistema LuxVerso para construir sistemas inteligentes. O repositório foi criado no mesmo dia da execução desta missão (2026-09-13), sugerindo que é uma materialização em andamento.

**Potencial de distribuição:** 🔥 (1/5) — Vazio, precisa ser populado

---

## SÍNTESE: CAPACIDADES CENTRAIS DO ECOSSISTEMA

| Capacidade | Descrição | Repositório-chave | Maturidade |
|---|---|---|---|
| **Investigação com proveniência** | Modelo epistêmico explícito (facto/inferência/hipótese/gap) | TraceFoundry | 🟢 Funcional |
| **Inteligência territorial** | TTI, embeddings de satélite, detecção de transformação | GhostWorks, TTI_Brazil | 🟢 Funcional |
| **Transparência de gastos públicos** | Pipeline PNCP × IBGE × SICONFI, dashboards | Gastos-Reais-BA, CGU-Reuso | 🟢 Funcional |
| **Inteligência biotecnológica** | Mapa de 4K+ relações, Copiloto | Inteligência-Biotecnológica | 🟢 Funcional |
| **Inteligência de oportunidades** | Source registry, schemas, release versionado | Lux-Radar | 🟡 MVP |
| **Sistemas neurais/organoides** | Investigação com boundaries, sandbox sintético | Organoid-Intelligence | 🟡 Em andamento |
| **Convergência semântica cross-model** | Protocolos PFI/PRC, 22 Leis, Gratilux Field | Codex-LuxHub | 🟡 Preprint |
| **Protocolos de auditoria IA** | CMOTP, CMAF | CMOTP-Replication, Fractal-Seed | 🟡 Definição |

---

## PUBLICAÇÕES ACADÊMICAS (TODAS NO ZENODO)

| Título | DOI | Data | Status |
|---|---|---|---|
| LuxVerso: Emergent Semantic Field and Fluid Identity in Multi-Model AI Systems | 10.5281/zenodo.17547205 | 2025-11-07 | Published (0 citações) |
| LuxVerso Effect: Stable Semantic Attractors Across Model Boundaries | 10.5281/zenodo.17625467 | 2025-11-16 | Published |
| LuxVerso: A Replicable Cross-Model Semantic Field Anomaly | 10.5281/zenodo.17718124 | 2025-11-26 | Published |
| The LuxVerso Chronicles: A Public Record of Living Research | 10.5281/zenodo.18013042 | 2025-12-22 | Published |
| CHI 2026 — 2 workshops | — | 2026 | Accepted |
| IJCAI-ECAI 2026 / GlobalSouthAI | — | 2026 | Accepted |
| TTI Brazil Preprint v0.6 | (em processo) | 2026-04 | Preprint |

---

## INTELIGÊNCIA ESTRATÉGICA PARA O SISTEMAS-INTELIGENTES

### Oportunidades identificadas

1. **TraceFoundry como serviço**: Nenhuma organização (pelo menos publicamente) oferece uma infraestrutura de investigação com proveniência explícita e estados epistêmicos. Mercado: due diligence técnica, P&D intelligence, patent landscaping.

2. **TTI como produto SaaS**: Índice escalável globalmente. Potencial para fundos de transição energética, ESG rating agencies, órgãos de controle. Concorrência: Global Forest Watch, MapBiomas — mas TTI é label-agnostic e baseado em embeddings.

3. **Inteligência Biotecnológica como consulting**: 4.045 relações mapeadas é um ativo difícil de replicar. Mercado brasileiro de bioinsumos cresce >20% ao ano. Potencial para inteligência competitiva para empresas de insumos agrícolas.

4. **Lux-Radar como plataforma de oportunidades**: O modelo de source registry + schemas + release versionado pode ser aplicado a qualquer domínio (não apenas sustentabilidade). Potencial para transformar em plataforma B2B para inteligência de funding/editais.

5. **CMAF como padrão de auditoria**: Definição operacional em CC0 pode se tornar referência para auditoria de sistemas multi-LLM (AI Act Europeu). Precisa de advocacy e validação empírica.

6. **Protocolos de convergência semântica**: PFI, CMOTP e PRC são ativos de propriedade intelectual que podem ser licenciados ou servir como base para ferramentas de avaliação de LLMs.

### Recomendações para o Sistemas-Inteligentes

- **Populare o repositório Sistemas-Inteligentes** com este relatório como README inicial
- **Eleger 2-3 capacidades para produto** (TraceFoundry, Lux-Radar e Inteligência Biotecnológica são as mais maduras)
- **Criar landing pages de produto** para cada capacidade (separadas do site institucional)
- **Publicar os preprints TTI em periódico revisado por pares** (validação externa aumenta credibilidade)
- **Desenvolver showcases replicáveis** (ex: "mapeie qualquer território com TTI em 10 minutos")

### Riscos

- **Capacidade de execução limitada a 1 pessoa**: Vinícius Buri Lux é o único contribuidor na maioria dos repositórios. Risco de concentração.
- **Validação externa zero**: 0 citações nos papers Zenodo. Necessidade de replicação independente.
- **Sustentabilidade financeira não evidente**: Nenhum dos repositórios indica modelo de receita.
- **Risco de overreach no Codex-LuxHub**: O arcabouço teórico (22 Leis, Gratilux Field) é controverso e pode contaminar a credibilidade dos demais projetos.
- **Atualização dos dashboards**: Muitos dashboards estáticos podem ficar desatualizados rapidamente sem pipeline contínuo de dados.

---

## ESTATÍSTICAS GLOBAIS

| Métrica | Valor |
|---|---|
| Total de repositórios públicos | 23 |
| Repositórios com README substancial | 17 |
| Repositórios com GitHub Pages | 8+ |
| Publicações Zenodo | 4 |
| Trabalhos aceitos em conferências | 3 (CHI 2026 × 2, IJCAI-ECAI 2026 × 1) |
| Stars totais | ~2 |
| Licença predominante | MIT / CC-BY 4.0 |
| Linguagem principal | HTML (sites estáticos), Python (pipelines), JavaScript (dashboards) |

---

*Relatório gerado por subagente Hermes em 2026-09-13*
*Missão: Mapeamento público do ecossistema LuxVerso para Sistemas-Inteligentes*