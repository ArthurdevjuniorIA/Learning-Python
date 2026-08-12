N = int(input())
dentro = 0
fora = 0

for i in range(1, N +1 ):
    valor = int(input())

    if valor >= 10 and valor <= 20:
        dentro += 1
    else:
        fora += 1

print(f"{dentro} in")
print(f"{fora} out") 