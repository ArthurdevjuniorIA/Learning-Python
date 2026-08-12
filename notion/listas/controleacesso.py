lista = []

while True:
    print("===== CONTROLE DE ACESSO =====")
    print("")
    print("1 - Registrar entrada")
    print("2 - Registrar saída")
    print("0 - Encerrar")

    opçao = int(input())

    if opçao == 0:
        break

    elif opçao == 1:
        nome = input("Digite o seu nome:")
        lista.append(nome)
        print("Entrada Registrada.")

    elif opçao == 2:
        if nome in lista:
            nome = input("Digite o seu nome:")
            lista.remove(nome)
            print("Saída registrada.")
        else:
            print("A sua entrada não foi registrada. Funcionário não encontrado.")
    else:
        print("Opção inválida. Tente novamente.")
        
print("")
print("=== FUNCIONÁRIOS PRESENTES ===")
for nome in lista:
    print(nome)