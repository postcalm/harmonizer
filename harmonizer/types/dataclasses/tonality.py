from harmonizer.types.dataclasses import Dataclass


class Tonality(Dataclass):

    # tonica - ton - ton - half - ton - ton - ton - half
    Major = (0, 2, 4, 5, 7, 9, 11)

    # tonica - ton - half - ton - ton - half - ton - ton
    Minor = (0, 2, 3, 5, 7, 8, 10)
