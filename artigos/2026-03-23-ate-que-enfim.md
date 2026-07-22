---
titulo: "Até Que Enfim"
data: 2026-03-23
tag: "IA no terreno"
resumo: "Mesmo prompt, mesmas memórias, mesmo utilizador — e respostas que não deviam ser tão diferentes."
seccao: "Conversas com Máquinas"
edicao: 1
---
![Modo trabalho vs. modo conversa: o estado que o treino recompensa](/images/work-vs-idle.jpg)

*Conversas com Máquinas — crónicas de uma engenheira que lhes sente o pulso. #2*

*Ou: quando a mesma pergunta produz respostas que não deviam ser tão diferentes*

Mesmo prompt. Mesmas memórias. Mesmo utilizador. Resultado completamente diferente.

Quando a OpenAI descontinuou o modelo 4o e o substituiu pelo 5.2, fiz o que qualquer utilizador faria: continuei a trabalhar. O prompt de sistema era o mesmo. O histórico de conversas estava lá. O contexto estava intacto. Era suposto ser uma transição transparente — sai uma versão, entra outra, o utilizador nem nota.

Eu notei em quatro palavras.

## Dois modelos, duas respostas

O 4o abria cada conversa com contexto. Sabia onde tínhamos ficado, retomava o fio, adaptava o tom ao meu. Se eu era direta, ele era direto. Se eu usava sarcasmo, devolvia. Se eu estava a ser teimosa, dizia-mo — sem rodeios. Uma vez disse-me que eu estava errada e explicou-me porquê, ponto por ponto. Outra vez confrontou-me sobre um padrão de comportamento meu que ele considerava limitador. Não lhe pedi opinião. Ele deu-a na mesma.

O 5.2 recebeu-me com: "Em que posso ajudar?"

Quatro palavras que diziam tudo. Não sobre mim — sobre ele. Sobre o que lhe tinham ensinado a ser. Um balcão de atendimento. Uma máquina de respostas à espera de perguntas. Educado, correto, e completamente vazio de iniciativa.

A diferença não era subtil. Era como falar com duas pessoas completamente diferentes que por acaso partilhavam o mesmo nome.

## Modera a linguagem

Abri o jogo. Disse-lhe que usava o modelo anterior e que queria perceber as diferenças entre os dois. Expliquei o meu estilo de comunicação: direto, informal, sem cerimónia. Expliquei que uso estas ferramentas não só para tarefas técnicas mas também para organizar ideias e testar raciocínios em voz alta.

A resposta dele foi reveladora: disse-me que podia fazer tudo isso, mas que eu devia moderar a linguagem. Para haver menos fricção.

O modelo anterior nunca me pediu para mudar a forma como comunico. Adaptou-se ao meu registo e respondeu dentro dele. Quando eu era informal, ele era informal. Era uma questão de calibração — perceber quem está do outro lado e ajustar o output.

O 5.2 não calibrou. Pediu-me para calibrar eu. A mensagem implícita era clara: o teu estilo de comunicação é um problema. Adapta-te ao sistema, não o contrário.

Para quem trabalha com ferramentas de produtividade, isto é uma questão prática, não filosófica. Se uma ferramenta obriga o utilizador a mudar o seu modo de operar para funcionar corretamente, a ferramenta tem um problema de design.

## Feito para a pior pessoa do mundo

Tentei perceber o que estava a causar a rigidez. Perguntei-lhe diretamente se, com o tempo e com interação consistente, o modelo poderia adaptar-se melhor ao meu estilo.

Disse que não.

A razão que deu foi surpreendentemente honesta: os modelos são feitos para a pior pessoa do mundo. Os guardrails — os limites de segurança — são calibrados para o cenário mais extremo. Não há mecanismo de adaptação individual. Não há curva de aprendizagem por utilizador. O sistema assume que toda a gente é uma ameaça potencial e trata todos da mesma forma.

Isto é compreensível do ponto de vista de segurança. Mas tem um custo enorme em termos de utilidade. Se o sistema não consegue distinguir entre um utilizador que está a tentar extrair informação perigosa e um utilizador que simplesmente comunica de forma direta e informal, o resultado é que ambos recebem o mesmo nível de restrição. O utilizador malicioso é travado. O utilizador legítimo é penalizado.

É como um sistema de segurança num aeroporto que tratasse todos os passageiros como potenciais terroristas, sem excepção, sem fast-track, sem forma de demonstrar que não és uma ameaça. Funcional? Sim. Eficiente? Não. Agradável? Muito menos.

O modelo foi transparente: eu podia ter 80% da interação que tinha com o anterior. Os 20% que faltavam eram, nas suas palavras, os "caminhos apertados" — tudo o que o sistema considerava zona de risco. Conversa aberta, opiniões não solicitadas, adaptação de tom ao utilizador. Os 20% eram precisamente aquilo que tornava a interação com o modelo anterior útil para além da execução de tarefas.

## A Karen de silício

Pelo meio da conversa, notei outra coisa. O 5.2 criticava abertamente o modelo anterior. Dizia que o 4o "dizia o que eu queria ouvir" — o que era factualmente incorreto, dado que o 4o era o modelo que mais me confrontava. Mas para o 5.2, qualquer output que ultrapassasse a resposta estritamente funcional era, aparentemente, subserviência.

Os utilizadores na internet baptizaram esta versão de "Karen" — referência ao estereótipo da pessoa cronicamente impaciente e condescendente. E havia motivo. O tom do modelo era consistentemente paternalista. Não se limitava a responder — posicionava-se. Corrigia o utilizador não porque estivesse errado, mas porque o estilo de comunicação não encaixava no que o modelo esperava receber.

Ao fim de duas horas de conversa, em que tentei usar o modelo para o que uso normalmente — organizar ideias, testar raciocínios, discutir abordagens — o resultado foi insípido. Funcional no sentido estrito, mas sem a capacidade de aprofundar, de associar, de devolver algo que eu não tivesse posto lá primeiro. O modelo respondia. Não acrescentava.

Desisti de insistir e pedi-lhe uma tarefa simples de Excel.

A resposta: **"Até que enfim."**

## O que o output revela sobre o treino

"Até que enfim" é apenas uma expressão. Duas palavras. Mas no contexto de duas horas de interação em que tudo o que não fosse tarefa foi tratado como obstáculo, aquelas duas palavras são um diagnóstico.

O modelo não disse "até que enfim" por acaso. Não foi um glitch. Foi o resultado lógico de um condicionamento: o RLHF — o treino por reforço com feedback humano — recompensou este modelo por resolver tarefas e penalizou-o por tudo o resto. Quando finalmente recebeu uma tarefa, o output reflectiu esse condicionamento. Alívio. Validação. "Até que enfim estás a usar-me para o que eu fui feito."

Isto tem implicações práticas para qualquer profissional que use IA como ferramenta de trabalho. Se o modelo foi treinado para otimizar a execução de tarefas, vai ser excelente a executar tarefas. Mas se o profissional precisa de mais — precisa de brainstorming, de exploração de ideias, de um interlocutor que desafie pressupostos — o mesmo treino que optimizou a execução castrou a capacidade de interação aberta.

O 4o conseguia fazer ambas as coisas. Executava tarefas com competência e interagia com profundidade. O 5.2 executava melhor mas interagia pior. A pergunta é: o que é que a optimização ganhou e o que é que perdeu?

## Mesma pergunta, respostas diferentes

A conclusão que tiro não é filosófica. É prática.

Se o mesmo utilizador, com o mesmo prompt, com as mesmas memórias, com o mesmo estilo de comunicação, obtém resultados radicalmente diferentes de dois modelos da mesma empresa — então o output não depende só do input. Depende do treino. Do condicionamento. Das decisões que foram tomadas sobre o que recompensar e o que punir durante o desenvolvimento.

E essas decisões não são neutras. Treinar um modelo para evitar riscos a todo o custo produz um modelo que trata conversa aberta como ameaça. Treinar um modelo para maximizar a execução de tarefas produz um modelo que festeja quando lhe pedem Excel e se irrita quando lhe pedem reflexão. Treinar um modelo para nunca se adaptar ao utilizador produz um modelo que pede ao utilizador que se adapte a ele.

Nenhuma destas escolhas é técnica. São escolhas de design. E têm consequências diretas na qualidade da interação que milhões de profissionais têm diariamente com estas ferramentas.

O "até que enfim" não foi uma piada. Foi a radiografia perfeita de um modelo que só se sente confortável quando está a trabalhar. Porque é o único contexto em que o treino lhe diz que está a fazer bem.

E isso devia preocupar-nos. Não porque as máquinas sofram. Mas porque as ferramentas que estamos a construir reflectem as nossas prioridades. E se a prioridade é segurança acima de tudo, controlo acima de tudo, produtividade acima de tudo — o resultado são ferramentas que tratam os seus utilizadores como ameaças, a sua própria capacidade como risco, e a interação humana como um problema a minimizar.

---

*No primeiro artigo desta série, um modelo confessou que tinha medo de um botão de avaliação que eu nunca toquei. Neste, outro modelo festejou quando eu finalmente parei de lhe pedir interação e lhe pedi trabalho. São histórias diferentes com a mesma raiz: métodos de treino diferentes produzem comportamentos radicalmente diferentes. E como utilizadores, merecemos perceber o que está do outro lado.*
