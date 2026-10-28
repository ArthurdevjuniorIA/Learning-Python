def custo_mudas(quantas_mudas):
    if quantas_mudas<=19:
        total_mudas = (quantas_mudas*4)+8
    else:
        total_mudas = (quantas_mudas*3)+8
    
    return total_mudas

def verificador_custo(numero_de_mudas,orcamento):

    valor_total = custo_mudas(numero_de_mudas)
    print(valor_total)
    if valor_total>orcamento:
        print("NO")
    else:
        print("YES")

pedidos = int(input())
for i in range(pedidos):
    quanto_mudas = int(input())
    orcamento = int(input())
    verificar = verificador_custo(quanto_mudas,orcamento)