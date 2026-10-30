from random import randint as aleatorio
possiveis = ["Pedra","Papel","Tesoura"]
Pedra = {"Pedra":1, "Papel":2,"Tesoura":0}
Papel = {"Papel":1, "Pedra":0,"Tesoura":1}
Tesoura = {"Tesoura":1, "Papel":0,"Pedra":2}
opcao_computador = possiveis[aleatorio(0,2)]
def verificacao(usuario,computador):
    if usuario == "Pedra":
        dict = Pedra
    elif usuario == "Tesoura":
        dict = Tesoura
    else:
        dict = Papel

    valor_computador = dict[computador]
    valor_usuario = dict[usuario]
    if valor_usuario>valor_computador:
        print("Você venceu!")
    elif valor_usuario == valor_computador:
        print("Empate")
    else:
        print("Você perdeu!")

def comparativo(usuario,computador):
    if usuario == possiveis[0]:
       verificacao(Pedra,computador)
    elif usuario == possiveis[1]:
        verificacao(Papel,computador)
    else:
        verificacao(Tesoura,computador)

opcoes = input("Escolha entre as opções de Papel,Tesoura e Papel: ").strip().title()
if opcoes not in possiveis:
    raise IndexError(print("A opção digitada não está entre as disponíveis"))
else:
    verificacao(opcoes,opcao_computador)
    print("O computador escolheu:",opcao_computador)