# Datos del proyecto

Los datasets no se almacenan en GitHub porque son privados y/o pesados.

## Descarga autorizada

1. Solicite acceso a los enlaces de Google Drive compartidos por el equipo.
2. Copie `config/dataset_links.example.json` como `config/dataset_links.json`.
3. Pegue los enlaces autorizados en ese archivo local.
4. Ejecute:

```bash
python scripts/download_data.py --config config/dataset_links.json
```

Los datos se descargarán bajo `data/raw/`.

## Convención de carpetas

```text
data/
├── raw/        # Archivos originales descargados desde Google Drive.
└── processed/  # Archivos derivados por limpieza, melt, tokenización o representación.
```

No suba archivos de datos a GitHub.
