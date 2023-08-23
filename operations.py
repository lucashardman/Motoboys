from models import schemas
import itertools


def _resultado_pesquisa(motoboys: list[schemas.Motoboy]) -> None:

    if len(motoboys) == 0:
        print("Motoboy não cadastrado.")
        return
    
    for motoboy in motoboys:
        print(f"Nome: {motoboy.nome}")
        preco_final = motoboy.precoFixo
        lojas = []
        for pedido in motoboy.pedidos:
            preco_final += pedido.preco * pedido.loja.comissao
            lojas.append(pedido.loja.nome)
        print(f"Total de pedidos: {len(motoboy.pedidos)}")
        print(f"Lojas dos pedidos: {', '.join(lojas)}")
        print(f"Recebimento total: R${'{:.2f}'.format(preco_final)}")
        

def pesquisa(motoboys: list[schemas.Motoboy]) -> None:

    pesquisa = input("Digite o nome do motoboy: ")
    if pesquisa == "":
        _resultado_pesquisa(motoboys=motoboys)
    elif pesquisa not in [motoboy.nome for motoboy in motoboys]:
        _resultado_pesquisa(motoboys=[])
    else:
        motoboy = [motoboy for motoboy in motoboys if motoboy.nome == pesquisa]
        _resultado_pesquisa(motoboys=motoboy)


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
        atribuido = False
        while atribuido is not True:
            motoboy = next(iter_motoboys)
            if motoboy.exclusividade == pedido.loja:
                motoboy.pedidos.append(pedido)
                atribuido = True
            elif not motoboy.exclusividade:
                motoboy.pedidos.append(pedido) 
                atribuido = True

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