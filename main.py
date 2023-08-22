from operations import get_motoboys, get_lojas, get_pedidos


def main():
    lojas = get_lojas()
    motoboys = get_motoboys(lojas=lojas)
    pedidos = get_pedidos(lojas=lojas)


if __name__ == "__main__":
    main()