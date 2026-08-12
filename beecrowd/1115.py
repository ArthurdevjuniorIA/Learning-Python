linha = input().split()
X = int(linha[0])
Y = int(linha[1])

while X != 0 and Y != 0:

    if X > 0 and Y < 0:
        print("quarto")
   
    elif X < 0 and Y < 0:
        print("terceiro")

    elif X < 0 and Y > 0:
        print("segundo")

    else:
        print("primeiro")
        
    linha = input().split()
    X = int(linha[0])
    Y = int(linha[1])