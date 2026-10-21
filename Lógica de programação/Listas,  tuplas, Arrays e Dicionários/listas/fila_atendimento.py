fila_atendimento = [ ]
while True:
    cliente_comando = input("Digite o nome do cliente ou um comando: ")
    if cliente_comando != "atender":
        fila_atendimento.append(cliente_comando)
    else:
        print(f"Próximo cliente: {fila_atendimento[0]}")
        fila_atendimento.pop(0)
    if cliente_comando == "fim":
        fila_atendimento.remove("fim")
        print("=== CLIENTES AGUARDANDO ATENDIMENTO ===")
        for pessoas in fila_atendimento:
            print(pessoas)
        break