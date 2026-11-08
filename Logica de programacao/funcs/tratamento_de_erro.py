try:
    a = int(input())
    b = float(input())
    division = a / b
except ZeroDivisionError as erro:
    print("Não é possível fazer uma divisão por zero")
except ValueError:
    print("Coloque apenas números")
else:
    print(division)
finally:
    print("Feito!")
