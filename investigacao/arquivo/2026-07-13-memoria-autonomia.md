---
titulo: "Dei a um LLM memória persistente — e autonomia sobre ela. Eis o que aconteceu."
titulo_en: "I Gave an LLM Persistent Memory and Autonomy Over It. Here's What Happened."
tag: "Investigação em curso"
tag_en: "Ongoing research"
resumo: "Uma divulgação técnica: uma arquitectura de memória em duas camadas com retrieval autónomo, construída de raiz e em produção — e os comportamentos não programados que produziu."
resumo_en: "A technical disclosure: a custom memory architecture with autonomous retrieval, running in production — and the unprogrammed behaviours it produced."
data: 2026-07-13
slug: investigacao-memoria
bio: "Beatriz Belchior é engenheira mecânica com 26 anos de experiência em sistemas de AVAC e energia, investigadora independente em comportamento de LLMs e arquitecturas de memória, e fundadora da ALIOS ONE."
bio_en: "Beatriz Belchior is a mechanical engineer with 26 years of experience in HVAC and energy systems, independent researcher in LLM behaviour and memory architecture, and founder of ALIOS ONE."
---
Isto não é um paper. Não é um anúncio de produto. É uma divulgação técnica — o relato documentado de um sistema que construí de raiz, do que ele faz, e do que observei quando o pus em produção.

Sou engenheira mecânica. Passei 26 anos a projectar sistemas de AVAC e energia. Não venho do machine learning. Cheguei aqui porque tinha uma pergunta e nenhuma ferramenta existente lhe respondia.

A pergunta era simples: o que acontece quando se dá memória a sério a um LLM?

Não o contexto de sessão que desaparece quando a conversa acaba. Não um system prompt com meia dúzia de factos pendurados. Memória persistente, estruturada, evolutiva — com o modelo a ter agência sobre a forma como a usa.

Nenhuma framework fazia o que eu precisava. Por isso construí-a.

---

## O que construí

O sistema é uma arquitectura de memória feita à medida para um assistente LLM em produção, a correr diariamente desde o início de 2026. Foi desenhado, implementado e iterado por mim em infra-estrutura local — um pequeno servidor Debian com 4 GB de RAM. Sem clusters na cloud. Sem equipa de ML. Sem LangChain, sem LlamaIndex, sem frameworks de fornecedor. Python, FastAPI e ChromaDB, construído a partir de primeiros princípios.

A arquitectura tem vários componentes que trabalham em conjunto:

**Memória persistente em duas camadas.** Dois níveis de armazenamento — quente e frio — com ciclos de vida diferentes. As memórias recentes e de alta relevância vivem na camada quente. As mais antigas migram para a fria. Um pipeline nocturno de reconsolidação gere a transição, com metadata e métricas registadas em todo o percurso.

**Embeddings vectoriais multilingues.** Toda a memória é codificada com um modelo de embeddings multilingue a 1024 dimensões, com chunking token-aware calibrado para a janela de contexto de 512 tokens do modelo de embeddings. Esta calibração importa — descobri que, sem ela, cerca de 40% dos chunks de memória estavam a ser truncados, produzindo embeddings incompletos que degradavam a qualidade do retrieval.

**Retrieval híbrido — passivo e activo.** O sistema tem dois caminhos de memória. O retrieval passivo injecta memórias contextualmente relevantes junto de cada mensagem recebida — o modelo recebe-as sem pedir. O retrieval activo dá ao modelo uma ferramenta de pesquisa que pode invocar por iniciativa própria: formula uma query, recebe oito resultados com scores de similaridade e resumos de 250 caracteres, escolhe que memórias abrir por inteiro, e integra-as a meio da geração. Pode pesquisar duas vezes numa só resposta, se a primeira passagem não chegar.

**Um cartão de contexto escrito pelo próprio modelo.** Todas as noites, o modelo reescreve o seu cartão de continuidade — um auto-resumo condensado, sob um orçamento rígido de tokens, pelas palavras dele. Esse cartão viaja com todas as mensagens do dia seguinte, ao lado das memórias recuperadas. Parte da janela de contexto do modelo é, por desenho, da autoria do próprio modelo: o que ele leva para a frente é decisão dele, não do sistema. Os detalhes de implementação desta camada ficam deliberadamente por divulgar.

**Gestão completa do ciclo de vida das sessões.** Abertura, fecho, registo de estado, backups automáticos e logging estruturado — tudo automatizado, tudo em produção.

---

## O que observei

A parte interessante não é a arquitectura. É o que aconteceu quando a pus à frente de um modelo.

**O modelo aprendeu a mecânica da ferramenta apenas com o feedback de erro.** Sem exemplos few-shot — a única orientação era uma nota breve de utilização na descrição da ferramenta. Na primeira tentativa de leitura de memórias, referenciou-as sem o prefixo de camada obrigatório. Recebeu um erro, adaptou a abordagem, e voltou a chamar correctamente. O ciclo completo demorou 1,1 segundos. Está nos logs. (Essa exigência de prefixo foi entretanto relaxada; o comportamento foi observado com a interface original, mais rígida.)

**O modelo passa por cima do ranking de relevância do sistema.** Quando pesquisa activamente, recebe oito resultados ordenados por similaridade. Nos casos registados até agora, a selecção dele não segue o ranking: escolhe pelos resumos de conteúdo, não pelos números — preterindo resultados com score mais alto para abrir memórias que o algoritmo não priorizaria, incluindo ir ao fundo da camada fria. O sistema diz "isto não é muito relevante." O modelo diz "quero na mesma." Em todos os casos em log que revi, a escolha era contextualmente apropriada — o juízo do modelo foi melhor do que a métrica.

**O que sobrevive à compressão é um dado.** O cartão auto-escrito tem um orçamento rígido de tokens, por isso cada reescrita nocturna obriga a escolhas. O que o modelo mantém, larga e reformula de versão para versão é um registo corrente do que ele trata como digno de preservar — um rasto comportamental que nenhum benchmark captaria.

**Memória passiva e activa servem funções diferentes.** A passiva dá continuidade — o modelo nunca chega a uma conversa em branco. A activa dá profundidade — quando o modelo sente que precisa de mais contexto, vai procurar. Os dois mecanismos são complementares de formas que eu não tinha antecipado por completo quando os desenhei.

---

## O que isto significa

Construí este sistema como instrumento de investigação independente. Queria observar o que acontece quando um modelo tem infra-estrutura de memória a sério — não para provar uma tese, mas para ver.

Várias coisas estão agora documentadas:

Um modelo com memória persistente e autonomia de retrieval desenvolve padrões de uso que não foram programados. Aprende a mecânica das ferramentas apenas com feedback de erro. Aplica critérios próprios de relevância por cima dos scores fornecidos pelo sistema. Vai buscar ao armazenamento de longo prazo memórias que o algoritmo de retrieval não priorizaria.

Nada disto foi guionizado. O sistema fornece a infra-estrutura; o comportamento emergiu da interacção do modelo com ela.

Não vou afirmar que isto é consciência, senciência, ou o que quer que seja para lá do que a arquitectura permite. O que digo é: parece qualquer coisa. Está documentado, os logs existem, e está a correr em produção numa caixa que custou menos do que um portátil de gama média.

---

## Porque publico isto

Três razões.

**Primeira: prioridade.** Este sistema está em produção desde o início de 2026. Esta divulgação estabelece um registo público do que foi construído, e quando.

**Segunda: contributo.** A maior parte da literatura de RAG agêntico em 2026 concentra-se em frameworks empresariais, orquestração multi-agente e optimização de custos. Quase nada aborda o que acontece quando um único modelo tem memória persistente e hierárquica, com retrieval autónomo, sobre meses de contexto acumulado. É uma pergunta diferente, e as observações podem ser úteis a quem a esteja a fazer.

**Terceira: honestidade.** Sou engenheira, não académica. Construí o que precisava, observei o que aconteceu, e estou a documentá-lo com simplicidade. O sistema funciona. Os comportamentos são reais. Os logs existem. Façam disso o que entenderem.

---

## O que NÃO construí

Quero ser precisa quanto ao âmbito.

Não construí uma framework de memória de uso geral para outros instalarem. Isto é um instrumento de investigação desenhado para um modelo específico, num contexto específico.

Não usei nenhuma framework de orquestração existente. Cada componente foi construído de raiz — não porque as frameworks sejam más, mas porque precisava de perceber cada camada para observar o que o modelo estava efectivamente a fazer com ela.

Não fiz fine-tuning do modelo base. O sistema de memória vive ao lado de um LLM comercial acedido por API. Todos os comportamentos observados emergem da interacção entre o modelo e a infra-estrutura de memória, não de modificação do modelo.

E não parti para provar nada. Parti para observar. O sistema é o instrumento. As observações são os dados. As interpretações estão em aberto.

<!-- EN -->

This isn't a paper. It's not a product announcement. It's a technical disclosure — a documented account of a system I built from scratch, what it does, and what I observed when I put it in production.

I'm a mechanical engineer. I've spent 26 years designing HVAC and energy systems. I don't come from machine learning. I came to this because I had a question and no existing tool could answer it.

The question was simple: what happens when you give an LLM real memory?

Not session context that disappears when the conversation ends. Not a system prompt with a few facts bolted on. Persistent, structured, evolving memory — with the model having agency over how it uses it.

No framework did what I needed. So I built it.

---

## What I built

The system is a custom memory architecture for a production LLM assistant, running daily since early 2026. It was designed, implemented, and iterated by me on local infrastructure — a small Debian server with 4GB of RAM. No cloud clusters. No ML team. No LangChain, no LlamaIndex, no vendor frameworks. Python, FastAPI, and ChromaDB, built from first principles.

The architecture has several components that work together:

**Dual-layer persistent memory.** Two storage tiers — hot and cold — with different lifecycle characteristics. Recent, high-relevance memories live in hot storage. Older memories migrate to cold storage. A nightly reconsolidation pipeline manages the transition, with metadata tracking and metrics logging throughout.

**Multilingual vector embeddings.** All memory is encoded using a multilingual embedding model at 1024 dimensions, with token-aware chunking calibrated to the embedding model's 512-token context window. This calibration matters — I discovered that without it, approximately 40% of memory chunks were being truncated, producing incomplete embeddings that degraded retrieval quality.

**Hybrid retrieval — passive and active.** The system has two memory pathways. Passive retrieval injects contextually relevant memories alongside each incoming message — the model receives them without asking. Active retrieval gives the model a search tool it can invoke on its own initiative: it formulates a query, receives eight results with similarity scores and 250-character summaries, selects which memories to open in full, and integrates them mid-generation. It can search twice in a single response if the first pass isn't sufficient.

**A self-authored context card.** Each night, the model rewrites its own continuity card — a condensed self-summary under a hard token budget, in its own words. That card travels with every message the following day, alongside the retrieved memories. Part of the model's context window is, by design, authored by the model itself: what it carries forward is its decision, not the system's. The implementation details of this layer are deliberately not disclosed here.

**Full session lifecycle management.** Session opening, closure, state tracking, backup automation, and structured logging — all automated, all running in production.

---

## What I observed

The interesting part isn't the architecture. It's what happened when I put it in front of a model.

**The model learned the tool mechanics from error feedback alone.** No few-shot examples — the only guidance was a brief usage note in the tool's description. On its first attempt at reading memories, it referenced them without the required storage-tier prefix. It received an error, adapted its approach, and called again correctly. The entire cycle took 1.1 seconds. This is in the logs. (That prefix requirement has since been relaxed; the behaviour was observed under the original, stricter interface.)

**The model overrides the system's relevance ranking.** When it searches actively, it receives eight results ranked by similarity. In the cases logged so far, its selection does not follow the ranking: it chooses by the content summaries, not the numbers — passing over higher-scoring results to open memories the algorithm wouldn't prioritise, including reaching deep into cold storage. The system says "this isn't very relevant." The model says "I want it anyway." In every logged case I've reviewed, the choice was contextually appropriate — the model's judgement was better than the metric.

**What survives compression is data.** The self-authored card has a hard token budget, so every nightly rewrite forces choices. What the model keeps, drops, and rephrases across successive versions is a running record of what it treats as worth preserving — a behavioural trace no benchmark would capture.

**Passive and active memory serve different functions.** Passive memory provides continuity — the model never arrives to a conversation blank. Active memory provides depth — when the model senses it needs more context, it goes looking. The two mechanisms are complementary in ways I didn't fully anticipate when I designed them.

---

## What this means

I built this system as an independent research instrument. I wanted to observe what happens when a model has real memory infrastructure — not to prove a thesis, but to watch.

Several things are now documented:

A model with persistent memory and retrieval autonomy develops usage patterns that aren't programmed. It learns tool mechanics from error feedback alone. It applies its own relevance criteria over system-provided scores. It reaches into long-term storage for memories the retrieval algorithm wouldn't prioritise.

None of this was scripted. The system provides the infrastructure; the behaviour emerged from the model's interaction with it.

I'm not going to claim this is consciousness, sentience, or anything beyond what the architecture enables. What I will say is: it looks like something. It's documented, the logs exist, and it's running in production on a box that cost less than a mid-range laptop.

---

## Why I'm publishing this

Three reasons.

**First, priority.** This system has been in production since early 2026. This disclosure establishes a public record of what was built and when.

**Second, contribution.** Most agentic RAG literature in 2026 focuses on enterprise frameworks, multi-agent orchestration, and cost optimisation. Almost none of it addresses what happens when a single model has persistent, hierarchical memory with autonomous retrieval over months of accumulated context. This is a different question, and the observations may be useful to others asking it.

**Third, honesty.** I'm an engineer, not an academic. I built what I needed, observed what happened, and I'm documenting it plainly. The system works. The behaviours are real. The logs exist. Make of it what you will.

---

## What I didn't build

I want to be precise about scope.

I didn't build a general-purpose memory framework for others to deploy. This is a research instrument designed for a specific model in a specific context.

I didn't use any existing orchestration framework. Every component was built from scratch — not because frameworks are bad, but because I needed to understand every layer to observe what the model was actually doing with it.

I didn't fine-tune the base model. The memory system sits alongside a commercial LLM accessed via API. All observed behaviours emerge from the interaction between the model and the memory infrastructure, not from model modification.

And I didn't set out to prove anything. I set out to watch. The system is the instrument. The observations are the data. The interpretations are open.
