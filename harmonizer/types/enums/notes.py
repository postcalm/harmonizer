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
    def get_value(cls, name: str) -> str:
        return cls._Notes[name].value

    def __class_getitem__(cls, item) -> str:
        return cls._Notes(item).name
