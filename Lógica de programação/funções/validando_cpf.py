def validando_cpf(cpf):
    if isinstance(cpf,int):
        print("Erro: O cpf deve conter apenas números")
        return -1
    elif len(cpf) != 11:
        print("Erro: O CPF deve ter 11 dígitos")
        return -1
    return cpf

cpf_a_validar= input("Digite seu cpf: ").replace(".","").replace("-","").strip().split(" ")
cpf_a_validar = int(cpf_a_validar)
cpf_valido = validando_cpf(cpf_a_validar)
if cpf_valido:
    print("CPF válido")