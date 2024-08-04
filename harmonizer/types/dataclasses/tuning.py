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

    Drop_D = (
        Notes.E,
        Notes.B,
        Notes.G,
        Notes.D,
        Notes.A,
        Notes.D,
    )

    Drop_C = (
        Notes.D,
        Notes.A,
        Notes.F,
        Notes.C,
        Notes.G,
        Notes.C,
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

    DAEACE = (
        Notes.E,
        Notes.C,
        Notes.A,
        Notes.E,
        Notes.A,
        Notes.D,
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
    Open_D = (
        Notes.D,
        Notes.A,
        Notes.G,
        Notes.D,
        Notes.A,
        Notes.D,
    )
