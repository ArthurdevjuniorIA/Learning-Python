while True:
    Jogos = ["FIFA 17", "FIFA 13", "FIFA 14", "FIFA 15", "PES 2013", "PES 2018", "PES 2019", "PES 2015"]
    print(Jogos)
    jogo_pedido = input("Insira qual jogo de futebol deveria ser adicionado a lista: ")
    jogos_padronizados = [jogo_pedido.strip().lower() for jogo_pedido in Jogos]
    if jogo_pedido in jogos_padronizados:
        print("Esse jogo já está na lista")
    else:
     Jogos.insert(0,jogo_pedido)
     print(Jogos)
     break
jogo_removido = Jogos.pop(5)
print(f"O {jogo_removido} esse jogo foi removido porque eu quis")
print(f"A nova lista agora é essa {Jogos}")