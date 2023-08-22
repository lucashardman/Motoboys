from operations import get_motoboys, get_lojas, get_pedidos, atribuir_pedidos


def main():

    lojas = get_lojas()
    motoboys = get_motoboys(lojas=lojas)
    pedidos = get_pedidos(lojas=lojas)
    motoboys = atribuir_pedidos(pedidos=pedidos, motoboys=motoboys)

    for motoboy in motoboys:
        print(motoboy)

if __name__ == "__main__":
    
    main()