import flet as ft

from harmonizer.core.size import FrameSize


class BaseApp:
    """Базовый класс для создания окна приложения"""

    window_size: FrameSize

    def __init__(self, page: ft.Page):
        self.page = page
        page.window.center()
        page.window.frameless = True
        page.window.shadow = True
        page.window.resizable = False

        page.window.title_bar_hidden = True
        page.window.title_bar_buttons_hidden = True

        self._resize(None)
        page.window.on_resized = self._resize

        self.init()

    def init(self):
        pass

    def _resize(self, _):
        self.page.window.width = \
            self.page.window.min_width = \
            self.page.window.max_width = self.window_size.width
        self.page.window.height = \
            self.page.window.min_height = \
            self.page.window.max_height = self.window_size.height
