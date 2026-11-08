def erro(mensagem):
      print(mensagem)
      return None

def tratando_erros(numero1,numero2,operacao):
      try:
            n1 = float(numero1)
            n2 = float(numero2)
      except (ValueError,TypeError):
            return erro("Erro: Digite apenas números válidos")
            
      if operacao not in ["+","-","*","/"]:
            return erro("Erro: Operação válida! Escolha apenas +,-,*,/ ")
      
      if operacao == "/" and n2 == 0:
            return erro("Erro: Não é possível dividir um número por zero")
            
      return n1,n2
      

        
def calculadora(numero1,numero2,operacao):
    if operacao == "+":
        return numero1+numero2
    elif operacao == "-":
            return numero1-numero2
    elif operacao == "*":
            return numero1*numero2
    elif operacao == "/":
            return  numero1/numero2
    
# Pede os inputs necessários
primeiro_numero = input("Digite o primeiro número: ").strip()
operacao = input("Escolha a operação (+, -, *, /): ").strip()
segundo_numero = input("Digite o segundo número: ").strip()

validacao = tratando_erros(primeiro_numero,segundo_numero,operacao)

if validacao:
      n1,n2 = validacao

      resultado =  calculadora(n1,n2,operacao)
      print("O resultado é",resultado)