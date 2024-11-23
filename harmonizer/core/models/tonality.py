from dataclasses import dataclass

from harmonizer.consts import TONALITY_CONFIG
from harmonizer.core import Singleton
from harmonizer.core.types.enums.tier import ColorTriplet, Tone
from harmonizer.utils.filesys import load_json


@dataclass
class Tonality:
    """
    Модель тональности
    """
    name: str
    sequence: list[int]
    colors: list[str]

    @property
    def colored(self) -> list[type[ColorTriplet]]:
        return [ColorTriplet[c.upper()] for c in self.colors]

    @property
    def tone(self) -> list[Tone]:
        return [Tone(c) for c in self.colors]


class Tonalities(metaclass=Singleton):
    """
    Тональности
    """

    __tonalities: dict[str, Tonality] = {}

    def __init__(self):
        for tid, ton in load_json(TONALITY_CONFIG).items():
            self.__tonalities[tid] = Tonality(**ton)

    def first(self) -> str:
        return self.ids()[0]

    def all(self) -> list[Tonality]:
        return list(self.__tonalities.values())

    def ids(self):
        return list(self.__tonalities.keys())

    def get(self, tonality: str) -> Tonality:
        return self.__tonalities.get(tonality)

    def __repr__(self):
        return repr(self.__tonalities)
