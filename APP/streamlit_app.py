import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000/chat"


st.set_page_config(
    page_title="SSP - Simplificando São Paulo",
    page_icon="🏙️"
)


st.title("🏙️ SSP — Simplificando São Paulo")
st.write("Seu assistente para descobrir lugares e experiências em São Paulo.")



if "mensagens" not in st.session_state:
    st.session_state.mensagens = []



for mensagem in st.session_state.mensagens:

    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])



pergunta = st.chat_input("O que você gostaria de conhecer em São Paulo?")


if pergunta:

  
    with st.chat_message("user"):
        st.write(pergunta)

    st.session_state.mensagens.append({
        "role": "user",
        "content": pergunta
    })


    
    try:

        resposta = requests.post(
            API_URL,
            json={
                "pergunta": pergunta
            }
        )


        if resposta.status_code == 200:

            dados = resposta.json()
            texto_resposta = dados["resposta"]

        else:

            texto_resposta = (
                f"Erro na API. Código: {resposta.status_code}"
            )


    except requests.exceptions.ConnectionError:

        texto_resposta = (
            "Não consegui conectar ao servidor FastAPI. "
            "Verifique se o servidor está rodando."
        )


    with st.chat_message("assistant"):
        st.write(texto_resposta)


    st.session_state.mensagens.append({
        "role": "assistant",
        "content": texto_resposta
    })