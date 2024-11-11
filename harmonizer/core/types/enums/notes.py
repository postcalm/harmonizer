from itertools import cycle
from enum import Enum


class Notes:

    class _Notes(str, Enum):
        A = "A"
        Bflat = "Bb"
        B = "B"
        C = "C"
        Csharp = "C#"
        D = "D"
        Eflat = "Eb"
        E = "E"
        F = "F"
        Fsharp = "F#"
        G = "G"
        Gsharp = "G#"

    @classmethod
    def get(cls, note: str = None) -> list:
        """
        Возвращает последовательность нот от указанной ноты

        :param note: Нота, от которой строится последовательность
        """
        note = note or cls._Notes.E  # standard E by default
        notes = cls._Notes._member_names_
        notes = [cls._Notes[n].value for n in notes]
        mark = -1
        new = []
        for n in cycle(notes):
            if note == n:
                mark += 1
            if mark == 1:
                new.append(n)
            if mark == 2:
                break
        return new

    @classmethod
    def get_pretty(cls, name: str) -> str:
        """
        Возвращает интерпретированное имя ноты по фактическому имени

        :param name: Нота
        """
        return cls._Notes[name].value

    @classmethod
    def get_name(cls, name: str) -> str:
        """
        Возвращает фактическое имя ноты по интерпретированному имени

        :param name: Нота
        """
        return cls._Notes(name).name
