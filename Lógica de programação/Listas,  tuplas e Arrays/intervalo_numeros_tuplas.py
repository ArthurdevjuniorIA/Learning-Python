de_0_a_20 = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
extenso = ["zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte"]
numero_desejado = int(input("Digite um número de 0 a 20: "))
if numero_desejado not in de_0_a_20:
    print("O número desejado não está entre o intervalo de 0 e 20")
else:
    for desejo, index in enumerate(de_0_a_20):
        if numero_desejado == desejo:
            print(f"O número escolhido por voce foi o {extenso[index]}")