import flet as ft

from harmonizer.gui.tuning import UITuning
from harmonizer.gui.guitar_neck import UIGuitarNeck


class UIHomepage(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/"
        self.padding = 20

        self.tuning = UITuning(page)
        self.guitar_neck = UIGuitarNeck(page)

        self.controls = [
            self.tuning,
            self.guitar_neck,
        ]
