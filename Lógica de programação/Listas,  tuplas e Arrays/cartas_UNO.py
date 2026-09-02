quantas_cartas = []
print("===== INVENTÁRIO DE CARTAS =====")
while True:
    identificacao_carta = int(input("Digite a identificação da carta (0 para encerrar): "))
    if identificacao_carta == 0:
        break
    quantas_cartas.append(identificacao_carta)
    quantas_cartas_set = set(quantas_cartas)
    for i in range(quantas_cartas_set):
        