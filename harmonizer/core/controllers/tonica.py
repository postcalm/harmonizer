import flet as ft

from harmonizer.core.controllers import BaseController
from harmonizer.core.views.tonica import TonicaViewer


class TonicaController(BaseController):
    """Контроллер тоники"""

    def __init__(self, page: ft.Page):
        self.viewer = TonicaViewer(page)
