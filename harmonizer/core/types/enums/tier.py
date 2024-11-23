from enum import IntEnum, Enum, auto

import flet as ft


class Functions(str, Enum):
    TONIC = ft.colors.GREEN_400
    SUBDOMINANT = ft.colors.YELLOW_400
    DOMINANT = ft.colors.PINK_400


class Tone(str, Enum):
    """
    Окрас ноты
    """
    MAJOR = "major"
    MINOR = "minor"
    DIM = "dim"


class ColorTriplet(str, Enum):
    MAJOR = ft.colors.PINK_400
    MINOR = ft.colors.LIGHT_BLUE_400
    DIM = ft.colors.LIGHT_GREEN_400


class Tier(IntEnum):
    PRIMA = auto()
    SECOND = auto()
    TERTIA = auto()
    QUART = auto()
    QUINT = auto()
    SEXTA = auto()
    SEPTIMA = auto()
    # OCTAVE = auto()
