from models import schemas
import itertools


def atribuir_pedidos(
        pedidos: list[schemas.Pedido],
        motoboys: list[schemas.Motoboy]
    ) -> list[schemas.Motoboy]:

    motoboys = sorted(
        motoboys, 
        key=lambda motoboy: motoboy.exclusividade is not None, 
        reverse=True
    )

    iter_motoboys = itertools.cycle(motoboys)

    for pedido in pedidos:

        motoboy = next(iter_motoboys)
        loja_exclusiva = False

        if motoboy.exclusividade == pedido.loja:
            motoboy.pedidos.append(pedido)
            loja_exclusiva = True
        if not loja_exclusiva and not motoboy.exclusividade:
            motoboy.pedidos.append(pedido) 

    return motoboys


def get_lojas() -> list[schemas.Loja]:
    
    return [
        schemas.Loja(
            nome="Loja1",
            comissao=0.05
        ),
        schemas.Loja(
            nome="Loja2",
            comissao=0.05
        ),
        schemas.Loja(
            nome="Loja3",
            comissao=0.15
        )
    ]


def get_motoboys(lojas: list[schemas.Loja]) -> list[schemas.Motoboy]:

    return [
        schemas.Motoboy(
            nome="Moto1",
            precoFixo=2.0,
            pedidos=[]
        ),
        schemas.Motoboy(
            nome="Moto2",
            precoFixo=2.0,
            pedidos=[]
        ),
        schemas.Motoboy(
            nome="Moto3",
            precoFixo=2.0,
            pedidos=[]
        ),
        schemas.Motoboy(
            nome="Moto4",
            exclusividade=[loja for loja in lojas if loja.nome == "Loja1"][0],
            precoFixo=2.0,
            pedidos=[]
        ),
        schemas.Motoboy(
            nome="Moto5",
            precoFixo=3.0,
            pedidos=[]
        )
    ]


def get_pedidos(lojas: list[schemas.Loja]) -> list[schemas.Pedido]:

    return [
        schemas.Pedido(
            nome="Pedido1",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja1"][0]
        ),
        schemas.Pedido(
            nome="Pedido2",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja1"][0]
        ),
        schemas.Pedido(
            nome="Pedido3",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja1"][0]
        ),
        schemas.Pedido(
            nome="Pedido4",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja2"][0]
        ),
        schemas.Pedido(
            nome="Pedido5",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja2"][0]
        ),
        schemas.Pedido(
            nome="Pedido6",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja2"][0]
        ),
        schemas.Pedido(
            nome="Pedido7",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja2"][0]
        ),
        schemas.Pedido(
            nome="Pedido8",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja3"][0]
        ),
        schemas.Pedido(
            nome="Pedido9",
            preco=50.00,
            loja=[loja for loja in lojas if loja.nome == "Loja3"][0]
        ),
        schemas.Pedido(
            nome="Pedido10",
            preco=100.00,
            loja=[loja for loja in lojas if loja.nome == "Loja3"][0]
        )
    ]