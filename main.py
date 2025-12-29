import json


def load_data_txt(path: str) -> list[list[str]]:
    """
    Lee data.txt y devuelve una lista de capítulos,
    donde cada capítulo es una lista de líneas.
    """
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Separar capítulos por ***
    raw_chapters = content.split("***")

    chapters = []
    for chapter in raw_chapters:
        lines = [
            line.strip()
            for line in chapter.strip().splitlines()
            if line.strip()
        ]
        chapters.append(lines)

    return chapters


def ask_metadata() -> dict:
    """
    Solicita los datos base por consola
    """
    print("Ingrese los datos para el JSON:\n")

    id_value = input("ID: ").strip()
    periodo = input("Periodo: ").strip()
    abrev = input("Abreviatura: ").strip()
    nome = input("Nombre: ").strip()

    return {
        "id": id_value,
        "periodo": periodo,
        "abrev": abrev,
        "nome": nome
    }


def build_json_structure(metadata: dict, chapters: list[list[str]]) -> list[dict]:
    """
    Construye la estructura del json siguiendo el formato de json.md
    """
    return {
            "id": metadata["id"],
            "periodo": metadata["periodo"],
            "nome": metadata["nome"],
            "abrev": metadata["abrev"],
            "capitulos": chapters
        }


def main():
    data_txt_path = "data.txt"
    output_json_path = "output.json"

    metadata = ask_metadata()
    chapters = load_data_txt(data_txt_path)

    result = build_json_structure(metadata, chapters)

    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\n✅ JSON generado correctamente en: {output_json_path}")


if __name__ == "__main__":
    main()
