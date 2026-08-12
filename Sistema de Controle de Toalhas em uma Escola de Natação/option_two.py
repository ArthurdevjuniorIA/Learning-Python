# 2. Consultar nadadores

print("\n========= NADADORES =========\n")

if len(codigos) > 0:
    for i in range(len(codigos)):
        print(f"{codigos[i]} - {nomes[i]}")
else:
    print("Nenhum nadador cadastrado.")