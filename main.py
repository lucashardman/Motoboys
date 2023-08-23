from operations import get_motoboys, get_lojas, get_pedidos, atribuir_pedidos, pesquisa


def main():

    lojas = get_lojas()
    motoboys = get_motoboys(lojas=lojas)
    pedidos = get_pedidos(lojas=lojas)
    motoboys = atribuir_pedidos(pedidos=pedidos, motoboys=motoboys)

    pesquisa(motoboys=motoboys)


if __name__ == "__main__":
    main()