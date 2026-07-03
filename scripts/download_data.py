"""Descarga datasets privados desde enlaces autorizados de Google Drive.

Uso:
    python scripts/download_data.py --config config/dataset_links.json

El archivo de configuración no se versiona y debe crearse a partir de
config/dataset_links.example.json.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import gdown


def validate_entry(name: str, entry: dict[str, Any]) -> None:
    required = {"kind", "url", "output"}
    missing = required.difference(entry)
    if missing:
        raise ValueError(f"'{name}' no contiene los campos requeridos: {sorted(missing)}")

    if entry["kind"] not in {"file", "folder"}:
        raise ValueError(f"'{name}.kind' debe ser 'file' o 'folder'.")

    url = str(entry["url"]).strip()
    if not url or "PEGAR_ENLACE" in url:
        raise ValueError(
            f"Debe reemplazar la URL de '{name}' en el archivo de configuración."
        )


def download_dataset(name: str, entry: dict[str, Any]) -> None:
    validate_entry(name, entry)

    kind = entry["kind"]
    url = str(entry["url"]).strip()
    output = Path(entry["output"])
    output.parent.mkdir(parents=True, exist_ok=True)

    print(f"\nDescargando: {name}")
    print(f"Tipo: {kind}")
    print(f"Destino: {output}")

    if kind == "folder":
        output.mkdir(parents=True, exist_ok=True)
        downloaded = gdown.download_folder(
            url=url,
            output=str(output),
            quiet=False,
            use_cookies=False,
        )
    else:
        downloaded = gdown.download(
            url=url,
            output=str(output),
            quiet=False,
            fuzzy=True,
        )

    if not downloaded:
        raise RuntimeError(
            f"No fue posible descargar '{name}'. Verifique que el enlace exista "
            "y que la cuenta tenga permisos de acceso."
        )

    print(f"Descarga completada: {name}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Descarga datasets desde Google Drive usando un archivo JSON local."
    )
    parser.add_argument(
        "--config",
        default="config/dataset_links.json",
        help="Ruta del archivo JSON con enlaces de Google Drive.",
    )
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.exists():
        print(
            "No se encontró el archivo de configuración. Cree una copia de "
            "config/dataset_links.example.json como config/dataset_links.json "
            "y complete los enlaces autorizados.",
            file=sys.stderr,
        )
        return 1

    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
        if not isinstance(config, dict) or not config:
            raise ValueError("El archivo de configuración debe contener al menos un dataset.")

        for name, entry in config.items():
            if not isinstance(entry, dict):
                raise ValueError(f"La configuración de '{name}' debe ser un objeto JSON.")
            download_dataset(name, entry)

    except (ValueError, RuntimeError, json.JSONDecodeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
