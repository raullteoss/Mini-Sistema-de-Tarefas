# ==========================================
# Mini Sistema de Tarefas (To-Do List)
# Desenvolvido para terminal (CLI)
# ==========================================
#
# Armazenamento: lista de dicionários, uma por tarefa:
#   {"descricao": str, "concluida": bool}
#
# O "ID" mostrado ao usuário (1, 2, 3...) é só visual: é o
# índice da lista (0, 1, 2...) somado a 1. Por isso, sempre que
# lemos um ID digitado pelo usuário, subtraímos 1 antes de usar
# como índice real da lista (ver concluir_tarefa/excluir_tarefa).

LARGURA_ID = 5
LARGURA_DESCRICAO = 25
LARGURA_STATUS = 10


def exibir_menu():
    """Exibe as opções de gerenciamento para o usuário."""
    print("\n" + "=" * 40)
    print("      GERENCIADOR DE TAREFAS V1.0")
    print("=" * 40)
    print("[1] - Adicionar Tarefa")
    print("[2] - Listar Tarefas")
    print("[3] - Concluir Tarefa (Marcar OK)")
    print("[4] - Excluir Tarefa")
    print("[5] - Sair")
    print("=" * 40)


def listar_tarefas(tarefas):
    """Exibe a lista de tarefas formatada em colunas (ID | Descrição | Status)."""
    print("\n" + "-" * 40)
    print("{:<{w1}} | {:<{w2}} | {:<{w3}}".format(
        "ID", "DESCRIÇÃO", "STATUS", w1=LARGURA_ID, w2=LARGURA_DESCRICAO, w3=LARGURA_STATUS
    ))
    print("-" * 40)

    if not tarefas:
        print("Sua lista está vazia.")
    else:
        # enumerate(start=1) gera o ID visual (índice real + 1)
        for i, tarefa in enumerate(tarefas, start=1):
            status = "✅ Concluída" if tarefa["concluida"] else "⏳ Pendente"
            print("{:<{w1}} | {:<{w2}} | {:<{w3}}".format(
                i, tarefa["descricao"], status, w1=LARGURA_ID, w2=LARGURA_DESCRICAO, w3=LARGURA_STATUS
            ))
    print("-" * 40)


def adicionar_tarefa(tarefas):
    """Cria uma nova tarefa (sempre iniciando como pendente) e adiciona à lista."""
    descricao = input("\nDigite a descrição da tarefa: ").strip()

    if not descricao:
        print("Erro: A descrição não pode ser vazia.")
        return

    nova_tarefa = {
        "descricao": descricao,
        "concluida": False,
    }
    tarefas.append(nova_tarefa)
    print("Sucesso: Tarefa '{}' adicionada!".format(descricao))


def concluir_tarefa(tarefas):
    """Marca uma tarefa existente como concluída, a partir do ID visual digitado."""
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        indice = int(input("\nDigite o ID da tarefa para concluir: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            print("Sucesso: Tarefa '{}' marcada como concluída!".format(tarefas[indice]["descricao"]))
        else:
            print("Erro: ID de tarefa inexistente.")
    except ValueError:
        print("Erro: Entrada inválida. Digite o número do ID.")


def excluir_tarefa(tarefas):
    """Remove uma tarefa da lista, a partir do ID visual digitado."""
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        indice = int(input("\nDigite o ID da tarefa para excluir: ")) - 1
        if 0 <= indice < len(tarefas):
            removida = tarefas.pop(indice)
            print("Sucesso: Tarefa '{}' excluída!".format(removida["descricao"]))
        else:
            print("Erro: ID de tarefa inexistente.")
    except ValueError:
        print("Erro: Entrada inválida. Digite o número do ID.")


def main():
    """Função principal: controla o loop do menu do sistema."""
    lista_de_tarefas = []  # lista de dicionários em memória

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            adicionar_tarefa(lista_de_tarefas)
        elif opcao == "2":
            listar_tarefas(lista_de_tarefas)
        elif opcao == "3":
            concluir_tarefa(lista_de_tarefas)
        elif opcao == "4":
            excluir_tarefa(lista_de_tarefas)
        elif opcao == "5":
            print("\nEncerrando sistema... Produtividade é a chave do sucesso!")
            break
        else:
            print("\nErro: Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
