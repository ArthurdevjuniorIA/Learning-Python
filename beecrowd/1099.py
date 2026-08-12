N = int(input())

for i in range(N):
    linha = input().split() # lê "4 5" e separa em ["4", "5"]
    valor = int(linha[0]) # pega o "4" e vira inteiro
    valor2 = int(linha[1])  # pega o "5" e vira inteiro

    inicio = min(valor, valor2) # Garante que inicio sempre seja o menor (min) e fim o maior(max), independente da ordem que o usuário digitou
    fim = max(valor, valor2)
    impares = 0  # zera a cada caso de teste

    for j in range(inicio +1 , fim):
        if j % 2 != 0:
         impares += j  # j para não conflitar com o i de cima 

    
    print(impares)