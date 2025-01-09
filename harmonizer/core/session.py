from harmonizer.core import Singleton
from harmonizer.core.models.harmony import Harmony


class Session(metaclass=Singleton):
    """Модель текущей сессии"""

    # Настройка/дроп
    tune: str = None
    # Тональность
    tonality: str = None
    # Тоника
    tonica: str = None
    # Текущая гармония
    harmony: Harmony = None
    # Выбранная ступень гармонии
    stage: int = None
    # Выбранный аккорд
    chord: str = None

    def __repr__(self):
        return repr(self.__dict__.items())
