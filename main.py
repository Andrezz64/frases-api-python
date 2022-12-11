from fastapi import FastAPI
from ler import getData
from gravar import WriteData
from pydantic import BaseModel
from pegarTotal import total
import random
app = FastAPI()

@app.get("/api/frases")
async def send():
    totaldeFrases = total()
    print(totaldeFrases)
    numeroDaFrase = random.randint(0,totaldeFrases)
    return getData(numeroDaFrase)

@app.post("/api/cadastrar")
async def cadastro(msg:dict):
    if msg["msg"] == "":
        return "Favor não digitar um valor vazio"
        
    elif msg["msg"] == " ":
        return "Favor não digitar um valor vazio"
    else:
        WriteData(msg["msg"])
        return "Frase cadastrada"