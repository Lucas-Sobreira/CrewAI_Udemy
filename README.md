# CrewAI

## Crews 
Permitem a criação de equipes de agentes autônomos, ou seja, multi agentes. Essas equipes são capazes de alcançar objetivos complexos, simulando equipes do mundo real.

## Agentes
Cada agente é responsável por uma tarefa específica. 
Como por exemplo:
    - Realizar análise de sentimentos;
    - Criar postagens, imagens e ou vídeos;
    - Salvar informações em Bancos de Dados (SQL, NoSQL e Vetorial) dependendo da aplicabilidade;

### Definições 
- Roles: Papel que o agente terá. 
Exemplo: Auxiliar, Economista, Nutricionista, etc;

- Objetivo (Goal): Define o que o agente deve alcançar, qual o objetivo dele. 
Exemplo: "Identificar tendências de mercado"

- Contexto/História (Backstory): Detalhes para guiar o agente. 
Exemplo: "Trabalhou na Wall Street por 10anos."

- Tarefas(Tasks): Roteiro para o sucesso
    - Ações específicas que os agentes devem executar para atingir seus objetivos;

    - Descrição (Description): Explicação clara do que precisa ser feito, como "Pesquisar artigos sobre IA na saúde";

    - Resultado esperado (Expected_Output): Define o formato e conteúdo do resultado da tarefa;

        - Exemplo: Resumo de 500 palavras; 
                Responda ao usuário o quanto foi gasto durante o dia;

    - Dependência (opcional): Quais tarefas precisam ser completadas antes desta poder ser iniciada. Isso garante a ordem correta do fluxo;
    
        - Exemplo: "A tarefa 'Coletar dados do cliente' deve ser concluída primeiro." 

- Ferramentas (Tools): A extensão das capacidades dos Agentes.
    - O que são ferramentas? Recursos que os agentes usam para realizar tarefas. 
        - Exemplo: APIs, Bancos de Dados, modelos de linguagem, bibliotecas de código;

- Orquestração e Conclusão: Agentes, tarefas e ferramentas interagem para formar uma Crew. O orquestrador agenda e executa as tarefas. 

### Criando um ipykernel (Kernel para rodar Jupyter Notebook no VS Code) 
```bash
poetry run python -m ipykernel install --user --name=analise-mercado --display-name "Poetry - Análise de Mercado"
```

### Para salvar o relatório em formato PDF 

Instale o wkhtmltopdf a partir do site: https://wkhtmltopdf.org/downloads.html

-------------------------------

## Projeto Analise de ações Ibovespa

### Criando Tools

- Criando Tools apartir de <span style="color: orange">documentos (.csv)</span> [ Agente 1 - Gerente do Cliente]

    Foi utilizada uma biblioteca para ler os dados e utiliza-los na criação da Crew.

    - CSVSearchTool;

- Criando Tools da <span style="color: orange">Yfinance (Yahoo Finance)</span> [Agente 2 - Analista de Ações]

    Foi utilizada uma biblioteca do próprio CrewAI para criar uma função personalizada para consultar os valores de um "papel" (ticket) utilizando a Yahoo Finance.

    ```bash
    from crewai.tools import BaseTool
    ```

- Criando Tools para <span style="color: orange">Pesquisa na Internet</span>

    No caso a pesquisa na Internet foi diretamente relacionada a alguns critérios sobre um "papel" (ticket) que usuário seleciona, para obter resultados como: 
        
    - Resumo das notícias sobre o ativo; 
    - Um "Rating" a respeito de Medo/Ganância das pessoas em adquirir o ativo;

    Para isso foi utilizado o "DuckDuckGo".

    ```bash
    from langchain_community.tools import DuckDuckGoSearchResults
    ```