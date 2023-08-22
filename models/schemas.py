from pydantic import BaseModel


class Loja(BaseModel):
    nome: str
    comissao: float


class Pedido(BaseModel):
    nome: str
    preco: float
    loja: Loja


class Motoboy(BaseModel):
    nome: str
    exclusividade: list[Loja]
    precoFixo: float
    pedidos: list[Pedido]
