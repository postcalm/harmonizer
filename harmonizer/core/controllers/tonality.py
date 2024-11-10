import flet as ft

from harmonizer.core.controllers import BaseController
from harmonizer.core.views.tonality import TonalityViewer


class TonalityController(BaseController):
    """Контроллер тональности"""

    def __init__(self, page: ft.Page):
        self.viewer = TonalityViewer(page)
