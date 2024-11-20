import flet as ft

from harmonizer.core.session import Session
from harmonizer.core.size import FrameSize


class Note(ft.Container):
    """Нота"""

    content: ft.Text

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
        harmony = Session().harmony
        if self.content.value in harmony.notes:
            self.bgcolor = harmony.get_color(self.content.value)
