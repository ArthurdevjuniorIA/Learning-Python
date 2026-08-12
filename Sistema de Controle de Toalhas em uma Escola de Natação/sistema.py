codigos = []
nomes = []
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
           codigos.append(codigo)
           nomes.append(nome)
           print("")
           print("Nadadores cadastrados com sucesso!")
