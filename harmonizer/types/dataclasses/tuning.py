from harmonizer.types.enums.notes import Notes
from harmonizer.types.dataclasses import Dataclass


class Tuning(Dataclass):
    # standard
    Standard_E = (
        Notes.E,
        Notes.B,
        Notes.G,
        Notes.D,
        Notes.A,
        Notes.E,
    )

    # midwest
    FACGCE = (
        Notes.E,
        Notes.C,
        Notes.G,
        Notes.C,
        Notes.A,
        Notes.F,
    )

    # open
    Open_C = (
        Notes.E,
        Notes.C,
        Notes.G,
        Notes.C,
        Notes.G,
        Notes.C,
    )
