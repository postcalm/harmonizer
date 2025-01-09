import flet as ft

from harmonizer.core.controllers import BaseController
from harmonizer.core.views.st_chord import StageViewer, ChordViewer


class StageController(BaseController):
    """"""

    def __init__(self, page: ft.Page):
        self.viewer = StageViewer(page)


class ChordController(BaseController):
    """Контроллер выбора аккорда"""

    def __init__(self, page: ft.Page):
        self.viewer = ChordViewer(page)
