from unidecode import unidecode

pergunta = int(input("Quantas variáveis você quer calcular? "))
soma = 0
subtracao = 0
multiplicacao = 1
divisao = 1
potenciacao = 1
radiciacao = 2
for i in range(pergunta):
    numero = float(input("Digite o numero(s): "))
    operacao = input("qual operação você deseja realizar? ")
    operacao_limpa = unidecode(operacao)

    if operacao_limpa == "soma":
        soma = numero+soma
    elif operacao_limpa == "subtracao":
        subtracao = numero-subtracao
    elif operacao_limpa == "multiplicacao":
        multiplicacao = numero*multiplicacao

