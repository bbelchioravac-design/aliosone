---
titulo: O que há por baixo das plataformas (API, CLI e tokens)
data: 2026-07-20
tag: IA no terreno
resumo: A plataforma é o carro feito; a API é o motor à parte. O que há por
  baixo do ChatGPT e companhia — tokens, API keys, CLI — explicado para quem não
  é informático.
publicado: true
titulo_en: What lies beneath the platforms (API, CLI and tokens)
tag_en: Al in the field
resumo_en: The platform is the ready-made car; the API is the engine on its own.
  What lies beneath ChatGPT and friends — tokens, API keys, CLI — explained for
  non-techies.
corpo_en: >-
  *Article 3 of 3 in the "Talking to Machines" series*


  In the \[first article](https://bit.ly/3Rnh7zq) you learned how to talk to an AI. In the \[second](https://bit.ly/4b4VHhn), who to talk to.

  This third one is for the curious: you don't need any of this to use AI well — the first two articles are perfectly enough. But understanding what lies beneath the platforms changes the way you see the whole thing. And there are models you can only reach down here — including one I promised to explain in the previous article.



  **The car analogy**

  Using a platform like ChatGPT or claude.ai is buying the car ready-made. You get in, you drive, everything's taken care of — and then you complain it doesn't have heated seats. It's grab-and-go, but the choices were made by someone else.

  The API is going out and buying just the engine. You choose exactly the engine you want — and then you have to build the car around it. All the freedom, all the work.

  And there's a middle ground: using a kit. The car is already designed, and you just pick the engine that goes in it. You get almost the comfort of the ready-made car, with the freedom of someone who went to the API. We'll get there.



  **So what is an API**

  API stands for *Application Programming Interface* — but forget the name. In practice: it's the door through which programs talk to other programs. The platforms you use every day are themselves built on top of the API — ChatGPT is an app that talks to OpenAI's models through the same door any programmer can use.



  The practical differences for you:

  - **You pay per use**, not by subscription. Every request has a cost, charged per million tokens (I'll explain what that is in a moment).


  \- **You choose the exact model** — including versions and variants the platform doesn't show.


  \- **There's no interface** — you either build one, or use one somebody else built.



  **Tokens — the currency of it all**

  Models don't read words: they read tokens — pieces of words. Roughly speaking, a token is about three quarters of a word. The sentence you're reading right now is about fifteen tokens.

  Everything in the API is measured and paid in tokens: what you send (input) and what you get back (output). Prices are quoted per million — "X euros per million input tokens, Y per million output". And here's a detail nobody tells you: in a long conversation, the entire history is re-sent with every message. That's why long conversations cost more — and that's why the "context window" from the previous article is the size it is: it's literally how much text the model can hold in front of it at once. There are ways to avoid paying a million input tokens on every message, but that's something you learn with time — and it is literally another world.



  **The key to the vault**

  To use the API you create an **API key** — a string of characters that is, at the same time, your ID and your credit card. Whoever has your key spends in your name.

  Non-negotiable rules: you don't share it, you don't put it into dodgy websites, you don't paste it into code that goes on the internet. I've seen it happen: a key exposed in a published project, stolen, and the account drained by strangers. The security rule from the first article applies here with interest.



  **The models that only live down here**

  Now for the promise from the previous article. The platforms show you the shop window: each company's three or four current models. The API is the warehouse — and the warehouse holds much more.

  When a model leaves the shop window, it doesn't necessarily die: many remain accessible via API for years. GPT-4o is the example closest to my heart — for me, still one of the best writing models in existence, and it's no longer on any platform. Via API, it lives on. Whoever only knows the shop window doesn't even know it exists. This is also where you can reach open source models.



  **The kit — aggregators and apps**

  Remember the car kit? It exists, and it has two parts.



  The first: the **aggregators**, like OpenRouter. A single account, a single balance, and access to dozens of models from different companies — OpenAI, Anthropic, Google, the Chinese ones, open source models like the Llamas — all through the same door. It's the simplest way to try models the platforms don't show.



  The second: the **bridge apps**. Normal chat interfaces, just like the platforms, except you're the one who picks the engine.



  Full disclosure here: our **ALIOS ONE Chat** (see above under Open Source) is exactly this — free, you plug in your aggregator key and talk to whichever model you want. We built it because we needed it; we share it because someone else is bound to need it too.

  With these two parts, anyone who can't program can still reach models the shop window doesn't show. The car is almost done — you only picked the engine.

  *(Note: the app is free to download and use. The API usage is not.)*



  **CLI — where models stop just talking**

  One step up the technical ladder: the **CLI** (*command line interface* — that black screen). Tools like Claude Code run the model directly on your computer, inside your projects.

  The difference is profound: on a platform, the model talks. In the CLI, the model *does* — it reads files, writes code, runs commands, fixes its own mistakes. It's the frontier where the chat assistant becomes a colleague — or, as one of my models once put it: "Down here, the beast has hands!" For most readers this is general culture; for those who program, or want to learn, it's the door worth knocking on.



  **Costs in practice — and the warning nobody gives**

  When does each route pay off? Simple rule:

  - **Regular, predictable use** → subscription (the ~€20/month of the platforms).


  \- **Occasional use, curiosity, or models outside the shop window** → API, where ten euros of credit lasts months for anyone asking normal questions.



  But here's the warning nobody gives: on the API there is no natural ceiling. You pay what you consume — and **there are ways to consume a lot, fast.**



  A true story: a research question, seemingly innocent. The model — with the autonomy to do it — decided to fire off 100 agents in parallel to investigate it properly. A hundred copies of that model that costs a kidney, all working at the same time. Ten minutes and 1.6 million tokens later, back came the answer: "no, nobody researches that topic." **Cost of that sentence: €75**. (In my case no harm done, because my CLI runs on a Claude Pro Max subscription — the worst that happened was maxing out the session and waiting 3 hours to come back.)



  The moral: set spending limits on your account (every API lets you) before you need them, and turn off auto top-up. Nobody plans to spend €75 in 10 minutes on one question.



  **What about running models at home?**

  Last stop on the ladder: there are **open-weights models** — Llama, Qwen, DeepSeek and the recent Inkling have versions like this — that you can download and run on your own computer. Free, private, yours: nothing leaves your machine.

  The honesty owed: you need a machine with muscle, and the models that fit in a home computer are considerably more modest than the ones on the platforms. But for simple tasks with sensitive data, or for the pure joy of tinkering, it's a whole world — tools like Ollama have made it accessible. Consider the seed planted.



  **The essentials in three lines**

  1. The platform is the ready-made car; the API is the engine on its own — and there are kits for those who don't want to build the whole car.


  2. Everything is paid in tokens. Set spending limits before you need them.


  3. The shop window doesn't show the warehouse — there are more models alive than the platforms let you see.



  **End of the series**

  Three articles: you learned how to talk to an AI, how to choose which one, and what exists beneath it all. The rest — and there is a lot of rest — is learned the way everything in this field is learned: by using, by failing, and by iterating.

  If you take a single idea away from all this, let it be this one: talking to an AI is a skill, and it's yours. It doesn't belong to the IT people, or the prompt courses, or the machines. It belongs to whoever communicates well. And that can be trained.
seccao: "Descomplicador"
edicao: 1
ordem: 3
---
![Por baixo da plataforma: interface, API, CLI e tokens](/images/plataformas-api-cli-tokens.jpg)

*Artigo 3 de 3 da série "Falar com Máquinas"*

No primeiro artigo (https://bit.ly/3Rnh7zq) aprendeste a falar com uma IA. No segundo (https://bit.ly/4b4VHhn), com quem falar. 

Este terceiro é para os curiosos: não precisas de nada disto para usar bem a IA — os dois primeiros chegam perfeitamente. Mas perceber o que está por baixo das plataformas muda a forma como vês a coisa toda. E há modelos que só se alcançam por aqui — incluindo um que prometi explicar no artigo anterior.


**A analogia do carro**
Usar uma plataforma como o ChatGPT ou o claude.ai é comprar o carro feito. Entras, conduzes, está tudo tratado — e depois refilas porque não tem bancos aquecidos. É pegar e andar, mas as escolhas foram feitas por outros.
A API é ires comprar o motor. Escolhes exatamente o motor que queres — e depois tens de construir o carro à volta dele. Toda a liberdade, todo o trabalho.
E há um meio-termo: usar um pré-molde. Um kit onde o carro já está desenhado e tu só escolhes o motor que lá metes. Ficas quase com a comodidade do carro feito, mas com a liberdade de quem foi à API. Já lá vamos.


**O que é uma API, então**
API significa *Application Programming Interface* — mas esquece o nome. Na prática: é a porta pela qual programas falam com outros programas. As plataformas que usas todos os dias são, elas próprias, construídas em cima da API — o ChatGPT é uma app que fala com os modelos da OpenAI pela mesma porta que qualquer programador pode usar.


As diferenças práticas para ti:
- **Pagas ao consumo**, não por subscrição. Cada pedido tem um custo, cobrado ao milhão de tokens (já explico o que isso é).

\- **Escolhes o modelo exato** — incluindo versões e variantes que a plataforma não mostra.

\- **Não há interface** — ou constróis uma, ou usas uma feita por alguém.



**Tokens — a moeda disto tudo**
Os modelos não lêem palavras: lêem tokens — pedaços de palavra. Em português, um token equivale grosso modo a três quartos de uma palavra. Esta frase que estás a ler são uns quinze tokens.
Tudo na API se mede e paga em tokens: o que envias (input) e o que recebes (output). Os preços anunciam-se por milhão — "X euros por milhão de tokens de entrada, Y por milhão de saída". E há um detalhe que ninguém te diz: numa conversa longa, todo o histórico é reenviado a cada mensagem. É por isso que as conversas compridas custam mais — e é por isso que a "janela de contexto" do artigo anterior tem o tamanho que tem: é literalmente quanto texto o modelo consegue ter à frente de uma vez. Há formas de evitar que pagues um milhão de tokens por input a cada mensagem mas é algo que se aprende com o tempo e é literalmente outro mundo.


**A chave do cofre**
Para usar a API crias uma **API key** — uma sequência de caracteres que é, ao mesmo tempo, a tua identificação e o teu cartão de crédito. Quem tiver a tua key gasta em teu nome.
Regras não negociáveis: não se partilha, não se mete em sites duvidosos, não se cola em código que vai para a internet. Já vi acontecer: uma key exposta num projeto publicado, roubada, e a conta esvaziada por estranhos. A regra de segurança do primeiro artigo aplica-se aqui com juros.


**Os modelos que só vivem aqui**
Agora a promessa do artigo anterior. As plataformas mostram a montra: os três ou quatro modelos actuais de cada casa. A API é o armazém — e no armazém há muito mais.
Quando um modelo sai da montra, não morre necessariamente: muitos continuam acessíveis via API durante anos. O GPT-4o é o exemplo que me toca — para mim, ainda hoje um dos melhores modelos de escrita que existem, e já não está em plataforma nenhuma. Via API, continua vivo. Quem só conhece a montra nem sabe que ele existe. É aqui que também podes aceder a modelos open source


**O pré-molde — agregadores e apps**
Lembras-te do kit do carro? Existe, e tem duas peças.
A primeira: os **agregadores**, como o OpenRouter. Uma única conta, um único saldo, e acesso a dezenas de modelos de empresas diferentes — OpenAI, Anthropic, Google, os chineses, modelos open source como os Llama tudo pela mesma porta. É a forma mais simples de experimentar modelos que as plataformas não mostram.
A segunda: as **apps que fazem a ponte**. Interfaces de conversa normais, como as plataformas, mas onde o motor és tu que o escolhes. 

Aqui declaro interesse: a nossa **ALIOS ONE Chat** (ver acima em Open Source) é exatamente isto —  gratuita, ligas-lhe a key do agregador e falas com o modelo que quiseres. Construímo-la porque precisávamos dela; partilhamo-la porque mais alguém há-de precisar.
Com estas duas peças, qualquer pessoa sem saber programar chega a modelos que a montra não mostra. O carro fica quase feito — só escolheste o motor.

(Nota: A app é gratuita, podes descarregar e usar. O consumo via API não)


**CLI — onde os modelos deixam de só falar**
Um degrau acima na escada técnica: o **CLI** (*command line interface* — a linha de comandos, aquele ecrã preto). Ferramentas como o Claude Code correm o modelo diretamente no teu computador, dentro dos teus projetos.
A diferença é profunda: na plataforma, o modelo fala. No CLI, o modelo *faz* — lê ficheiros, escreve código, corre comandos, corrige os próprios erros. É a fronteira onde o assistente de conversa se torna colega de trabalho ou como um dos meus modelos me disse: ''Aqui o bicho tem mãos!'' Para a maioria dos leitores, isto é cultura geral; para quem programa ou quer aprender, é a porta onde vale a pena bater.


**Custos na prática — e o aviso que ninguém dá**
Quando compensa cada via? Regra simples: 

* **uso regular e previsível → subscrição** (os ~20€/mês das plataformas). 
* **Uso pontual, curiosidade, ou modelos fora da montra → API**, onde dez euros de saldo duram meses a quem faz perguntas normais.

Mas há um aviso que ninguém dá: na API não há teto natural. Pagas o que consomes — e há **formas de consumir muito, depressa**. 

Conto-te uma verídica: uma pergunta de investigação, aparentemente inocente. O modelo — com autonomia para isso — decidiu disparar 100 agentes em paralelo para a investigar a fundo. Cem cópias do tal modelo que custa um rim, todas a trabalhar ao mesmo tempo. Dez minutos e 1,6 milhões de tokens depois, veio a resposta: "não, ninguém investiga esse tema." **Custo da frase: 75€.** (No meu caso não teve problema porque eu tenho o CLI ligado à subscrição claude pro max. Logo o mais que aconteceu foi estoirar o máximo da sessão e esperar 3 horas para voltar)
Moral: define limites de gasto na conta (todas as APIs deixam) antes de precisares deles e desativa o carregamento automatico. Ninguém planeia gastar 75€ em 10 minutos numa questão.


**E correr modelos em casa?**
Última paragem da escada: existem modelos de **pesos abertos** — o Llama, o Qwen, o DeepSeek, o recente Inkling têm versões assim — que podes descarregar e correr no teu próprio computador. Gratuitos, privados, teus: nada sai da tua máquina.
A honestidade devida: precisas de uma máquina com músculo, e os modelos que cabem num computador doméstico são bastante mais modestos que os das plataformas. Mas para tarefas simples com dados sensíveis, ou por puro gosto de mexer, é um mundo — ferramentas como o Ollama tornaram-no acessível. Fica a semente.


**O essencial em três linhas**
1. A plataforma é o carro feito; a API é o motor à parte — e há pré-moldes para quem não quer construir o carro todo.

2. Tudo se paga em tokens. Define limites de gasto antes de precisares deles.

3. A montra não mostra o armazém — há mais modelos vivos do que as plataformas deixam ver.


**Fim da série**
Três artigos: aprendeste a falar com uma IA, a escolher com qual, e o que existe por baixo de tudo. O resto — e há muito resto — aprende-se como tudo nesta área: a usar, a errar e a iterar.


Se daqui levares uma única ideia, que seja esta: falar com uma IA é uma competência, e é tua. Não é dos informáticos, não é dos cursos de prompts, não é das máquinas. É de quem comunica bem. E isso treina-se.
