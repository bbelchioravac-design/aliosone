---
titulo: Que modelo escolher (e porque não são todos iguais)
data: 2026-07-20
tag: IA no terreno
resumo: "Há mais modelos de IA do que batatas. Este é o mapa: qual usar para quê
  — e quais falam mesmo português de Portugal."
publicado: true
titulo_en: Which model to choose (and why they're not all the same)
tag_en: Al in the field
resumo_en: "There are more AI models than potatoes. Here's the map: which one to
  use for what — and which ones actually speak proper Portuguese."
corpo_en: >-
  *Article 2 of 3 in the "Talking to Machines" series*


  In the first article (https://bit.ly/3Rnh7zq) you learned how to talk to an AI. Today: *who* to talk to. Because they're not all the same — and the differences matter more than they seem.



  Before we start, two honest warnings.



  First: there are more models than potatoes. New ones come out every week — literally — and a complete list would be brutal and useless. I'm sticking to the best-known ones and the ones I use. If your favourite isn't here, it's not contempt: it's triage.



  Second: part of what follows is industry consensus, part is my own experience. I'll flag it when it's mine. And one important note: the experience you have with a model depends a lot on who's talking to it. The way you communicate — the context you give, the questions you ask — changes what the model gives back. My way of communicating is quite particular, so your experience may not match mine. One of these days I'll write about this, because it deserves an article of its own.



  **A model is not a platform**

  This is possibly the most useful concept in this entire article.

  The platform is the brand; the model is the engine. And the same brand sells several engines. Inside ChatGPT there are several GPT models. Inside claude.ai there are several Claudes. There's a selector — usually discreet, somewhere at the top of the conversation — that almost nobody touches. And it changes everything.

  The logic is nearly always the same, on any platform:

  - **Light, fast models** — answer in an instant, good for everyday use: simple questions, emails, short summaries.


  \-**Heavy models (the "flagships")** — slower and more expensive, but with a different depth. For serious work.


  \- **"Thinking" models** — they reason before answering, sometimes for minutes. Worth it for complex problems; for asking for an email they're pure waste.



  Practical rule: if a wrong answer will cost you time or money, use the heavy model. If it's everyday chat, the light one will do.



  **The task-by-task guide**

  **Writing text**

  It depends on the kind of writing. For technical text — articles, reports, documentation — almost all the heavy models do a good job: any Claude, the bigger GPTs, Qwen 3.6 Plus, DeepSeek. For high-quality creative writing, the field narrows: for me, the best are still GPT-4o (nowadays only accessible via API — I'll explain what that means in the next article) and Claude Opus 4.6. For more daring literature, some people prefer models with fewer content restrictions — Grok has that reputation. Not my thing, but the consensus exists.



  **Programming**

  I can only speak for the ones I've tried: Claude Opus, GPT and Claude Fable. For me, Fable is clearly ahead, with Opus right behind. Some people swear by GPT-5.6, and Qwen 3.6 Plus and Kimi K2.5 also have a good reputation.

  A practical warning: Fable costs a kidney — it's only available on the top-tier plans or by paying for credits. If you're starting out, a mid-range model is perfectly fine.



  **Analysing long documents**

  Here the feature that matters is the "context window" — the amount of text the model can hold in mind at once. For long reports, contracts, or several documents at a time, look for models with a 1-million-token window (roughly speaking, thousands of pages). I use Opus and Qwen; Gemini is also known for this.



  **Searching with current sources**

  Gemini and Grok do integrated web search. Lots of people use Perplexity — which isn't quite a model, it's a product built for search — and use it well. Not my case, but it would be dishonest not to mention it.



  **Generating images**

  Nano Banana (Google) and GPT's image generator are, for me and by far, the best. Grok generates images too; I've never tried it.



  **Brainstorming and helping you think**

  Here lies the subtlest difference of all — and the one fewest people know about. There are models that merely comment on what you say, and models that pull the idea out of you, extrapolate, bring up what you hadn't seen. For simple brainstorming, any model will do. For untangling a complex, new idea that doesn't exist yet — only the top models. These are the conversations where the price difference earns its keep.



  **Writing in European Portuguese**

  The section nobody writes — so I will. Not all models master European Portuguese, and some pretend they do. In my experience, in order: GPT, Claude, Qwen, DeepSeek — and then it drops off a cliff. Gemini tends to repeat itself, Grok likewise, Kimi starts throwing English words into the middle of sentences, and Le Chat, last time I tested it, still couldn't speak proper Portuguese from Portugal. A simple test you can run: ask for a text in the informal second person singular and see if the verbs survive.



  **The Chinese models — a note of their own**

  You'll have noticed that Qwen (Alibaba), DeepSeek and Kimi (Moonshot) come up several times above. That's no accident: they are technically very capable, and free or nearly free. You access them through a website, like the others — nothing to install.

  The note that's specific to them: your data goes to servers in China, under privacy rules different from Europe's. That's no reason for panic, and no reason to ignore them — it's a reason for judgement. Apply the rule from the first article with an extra layer: don't write anything you wouldn't put in an email to an external supplier.



  **How to decide in practice**

  Forget the benchmarks and the rankings — they change every month and measure things that probably aren't your use case. The durable rule is different:



  **Give the same real task to two or three models and compare.** An email you actually need to send, a document you actually need to summarise. See which one does it better. Repeat with a different kind of task. After a week you'll know more about what works for you than any online comparison could tell you.

  The best model isn't the one that won the benchmark. It's the one that works for you, in your language, on your tasks.



  **A note on shelf life**

  This article was written in July 2026. The names and versions will change — that's guaranteed. But the decision rules stay: light for the everyday, heavy for what matters, big window for long documents, real-world testing before you choose.



  **The essentials in three lines**

  1. A model is not a platform — find the selector and learn to use it.


  2. Light for the everyday, heavy for what matters.


  3. Test with your own real tasks. The best model is the one that works for you.



  Now you know how to talk, and who to talk to. In the next article: **what lies beneath the platforms** — API, CLI, tokens, and why some models can only be reached down there.
seccao: "Descomplicador"
edicao: 1
ordem: 2
---
![Que modelo escolher: cada modelo tem forças diferentes](/images/que-modelo-escolher-arte.jpg)

*Artigo 2 de 3 da série "Falar com Máquinas"*

No primeiro artigo (https://bit.ly/3Rnh7zq) aprendeste a falar com uma IA. Hoje: com *quem* falar. Porque não são todos iguais — e as diferenças interessam mais do que parecem.


Antes de começar, dois avisos honestos.


Primeiro: há mais modelos do que batatas. Saem novos todas as semanas — literalmente — e uma lista completa seria brutal e inútil. Vou basear-me nos mais conhecidos e nos que uso. Se o teu favorito não aparece, não é desprezo: é triagem.


Segundo: parte do que se segue é consenso da indústria, parte é experiência minha. Aviso quando for a minha. E uma nota importante: a experiência com um modelo depende muito de quem fala com ele. A forma como comunicas — o contexto que dás, as perguntas que fazes — muda o que o modelo te devolve. A minha forma de comunicar é particular, e por isso a tua experiência pode não coincidir com a minha. Um dia destes escrevo sobre isto, porque merece artigo próprio.


**Modelo não é plataforma**
Este é possivelmente o conceito mais útil do artigo inteiro.
A plataforma é a marca; o modelo é o motor. E a mesma marca vende vários motores. Dentro do ChatGPT há vários modelos GPT. Dentro do claude.ai há vários Claude. Há um selector — normalmente discreto, algures no topo da conversa — que quase ninguém toca. E que muda tudo.


A lógica é quase sempre a mesma, em qualquer plataforma:
- **Modelos leves e rápidos** — respondem num instante, servem para o dia-a-dia: perguntas simples, emails, resumos curtos.

\- **Modelos pesados (os "flagship")** — mais lentos e mais caros, mas com outra profundidade. Para trabalho a sério.

\- **Modelos "thinking"** — raciocinam antes de responder, às vezes durante minutos. Valem a pena para problemas complexos; para pedir um email são desperdício puro.


Regra prática: se a resposta te vai custar tempo ou dinheiro caso venha errada, usa o modelo pesado. Se é conversa corrente, o leve chega.


**O guia por tarefa**
**Escrever texto**
Depende do tipo de escrita. Para texto técnico — artigos, relatórios, documentação — quase todos os modelos pesados fazem bom trabalho: qualquer Claude, os GPT maiores, o Qwen 3.6 Plus, o DeepSeek. Para escrita criativa de alta qualidade, o campo estreita: para mim, os melhores continuam a ser o GPT-4o (hoje só acessível via API — explico o que isso é no próximo artigo) e o Claude Opus 4.6. Para literatura mais ousada, há quem prefira modelos com menos restrições de conteúdo — o Grok tem essa fama. Não é a minha praia, mas o consenso existe.


**Programar**
Só posso falar dos que experimentei: Claude Opus, GPT e Claude Fable. Para mim, o Fable está claramente à frente, com o Opus logo atrás. Há quem prefira o GPT-5.6, e o Qwen 3.6 plus e Kimi K2.5 também têm boa reputação. 

**Um aviso prático: o Fable custa um rim** — só está acessível nos planos de topo ou pagando créditos. Para quem começa, um modelo intermédio chega perfeitamente.


**Analisar documentos longos**
Aqui a característica que interessa é a "janela de contexto" — a quantidade de texto que o modelo consegue ter presente ao mesmo tempo. Para relatórios extensos, contratos ou vários documentos de uma vez, procura modelos com janela de 1 milhão de tokens (grosso modo, milhares de páginas). Eu uso o Opus e o Qwen; o Gemini também é conhecido por isto.


**Pesquisar com fontes actuais**
Gemini e Grok fazem pesquisa na web de forma integrada. Muita gente usa o Perplexity — que não é bem um modelo, é um produto construído para pesquisa — e usa-o bem. Não é o meu caso, mas seria desonesto não o mencionar.


**Gerar imagens**
Nano Banana (Google) e o gerador do GPT são, para mim e de longe, os melhores. O Grok também gera; nunca experimentei.


**Brainstorming e ajudar a pensar**
Aqui está a diferença mais subtil de todas — e a que menos gente conhece. Há modelos que apenas comentam o que dizes, e modelos que puxam a ideia para fora, extrapolam, trazem o que tu não tinhas visto. Para brainstorming simples, qualquer um serve. Para destrinçar uma ideia complexa, nova, que ainda não existe — só os modelos de topo. É nestas conversas que a diferença de preço se justifica.


**Escrever em português europeu**
A secção que ninguém escreve — por isso escrevo eu. Nem todos os modelos dominam o PT-PT, e alguns fingem que sim. Na minha experiência, por ordem: GPT, Claude, Qwen, DeepSeek — e depois cai a pique. O Gemini tende a repetir-se, o Grok idem, o Kimi começa a atirar palavras em inglês para o meio das frases, e o Le Chat, da última vez que testei, ainda não falava português de Portugal de jeito. Teste simples que podes fazer: pede um texto na segunda pessoa do singular e vê se os verbos sobrevivem.


**Os modelos chineses — uma nota à parte**
Repararás que o Qwen (Alibaba), o DeepSeek e o Kimi (Moonshot) aparecem várias vezes acima. Não é acaso: são tecnicamente muito capazes, e gratuitos ou quase. Acedem-se por site, como os outros — não precisas de instalar nada.
A nota que lhes é específica: os dados vão para servidores na China, com regras de privacidade diferentes das europeias. Não é razão para pânico nem para os ignorar — é razão para critério. Aplica a regra do primeiro artigo com uma camada extra: não escrevas nada que não porias num email a um fornecedor externo. 


**Como decidir na prática**
Esquece os benchmarks e os rankings — mudam todos os meses e medem coisas que provavelmente não são o teu caso. A regra durável é outra:


**Dá a mesma tarefa real a dois ou três modelos e compara.** Um email que precisas mesmo de enviar, um documento que precisas mesmo de resumir. Vê qual devolve melhor. Repete com outro tipo de tarefa. Ao fim de uma semana sabes mais sobre o que te serve do que qualquer comparativo online.
O melhor modelo não é o que ganhou o benchmark. É o que funciona para ti, na tua língua, nas tuas tarefas.


**Nota de validade**
Este artigo foi escrito em Julho de 2026. Os nomes e as versões vão mudar — é garantido. Mas as regras de decisão ficam: leve para o corrente, pesado para o importante, janela grande para documentos longos, teste real antes de escolher. 


**O essencial em três linhas**
1. Modelo não é plataforma — procura o selector e aprende a usá-lo.

2. Leve para o dia-a-dia, pesado para o que importa.

3. Testa com tarefas reais tuas. O melhor modelo é o que funciona para ti.


Já sabes falar e já sabes com quem. No próximo artigo: **o que há por baixo das plataformas** — API, CLI, tokens, e porque é que alguns modelos só se alcançam por lá.
