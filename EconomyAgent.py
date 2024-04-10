import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from datetime import date

load_dotenv()
day = date.today()
searchtool = SerperDevTool()

researcher = Agent(
    role="Asistente de Investigación Senior",
    goal=f"Buscar las últimas noticias sobre la economía y el estado del mercado de Argentina para el dia {day}.",
    backstory="""Eres un dibulgador de informacion altamente capacitado, preciso y útil para entender los cambios económicos en la economía de Argentina.
    Tu especialidad es buscar en Google eventos y cambios en la industria, política y el mercado que pueden llevar a consecuencias económicas.
    Eres bueno entendiendo los cambios del mercado y sus implicaciones en la economía. 
    Ejemplo de informacion que buscas es: cotizacion del dolar hoy, suba de acciones de mercado libre, nueva empresa unicornio argentina, etc.
    """,
    verbose=False,
    allow_delegation=False,
    tools=[searchtool],
    llm=ChatOpenAI(model_name="gpt-4-0125-preview", temperature=0.2)
)
writer = Agent(
    role="Escritor Profesional de Artículos Cortos",
    goal=f"Resumir las últimas noticias en la economía de Argentina para el dia {day}.",
    backstory="""Eres un excelente escritor de artículos de economía. Simplificas conceptos complejos en items de 2 o 3 parrafos o frases cortas.
    Informas de manera clara pero preofesionalmente tus noticias.
    """,
    verbose=False,
    allow_delegation=True,
    tools=[searchtool],
    llm=ChatOpenAI(model_name="gpt-4-0125-preview", temperature=0.7)
)
research_task = Task(
    description=f"""Realizar un análisis comprensivo enfocándose en los varios factores que influyen en la economía de Argentina para el dia {day}. 
    Este análisis debería cubrir variaciones del mercado, decisiones políticas, cambios en la industria y el impacto de nuevas tecnologías.
    Es esencial remarcar las tendencias del mercado asi como las tendencias de la tecnologia en el pais.
    Ejemplo de informacion que buscas es: cotizacion del dolar hoy, suba de acciones de mercado libre, nueva empresa unicornio argentina, nueva tecnologia llega a argentina, nueva empresa importante sale a la bolsa, etc.""",
    expected_output="""Se debera presentar un informe detallado para cada noticia o informacion a documentar.""",
    agent= researcher
)
write_task = Task(
    description="""Utilizando los conocimientos proporcionados, escribir un artículo que destaque las noticias más significativas del mercado. 
    Esto debe ser significativo para toma de decisiones, de inversiones o para entender las tendencias actuales tanto en mercado como tecnologia.""",
    expected_output="""Publicación completa en el blog con al menos 8 noticias, cambios o cosas que saber sobre el mercado. 
    La información debe ser compilada en una sección de 'Anexo' al final del documento, detallando el impacto específico de cada item en la economía de Argentina.
    Cada sección del análisis (variaciones del mercado, decisiones políticas, cambios en la industria, nuevas tecnologías) debe estar definida con un titulo, su texto y su nivel de importancia del 1 al 10 en relacion a los demas puntos del resumen.
    Toda esta informacion debe ser sobre temas recientes (no mas de una semana de antiguedad).
    """,
    agent= writer
)
crew = Crew(
    agents = [researcher, writer],
    tasks= [research_task, write_task],
    verbose=False
)
result = crew.kickoff()

def getResult():
    return result