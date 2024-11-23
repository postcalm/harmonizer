from harmonizer import core
from harmonizer.core.models.tonality import Tonalities
from harmonizer.core.models.tuning import Tuning
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
                core.session.Session().tune or
                Tuning().first()
        )
        self.tonality = (
                tonality or
                core.session.Session().tonality or
                Tonalities().first()
        )
        self.tonica = (
                tonica or
                core.session.Session().tonica or
                Notes.get_pretty(Tuning().get(self.tune).last())
        )

        tonality = Tonalities().get(self.tonality)
        notes = Notes.get(self.tonica)
        notes = [notes[t] for t in tonality.sequence]
        self._harmony = {}
        for n, c, t in zip(notes, tonality.colored, tonality.tone):
            self._harmony[n] = {"color": c, "tone": t}

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
        return str(self._harmony.get(note).get("color").value)

    def get_tone(self, note: str) -> str:
        """
        Возвращает тон (настроение) ноты

        :param note: Нота
        :return: Тон
        """
        return str(self._harmony.get(note).get("tone").value)
