cadastados = [ ]
nao_fim = True
while nao_fim:
    participante = input("Nome do participante (ou 'fim' para encerrar): ")
    if participante not in cadastados:
        cadastados.append(participante)
        print("Participante cadastrado com sucesso.")
    elif participante in cadastados:
        print("Participante já cadastrado.")
    if participante == "fim":
        nao_fim = False
        break
print("=== LISTA DE PRESENÇA ===")
for nome in cadastados:
    print(*cadastados)