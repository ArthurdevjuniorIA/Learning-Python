lista = []

while True:
    nome = input("Nome do participante (ou 'fim' para encerrar):")

    if nome.strip().lower() == "fim":
        break
    else:
        if nome not in lista:
            lista.append(nome)
            print("Participante cadastrado com sucesso.")
        else:
            print("Participante já cadastrado.")
print("")
print("=== LISTA DE PRESENÇA ===")
for nome in lista:
    print(nome)