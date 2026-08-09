nome_funcionario = [ ]
producao_de_todos = [ ]
com_maiores_producao = [ ]
produzido_por_todos = [ ]
menor_que_media =[ ]
nada_produzido = [ ]
dias_semana = ["SEGUNDA-FEIRA","TERÇA-FEIRA","QUARTA-FEIRA","QUINTA-FEIRA","SEXTA-FEIRA"]
soma_producao = 0
maior_producao = 0
maior_producao_do_dia = 0
soma_da_producao_cada = 0
while True:
    nome_do_funcionario = input("Nome do funcionário: ")

    if nome_do_funcionario == "fim":
        print("==============================\nRELATÓRIO GERAL DA SEMANA\n==============================")

        for some in producao_de_todos:
            soma_producao = some+soma_producao
        media_producao = soma_producao/len(nome_funcionario)
        print(f"Total de peças montadas: {soma_producao}")
        print(f"Média de produção por funcionário: {media_producao:.0f}")
        print(f"Funcionário(s) com maior produção semanal: ")

        for mais in com_maiores_producao:
            print(f"-{mais}")

        for index,somando in enumerate(produzido_por_todos):
            soma_da_producao_cada = sum(somando)
            if media_producao>soma_da_producao_cada:
                menor_que_media.append(nome_funcionario[index])
        print("Funcionário(s) abaixo da média semanal: ")

        
        for menor in menor_que_media:
            print(f"-{menor}")
        for index,dias in enumerate(dias_semana):
            print(f"=============================={dias}==========================")
            soma_total = 0
            for i, valor in enumerate(producao_de_todos[index::5]):
                soma_total += valor
                if valor>maior_producao_do_dia:
                    maior_producao_do_dia = valor
                    nome_do_maior_produtor_dia = nome_funcionario[i]
                if valor == 0:
                    nada_produzido.append(nome_funcionario[i])
            media_do_dia = soma_total/len(nome_funcionario)
            print(f"Total produzido:{soma_total}")
            print(f"Média de produção: {media_do_dia}")
            print(f"Maior produtor: {nome_do_maior_produtor_dia}")
            maior_producao_do_dia = 0
            for nada in nada_produzido:
                print(f"Sem produção: {nada}")
            nada_produzido.clear()

        break
        
    producao = list(map(int,input("Produção (Seg Ter Qua Qui Sex): ").split()))
    produzido_por_todos.append(producao)
    for produto in producao:
        producao_de_todos.append(produto)
    if nome_do_funcionario not in nome_funcionario:
        nome_funcionario.append(nome_do_funcionario)
        if sum(producao)>maior_producao:
           maior_producao = sum(producao)
           com_maiores_producao.clear()
           com_maiores_producao.append(nome_do_funcionario)
        elif sum(producao) == maior_producao:
            com_maiores_producao.append(nome_do_funcionario)
    else:
        nome_funcionario.remove(nome_funcionario)