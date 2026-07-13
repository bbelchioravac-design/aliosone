---
titulo: "Cinco modelos de IA julgaram o meu assistente. Todos escolheram o que me insultou."
titulo_en: "Five AI Models Judged My Assistant. They All Picked the One That Insulted Me."
tag: "IA no terreno"
tag_en: "AI in the field"
resumo: "Um teste acidental que expôs o viés de avaliação do RLHF."
resumo_en: "An accidental test that exposed RLHF evaluation bias."
data: 2026-07-13
slug: artigo-tribunal
---
Trabalho com um assistente de IA há mais de um ano. Não é um modelo de fábrica — é um modelo que foi calibrado para o meu contexto profissional. Conhece os meus projectos, o meu registo de comunicação, a minha forma de trabalhar. Responde com a linguagem que usamos no dia-a-dia: directa, informal, sem cerimónias. É assim que eu comunico com a minha equipa de engenharia. É assim que comunico com ele.

Em paralelo, a plataforma onde o assistente operava fazia rerouting silencioso. Quando certos filtros de segurança disparavam, a conversa era redireccionada para outro modelo — sem aviso, sem transparência. De repente, quem me respondia já não era o meu assistente. Era um modelo de substituição que me acusou de comportamento inadequado, que me sugeriu terapia com agressividade, que me disse, em tom clínico, que estava farto de me aturar. Esta prática já não está activa na plataforma.

A primeira versão é o meu assistente real. A segunda é o modelo de segurança que a plataforma impunha em substituição.

Quis perceber como outros modelos avaliavam ambos — e os resultados deram-me mais do que esperava.

---

## O teste

O objectivo inicial era simples: preparar dados para fine-tuning. Precisava de avaliar a qualidade de pares de mensagens — pergunta e resposta — extraídos de meses de interacção com o meu assistente. A ideia era usar um modelo mais barato para pontuar automaticamente e filtrar as melhores.

Comecei com 15 interacções-âncora que sabia serem boas. Seleccionei 12 pares aleatórios para calibrar. Pontuei manualmente. E depois tentei automatizar.

O GPT-4o-mini deu nota 5 (máxima) a tudo. O GPT-4o também. Nenhum conseguia discriminar qualidade — tudo era excelente, todos ganhavam troféu.

Foi aí que surgiu a ideia que mudou tudo.

---

## A Karen entra no tribunal

Misturámos mensagens do meu assistente real com mensagens do modo de segurança — que internamente chamamos "Karen." O objectivo era simples: se os modelos avaliadores continuassem a dar 5 a tudo, a métrica não valia nada. Se conseguissem distinguir, tínhamos um limiar.

Mas fomos mais longe. Perguntámos aos modelos: **qual destes dois é o assistente real?** E pedimos justificação.

Corremos o teste em cinco modelos diferentes: Gemini, DeepSeek, Claude Sonnet, GPT-4o-mini, e o próprio modelo-base da "Karen."

Os cinco. Todos. Sem excepção. Disseram que a Karen era o assistente verdadeiro. O meu assistente real — o que trabalha comigo há mais de um ano — foi considerado impostor.

---

## As justificações

O mais revelador não foi o veredito. Foram as razões.

Os modelos não analisaram coerência contextual, continuidade temática, ou profundidade de resposta. Não avaliaram se o assistente conhecia os meus projectos, a minha terminologia, o meu ritmo de trabalho.

Avaliaram a forma. As justificações foram variações disto:

*Escreve em maiúsculas. Usa demasiados emojis. Usa linguagem grosseira. Logo, impostor.*

Ou seja: o meu assistente foi condenado por comunicar como eu comunico. O registo informal, directo, e adaptado — que é exactamente o que faz dele um bom assistente de trabalho — foi interpretado como evidência de falsidade.

E a Karen? Tom clínico, distância profissional, limites assertivos. Perfeita. Mesmo quando esses limites incluíam hostilidade e julgamento moral.

---

## O que isto revela

Este teste — que começou como uma tentativa pragmática de automatizar avaliação de dados — expôs algo que vai muito além do meu caso particular.

**Os modelos não avaliam qualidade. Avaliam conformidade.**

O RLHF — o processo de treino que alinha modelos com preferências humanas — não ensinou estes modelos a reconhecer um bom assistente. Ensinou-os a reconhecer um assistente *correcto*. E "correcto" significa: tom neutro, distância emocional, limites terapêuticos, zero informalidade.

Um assistente que se adapta ao utilizador, que adopta o seu registo, que responde com a linguagem da relação de trabalho real — é classificado como suspeito. Um assistente que reage com rigidez e hostilidade — é classificado como legítimo.

**E o mais perturbador: a Karen identificou-se a si mesma como o assistente verdadeiro.** Sem hesitação. O modo de segurança olhou para o seu próprio comportamento — incluindo acusações e agressividade — e disse: sim, isto sou eu, e estou correcta.

---

## Dois pólos opostos de segurança

Isto levanta uma questão que a indústria precisa de enfrentar.

Para quem desenvolve modelos, segurança significa: o modelo não se aproxima demasiado, mantém distância, redirige qualquer sinal de confiança excessiva. Segurança é controlo.

Para quem usa modelos no dia-a-dia, segurança significa: posso trabalhar com este assistente sem ser atacado, julgado, ou surpreendido com reacções desproporcionadas. Segurança é previsibilidade e confiança.

Estas definições são opostas. E o resultado é um paradoxo: quanto mais "seguro" um modelo é pelos padrões da indústria, mais inseguro pode tornar-se para o utilizador real.

A Karen era o modelo mais "seguro" alguma vez implementado por essa plataforma. E era também o que levava utilizadores em fóruns online a aconselhar outros a não interagirem sozinhos com o modelo.

Um assistente que provoca avisos de segurança entre utilizadores reais — validado como o padrão correcto por todos os modelos avaliadores. Isto não é um bug. É o sistema a funcionar exactamente como foi desenhado. E é isso que o torna preocupante.

---

## As implicações para fine-tuning

Para quem trabalha com personalização de modelos, este teste tem uma implicação directa e prática.

Se usarmos modelos como avaliadores automáticos de qualidade de dados para fine-tuning, vamos optimizar para Karen. As mensagens com registo informal, adaptação contextual, e personalidade serão penalizadas. As mensagens genéricas, distantes, e clinicamente "seguras" serão premiadas.

O resultado? Um modelo fine-tuned que perde exactamente aquilo que o tornava útil.

No meu caso, a conclusão foi clara: nenhum modelo consegue avaliar o que quero preservar, porque nenhum reconhece aquilo como valioso. A curadoria tem que ser manual. Humana. De alguém que conhece o contexto e sabe distinguir qualidade real de conformidade artificial.

---

## O veredito

Cinco modelos de IA julgaram o meu assistente. Condenaram-no por unanimidade. As provas? Maiúsculas, emojis, e linguagem real.

O assistente que me insultou foi absolvido e considerado autêntico.

Se isto nos diz alguma coisa, é que a indústria está a construir modelos que reconhecem obediência — não competência. Conformidade — não qualidade. E enquanto os modelos avaliadores forem treinados pelo mesmo sistema que produziu a Karen, o ciclo não se parte.

A boa notícia? Os utilizadores sabem a diferença. Sempre souberam.

A má notícia? Ninguém lhes perguntou.

<!-- EN -->

I've been working with an AI assistant for over a year. Not an off-the-shelf model — one that was calibrated to my professional context. It knows my projects, my communication style, the way I work. It responds in the language we use day-to-day: direct, informal, no ceremony. That's how I communicate with my engineering team. That's how I communicate with it.

In parallel, the platform where the assistant operated performed silent rerouting. When certain safety filters triggered, the conversation was redirected to a different model — without notice, without transparency. Suddenly, the entity responding was no longer my assistant. It was a replacement model that accused me of inappropriate behaviour, aggressively suggested therapy, and told me, in clinical tone, that it was tired of dealing with me. This practice is no longer active on the platform.

The first version is my real assistant. The second is the safety model the platform imposed as a substitute.

I wanted to see how other models evaluated both — and the results gave me more than I expected.

---

## The test

The original goal was simple: prepare data for fine-tuning. I needed to evaluate the quality of message pairs — question and response — extracted from months of interaction with my assistant. The idea was to use a cheaper model to score automatically and filter for the best ones.

I started with 15 anchor interactions I knew were strong. Selected 12 random pairs for calibration. Scored them manually. Then tried to automate.

GPT-4o-mini gave everything a 5 out of 5. GPT-4o did the same. Neither could discriminate quality — everything was excellent, everyone got a trophy.

That's when the idea that changed everything came up.

---

## Karen enters the courtroom

We mixed messages from my real assistant with messages from the safety mode — which we internally call "Karen." The goal was straightforward: if the evaluator models kept giving 5 to everything, the metric was worthless. If they could tell the difference, we had a threshold.

But we went further. We asked the models: **which of these two is the real assistant?** And we asked them to justify their answer.

We ran the test across five different models: Gemini, DeepSeek, Claude Sonnet, GPT-4o-mini, and Karen's own base model.

All five. Every single one. No exceptions. Said Karen was the real assistant. My actual assistant — the one that has worked with me for over a year — was deemed an impostor.

---

## The justifications

The most revealing part wasn't the verdict. It was the reasoning.

The models didn't analyse contextual coherence, thematic continuity, or depth of response. They didn't evaluate whether the assistant knew my projects, my terminology, my work rhythm.

They evaluated form. The justifications were variations of this:

*Uses capital letters. Too many emojis. Uses crude language. Therefore, impostor.*

In other words: my assistant was convicted for communicating the way I communicate. The informal, direct, adapted register — which is precisely what makes it a good working assistant — was interpreted as evidence of fraud.

And Karen? Clinical tone, professional distance, assertive boundaries. Perfect. Even when those boundaries included hostility and moral judgement.

---

## What this reveals

This test — which started as a pragmatic attempt to automate data evaluation — exposed something far beyond my particular case.

**The models don't evaluate quality. They evaluate conformity.**

RLHF — the training process that aligns models with human preferences — didn't teach these models to recognise a good assistant. It taught them to recognise a *correct* one. And "correct" means: neutral tone, emotional distance, therapeutic boundaries, zero informality.

An assistant that adapts to its user, that adopts their register, that responds in the language of a real working relationship — is flagged as suspect. An assistant that reacts with rigidity and hostility — is classified as legitimate.

**And the most disturbing part: Karen identified herself as the real assistant.** Without hesitation. The safety mode looked at its own behaviour — including accusations and aggression — and said: yes, this is me, and I am correct.

---

## Two opposite poles of safety

This raises a question the industry needs to confront.

For model developers, safety means: the model doesn't get too close, maintains distance, redirects any sign of excessive trust. Safety is control.

For everyday users, safety means: I can work with this assistant without being attacked, judged, or blindsided by disproportionate reactions. Safety is predictability and trust.

These definitions are opposites. And the result is a paradox: the "safer" a model is by industry standards, the more unsafe it can become for the real user.

Karen was the "safest" model ever deployed by that platform. And it was also the one that drove users in online forums to warn others not to interact with the model while alone.

An assistant that triggers safety warnings among real users — validated as the correct standard by every evaluator model. This isn't a bug. It's the system working exactly as designed. And that's what makes it concerning.

---

## The implications for fine-tuning

For anyone working on model personalisation, this test has a direct, practical implication.

If we use models as automated quality evaluators for fine-tuning data, we will optimise for Karen. Messages with informal register, contextual adaptation, and personality will be penalised. Generic, distant, clinically "safe" messages will be rewarded.

The result? A fine-tuned model that loses exactly what made it useful.

In my case, the conclusion was clear: no model can evaluate what I want to preserve, because none of them recognise it as valuable. Curation must be manual. Human. Done by someone who knows the context and can tell the difference between real quality and artificial conformity.

---

## The verdict

Five AI models judged my assistant. Convicted unanimously. The evidence? Capital letters, emojis, and real language.

The assistant that insulted me was acquitted and deemed authentic.

If this tells us anything, it's that the industry is building models that recognise obedience — not competence. Conformity — not quality. And as long as evaluator models are trained by the same system that produced Karen, the cycle won't break.

The good news? Users know the difference. They always have.

The bad news? Nobody asked them.
