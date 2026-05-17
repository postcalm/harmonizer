from dataclasses import dataclass

import harmonizer.core.session
from harmonizer.core import Singleton
from harmonizer.core.types.enums.notes import Notes
from harmonizer.consts import TUNING_FILE, USER_TUNE_FILE
from harmonizer.utils.configs import convert_config_tune_to_new_style
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

    __tunings: dict[str, dict[str, GuitarTune]] = {}

    def __init__(self):
        convert_config_tune_to_new_style(USER_TUNE_FILE)
        self.__fill(load_json(TUNING_FILE))
        self.__fill(load_json(USER_TUNE_FILE))

    def first(self) -> str:
        """Первый набор гитарной настройки"""
        return list(self.__tunings.get(self.__inst).keys())[0]

    def last(self) -> str:
        """Последний набор гитарной настройки"""
        return list(self.__tunings.get(self.__inst).keys())[-1]

    def update(self) -> None:
        """Обновляет список настроек"""
        self.__fill(load_json(USER_TUNE_FILE))

    def all(self) -> list[GuitarTune]:
        """Возвращает все доступные настройки"""
        return list(self.__tunings.get(self.__inst).values())

    def get(self, tune: str) -> GuitarTune:
        """
        Возвращает гитарную настройку

        :param tune: Идентификатор настройки
        :return: Настройка
        """
        return self.__tunings.get(self.__inst).get(tune)

    def __fill(self, data: dict):
        for inst, tunes in data.items():
            self.__tunings[inst] = self.__tunings.get(inst, {})
            for tid, tune in tunes.items():
                if tid not in self.__tunings[inst]:
                    self.__tunings[inst].update({tid: GuitarTune(**tune)})

    @property
    def __inst(self):
        # обход цикличного импорта
        return harmonizer.core.session.Session().instrument
