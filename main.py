from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from datetime import date, time
from enum import Enum

app = FastAPI()


# Estado permitido
class EstadoReserva(str, Enum):
    activa = "activa"
    cancelada = "cancelada"
    finalizada = "finalizada"


# Modelo de datos
class Reserva(BaseModel):
    id_reserva: int
    id_sala: int
    id_usuario: int
    fecha: date
    hora_inicio: time
    hora_fin: time
    personas: int = Field(gt=0, description="Debe ser mayor que 0")
    estado: EstadoReserva


# Base de datos en memoria del servidor
reservas_db: List[Reserva] = []


@app.get("/")
def home():
    return {"mensaje": "Microservicio de reservas funcionando."}

@app.post("/reservas", response_model=Reserva)
def crear_reserva(reserva: Reserva):

    # Validar que no exista mismo ID
    for r in reservas_db:
        if r.id_reserva == reserva.id_reserva:
            raise HTTPException(status_code=400, detail="ID de reserva ya existe")

    reservas_db.append(reserva)
    return reserva

@app.get("/reservas", response_model=List[Reserva])
def obtener_reservas():
    return reservas_db