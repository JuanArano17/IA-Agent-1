# DocxGenerator: Generador de Documentos para Análisis Económico de Argentina

DocxGenerator es una herramienta diseñada para automatizar la creación de documentos de Word que contienen un análisis comprensivo de la economía argentina, basado en las últimas noticias y tendencias del mercado. Este proyecto utiliza Python y diversas bibliotecas para extraer, analizar y documentar los factores que influencian la economía de Argentina.

## Pre-requisitos

Antes de comenzar, asegúrate de tener Python instalado en tu sistema. Este proyecto ha sido desarrollado y probado con Python 3.8 y versiones superiores.

## Instalación

Para configurar tu entorno de desarrollo y trabajar con el proyecto DocxGenerator, sigue los siguientes pasos:

### Clonar el Repositorio

Primero, clona el repositorio a tu máquina local usando git:

```bash
git clone https://github.com/tu-usuario/DocxGenerator.git
cd DocxGenerator```

###Crear un Entorno Virtual
Es recomendable utilizar un entorno virtual para manejar las dependencias de manera aislada. Puedes crear un entorno virtual utilizando venv:

```bash
python -m venv venv```

###Para activar el entorno virtual, ejecuta:

En Windows:
```bash
.\venv\Scripts\activate```

En macOS y Linux:
```bash
source venv/bin/activate```

###Instalar las Dependencias
Con el entorno virtual activado, instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt```
Este comando instalará todas las bibliotecas necesarias para ejecutar el proyecto, incluyendo python-docx para la generación de documentos y cualquier otra dependencia listada en requirements.txt.

##Configuración
Antes de ejecutar el script, asegúrate de configurar las variables de entorno necesarias. Crea un archivo .env en el directorio raíz del proyecto y añade las siguientes variables:

```plaintext
OPENAI_API_KEY=tu_clave_api_aqui
SERPER_API_KEY=tu_clave_api_aqui```
Estas claves son necesarias para acceder a las APIs utilizadas por el proyecto.

##Ejecución
Con las dependencias instaladas y el entorno configurado, estás listo para ejecutar el script DocxGenerator. Para generar el documento de Word con el análisis de la economía argentina, ejecuta:

```bash
python3 DocxGenerator.py```
Este comando iniciará el proceso de recopilación y análisis de datos, y generará un documento de Word Analisis_Economia_Argentina.docx en el directorio del proyecto.
