# Importa a classe FastAPI do módulo fastapi
from fastapi import FastAPI

# Cria a instância da aplicação FastAPI usando o nome APP em maiúsculo, conforme requisitado
APP = FastAPI()

# Define a rota para o endpoint GET "/"
@APP.get("/")
def hello_world():
    # Retorna o dicionário que será convertido automaticamente para JSON
    return {"Mensagem": "Olá"}
