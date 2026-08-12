op = ""

while op != 0:

 print("===== MENU ======")
 print("1 - Abrir cadastro")
 print("2 - Consultar dados")
 print("3 - Atualizar informações")
 print("4 - Excluir registro")
 print("0 - Sair")

 op = int(input("Digite a sua opção:"))

 if op ==1: 
    print("Opção: 1")
    print("Cadastro aberto com sucesso!")
    
 elif op ==2:
    print("Opção: 2")
    print("Consulta realizada com sucesso!")
    
 elif op ==3:
    print("Opção: 3")
    print("Informações atualizadas com sucesso!")
    
 elif op ==4:
    print("Registro excluído com sucesso!")
    
 elif op ==0:
    print("Opção 0")
    print("Sistema encerrado")
    break

 else: 
    print("Opção inválida")