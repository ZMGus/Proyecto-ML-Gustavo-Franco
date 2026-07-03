# Análisis de verbatims mediante procesamiento de lenguaje natural y clasificación multietiqueta

**Asignatura:** Introducción al Aprendizaje Automático  
**Integrantes:** Franco Reinoso y Gustavo Montoya  
**Profesor:** Alejandro Veloz  

## Descripción del proyecto

Este repositorio contiene el código, las configuraciones y la documentación del proyecto de análisis de comentarios abiertos (*verbatims*) mediante técnicas de procesamiento de lenguaje natural (NLP) y modelos clásicos de aprendizaje automático.

El proyecto se organiza en dos líneas de trabajo desarrolladas de forma independiente y comparables metodológicamente:

- **Línea A: comentarios del sector seguros.** Se transforma la base desde formato ancho a formato largo, se limpian y normalizan los textos, se generan cinco variantes de preprocesamiento y se comparan representaciones TF-IDF con n-gramas y Word2Vec mediante modelos KNN multietiqueta.
- **Línea B: comentarios del ámbito hospitalario.** Se aplica una lógica equivalente de limpieza, preparación, representación y modelamiento sobre un segundo conjunto de datos. 

La documentación y notebooks específicos ademas de archivos .csv de ambas líneas estaran incorporados en la carpeta `notebooks/`.
La comparación considera el efecto de la representación textual, el preprocesamiento y los hiperparámetros sobre métricas de clasificación y tiempos de ejecución.

## Objetivos

1. Preparar comentarios abiertos para análisis mediante limpieza y normalización textual.
2. Comparar variantes de preprocesamiento: texto limpio, sin tildes, sin stopwords controladas, stemming y lematización.
3. Construir representaciones TF-IDF con n-gramas y Word2Vec.
4. Entrenar y evaluar modelos KNN multietiqueta con una división común de entrenamiento, validación y prueba.
5. Comparar configuraciones mediante accuracy exacta, precision, recall, F1, Hamming loss y tiempos de ejecución.
6. Documentar un pipeline reproducible sin publicar datasets privados o pesados en GitHub.

## Estructura esperada del repositorio

```text
.
├── README.md
├── requirements.txt
├── .gitignore                    
├── notebooks/
│   ├── LineaA_KNN.ipynb
│   └── [notebooks y archivos de la Línea B]
│   └── Base Etiquetada para tfidf
│   └── Base Etiquetada para Word2Vec                                                     
└── report/                             # Informe LaTeX, bibliografía, figuras y PDF final.
```

## Requisitos de software

- Python 3.10 o superior.
- `pip` para instalación de dependencias.
- Jupyter Notebook o Visual Studio Code con extensión de Jupyter.
- Acceso autorizado a los enlaces de Google Drive compartidos por el equipo.

Las dependencias principales se encuentran en [`requirements.txt`](requirements.txt).

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/ZMGus/Proyecto-ML-Gustavo-Franco.git
cd Proyecto-ML-Gustavo-Franco
```

### 2. Crear y activar un entorno virtual

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```bat
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Descargar recursos lingüísticos necesarios

El proyecto utiliza el modelo en español de spaCy para lematización y recursos de NLTK para algunas tareas de preprocesamiento.

```bash
python -m spacy download es_core_news_sm
```

Luego, ejecute una vez en Python o Jupyter:

```python
import nltk
nltk.download("stopwords")
nltk.download("punkt")
```

## Obtención manual de los datasets

Los datasets no se incluyen en el repositorio porque contienen información privada y/o archivos de gran tamaño. Los archivos se comparten mediante Google Drive únicamente con los integrantes y el equipo docente autorizado.

### Enlaces de acceso autorizado

- **Dataset Línea A (sector seguros):** `https://docs.google.com/spreadsheets/d/1amznIch7_tSg1yRvxd2QLEjFcwN8Pygd/edit?gid=1317965515#gid=1317965515`
- **Dataset Línea B (ámbito hospitalario):** `https://docs.google.com/spreadsheets/d/1YkGvjsuF4Que-rcSdqKZCIvCkNPiHBbu/edit?gid=1036962913#gid=1036962913`

### Procedimiento de descarga

1. Inicie sesión con la cuenta a la que se otorgó permiso de acceso.
2. Abra el enlace de Google Drive correspondiente a la línea de trabajo.
3. Descargue manualmente el archivo o carpeta compartida.
4. Guarde los archivos originales en la misma altura que los notebooks
5. Ejecute el notebook de la línea correspondiente.

## Ejecución y reproducción de experimentos

### Línea A: sector seguros

1. Descargue manualmente el archivo autorizado desde Google Drive y guárdelo a la misma altura que el notebook de la Linea A
2. Abra el notebook de la Línea A:

```bash
jupyter notebook notebooks/LineaA_KNN.ipynb
```

### Línea B: sector seguros

Agrear Linea B

3. Ejecute las celdas en el orden definido en el notebook:

   - carga y validación de datos;
   - transformación a formato largo mediante `melt`;
   - limpieza y normalización textual;
   - construcción de las cinco variantes de texto;
   - extracción de características con TF-IDF y Word2Vec;
   - carga o cruce de etiquetas manuales;
   - división multietiqueta train--validation--test;
   - búsqueda de hiperparámetros KNN;
   - evaluación de métricas y ajuste de umbrales por categoría.

### Línea B: ámbito hospitalario

```text
[Completar con el notebook, archivo de entrada y orden de ejecución desarrollado para la Línea B.]
```
