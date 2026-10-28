def idade_ultimo_filho(idade_mae,filho,filho2):
    idade_ultimo = idade_mae-(filho+filho2)
    idades = [filho,filho2,idade_ultimo]
    mais_velho = max(idades)
    return mais_velho
idade_mae = int(input())
idade_filho1 = int(input())
idade_filho2 = int(input())
ultimo_filho = idade_ultimo_filho(idade_mae,idade_filho1,idade_filho2)
print(ultimo_filho)