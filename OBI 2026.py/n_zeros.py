numero = int(input())
binario = list(map(int,input().split()))
limpa = [item.replace(" ", "").replace(",", "") for item in binario]
quantos_100 = 0
for i in range(len(binario)):
    quantidade = limpa.count(100)
print(quantos_100)