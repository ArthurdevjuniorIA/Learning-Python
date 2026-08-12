N = int(input())
n = 0
n2 = 0

for i in range(N):
   d = 0
   linha = input().split()
   n = int(linha[0])
   n2 = int(linha[1])

   

   if n2 ==0:
      print("divisao impossivel")
   else: 
    d = n / n2

    print(f"{d:.1f}")


   
