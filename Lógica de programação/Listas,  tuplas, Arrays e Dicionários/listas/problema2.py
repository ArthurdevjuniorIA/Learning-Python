bolas = [ ]
bolas_total = [ ]
while True:
    cor_bolinha = input("Cor da bolinha (ou FIM): ")
    if cor_bolinha == "FIM":
        print("===== INVENTÁRIO =====")
        for cor in bolas:
            print(f"{cor}: {bolas_total}(s) ")
        break
    else:
        if cor_bolinha not in bolas:
            bolas.append(cor_bolinha)
            bolas_total.append(cor_bolinha)
        else:
            bolas_total.append(cor_bolinha)
            bolas_total.count(cor_bolinha)
            continue