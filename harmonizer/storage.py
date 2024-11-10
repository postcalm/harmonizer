from pathlib import Path

from harmonizer.utils.filesys import load_json, update_json


class Storage:
    """Хранилище приложения"""

    STORAGE_FILE: Path

    @classmethod
    def get(cls, param: str) -> str | int | bool | None:
        """
        Получить значение параметра

        :param param: Название параметра
        :return: Значение параметра или None
        """
        return load_json(cls.STORAGE_FILE).get(param, None)

    @classmethod
    def set(cls, param: str, value: str | int | bool) -> None:
        """
        Задать значение параметра

        :param param: Название параметра
        :param value: Значение параметра
        :return: None
        """
        update_json(cls.STORAGE_FILE, {param: value})
