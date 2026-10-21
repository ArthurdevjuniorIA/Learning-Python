while True:
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite sua idade: "))
    atendimento_prioritario = [ ]
    atendimento_normal = [ ]
    if idade>=60:
        atendimento_prioritario.append(idade)
    else:
        atendimento_normal.append(idade)
    for prioritario in atendimento_prioritario:
        print(atendimento_prioritario[0])
        if atendimento_prioritario == [ ]:
            for normal in atendimento_normal:
                print(atendimento_normal[0])