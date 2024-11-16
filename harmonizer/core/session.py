from harmonizer.core import Singleton


class Session(metaclass=Singleton):
    """Модель текущей сессии"""

    # Настройка/дроп
    tune: str = None
    # Тональность
    tonality: str = None
    # Тоника
    tonica: str = None

    def __repr__(self):
        return repr(self.__dict__.items())
