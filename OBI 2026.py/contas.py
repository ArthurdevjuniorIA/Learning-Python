def quantas_contas(valor_disponivel,despesa_acouge,despesa_farmacia,despesa_padaria):
    quantas_contas = 0
    if valor_disponivel>=despesa_acouge:
        valor_disponivel = valor_disponivel - despesa_acouge
        quantas_contas+=1
    if valor_disponivel>=despesa_farmacia:
        valor_disponivel = valor_disponivel-despesa_farmacia
        quantas_contas+=1
    if valor_disponivel>=despesa_padaria:
        valor_disponivel = valor_disponivel-despesa_padaria
        quantas_contas+=1
    return quantas_contas

valor = int(input())
despesa1 = int(input())
despesa2 = int(input())
despesa3 = int(input())
valor_total = quantas_contas(valor,despesa1,despesa2,despesa3)
print(valor_total)