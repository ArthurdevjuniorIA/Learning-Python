lista = []

while True:
    nome = input("Digite o nome do cliente ou um comando:")

    if nome == "fim":
        break
    elif nome == "atender":
        #checa automáticamente se a lista está vazia ou não.
        if lista:
            #remove o primeiro elemento da lista.
            cliente = lista.pop(0)
            print(f"Próximo cliente:", cliente)
        else:
            print("Não há clientes aguardando atendimento no momento.")

    else:
        lista.append(nome)

print("=== CLIENTES AGUARDANDO ATENDIMENTO ===")
for i in lista:
    print(i)

    