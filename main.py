from fastapi import FastAPI
from datetime import datetime
import pandas as pd

app = FastAPI()


def fibonacci(n: int):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    serie = [0, 1]
    for i in range(2, n):
        serie.append(serie[i - 1] + serie[i - 2])
    return serie


@app.get("/")
def home():
    return {"mensaje": "API de Fibonacci funcionando correctamente."}


@app.get("/fibonacci/{n}")
def generar_fibonacci(n: int):
    serie = fibonacci(n)
    fecha = datetime.now()

    df = pd.DataFrame({
        "fecha": [fecha] * len(serie),
        "posicion": list(range(len(serie))),
        "valor": serie
    })

    df.to_csv("logs.txt", mode="a", index=False, header=False)

    return {
        "cantidad": n,
        "serie": serie
    }