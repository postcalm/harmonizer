import flet as ft

from harmonizer.core.controllers import BaseController
from harmonizer.core.views.guitar import GuitarViewer


class GuitarController(BaseController):
    """Контроллер гитарного строя"""

    def __init__(self, page: ft.Page):
        self.viewer = GuitarViewer(page)
