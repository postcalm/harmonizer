from itertools import cycle


class Notes:
    A: str = "A"
    Bflat: str = "Bb"
    B: str = "B"
    C: str = "C"
    Csharp: str = "C#"
    D: str = "D"
    Eflat: str = "Eb"
    E: str = "E"
    F: str = "F"
    Fsharp: str = "F#"
    G: str = "G"
    Gsharp: str = "G#"

    @classmethod
    def get(cls, note: str = None) -> list:
        note = note or cls.E  # standard E by default
        notes = cls.__annotations__.keys()
        notes = [cls.__dict__.get(n) for n in notes]
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

    def __class_getitem__(cls, item):
        return getattr(cls, item)
