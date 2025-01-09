import flet as ft

from harmonizer.core.controllers import BaseController
from harmonizer.core.views.chords import ChordsViewer


class ChordsController(BaseController):
    """Контроллер выбора аккорда"""

    def __init__(self, page: ft.Page):
        self.viewer = ChordsViewer(page)
