from funcoes import *

while True:
    menu = input("""\n
        1 - Adicionar Nova Tarefa
        2 - Listar Tarefas
        3 - Marcar Tarefa como Concluída
        4 - Exibir Tarefas por Prioridade
        5 - Exibir Tarefas por Categoria
        0 - Sair
    """)
    if menu == "1":
        titulo = input("Título da tarefa: ")
        descricao = input("Descrição da tarefa: ")
        prioridade = input("Prioridade (Alta, Média, Baixa): ")
        categoria = input("Categoria: ")
        adicionar_tarefas(titulo, descricao, prioridade, categoria)
    elif menu == "2":
        listar_tarefas(lista_de_tarefas)
    elif menu == "3":
        titulo = input("Título da tarefa a ser marcada como concluída: ")
        marcar_tarefa_como_concluida(titulo)
    elif menu == "4":
        exibir_tarefas_por_criterio("Prioridade")
    elif menu == "5":
        exibir_tarefas_por_categoria()
    elif menu == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")