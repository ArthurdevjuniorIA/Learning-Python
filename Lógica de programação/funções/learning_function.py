def minha_funcao():
    print("Tô começando em funções papito!")
def verificador_paridade():
    try:
        numero = int(input())
        if numero % 2 == 0:
            print("O número é par!")
        else:
            print("O número é ímpar!")
    except:
        print("não vale!")
    return numero
'''
def estudando_parametros(dia_do_aniversario, dia_de_hoje):
    if dia_do_aniversario == dia_de_hoje:
        print("Parabéns, hoje é seu aniversário")
    else:
        print("Hoje não é seu aniversário")
dia_de_hoje = "0910"
dia_de_hoje = int(dia_de_hoje)
dia_do_aniversario = int(input("Quando é o seu aniversário? ").strip().replace("/",""))
estudando_parametros(dia_do_aniversario,dia_de_hoje)
'''
def funcao_somar(x):
    return x+2
printar = funcao_somar(4)
print(printar)