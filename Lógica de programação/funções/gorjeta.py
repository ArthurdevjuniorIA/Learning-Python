def calculo_gorjeta(valor_conta,porcentagem_gorjeta):
    gorjeta = (valor_conta*porcentagem_gorjeta)/100
    return gorjeta
def total_valor(total_gorjeta):
    return valor_total + total_gorjeta
try:
    valor_total = float(input("Digite o valor da conta: "))
    porcentagem_da_gorjeta = float(input("Digite a porcentagem de gorjeta: "))
except ValueError:
    print("Você digitou outro tipo de texto")
except TypeError:
    print("Você digitou dois números de tipos diferentes")

gorjeta = calculo_gorjeta(valor_total,porcentagem_da_gorjeta)
todo_valor = total_valor(gorjeta)
print("O valor da gorjeta é ",gorjeta)
print("O valor total da conta é: R$",todo_valor)