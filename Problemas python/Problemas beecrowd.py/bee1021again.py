notas = [10000,5000,2000,1000,500,200]
moedas = [100,50,25,10,5,1]
quantidade = [ ]
number = float(input())
number = round(number*100)
for nota in notas:
    divisivel = number//nota
    number = number- nota*divisivel
    quantidade.append(divisivel)
for moeda in moedas:
    divisivel = number//moeda
    number = number- moeda*divisivel
    quantidade.append(divisivel)
print("NOTAS:")
print(f"{quantidade[0]} nota(s) de R$ 100.00")
print(f"{quantidade[1]} nota(s) de R$ 50.00")
print(f"{quantidade[2]} nota(s) de R$ 20.00")
print(f"{quantidade[3]} nota(s) de R$ 10.00")
print(f"{quantidade[4]} nota(s) de R$ 5.00")
print(f"{quantidade[5]} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{quantidade[6]} moeda(s) de R$ 1.00")
print(f"{quantidade[7]} moeda(s) de R$ 0.50")
print(f"{quantidade[8]} moeda(s) de R$ 0.25")
print(f"{quantidade[9]} moeda(s) de R$ 0.10")
print(f"{quantidade[10]} moeda(s) de R$ 0.05")
print(f"{quantidade[11]} moeda(s) de R$ 0.01")