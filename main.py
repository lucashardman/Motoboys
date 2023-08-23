from operations import get_motoboys, get_lojas, get_pedidos, atribuir_pedidos, pesquisa
from models.schemas import Motoboy, Pedido, Loja

def main():

    lojas: list[Loja] = get_lojas()
    motoboys: list[Motoboy] = get_motoboys(lojas=lojas)
    pedidos: list[Pedido] = get_pedidos(lojas=lojas)
    
    motoboys = atribuir_pedidos(pedidos=pedidos, motoboys=motoboys)

    pesquisa(motoboys=motoboys)
    

if __name__ == "__main__":
    main()