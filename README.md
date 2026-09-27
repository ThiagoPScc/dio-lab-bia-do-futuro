# SSP - Simplificando São Paulo | Guia turistico de IA para conhecer SP

## Contexto

Em 2025 São Paulo bateu record em turistas na cidade, com isso existe a oportunidade de criar ferramentas que possam auxiliar essas pessoas em conhecer São Paulo. Como a cidade é a maior da america latina, um guia simples muitas vezes não atende nossas necessidades, sendo assim criei esse assistente de IA focado em guiar pessoa pela cidade de forma mais interativa.

---

### 1. Documentação do Agente

# O que o agente faz?
> O agente tenta entender as necessidades e vontades do usuário poder recomendar locais com base nos requisitos oferecidos pelo usuário.
# Persona e Tom de Voz
> Ele tenta se comunicar de forma amigavel, informal e paciente, sempre tentando entender o usuário e oferencendo recomendações como um amigo.
# Arquitetura e Segurança 
> estão no arquivo de documentação em `docs`

📄 **documentação:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

Utilize os **dados mockados** disponíveis na pasta [`data/`](./data/) para alimentar seu agente:

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `pontosTuristicos.csv` | CSV | principais cartões postais de SP |
| `restaurantes.csv` | CSV | Restaurantes, bares, food trucks. Locais onde é possivel comer algo durante os passeios|
| `entreterimento.csv` | CSV | Locais de entreterimento como cinemas, parques e cultura |


### 3. Prompts do Agente

>Os promps estão no arquivo de `prompts` em `docs`

📄 **Prompts:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Aqui está a aplicação em sua forma MVP

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

Descreva como você avalia a qualidade do seu agente:

**Métricas Usadas:**
- Precisão/assertividade das respostas
- Taxa de respostas seguras (sem alucinações)
- Coerência com as solucitações do cliente
- Detalhamento das respostas e coerencia com os dados apresentados

📄 **Metricas:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Aqui está um breve vídeo explicando o agente.

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Ferramentas Sugeridas

Todas as ferramentas abaixo possuem versões gratuitas:

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | [Ollama](https://ollama.ai/) |
| **Desenvolvimento** |[Google Colab](https://colab.research.google.com/) |
| **Orquestração** | FastAPI |
| **Diagramas** | [Mermaid](https://mermaid.js.org/ |

---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico_atendimento.csv     # Histórico de atendimentos (CSV)
│   ├── perfil_investidor.json        # Perfil do cliente (JSON)
│   ├── produtos_financeiros.json     # Produtos disponíveis (JSON)
│   └── transacoes.csv                # Histórico de transações (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # (exemplo de estrutura)
│
├── 📁 assets/                        # Imagens e diagramas
│   └── ...
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```

---
