from enum import IntEnum, auto

import flet as ft


class Functions:
    TONIC = ft.colors.GREEN_400
    SUBDOMINANT = ft.colors.YELLOW_400
    DOMINANT = ft.colors.PINK_400


class Triplet:
    MAJOR = ft.colors.PINK_400
    MINOR = ft.colors.LIGHT_BLUE_400
    DIM = ft.colors.LIGHT_GREEN_400


# noinspection PyArgumentList
class Tier(IntEnum):
    PRIMA = auto()
    SECOND = auto()
    TERTIA = auto()
    QUART = auto()
    QUINT = auto()
    SEXTA = auto()
    SEPTIMA = auto()
    # OCTAVE = auto()
