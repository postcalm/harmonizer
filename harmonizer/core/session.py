from harmonizer.core import Singleton
from harmonizer.core.types.enums.tier import Triplet


class Session(metaclass=Singleton):
    """Модель текущей сессии"""

    # Настройка/дроп
    tune: str = None
    # Тональность
    tonality: str = None
    # Тоника
    tonica: str = None
    # Текущая гармония
    harmony: dict[str, Triplet] = None

    def __repr__(self):
        return repr(self.__dict__.items())
