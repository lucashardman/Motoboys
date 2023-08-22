from pydantic import BaseModel
from typing import Optional

class Motoboy(BaseModel):
    nome: str
    exclusividade: list[str]
    precoFixo: float


class Loja(BaseModel):
    nome: str
    comissao: float


class Pedido(BaseModel):
    nome: str
    preco: float
    loja: Loja
    motoboy: Motoboy