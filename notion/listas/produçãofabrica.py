nomes = []
producoes = []
dias = ("seg","ter","qua","qui","sex")
while True:
    nome = input("Nome do funcionário: ")
    if nome == "fim":
        break
    nomes.append(nome)
    producao = list(map(int,input("Produção (Seg Ter Qua Qui Sex): ").split()))
    producoes.append(producao)
print()
print("==============================")
print("RELATÓRIO GERAL DA SEMANA")
print("==============================")

total_funcionario = []

for producao in producoes:
    total = sum(producao)
    total_funcionario.append(total)

total_geral = sum(total_funcionario)
media_funcionario = total_geral/len(nomes)
maior_producao_semanal_funcionario = max(total_funcionario)

print(f"Total de peças montadas: {total_geral}")
print(f"Média de produção por funcionário: {media_funcionario}")

print(nomes)
print(total_funcionario)
print(maior_producao_semanal_funcionario)

print("Funcionário(s) com maior produção semanal:")
for i in range(len(nomes)):
    if total_funcionario[i] == maior_producao_semanal_funcionario:
        print(f" - {nomes[i]}")

for nome, total in zip(nomes,total_funcionario):
    if total == maior_producao_semanal_funcionario:
        print(f" - {nome}")    

maiores_produtores = [nome for nome, total in zip(nomes, total_funcionario) if total == maior_producao_semanal_funcionario]
print(maiores_produtores)

print("Funcionário(s) abaixo da média semanal:")
for nome, total in zip(nomes, total_funcionario):
    if total < media_funcionario:
        print(f" - {nome}")

for i in range(len(dias)):
    print("==============================")
    print(dias[i])
    print("==============================")

    producoes_dia = []
    for producao in producoes:
        producoes_dia.append(producao[i])
    print(producoes_dia)
    total_dia = sum(producoes_dia)
    media_dia = total_dia/len(producoes_dia)
    maior_producao_dia = max(producoes_dia)


    print(f"Total produzido: {total_dia}")
    print(f"Média de produção: {media_dia}")
    print("Maior produtor:")
    for nome, producao_dia in zip(nomes, producoes_dia):
        if producao_dia == maior_producao_dia:
            print(f" - {nome}")