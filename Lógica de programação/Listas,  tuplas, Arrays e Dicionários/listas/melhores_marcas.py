melhores_marcas = [ ]
while True:
    marca_obtida = float(input("Marca obtida (0 para encerrar): "))
    if marca_obtida == 0:
        print("===== 10 MELHORES MARCAS =====")
        for i in range(len(melhores_marcas)):
            print(f"{i+1}º {melhores_marcas[0+i]}")
            if i>10:
                break
        break
    else:
        melhores_marcas.append(marca_obtida)
        melhores_marcas.sort(reverse = True)
        print(melhores_marcas)
       