import json

from harmonizer.types.enums.notes import Notes
from harmonizer.types.dataclasses import Dataclass
from harmonizer.consts import TUNING_FILE, USER_TUNE_FILE


class _Tuning(Dataclass):
    # midwest
    # FACGCE = (
    #     Notes.E,
    #     Notes.C,
    #     Notes.G,
    #     Notes.C,
    #     Notes.A,
    #     Notes.F,
    # )
    #
    # DAEACE = (
    #     Notes.E,
    #     Notes.C,
    #     Notes.A,
    #     Notes.E,
    #     Notes.A,
    #     Notes.D,
    # )

    # open
    # Open_C = (
    #     Notes.E,
    #     Notes.C,
    #     Notes.G,
    #     Notes.C,
    #     Notes.G,
    #     Notes.C,
    # )
    # Open_D = (
    #     Notes.D,
    #     Notes.A,
    #     Notes.G,
    #     Notes.D,
    #     Notes.A,
    #     Notes.D,
    # )

    def __new__(cls, *args, **kwargs):
        for tune, notes in kwargs.items():
            setattr(cls, tune, tuple(Notes[note] for note in notes))
        cls.update()
        return super().__new__(cls)

    @classmethod
    def update(cls) -> None:
        data = {}
        if USER_TUNE_FILE.exists():
            data = json.load(USER_TUNE_FILE.open())
        for tune, notes in data.items():
            setattr(cls, tune, tuple(Notes[note] for note in notes))


Tuning = _Tuning(**json.load(TUNING_FILE.open()))
