from dataclasses import dataclass

from harmonizer.core import Singleton
from harmonizer.core.types.enums.notes import Notes
from harmonizer.consts import TUNING_FILE, USER_TUNE_FILE
from harmonizer.utils.filesys import load_json


@dataclass
class GuitarTune:
    id: str
    name: str
    notes: tuple[str, ...]

    def __post_init__(self):
        self.notes = tuple(Notes.get_name(n) for n in self.notes)

    def first(self):
        """Нота на первой струне"""
        return self.notes[0]

    def last(self):
        """Нота на последней струне"""
        return self.notes[-1]


class Tuning(metaclass=Singleton):

    __tunings: dict[str, GuitarTune] = {}

    def __init__(self):
        self.__fill(load_json(TUNING_FILE))
        self.__fill(load_json(USER_TUNE_FILE))

    def first(self) -> str:
        """Первый набор гитарной настройки"""
        return list(self.__tunings.keys())[0]

    def last(self) -> str:
        """Последний набор гитарной настройки"""
        return list(self.__tunings.keys())[-1]

    def update(self) -> None:
        """Обновляет список настроек"""
        self.__fill(load_json(USER_TUNE_FILE))

    def all(self) -> list[GuitarTune]:
        """Возвращает все доступные настройки"""
        return list(self.__tunings.values())

    def get(self, tune: str) -> GuitarTune:
        """
        Возвращает гитарную настройку

        :param tune: Идентификатор настройки
        :return: Настройка
        """
        return self.__tunings.get(tune)

    def __fill(self, data: dict):
        for tid, tune in data.items():
            if tid not in self.__tunings:
                self.__tunings[tid] = GuitarTune(**tune)
