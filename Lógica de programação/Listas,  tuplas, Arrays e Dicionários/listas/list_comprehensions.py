# from time import time
# start = time()
# # lista = [n**2 for n in range(1,100000000)]
# # for n in range(1,100000000):
# #     n = n**2
# # end = time()
# # print("O tempo total gasto foi de:", end - start)

nomes = [ "maria", "clara","camila"]
nomes_corrigidos = [nome.title() for nome in nomes]
print(nomes_corrigidos)
# for nome in nomes:
#     nomes_corrigidos.append(nome.title())
# print(*nomes_corrigidos)