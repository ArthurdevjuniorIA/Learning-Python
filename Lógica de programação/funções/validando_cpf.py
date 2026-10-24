def validando_cpf(cpf):
    if not isinstance(cpf,int) or not str(cpf).isdigit():
        print("Erro: O cpf deve conter apenas números")
        return -1
    elif len(str(cpf)) != 11:
        print("Erro: O CPF deve ter 11 dígitos")
        return -1
    return cpf

cpf_a_validar= input("Digite seu cpf: ").replace(".","").replace("-","").strip()
cpf_limpo = " ".join(cpf_a_validar.split())
cpf_limpo = int(cpf_limpo)
cpf_valido = validando_cpf(cpf_limpo)
if cpf_valido == cpf_limpo:
    print("CPF válido")
