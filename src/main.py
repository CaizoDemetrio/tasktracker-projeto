def mostrar_menu():
    print("\n--- TASK TRACKER ---")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")
    return input("Escolha uma opção: ")

def cadastrar_tarefa(tarefas):
    print("\n-- CADASTRAR NOVA TAREFA --")
    
    titulo = input("Título da tarefa: ")
    descricao = input("Descrição da tarefa: ")
    prioridade = input("Prioridade (Alta, Média, Baixa): ")
    data_limite = input("Data Limite (ex: DD/MM/AAAA): ")
    
    nova_tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }
    
    tarefas.append(nova_tarefa)
    print("\nTarefa cadastrada com sucesso!")

def visualizar_tarefas(tarefas):
    print("\n-- TAREFAS CADASTRADAS --")
    if len(tarefas) == 0:
        print("Não existem tarefas cadastradas no momento.")
        return
        
    for i, tarefa in enumerate(tarefas, 1):
        print(f"\nTarefa {i}:")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data Limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")
        print("-" * 25)

def main():
    tarefas = []
    while True:
        opcao = mostrar_menu()
        if opcao == '1':
            cadastrar_tarefa(tarefas)
        elif opcao == '2':
            visualizar_tarefas(tarefas)
        elif opcao == '3':
            print("Saindo da aplicação. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()