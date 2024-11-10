import flet as ft

from harmonizer.core.controllers import BaseController
from harmonizer.core.views.tune import TuneViewer


class TuneController(BaseController):
    """Контроллер гитарного строя/дропа"""

    def __init__(self, page: ft.Page):
        self.viewer = TuneViewer(page)
