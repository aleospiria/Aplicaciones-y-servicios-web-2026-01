import pandas as pd
from datetime import datetime


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    serie = [0, 1]

    for i in range(2, n):
        serie.append(serie[i - 1] + serie[i - 2])

    return serie


def guardar_log_fibonacci(n):
    serie = fibonacci(n)
    fecha = datetime.now()

    # Creamos un DataFrame
    df = pd.DataFrame({
        "fecha": [fecha] * len(serie),
        "posicion": list(range(len(serie))),
        "valor": serie
    })

    # Guardamos en modo append (como log)
    df.to_csv("datos.txt", mode="a", index=False, header=False)


if __name__ == "__main__":
    guardar_log_fibonacci(100)

    # Leer el archivo con Pandas
    columnas = ["fecha", "posicion", "valor"]
    df_logs = pd.read_csv("Datos.txt", names=columnas)

    print("Contenido del log:")
    print(df_logs)
