import json
from pathlib import Path


def create_json(path: Path, data: dict) -> None:
    """
    Создаёт новый json-конфиг

    :param path: Путь до конфига
    :param data: Данные
    :return: None
    """
    path.write_text(json.dumps(data, indent=2))


def load_json(path: Path) -> dict:
    """
    Читает json-конфиг

    :param path: Путь до конфига
    :return: Содержимое конфига
    """
    return json.load(path.open())


def update_json(path: Path, data: dict) -> None:
    """
    Обновляет json-конфиг.
    Если конфиг не существует - создаёт новый

    :param path: Путь до конфига
    :param data: Данные
    :return: None
    """
    olddata = {}
    if path.exists():
        olddata = load_json(path)
    olddata.update(data)
    create_json(path, olddata)
