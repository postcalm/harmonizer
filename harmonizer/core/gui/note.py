import flet as ft

from harmonizer.core.session import Session
from harmonizer.core.size import FrameSize
from harmonizer.core.models.tonality import Tonalities
from harmonizer.core.models.tuning import Tuning
from harmonizer.core.types.enums.notes import Notes


class Note(ft.Container):
    """Нота"""

    def __init__(
            self,
            note: str,
            size: FrameSize,
            shape: ft.BoxShape = ft.BoxShape.CIRCLE,
    ):
        """
        :param note: Название ноты
        :param size: Размер ноты
        :param shape: Форма ноты
        """
        super().__init__()
        self.content = ft.Text(note, size=24)
        self.alignment = ft.alignment.center
        self.width = size.width
        self.height = size.height
        self.bgcolor = ft.colors.GREY_300
        self.shape = shape
        self.shadow = ft.BoxShadow(
            blur_radius=5,
            color=ft.colors.BLACK,
            offset=ft.Offset(4, -3),
            blur_style=ft.ShadowBlurStyle.NORMAL,
        )
        self.paint()

    def paint(self) -> None:
        tune = Session().tune or Tuning().first()
        tonality = Session().tonality or Tonalities().first()
        tonica = Session().tonica or Notes.get_pretty(Tuning().get(tune).last())
        tonality = Tonalities().get(tonality)
        notes = Notes.get(tonica)
        notes = [notes[t] for t in tonality.sequence]
        notes = dict(zip(notes, tonality.colored))
        if self.content.value in notes.keys():
            self.bgcolor = notes.get(self.content.value).value
