N = int(input())
resultado = 0
resultado2 = 0
resultado3 = 0
rfinal = 0
for i in range(N):
    linha = input().split() # lê "4 5" e separa em ["4", "5"]
    valor = float(linha[0]) # pega o "4" e vira float
    valor2 = float(linha[1])  # pega o "5" e vira float
    valor3 = float(linha[2]) 

    resultado = valor * 2
    resultado2 = valor2 * 3
    resultado3 = valor3 * 5

    rfinal = (resultado + resultado2 + resultado3) / 10

    print(f"{rfinal:.1f}")