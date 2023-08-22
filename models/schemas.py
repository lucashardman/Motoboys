from pydantic import BaseModel
from typing import Optional


class Loja(BaseModel):
    nome: str
    comissao: float


class Pedido(BaseModel):
    nome: str
    preco: float
    loja: Loja


class Motoboy(BaseModel):
    nome: str
    precoFixo: float
    pedidos: list[Pedido]
    exclusividade: Optional[Loja] = None
