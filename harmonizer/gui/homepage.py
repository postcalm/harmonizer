import flet as ft

from harmonizer.gui.tuning import UITuning
from harmonizer.gui.guitar_neck import UIGuitarNeck
from harmonizer.gui.tonality import UITonality
from harmonizer.gui.tonica import UITonica


class UIHomepage(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/"
        self.padding = 20
        page.client_storage.clear()

        self.tuning = UITuning(page)
        self.guitar_neck = UIGuitarNeck(page)
        self.tonality = UITonality(page)
        self.tonica = UITonica(page)

        self.controls = [
            ft.Row([self.tuning, self.tonality, self.tonica]),
            self.guitar_neck,
        ]
