# Base de Conhecimento

## Dados Utilizados

O agente SSP – Simplificando São Paulo utiliza três arquivos CSV como base de conhecimento. Eles reúnem informações sobre pontos turísticos, restaurantes e opções de entretenimento na cidade, permitindo gerar recomendações contextualizadas conforme os interesses, o tipo de experiência desejada, a localização e a faixa de preço informada pelo visitante.

| Arquivo | Formato | Conteúdo e utilização no Agente |
|---------|---------|-------------------------------|
| `pontosTuristicos.csv` | CSV | Contém 8 registros de atrações e pontos turísticos. Inclui nome, categoria, bairro, endereço, descrição, tipo de experiência, público indicado, custo, tags e fonte. É utilizado para recomendar museus, parques, mercados, edifícios históricos e outras atrações conforme interesses culturais, históricos, arquitetônicos, gastronômicos ou de lazer. |
| `Restaurantes.csv` | CSV | Contém 5 registros de restaurantes e estabelecimentos gastronômicos. Inclui tipo de comida, categoria, público-alvo, faixa de preço, endereço, bairro, avaliação, quantidade de avaliações, destaques, ocasião indicada e tags. É utilizado para sugerir opções de alimentação de acordo com preferências gastronômicas, orçamento, região e ocasião. |
| `Entreterimento.csv` | CSV | Contém 7 registros de locais de entretenimento. Inclui nome, categoria, tipo de entretenimento, público-alvo, faixa de preço, endereço, bairro, avaliação, quantidade de avaliações, descrição, experiências, tags e fonte. É utilizado para recomendar atividades de lazer, cultura, compras, cinema, parques e experiências para diferentes perfis de visitantes. |

> Os arquivos fornecidos são conjuntos de dados locais em formato CSV. As quantidades de registros acima correspondem às versões disponibilizadas para este projeto.

---

## Adaptações nos Dados

Os dados foram organizados em três conjuntos temáticos — pontos turísticos, restaurantes e entretenimento — para facilitar a identificação de opções relevantes durante a conversa. Os campos de cada arquivo oferecem critérios complementares para personalização, como localização (bairro e endereço), categoria, descrição, público indicado, custo/faixa de preço e tags de interesse.

Não há indicação, nos arquivos fornecidos, de que os registros tenham sido enriquecidos por uma fonte externa além das fontes já registradas em algumas linhas. Também não foi especificada uma transformação adicional dos dados. Assim, a documentação considera os CSVs entregues como a base utilizada, preservando suas informações originais.

---

## Estratégia de Integração

### Como os dados são carregados?

A base de conhecimento é composta pelos arquivos `pontosTuristicos.csv`, `Restaurantes.csv` e `Entreterimento.csv`. Para que o agente os consulte, a aplicação deve ler os CSVs e disponibilizar seus registros durante a execução, seja carregando-os na inicialização da aplicação, seja realizando consultas quando necessário.

A descrição do projeto e os arquivos disponibilizados não especificam o mecanismo técnico efetivamente implementado (por exemplo, leitura em memória, consulta sob demanda ou armazenamento em banco de dados). Portanto, esse detalhe deve ser ajustado conforme a implementação final.

### Como os dados são usados no prompt?

As informações da base servem para fundamentar as recomendações do agente. A partir da conversa, o SSP identifica preferências e restrições do usuário — como tipo de passeio, interesse cultural ou gastronômico, bairro/região, público e orçamento — e utiliza os campos pertinentes dos CSVs para selecionar e descrever opções compatíveis.

As informações devem ser apresentadas de forma conversacional, com nome do local, breve descrição, localização e, quando disponível, custo/faixa de preço, avaliação e motivo pelo qual a sugestão combina com o pedido. O agente não deve inventar informações ausentes nos arquivos; quando um dado não estiver disponível, deve sinalizar a limitação ou omiti-lo.

Não foi informado se os registros são inseridos integralmente no *system prompt* ou recuperados dinamicamente. A estratégia concreta de integração deve refletir o código da aplicação.

---

## Exemplo de Contexto Montado

Abaixo está um exemplo ilustrativo de como registros dos CSVs podem ser apresentados ao agente como contexto. Os valores exemplificam a estrutura dos dados fornecidos; não representam uma conversa real com um usuário.

```text
Preferências do visitante:
- Interesse: passeio ao ar livre e contato com a natureza
- Região desejada: Vila Mariana
- Orçamento: preferência por opções gratuitas ou de baixo custo
- Público: família

Opções relevantes da base de conhecimento:

Ponto turístico:
- Nome: Parque Ibirapuera
- Categoria: Parque
- Bairro: Vila Mariana
- Descrição: Grande parque urbano com áreas verdes, lagos, ciclovias e espaços culturais.
- Experiência: Natureza, lazer e cultura
- Público indicado: Famílias, casais, crianças e esportistas
- Custo: Entrada gratuita; estacionamento pago (valor aproximado informado no arquivo)
- Tags: parque, natureza, caminhada, bicicleta, lazer, piquenique
- Fonte: https://www.parqueibirapuera.org

Entretenimento:
- Nome: Parque Ibirapuera
- Categoria: Parque
- Tipo: Lazer ao ar livre
- Público-alvo: Famílias, casais, crianças, esportistas e turistas
- Faixa de preço: Baixo; entrada gratuita; estacionamento informado separadamente
- Descrição: Grande parque urbano com áreas verdes, lagos e espaços de convivência.
- Experiências: Caminhadas, piqueniques, passeios de bicicleta e contato com a natureza
- Avaliação: 4.8/5 (297.697 avaliações, conforme o CSV)
- Tags: parque, natureza, caminhada, bicicleta, família, lazer, gratuito
- Fonte: Google Maps

Instrução de resposta:
- Recomende opções que correspondam às preferências do visitante.
- Explique brevemente a relação entre a sugestão e o pedido.
- Informe localização e custos somente conforme os dados disponíveis.
- Não invente horários, disponibilidade, preços atualizados ou outras informações ausentes da base.
```
