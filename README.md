# Análisis de verbatims mediante procesamiento de lenguaje natural y clasificación multietiqueta

**Asignatura:** Introducción al Aprendizaje Automático  
**Integrantes:** Franco Reinoso y Gustavo Montoya  
**Profesor:** Alejandro Veloz  

## Descripción del proyecto

Este repositorio contiene el código, configuraciones y documentación del proyecto de análisis de comentarios abiertos (verbatims) mediante técnicas de procesamiento de lenguaje natural (NLP) y modelos clásicos de aprendizaje automático.

El proyecto se organiza en dos líneas de trabajo desarrolladas de forma independiente y comparables metodológicamente:

- **Línea A: comentarios del sector seguros.** Se transforma la base desde formato ancho a formato largo, se limpian y normalizan los textos, se generan cinco variantes de preprocesamiento y se comparan representaciones TF-IDF con n-gramas y Word2Vec mediante modelos KNN multietiqueta.
- **Línea B: comentarios del ámbito hospitalario.** Se aplica una lógica equivalente de limpieza, preparación, representación y modelamiento sobre un segundo conjunto de datos. La documentación y notebooks específicos de esta línea deben incorporarse en la carpeta `notebooks/`.

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
├── config/
│   ├── dataset_links.example.json
│   └── dataset_links.json              # Local; no se versiona.
├── data/
│   ├── README.md
│   ├── raw/                            # Datos descargados desde Google Drive; no se versionan.
│   └── processed/                      # Datos derivados; no se versionan si son pesados.
├── notebooks/
│   ├── Proyecto_ML_Universidad_feature_extraction_corregido.ipynb
│   └── [notebooks de la Línea B]
├── scripts/
│   └── download_data.py
├── models/                             # Modelos, vectores y objetos serializados; no se versionan si son pesados.
├── outputs/                            # Métricas, tablas y figuras reproducibles.
└── report/                             # Informe LaTeX, bibliografía, figuras y PDF final.
```

## Requisitos de software

- Python 3.10 o superior.
- `pip` para instalación de dependencias.
- Jupyter Notebook o Visual Studio Code con extensión de Jupyter.
- Acceso autorizado a los enlaces de Google Drive que contienen los datasets.

Las dependencias principales se encuentran en [`requirements.txt`](requirements.txt).

## Instalación

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
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

## Obtención de los datasets

Los datasets no se incluyen en el repositorio porque contienen información privada y/o archivos de gran tamaño. Los archivos se distribuyen mediante enlaces de Google Drive con permisos para el equipo docente y los integrantes del proyecto.

### Configuración de enlaces

1. Copie el archivo de ejemplo:

```bash
cp config/dataset_links.example.json config/dataset_links.json
```

En Windows PowerShell:

```powershell
Copy-Item config/dataset_links.example.json config/dataset_links.json
```

2. Abra `config/dataset_links.json` y reemplace los valores de `url` por los enlaces compartidos de Google Drive.

```json
{
  "dataset_linea_a": {
    "kind": "file",
    "url": "PEGAR_ENLACE_DE_GOOGLE_DRIVE_AQUI",
    "output": "data/raw/dataset_linea_a"
  },
  "dataset_linea_b": {
    "kind": "file",
    "url": "PEGAR_ENLACE_DE_GOOGLE_DRIVE_AQUI",
    "output": "data/raw/dataset_linea_b"
  }
}
```

> Si cada dataset se comparte como carpeta de Google Drive, cambie `"kind": "file"` por `"kind": "folder"`.

3. Descargue los archivos:

```bash
python scripts/download_data.py --config config/dataset_links.json
```

El script descarga los datos en `data/raw/`. Esta carpeta está excluida del control de versiones mediante `.gitignore`.

## Ejecución y reproducción de experimentos

### Línea A: sector seguros

1. Confirme que el archivo correspondiente se encuentre en `data/raw/`.
2. Abra el notebook de la Línea A:

```bash
jupyter notebook notebooks/Proyecto_ML_Universidad_feature_extraction_corregido.ipynb
```

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

4. Los resultados deben guardarse en `outputs/` y los objetos entrenados en `models/`, evitando subir archivos grandes al repositorio.

### Línea B: ámbito hospitalario

```text
[Completar con el notebook, archivo de entrada y orden de ejecución desarrollado para la Línea B.]
```

## Reproducibilidad

Para garantizar comparabilidad entre configuraciones, los experimentos deben mantener:

- la misma muestra etiquetada dentro de cada línea de trabajo;
- una división fija de entrenamiento, validación y prueba;
- una semilla aleatoria común (`SEED = 42`, salvo que el notebook indique otra);
- las mismas métricas de evaluación para las configuraciones comparadas;
- registro de representación, versión de texto, hiperparámetros, tiempos y métricas finales.

En la Línea A, los experimentos comparan cinco variantes de texto y dos representaciones, generando diez configuraciones KNN antes de la calibración de umbrales por categoría.

## Resultados principales disponibles

En la Línea A, el análisis previo a la calibración de umbrales identificó como mejor resultado observado a `KNN__TFIDF_NGRAMS__texto_v5_lemma`. Posteriormente, se aplicó una etapa adicional de ajuste de umbrales por categoría, orientada a mejorar el equilibrio entre precision y recall. Los resultados detallados, tablas y reportes de clasificación se encuentran documentados en el informe final de la carpeta `report/`.

```text
[Incorporar aquí el resumen de resultados de la Línea B cuando se agreguen sus archivos y métricas finales.]
```

## Privacidad y uso de datos

Los datasets utilizados son de carácter privado. No deben subirse al repositorio, redistribuirse públicamente ni utilizarse fuera del contexto académico autorizado. El repositorio solo contiene código, configuraciones, instrucciones de descarga y documentación necesaria para reproducir el procesamiento por personas que dispongan de autorización para acceder a los enlaces compartidos.

## Informe final

El informe escrito en LaTeX, las figuras, la bibliografía y el PDF final deben almacenarse en la carpeta `report/`. No se deben incluir listados extensos de código dentro del informe; el código fuente se evalúa directamente desde este repositorio.

## Contacto

Para consultas sobre la reproducción del proyecto, contactar a los integrantes mediante los canales definidos para la asignatura.
