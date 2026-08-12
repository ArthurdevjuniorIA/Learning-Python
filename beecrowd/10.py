salario = float(input("Digite o seu salário:"))

if salario <= 2000.00:
    print("Isento")
elif salario >= 2000.01 and salario <= 3000.00:
    imposto = (salario - 2000) * 0.08
    print(imposto)
elif salario >= 3000.01 and salario <= 4500.00:
    imposto1 = 1000 * 0.08
    imposto2 = (salario - 3000) * 0.18
    print(imposto1 + imposto2)
else:
     imposto1 = 1000 * 0.08
     imposto2 = 2000 * 0.18
     print(imposto1 + imposto2)