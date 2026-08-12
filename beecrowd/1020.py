idade =  int(input())

ano = idade // 365
resto = idade % 365

meses = resto // 30
dias = resto % 30

print(f"{ano:.0f} ano(s)")
print(f"{meses:.0f} mes(es)")
print(f"{dias:.0f} dia(s)")
