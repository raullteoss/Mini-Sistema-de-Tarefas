Mini Sistema de Tarefas (To-Do List)
Um gerenciador de tarefas simples e eficiente. Disponível em duas versões: a original via terminal (CLI) e uma interface web que reproduz a mesma lógica.
Funcionalidades
Adicionar Tarefas: criação dinâmica de itens com status inicial "Pendente".
Listagem Numerada: visualização clara com IDs gerados automaticamente.
Conclusão de Tarefas: alteração de status para tarefas finalizadas.
Exclusão: remoção de itens da lista por ID.
Validação de Erros: proteção contra entradas de texto em campos numéricos ou IDs inexistentes.
Estrutura do repositório
```
mini-sistema-de-tarefas/
├── cli/
│   └── gerenciador_tarefas.py   # versão original, via terminal
└── web/
    └── index.html               # interface web (HTML/CSS/JS puro)
```
Versão CLI
Detalhes técnicos
Python 3.x
Armazenamento: lista de dicionários (`List[dict]`).
Formatação: uso de `.format()` para alinhamento de colunas no terminal.
Indexação: o ID visual mostrado ao usuário (1, 2, 3...) é convertido internamente para o índice real da lista (0, 1, 2...).
Como executar
```bash
cd cli
python3 gerenciador_tarefas.py
```
Versão Web
Interface simples em HTML/CSS/JS que roda direto no navegador, sem instalação e sem back-end. Reproduz as mesmas mensagens e validações da versão CLI (adicionar, concluir, excluir), com a diferença de que concluir/excluir é feito clicando na tarefa em vez de digitar o ID — mais natural em uma interface visual. Os dados existem apenas em memória durante a sessão; ao atualizar a página, a lista é reiniciada.
Como executar
Basta abrir o arquivo `web/index.html` em qualquer navegador. Não requer servidor.
Autor
Projeto desenvolvido como exercício acadêmico de lógica de programação e estruturas de dados em Python.


