from harmonizer.types.dataclasses import Dataclass
from harmonizer.types.enums.tier import Triplet


class Tonality(Dataclass):
    # tonica - ton - ton - half - ton - ton - ton - half
    Major = (
        (0, 2, 4, 5, 7, 9, 11),
        (
            Triplet.MAJOR,
            Triplet.MINOR,
            Triplet.MINOR,
            Triplet.MAJOR,
            Triplet.MAJOR,
            Triplet.MINOR,
            Triplet.DIM,
        ),
    )

    # tonica - ton - half - ton - ton - half - ton - ton
    Minor = (
        (0, 2, 3, 5, 7, 8, 10),
        (
            Triplet.MINOR,
            Triplet.DIM,
            Triplet.MAJOR,
            Triplet.MINOR,
            Triplet.MINOR,
            Triplet.MAJOR,
            Triplet.MAJOR,
        ),
    )
