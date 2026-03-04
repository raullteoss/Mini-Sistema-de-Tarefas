#  Mini Sistema de Tarefas (To-Do List)

Um gerenciador de tarefas simples e eficiente executado inteiramente no terminal. Este projeto simula um ambiente de produtividade onde o usuário pode organizar suas atividades diárias.

##  Funcionalidades
- **Adicionar Tarefas:** Criação dinâmica de itens com status inicial "Pendente".
- **Listagem Numerada:** Visualização clara com IDs gerados automaticamente.
- **Conclusão de Tarefas:** Alteração de status para tarefas finalizadas.
- **Exclusão:** Remoção de itens da lista por ID.
- **Validação de Erros:** Proteção contra entradas de texto em campos numéricos ou IDs inexistentes.

##  Detalhes Técnicos
- **Python 3.x**
- **Armazenamento:** Lista de Dicionários (`List[dict]`).
- **Formatação:** Uso rigoroso de `.format()` para alinhamento de colunas no terminal.

##  Aprendizados
Este projeto exercita a lógica de **indexação**, onde o ID visual apresentado ao usuário (ex: 1, 2, 3) é convertido internamente para o índice da lista (0, 1, 2), demonstrando controle preciso sobre estruturas de dados.
