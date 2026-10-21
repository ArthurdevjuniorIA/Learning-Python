quantas_cartas_sem_repeticao = []
quantas_cartas_total = [ ]
print("===== INVENTÁRIO DE CARTAS =====")
while True:
    identificacao_carta = int(input("Digite a identificação da carta (0 para encerrar): "))
    if identificacao_carta == 0:
        print(" ===== RELATÓRIO DO INVENTÁRIO =====")
        for i in range(len(quantas_cartas_sem_repeticao)):
                for n in range(len(quantas_cartas_total)):
                    conta = quantas_cartas_total.count(quantas_cartas_sem_repeticao[i])
                print(f"Carta {quantas_cartas_sem_repeticao[i]}: {conta}")
        break
    if identificacao_carta not in quantas_cartas_total:
        quantas_cartas_sem_repeticao.append(identificacao_carta)
    quantas_cartas_total.append(identificacao_carta)
    
    