lista = []
for i in range(1, 11):
    nome = input(f"Informe o nome do {i}º colocado:")
    lista.append(nome)

while True:
    nome = input("Nome do candidato a desclassificar (ou 'fim' para encerrar):")

    if nome == "fim":
        break
    else:
        if nome in lista:
            lista.remove(nome)
            lista.append("[DESCLASSIFICADO]")
            print("Candidato Desclassificado.")

print("=== CLASSIFICAÇÃO ATUALIZADA ===")
for i, nome in enumerate(lista, start = 1):
    print(f"{i}º lugar: {nome}")