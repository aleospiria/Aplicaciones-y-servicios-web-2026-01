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


# Base de datos en memoria
reservas_db: List[Reserva] = []


@app.get("/")
def home():
    return {"mensaje": "Microservicio de reservas funcionando."}