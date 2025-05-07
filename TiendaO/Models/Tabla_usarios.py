import reflex as rx 
from typing import Optional
from sqlmodel import Field

class User(rx.Model, table=True):
    Id: Optional[int] = Field(default=None, primary_key=True)
    Nombre: str
    Email: str
    Contraseña: str
    tipo: str
    #fecha_creacion: int


