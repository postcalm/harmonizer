from typing import Any

import flet as ft

from harmonizer.core.size import FrameSize


class BaseView(ft.Container):
    """Базовый класс отображения элементов управления"""

    pad: ft.Padding = None
    size: FrameSize = FrameSize()

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.padding = self.pad
        self.width = self.size.width
        self.height = self.size.height

        self.init()

    def init(self) -> None:
        """Инициализация элемента управления"""

    def set_content(
            self,
            layout: type[ft.Row | ft.Column],
            content: list[ft.Control],
            **kwargs: Any,
    ) -> None:
        """
        Задать содержимое элемента управления

        :param layout: Расположение элемента управления
        :param content: Содержимое элемента управления
        :param kwargs: Прочие аргументы layout
        :return: None
        """
        self.content = layout(content, **kwargs)

    def draw(self, *args, **kwargs) -> None:
        """Отрисовать элемент управления"""

    def hide(self, *args, **kwargs) -> None:
        """Скрыть элемент управления"""


class InstrumentViewer(BaseView):
    """Класс для отрисовки инструмента"""


class SettingsViewer(BaseView):
    """Класс для отрисовки элементов настройки"""

    def set_content(
            self,
            layout: type[ft.Dropdown],
            content: list[ft.dropdown.Option],
            **kwargs: Any,
    ) -> None:
        self.content = layout(options=content, **kwargs)
