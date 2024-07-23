from harmonizer.notes import Notes


class _tuning:  # noqa
    @classmethod
    def aslist(cls) -> list[str]:
        return [k for k in cls.__dict__ if not k.startswith("__")]

    @classmethod
    def asdict(cls) -> dict[str, tuple]:
        return {k: v for k, v in cls.__dict__.items() if not k.startswith("__")}

    @classmethod
    def get_name(cls, item: tuple) -> str:
        invert = {v: k for k, v in cls.__dict__.items()}
        name = invert.get(item, "")
        return name.replace("_", " ")


class Tuning(_tuning):
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
