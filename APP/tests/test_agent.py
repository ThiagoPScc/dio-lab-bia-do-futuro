from ollama import chat
from app.knowledge import consultar_base
from app.prompts import SYSTEM_PROMPT


MODEL = "llama3.1:8b"


# Carrega os dados dos CSVs
contexto = consultar_base()


# Monta o prompt do sistema
system = SYSTEM_PROMPT.format(
    contexto=contexto
)


# Pergunta do usuário
pergunta = "Qual é o horário de funcionamento do Museu do Ipiranga?"


mensagens = [
    {
        "role": "system",
        "content": system
    },
    {
        "role": "user",
        "content": pergunta
    }
]


# Envia para o Ollama
resposta = chat(
    model=MODEL,
    messages=mensagens
)


print("\n=== RESPOSTA DO SSP ===\n")
print(resposta.message.content)