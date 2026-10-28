def quantos_notebooks(tomada1,tomada2,tomada3,tomada4):
    total = (tomada1+tomada2+tomada3+tomada4)-3
    return total

soquete1,soquete2,soquete3,soquete4 = map(int,input("").split())
valor = quantos_notebooks(soquete1,soquete2,soquete3,soquete4)
print(valor)