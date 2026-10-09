'''
conjunto = {

}
def argumentos_dicionarios(*argumento,**dicionario):
    print(f"Enviaram {len(argumento)} para a função")
    print(f"Enviaram {len(dicionario)} para a função")
    conjunto["cada Pessoa"] = dicionario
argumentos_dicionarios("Bomdia","TUTU","MARISA","ALBERTO",nome="Arthur",idade=30, cpf=111111111)
for conju in conjunto:
    print(conju)
'''
nome1 = "Arthur"
altura1 = 1.76
peso1 = 65
nome2 = "Marisa"
altura2 = 1.65
peso2 = 65
nome3 = "Lorenzo"
altura3 = 1.20
peso3 = 30

def calcular_IMC(nome,altura,peso):
    IMC = peso/ (altura **2)
    print(f"O IMC É: {IMC:.2f}")
    if 17<IMC<25:
        return nome + " está no peso ideal"
    elif IMC<17:
        return nome + " está muito magro, necessitas comer"
    else:
        nome + " está precisando perder peso"
calculo = calcular_IMC(nome1,altura1,peso1)
calcular = calcular_IMC(nome2,altura2,peso2)
calculando = calcular_IMC(nome3,altura3,peso3)
print(calculo)
print(calcular)
print(calculando)