import flet as ft

from harmonizer.gui.tuning import UITuning
from harmonizer.gui.guitar_neck import UIGuitarNeck
from harmonizer.gui.tonality import UITonality


class UIHomepage(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/"
        self.padding = 20

        self.tuning = UITuning(page)
        self.guitar_neck = UIGuitarNeck(page)
        self.tonality = UITonality(page)

        self.controls = [
            ft.Row([self.tuning, self.tonality]),
            self.guitar_neck,
        ]
