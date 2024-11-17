from enum import Enum

from harmonizer.core.gui.note import get_harmony
from harmonizer.core.models.tuning import Tuning
from harmonizer.core.session import Session


class ChordTypes(Enum):
    """
    Типы аккордов
    """
    TRIAD = (1, 3, 5)
    POWER = (1, 5)
    SUS2 = (1, 2, 5)
    SUS4 = (1, 4, 5)
    SEPTACORD = (1, 3, 5, 7)


class Chord:
    """
    Модель аккорда
    """

    harmony: list[str]

    def __init__(self):
        self.harmony = list(Session().harmony.keys())

    @property
    def triad(self) -> list[str]:
        return self._get_chord(ChordTypes.TRIAD)

    @property
    def sus2(self) -> list[str]:
        return self._get_chord(ChordTypes.SUS2)

    @property
    def sus4(self) -> list[str]:
        return self._get_chord(ChordTypes.SUS4)

    @property
    def power(self) -> list[str]:
        return self._get_chord(ChordTypes.POWER)

    @property
    def septacord(self) -> list[str]:
        return self._get_chord(ChordTypes.SEPTACORD)

    def _get_chord(self, chord_type: ChordTypes) -> list[str]:
        return [self.harmony[n - 1] for n in chord_type.value]
