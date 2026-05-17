from pathlib import Path

from harmonizer.utils.filesys import load_json, create_json


def convert_config_tune_to_new_style(filepath: Path) -> None:
    """
    Конвертирует конфиг файл в новый формат

    :param filepath: Путь до конфига

    :return: None
    """
    styles = {
        6: "six_string",
        7: "seven_string",
    }
    data = load_json(filepath)
    new_data = {
        "six_string": {},
        "seven_string": {},
    }
    converted = False
    old_file = filepath.parent / f"{filepath.stem}.old.json"
    create_json(old_file, data)
    for k in data.keys():
        if k in styles.values():
            continue
        length = len(data[k]["notes"])
        new_data[styles[length]].update({k: data[k]})
        converted = True
    if converted:
        create_json(filepath, new_data)
