import json
import os

# Nome do arquivo onde as tarefas serão salvas
ARQUIVO_TAREFAS = "tarefas.json"

def carregar_tarefas():
    """Lê as tarefas salvas no arquivo JSON"""
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    """Salva a lista de tarefas no arquivo JSON"""
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

def menu():
    tarefas = carregar_tarefas()
    
    while True:
        print("\n" + "="*30)
        print("   BOT ORGANIZADOR DE TAREFAS")
        print("="*30)
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Remover Tarefa")
        print("5. Sair")
        print("="*30)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nova_tarefa = input("\nDigite a descrição da tarefa: ")
            if nova_tarefa.strip():
                tarefas.append({"descricao": nova_tarefa, "concluida": False})
                salvar_tarefas(tarefas)
                print("✔ Tarefa adicionada com sucesso!")
            else:
                print("❌ Erro: A descrição não pode ser vazia.")
            
        elif opcao == "2":
            print("\n📋 SUAS TAREFAS:")
            if not tarefas:
                print("Sua lista está vazia no momento.")
            for i, t in enumerate(tarefas):
                status = "[X]" if t["concluida"] else "[ ]"
                print(f"{i+1}. {status} {t['descricao']}")
                
        elif opcao == "3":
            if not tarefas:
                print("\n❌ Nenhuma tarefa cadastrada para concluir.")
                continue
            print("\n📋 SELECIONE A TAREFA PARA CONCLUIR:")
            for i, t in enumerate(tarefas):
                status = "[X]" if t["concluida"] else "[ ]"
                print(f"{i+1}. {status} {t['descricao']}")
            try:
                indice = int(input("Digite o número da tarefa: ")) - 1
                if 0 <= indice < len(tarefas):
                    tarefas[indice]["concluida"] = True
                    salvar_tarefas(tarefas)
                    print("✔ Tarefa marcada como concluída!")
                else:
                    print("⚠ Número inválido!")
            except ValueError:
                print("⚠ Entrada inválida! Digite apenas números.")

        elif opcao == "4":
            if not tarefas:
                print("\n❌ Nenhuma tarefa cadastrada para remover.")
                continue
            print("\n📋 SELECIONE A TAREFA PARA REMOVER:")
            for i, t in enumerate(tarefas):
                status = "[X]" if t["concluida"] else "[ ]"
                print(f"{i+1}. {status} {t['descricao']}")
            try:
                indice = int(input("Digite o número da tarefa: ")) - 1
                if 0 <= indice < len(tarefas):
                    tarefa_removida = tarefas.pop(indice)
                    salvar_tarefas(tarefas)
                    print(f"✔ Tarefa '{tarefa_removida['descricao']}' removida com sucesso!")
                else:
                    print("⚠ Número inválido!")
            except ValueError:
                print("⚠ Entrada inválida! Digite apenas números.")

        elif opcao == "5":
            print("\nEncerrando o bot... Até logo!")
            break
        else:
            print("\n⚠ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
    
