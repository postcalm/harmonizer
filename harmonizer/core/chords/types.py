from enum import Enum

from harmonizer.core.models.interval import Interval


class ChordTypes(Enum):
    """
    Типы аккордов
    """
    MAJ_TRIAD = (
        Interval.C_PRIMA,
        Interval.M_TERTIA,
        Interval.S_TERTIA,
    )
    MIN_TRIAD = (
        Interval.C_PRIMA,
        Interval.S_TERTIA,
        Interval.M_TERTIA,
    )
    POWER = (
        Interval.C_PRIMA,
        Interval.C_QUINTA,
    )
    SUS2 = (
        Interval.C_PRIMA,
        Interval.M_SECUNDA,
        Interval.C_QUARTA,
    )
    SUS4 = (
        Interval.C_PRIMA,
        Interval.C_QUARTA,
        Interval.M_SECUNDA,
    )
    MAJ_SEPT = (
        Interval.C_PRIMA,
        Interval.M_TERTIA,
        Interval.S_TERTIA,
        Interval.M_TERTIA,
    )
    MIN_SEPT = (
        Interval.C_PRIMA,
        Interval.S_TERTIA,
        Interval.M_TERTIA,
        Interval.S_TERTIA,
    )
