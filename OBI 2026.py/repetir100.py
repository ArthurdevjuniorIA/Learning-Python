tamanho_sequencia = int(input())
number = list(map(int,input().split()))
de_3_em_3 = [number[i::i+3] for i in range(0,len(number),3)]
padrao_100 = 0
for i in range(len(de_3_em_3)):
    for cem in i:
        cem