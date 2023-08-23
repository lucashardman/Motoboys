from models.schemas import Motoboy, Pedido, Loja
from typing import Iterable
import itertools


def _resultado_pesquisa(motoboys: list[Motoboy]) -> None:

    if len(motoboys) == 0:
        print("Motoboy não cadastrado.")
        return
    
    for motoboy in motoboys:
        print(f"Nome: {motoboy.nome}")
        preco_final: float = motoboy.precoFixo
        lojas: list[str] = []
        for pedido in motoboy.pedidos:
            preco_final += pedido.preco * pedido.loja.comissao
            lojas.append(pedido.loja.nome)
        print(f"Total de pedidos: {len(motoboy.pedidos)}")
        print(f"Lojas dos pedidos: {', '.join(lojas)}")
        print(f"Recebimento total: R${'{:.2f}'.format(preco_final)}")
        

def pesquisa(motoboys: list[Motoboy]) -> None:

    pesquisa: str = input("Digite o nome do motoboy: ")
    if pesquisa == "":
        _resultado_pesquisa(motoboys=motoboys)
    elif pesquisa not in [motoboy.nome for motoboy in motoboys]:
        _resultado_pesquisa(motoboys=[])
    else:
        motoboy = [motoboy for motoboy in motoboys if motoboy.nome == pesquisa]
        _resultado_pesquisa(motoboys=motoboy)


def atribuir_pedidos(
        pedidos: list[Pedido],
        motoboys: list[Motoboy]
    ) -> list[Motoboy]:

    motoboys = sorted(
        motoboys, 
        key=lambda motoboy: motoboy.exclusividade is not None, 
        reverse=True
    )

    iter_motoboys: Iterable[Motoboy] = itertools.cycle(motoboys)

    for pedido in pedidos:
        atribuido: bool = False
        while atribuido is not True:
            motoboy = next(iter_motoboys)
            if motoboy.exclusividade == pedido.loja:
                motoboy.pedidos.append(pedido)
                atribuido = True
            elif not motoboy.exclusividade:
                motoboy.pedidos.append(pedido) 
                atribuido = True

    return motoboys


def get_lojas() -> list[Loja]:

    return [
        Loja(
            nome="Loja1",
            comissao=0.05
        ),
        Loja(
            nome="Loja2",
            comissao=0.05
        ),
        Loja(
            nome="Loja3",
            comissao=0.15
        )
    ]


def get_motoboys(lojas: list[Loja]) -> list[Motoboy]:

    return [
        Motoboy(
            nome="Moto1",
            precoFixo=2.0,
            pedidos=[]
        ),
        Motoboy(
            nome="Moto2",
            precoFixo=2.0,
            pedidos=[]
        ),
        Motoboy(
            nome="Moto3",
            precoFixo=2.0,
            pedidos=[]
        ),
        Motoboy(
            nome="Moto4",
            exclusividade=[loja for loja in lojas if loja.nome == "Loja1"][0],
            precoFixo=2.0,
            pedidos=[]
        ),
        Motoboy(
            nome="Moto5",
            precoFixo=3.0,
            pedidos=[]
        )
    ]


def get_pedidos(lojas: list[Loja]) -> list[Pedido]:

    return [
        Pedido(
            nome="Pedido1",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja1"][0]
        ),
        Pedido(
            nome="Pedido2",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja1"][0]
        ),
        Pedido(
            nome="Pedido3",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja1"][0]
        ),
        Pedido(
            nome="Pedido4",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja2"][0]
        ),
        Pedido(
            nome="Pedido5",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja2"][0]
        ),
        Pedido(
            nome="Pedido6",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja2"][0]
        ),
        Pedido(
            nome="Pedido7",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja2"][0]
        ),
        Pedido(
            nome="Pedido8",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja3"][0]
        ),
        Pedido(
            nome="Pedido9",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja3"][0]
        ),
        Pedido(
            nome="Pedido10",
            preco=100.00,
            loja=[loja for loja in lojas if loja.nome == "Loja3"][0]
        )
    ]