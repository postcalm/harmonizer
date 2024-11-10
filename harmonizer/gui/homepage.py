import flet as ft

from harmonizer.core.controllers.control import ControlController
from harmonizer.core.controllers.guitar import GuitarController
from harmonizer.core.controllers.tonality import TonalityController
from harmonizer.core.controllers.tonica import TonicaController
from harmonizer.core.controllers.tune import TuneController
from harmonizer.core.gui.menu_bar import Menu
from harmonizer.consts import MAIN_WINDOW_SIZE


class Homepage(ft.View):
    """Домашняя страница"""

    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/"
        self.padding = 0

        control = ControlController()

        self.menu = Menu(MAIN_WINDOW_SIZE, page)
        self.tuning = TuneController(page)
        self.instrument = GuitarController(page)
        self.tonality = TonalityController(page)
        self.tonica = TonicaController(page)

        control.add("tune", self.tuning)
        control.add("tonica", self.tonica)
        control.add("tonality", self.tonality)
        control.add("instrument", self.instrument)

        self.controls = [
            self.menu,
            ft.Container(
                ft.Row([
                    self.tuning.viewer,
                    self.tonality.viewer,
                    self.tonica.viewer,
                ]),
                padding=ft.Padding(20, 10, 20, 0)
            ),
            self.instrument.viewer,
        ]
