A,B,C = map(int, input().split())
if A != B and A!=C:
    print("A")
elif B !=A and B!=C:
    print("B")
elif C != A and C!=B:
    print("C")
else:
    print("*")
num_1 = 'eu'
num_2 = 'oi'
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1+num_2)