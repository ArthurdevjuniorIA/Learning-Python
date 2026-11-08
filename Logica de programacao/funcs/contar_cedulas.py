def contador_cedulas(valor):
    notas_100 = 0
    notas_50 = 0
    notas_20 = 0
    notas_10 = 0
    notas_5 = 0
    notas_2 = 0
    
    valor_bool = valor % 2 == 0
    if not valor_bool:
        print("Erro: O valor deve ser múltiplo de 2.")
        return None
        
    while valor > 0:
        if valor >= 100:       # Mudamos para >= para ficar mais legível
            notas_100 += 1
            valor -= 100       # Subtrai apenas 100 do valor total
        elif valor >= 50:
            notas_50 += 1
            valor -= 50        # Subtrai apenas 50
        elif valor >= 20:
            notas_20 += 1
            valor -= 20
        elif valor >= 10: 
            notas_10 += 1
            valor -= 10
        elif valor >= 5:
            notas_5 += 1
            valor -= 5
        elif valor >= 2:
            notas_2 += 1
            valor -= 2
    
    return notas_100, notas_50, notas_20, notas_10, notas_5, notas_2

valor_entregue = int(input("Digite o valor a ser entregue: "))
notas = contador_cedulas(valor_entregue)

if notas: # Só printa se não retornou None
    print("Células entregues: ")
    print(f"100: {notas[0]}\n50: {notas[1]}\n20: {notas[2]}\n10: {notas[3]}\n5: {notas[4]}\n2: {notas[5]}")
