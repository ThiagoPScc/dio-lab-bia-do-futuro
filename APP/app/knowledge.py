import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


ARQUIVOS = {
    "pontos_turisticos": "pontosTuristicos.csv",
    "restaurantes": "Restaurantes.csv",
    "entretenimento": "Entreterimento.csv"
}


def carregar_base():
    base = {}

    for categoria, arquivo in ARQUIVOS.items():
        caminho = DATA_DIR / arquivo

        base[categoria] = pd.read_csv(
            caminho,
            encoding="utf-8"
        ).fillna("Não informado")

    return base

def consultar_base():
    base = carregar_base()

    contexto = ""

    for categoria, df in base.items():
        contexto += f"\n\n## {categoria.upper()}\n"

        for _, registro in df.iterrows():
            contexto += registro.to_json(
                force_ascii=False
            ) + "\n"

    return contexto

if __name__ == "__main__":
    contexto = consultar_base()

    print(contexto)