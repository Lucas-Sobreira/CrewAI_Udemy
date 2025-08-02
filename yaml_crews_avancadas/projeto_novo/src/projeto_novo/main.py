#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import ProjetoNovo

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'definicao_sistema': """
        Um sistema para criação de conteúdo de cursos de Inteligência Artificial Generativa que desenvolve
        uma abordagem estruturada, começando com uma pesquisa aprofundada de conteúdos relevantes, 
        seguida pela reunião e organização de tópicos importantes.
        Em seguida, define o escopo do curso e cria uma apostila abrangente e didática, garantindo
        que o material seja de alta qualidade e relevância para os alunos.
    """
    }
    
    try:
        ProjetoNovo().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        ProjetoNovo().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ProjetoNovo().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        ProjetoNovo().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

run()