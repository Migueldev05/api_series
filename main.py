from fastapi import FastAPI
from typing import Optional
app = FastAPI()
@app.get("/")
def read_root():
    return {"mensagem":"Olá, mundo!"}

@app.get("/itens/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# Crie uma rota que retorne a soma de dois número passados por caminho (path de url)

# Extra: melhore a tipagem do código usando tipos do módulo typing onde for necessário

@app.get("/soma/{a}/{b}")
def soma(a: int, b: int):
    return {"Resultado": a + b}