import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from datetime import date, datetime
from DocxGenerator import generateDocx
from tools.BCRATool import BCRATool

load_dotenv()
day = date.today()
full_day = datetime.today()
searchtool = SerperDevTool()
bcra_tool = BCRATool()

researcher = Agent(
    role="Asistente de Investigación Profesional",
    goal=f"Buscar y encontrar cambios específicos y actuales en la economía argentina para el día {day}, enfocándose en datos económicos concretos sin sesgos ideológicos.",
    backstory="""Especialista en la recopilación de información económica actualizada, con énfasis en datos objetivos y relevantes para análisis económicos y financieros.
    Utiliza la bcra_tool para acceder a indices del banco central de argentina.""",
    tools=[searchtool, bcra_tool],
    verbose=True,
    allow_delegation=False,
)

writer = Agent(
    role="Escritor Profesional de Artículos Cortos",
    goal=f"Resumir las últimas noticias en la economía de Argentina para el día {day}, manteniendo un enfoque neutral y basado en datos.",
    backstory="""Experto en la redacción de artículos económicos claros y objetivos, utilizando información precisa y actualizada para informar al público.""",
    verbose=True,
    allow_delegation=True,
    tools=[searchtool],
)

research_task = Task(
    description=f"""Buscar datos económicos específicos y actualizados de Argentina para el día {day}, incluyendo cotizaciones de divisas, índices bursátiles, y movimientos de acciones relevantes.""",
    agent=researcher,
    expected_output="""Informe detallado con datos económicos concretos de la última semana.""",
)

write_task = Task(
    description="""Escribir un artículo resumiendo las noticias económicas más relevantes de la semana, con un enfoque neutral y basado en datos. En español""",
    agent=writer,
    expected_output="""Artículo completo con resúmenes claros y objetivos de las noticias económicas más importantes de la última semana.""",
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    verbose=True,
    output_log_file=f"Logs{full_day}.txt",
)
result = crew.kickoff()
generateDocx(result)