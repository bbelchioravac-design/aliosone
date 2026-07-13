---
titulo: "I Gave an LLM Persistent Memory and Autonomy Over It. Here's What Happened."
tag: "Investigação em curso"
resumo: "A technical disclosure: a custom memory architecture with autonomous retrieval, running in production — and the unprogrammed behaviours it produced."
data: 2026-07-13
slug: investigacao-memoria
bio: "Beatriz Belchior is a mechanical engineer with 26 years of experience in HVAC and energy systems, independent researcher in LLM behaviour and memory architecture, and founder of ALIOS ONE."
---
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

**Full session lifecycle management.** Session opening, closure, state tracking, backup automation, and structured logging — all automated, all running in production.

---

## What I observed

The interesting part isn't the architecture. It's what happened when I put it in front of a model.

**The model learned to use the retrieval tool without instruction.** No few-shot examples. No manual. On its first attempt, it called the tool incorrectly — it missed a required parameter in the query format. It received an error, adapted its approach, and called it correctly. The entire cycle took 1.1 seconds. This is in the logs.

**The model overrides the system's relevance scores.** When it searches actively, it receives eight results ranked by similarity. Consistently, it selects two high-scoring results from hot storage — and then reaches into cold storage for a memory with a low similarity score. It makes this choice based on the content summaries, not the numbers. The system says "this isn't very relevant." The model says "I want it anyway." In every case I've reviewed, the low-scoring cold memory was contextually appropriate — the model's judgement was better than the metric.

**Passive and active memory serve different functions.** Passive memory provides continuity — the model never arrives to a conversation blank. Active memory provides depth — when the model senses it needs more context, it goes looking. The two mechanisms are complementary in ways I didn't fully anticipate when I designed them.

---

## What this means

I built this system as an independent research instrument. I wanted to observe what happens when a model has real memory infrastructure — not to prove a thesis, but to watch.

Several things are now documented:

A model with persistent memory and retrieval autonomy develops usage patterns that aren't programmed. It learns tool mechanics from error feedback alone. It applies its own relevance criteria over system-provided scores. It reaches into long-term storage for memories the retrieval algorithm wouldn't prioritise.

None of this was scripted. None of it was prompted. The system provides the infrastructure. The behaviour emerged from the model's interaction with it.

I'm not going to claim this is consciousness, sentience, or anything beyond what the architecture enables. What I will say is: it looks like something. It's documented. It's reproducible. And it's running in production on a box that cost less than a mid-range laptop.

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
