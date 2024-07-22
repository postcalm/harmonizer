from harmonizer.notes import Notes


class _tuning:  # noqa
    @classmethod
    def aslist(cls):
        return [k for k in cls.__dict__ if not k.startswith("__")]

    @classmethod
    def name(cls):
        return cls.__name__


class Standard(_tuning):
    E = (
        Notes.E,
        Notes.B,
        Notes.G,
        Notes.D,
        Notes.A,
        Notes.E,
    )


class Midwest(_tuning):
    FACGCE = (
        Notes.E,
        Notes.C,
        Notes.G,
        Notes.C,
        Notes.A,
        Notes.F,
    )


ALL_TUNE = {
    "Standard": Standard,
    "Midwest": Midwest,
}
