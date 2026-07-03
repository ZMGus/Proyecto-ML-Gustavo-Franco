# Análisis de verbatims mediante procesamiento de lenguaje natural y clasificación multietiqueta

**Asignatura:** Introducción al Aprendizaje Automático  
**Integrantes:** Franco Reinoso y Gustavo Montoya  
**Profesor:** Alejandro Veloz  

## Índice

- [Descripción del proyecto](#descripción-del-proyecto)
- [Objetivos](#objetivos)
- [Estructura esperada del repositorio](#estructura-esperada-del-repositorio)
- [Requisitos de software](#requisitos-de-software)
- [Instalación](#instalación)
- [Ejecución y reproducción de experimentos](#ejecución-y-reproducción-de-experimentos)

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
6. Documentar un pipeline reproducible.

## Estructura esperada del repositorio

```text
.
├── README.md
├── requirements.txt
├── .gitignore                    
├── notebooks/
│   ├── LineaA_KNN.ipynb
│   └── LineaB_SVM.ipynb
│   └── Datos_Hospital.xlsx
│   └── Datos_Seguros.csv
│   └── Base Etiquetada para tfidf
│   └── Base Etiquetada para Word2Vec                                                     
└── report/                             # Informe LaTeX, bibliografía, figuras y PDF final.
```

## Requisitos de software

- Python 3.10 o superior.
- `pip` para instalación de dependencias.
- Jupyter Notebook o Visual Studio Code con extensión de Jupyter.

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

## Ejecución y reproducción de experimentos

### Línea A: sector seguros

```bash
jupyter notebook notebooks/LineaA_KNN.ipynb
```

### Línea B: ámbito hospitalario

```bash
jupyter notebook notebooks/LineaB_SVM.ipynb
```

Ejecute las celdas en orden. El notebook crea automáticamente la carpeta `notebooks/artifacts/` y guarda allí todos los artefactos generados (matrices, modelos, resultados y figuras).
