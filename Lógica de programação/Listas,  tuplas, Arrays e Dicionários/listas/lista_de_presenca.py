lista =[]
while True:
    alunos = input("Digite o nome do participante (ou 'fim' para encerrar): ")
    if alunos != "fim":
        lista.append(alunos)
    elif alunos == "fim":
        break
print("=== LISTA DE PRESENÇA ===")
print(*lista, sep="\n")