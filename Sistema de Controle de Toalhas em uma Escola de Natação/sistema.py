codigo = []
nome = []
quantidade = []

while True:
    print("=================================")
    print(" NADO LIVRE")
    print("=================================")
    print(" ")
    print("1 - Cadastrar nadador")
    print("2 - Consultar nadadores")
    print("3 - Registrar retirada de toalhas")
    print("4 - Consultar toalhas em uso")
    print("0 - Sair")
    print("")
    opçao = input("Escolha uma opção:")


    if opçao == 1:
        print("===== CADASTRO DE NADADOR =====")
        print("")
        codigo = input("Código:")
        nome = input("Nome:")

        if codigo.isdigit() and nome.isalnum():
=======
lista = []

codigo, nome = map(input().split())

codigo = int(codigo)

lista.append(list(codigo, nome))

lista = [
    [100, "Nome"],
    [100, "Nome"]
]

