from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

import agentops
import os
from dotenv import load_dotenv

load_dotenv()

AGENTOPS_API_KEY=os.getenv("AGENTOPS_API_KEY")
agentops.init(api_key=AGENTOPS_API_KEY)

@CrewBase
class ProjetoNovo():
    """ProjetoNovo crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    ## Agents
    @agent
    def product_owner(self) -> Agent:
        return Agent(
            config=self.agents_config['product_owner'], # type: ignore[index]
            verbose=True
        )

    @agent
    def arquiteto_de_solucoes(self) -> Agent:
        return Agent(
            config=self.agents_config['arquiteto_de_solucoes'], # type: ignore[index]
            verbose=True
        )

    @agent
    def analista_de_processos(self) -> Agent:
        return Agent(
            config=self.agents_config['analista_de_processos'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def desenvolvedor_python(self) -> Agent:
        return Agent(
            config=self.agents_config['desenvolvedor_python'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def qa_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_engineer'], # type: ignore[index]
            verbose=True
        )

    ## Tasks
    @task
    def definir_escopo_do_sistema(self) -> Task:
        return Task(
            config=self.tasks_config['definir_escopo_do_sistema'], # type: ignore[index]
        )

    @task
    def modelar_agentes(self) -> Task:
        return Task(
            config=self.tasks_config['modelar_agentes'], # type: ignore[index]
            output_file='./projeto_novo/src/projeto_novo/output/agents.yaml'
        )
    
    @task
    def estruturar_tarefas(self) -> Task:
        return Task(
            config=self.tasks_config['estruturar_tarefas'], # type: ignore[index]
            context=[self.definir_escopo_do_sistema()],
            output_file='./projeto_novo/src/projeto_novo/output/tasks.yaml'
        )
    
    @task
    def desenvolver_orquestrador(self) -> Task:
        return Task(
            config=self.tasks_config['desenvolver_orquestrador'], # type: ignore[index]
            context=[self.definir_escopo_do_sistema(),
                     self.modelar_agentes()],
            output_file='./projeto_novo/src/projeto_novo/output/crew.py'
        )
    
    @task
    def validar_sistema(self) -> Task:
        return Task(
            config=self.tasks_config['validar_sistema'], # type: ignore[index]
            output_file='./projeto_novo/src/projeto_novo/report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ProjetoNovo crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
