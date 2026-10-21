carrinho = [ ]
while True:
    produto = input("Digite qual produto você deseja colocar no seu carrinho: ").lower()
    if produto not in carrinho:
        print(f"{produto} adicionado ao carrinho")
        carrinho.append(produto)
    else:
        carrinho.remove(produto)
        print(f"O {produto} já está no carrinho")