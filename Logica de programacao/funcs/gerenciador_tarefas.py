from time import sleep

# --- DECORADORES ---

def precisa_de_tarefas(func):
    """Impede a execução da função se o dicionário de tarefas estiver vazio."""
    def wrapper(tarefas, *args, **kwargs):
        if not tarefas:
            print("\n ⚠️  Nenhuma tarefa registrada ainda!")
            return None
        return func(tarefas, *args, **kwargs)
    return wrapper

def pausar_execucao(func):
    """Pausa a tela por 1.5 segundos após a execução da função."""
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        sleep(1.5)
        return resultado
    return wrapper


# --- FUNÇÕES DO SISTEMA ---

def exibir_menu():
    print("\n" + "="*25)
    print("    MENU DE TAREFAS")
    print("="*25)
    print("1. Adicionar tarefa")
    print("2. Visualizar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

@pausar_execucao
def adicionar_tarefa(tarefas, id_atual):
    tarefa = input("Digite a tarefa a adicionar: ").strip()
    if tarefa:
        tarefas[id_atual] = tarefa
        print(f"✅ Tarefa '{tarefa}' adicionada com sucesso!")
        return id_atual + 1
    print("⚠️  A descrição da tarefa não pode estar vazia.")
    return id_atual

@pausar_execucao
@precisa_de_tarefas
def listar_tarefas(tarefas):
    print("\n--- SUA LISTA DE TAREFAS ---")
    for key, valor in tarefas.items():
        print(f"{key}. {valor}")

@pausar_execucao
@precisa_de_tarefas
def remover_tarefa(tarefas):
    print("\n--- REMOVER TAREFA ---")
    for key, valor in tarefas.items():
        print(f"{key}. {valor}")
    
    try:
        remover = int(input("Digite o número da tarefa a remover: "))
        if remover in tarefas:
            removida = tarefas.pop(remover)
            print(f"🗑️  Tarefa '{removida}' removida com sucesso!")
        else:
            print("❌ Erro: O número digitado não existe na lista.")
    except ValueError:
        print("❌ Erro: Digite apenas números inteiros.")


# --- FLUXO PRINCIPAL ---

def main():
    tarefas = {}
    quantidade_tarefas = 1

    while True:
        exibir_menu()
        try:
            opcao = int(input("\nEscolha uma opção (1-4): "))
        except ValueError:
            print("❌ Por favor, digite um número válido.")
            sleep(1)
            continue

        if opcao == 1:
            quantidade_tarefas = adicionar_tarefa(tarefas, quantidade_tarefas)
        elif opcao == 2:
            listar_tarefas(tarefas)
        elif opcao == 3:
            remover_tarefa(tarefas)
        elif opcao == 4:
            print("👋 Saindo do sistema...")
            sleep(1)
            break
        else:
            print("⚠️  Opção inválida! Escolha entre 1 e 4.")
            sleep(1)

if __name__ == "__main__":
    main()