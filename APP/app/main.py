from fastapi import FastAPI
from pydantic import BaseModel
from ollama import chat

from app.knowledge import consultar_base
from app.prompts import SYSTEM_PROMPT


MODEL = "llama3.1:8b"


app = FastAPI(
    title="SSP - Simplificando São Paulo",
    description="API do agente turístico SSP",
    version="1.0.0"
)


class Pergunta(BaseModel):
    pergunta: str


@app.get("/")
def inicio():
    return {
        "mensagem": "SSP está funcionando!"
    }


@app.post("/chat")
def conversar(dados: Pergunta):

    contexto = consultar_base()

    system = SYSTEM_PROMPT.format(
        contexto=contexto
    )

    mensagens = [
        {
            "role": "system",
            "content": system
        },
        {
            "role": "user",
            "content": dados.pergunta
        }
    ]

    resposta = chat(
        model=MODEL,
        messages=mensagens
    )

    return {
        "resposta": resposta.message.content
    }