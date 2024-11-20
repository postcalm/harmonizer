from harmonizer.core.models.tonality import Tonalities
from harmonizer.core.models.tuning import Tuning
from harmonizer.core.session import Session
from harmonizer.core.types.enums.notes import Notes


class Harmony:
    """
    Гармония (гамма)
    """

    tune: str
    tonica: str
    tonality: str

    def __init__(
            self,
            tune: str = None,
            tonica: str = None,
            tonality: str = None,
    ):
        """
        Возвращает гамму и цвета для раскраски.
        Если ни один аргумент не задан, то будет возвращена гамма для
        стандартного строя E в мажоре.

        :param tune: Гитарная настройка
        :param tonica: Тоника
        :param tonality: Тональность
        """
        self.tune = (
                tune or
                Session().tune or
                Tuning().first()
        )
        self.tonality = (
                tonality or
                Session().tonality or
                Tonalities().first()
        )
        self.tonica = (
                tonica or
                Session().tonica or
                Notes.get_pretty(Tuning().get(self.tune).last())
        )

        tonality = Tonalities().get(self.tonality)
        notes = Notes.get(self.tonica)
        notes = [notes[t] for t in tonality.sequence]
        self._harmony = dict(zip(notes, tonality.colored))

    @property
    def notes(self):
        """
        Список нот гаммы
        """
        return list(self._harmony.keys())

    def get_color(self, note: str) -> str:
        """
        Возвращает цвет ноты в UI

        :param note: Нота
        :return: Цвет ноты
        """
        return self._harmony.get(note).value
