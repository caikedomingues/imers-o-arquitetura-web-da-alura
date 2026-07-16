import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Cria a instância da aplicação FastAPI usando o nome app em minúsculo
app = FastAPI()

# Define o caminho absoluto da pasta de imagens para o servidor encontrar a pasta
# independente de onde o script for executado.
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Configura os arquivos estáticos: monta a pasta PASTA_IMAGENS na rota "/imgs"
app.mount("/imgs", StaticFiles(directory=PASTA_IMAGENS), name="imgs")

# Lista de figurinhas de exemplo conforme especificado
figurinhas = [
    {
        "id": 1,
        "nome": "Alan Turing",
        "categoria": "IA",
        "imagem_url": "/imgs/01-alan-turing.jpg"
    },
    {
        "id": 2,
        "nome": "John McCarthy",
        "categoria": "IA",
        "imagem_url": "/imgs/02-john-mccarthy.jpg"
    }
]

# Rota para listar todas as figurinhas cadastradas (único endpoint)
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna a lista de figurinhas
    return figurinhas
