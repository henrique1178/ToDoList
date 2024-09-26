lista_de_tarefas = []

def adicionar_tarefas(titulo, descricao, prioridade, categoria):
    if prioridade not in ["Alta", "Média", "Baixa"]:
        print("Prioridade inválida. Use 'Alta', 'Média' ou 'Baixa'.")
        return

    tarefa = {
        "Titulo": titulo,
        "Descrição": descricao,
        "Prioridade": prioridade,
        "Categoria": categoria,
        "Concluída": False
    }
    lista_de_tarefas.append(tarefa)

def listar_tarefas(tarefas):
    if not tarefas:
        print("Lista vazia, adicione itens a essa lista!")
        return
    for tarefa in tarefas:
        status = "Concluída" if tarefa["Concluída"] else "Pendente"
        print(
            f"- {tarefa['Titulo']} \n"
            f"  - Descrição: {tarefa['Descrição']} \n"
            f"  - Prioridade: {tarefa['Prioridade']} \n"
            f"  - Categoria: {tarefa['Categoria']} \n"
            f"  - Status: {status}\n"
        )

def marcar_tarefa_como_concluida(titulo):
    for tarefa in lista_de_tarefas:
        if tarefa["Titulo"] == titulo:
            tarefa["Concluída"] = True
            print(f"Tarefa '{titulo}' marcada como concluída.")
            return
    print(f"Tarefa '{titulo}' não encontrada.")

def exibir_tarefas_por_criterio(criterio):
    if not lista_de_tarefas:
        print("Lista vazia, adicione itens a essa lista!")
        return
    tarefas_ordenadas = sorted(lista_de_tarefas, key=lambda x: x[criterio])
    
    print(f"\nTarefas Organizadas Por {criterio.capitalize()}:")
    listar_tarefas(tarefas_ordenadas)

def exibir_tarefas_por_categoria():
    if not lista_de_tarefas:
        print("Lista vazia, adicione itens a essa lista!")
        return
    categorias_exibidas = set()
    print("\nTarefas Organizadas Por Categoria:")
    
    for tarefa in lista_de_tarefas:
        categoria = tarefa["Categoria"]
        if categoria not in categorias_exibidas:
            categorias_exibidas.add(categoria)
            print(f"\nCategoria: {categoria}")
            listar_tarefas([t for t in lista_de_tarefas if t["Categoria"] == categoria])