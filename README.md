# Motoboys

Este é um script simples que calcula a ordem que os motoboys irão buscar os pedidos nas lojas cadastradas.

O script pede um input com o nome do motoboy e responde: quem é o motoboy, quantos pedidos ele tem, quais são as lojas dos pedidos e qual é o valor total que ele irá receber como pagamento.

Para adicionar ou remover motoboys, lojas e pedidos, basta adicionar um objeto referente na lista que é retornada nas respectivas funções: get_motoboys(), get_lojas() e get_pedidos(), localizadas no arquivo operations.py.

## Pré-requisitos

Antes de executar o aplicativo, certifique-se de ter o seguinte instalado em sua máquina:

- Python 3.9 ou superior
- pipenv (gerenciador de pacotes Python)


## Configuração do Ambiente

1. Clone o repositório do projeto para o seu computador:

```bash
git clone https://github.com/lucashardman/Motoboys.git
```

2. Acesse o diretório do projeto:

```bash
cd <caminho_do_diretório>
```

3. Instalação das dependências e ativação do ambiente virtual:

```bash
pipenv install
pipenv shell
```

## Executando o Aplicativo

1. Executar o script:

```bash
python main.py
```

2. Digitar o nome do motoboy:

```bash
Digite o nome do motoboy: <digitar o nome do motoboy>
```

3. Resposta do script:

- Caso passar um nome válido: retorna o motoboy referente ao nome.

```bash
Nome: Moto1
Total de pedidos: 3
Lojas dos pedidos: Loja1, Loja2, Loja3
Recebimento total: R$22.00
```

- Caso passar um nome inválido: retona mensagem de que o motoboy não está cadastrado.

```bash
Motoboy não cadastrado.
```

- Caso não passar nenhum valor: retorna todos os motoboys.

```bash
Nome: Moto4
Total de pedidos: 1
Lojas dos pedidos: Loja1
Recebimento total: R$4.50
Nome: Moto1
Total de pedidos: 3
Lojas dos pedidos: Loja1, Loja2, Loja3
Recebimento total: R$22.00
Nome: Moto2
Total de pedidos: 2
Lojas dos pedidos: Loja1, Loja2
Recebimento total: R$7.00
Nome: Moto3
Total de pedidos: 2
Lojas dos pedidos: Loja2, Loja3
Recebimento total: R$12.00
Nome: Moto5
Total de pedidos: 2
Lojas dos pedidos: Loja2, Loja3
Recebimento total: R$13.00
```