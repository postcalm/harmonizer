import flet as ft

from harmonizer.gui.tuning import UITuning
from harmonizer.gui.guitar_neck import UIGuitarNeck
from harmonizer.gui.tonality import UITonality
from harmonizer.gui.tonica import UITonica
from harmonizer.gui.menu_bar import Menu
from harmonizer.consts import MAIN_WINDOW_SIZE


class UIHomepage(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/"
        self.padding = 0
        page.client_storage.clear()

        self.menu = Menu(MAIN_WINDOW_SIZE, page)
        self.tuning = UITuning(page)
        self.guitar_neck = UIGuitarNeck(page)
        self.tonality = UITonality(page)
        self.tonica = UITonica(page)

        self.controls = [
            self.menu,
            ft.Container(
                ft.Row([self.tuning, self.tonality, self.tonica]),
                padding=ft.Padding(20, 10, 20, 0)
            ),
            self.guitar_neck,
        ]
