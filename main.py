import flet as ft

from harmonizer.gui.homepage import UIHomepage


class Harmonizer:

    def __init__(self, page: ft.Page):
        self.page = page
        page.window.center()
        page.title = "Harmonizer"

        self._resize(None)

        self.homepage = UIHomepage(page)

        page.on_route_change = self.route_change
        page.go(page.route)

        page.window.on_event = self._resize

    def route_change(self, _):
        self.page.views.clear()
        self.page.views.append(self.homepage)
        self.page.update()

    def _resize(self, _):
        self.page.window.max_width = \
            self.page.window.min_width = \
            self.page.window.width = 800
        self.page.window.max_height = \
            self.page.window.min_height = \
            self.page.window.height = 470


ft.app(Harmonizer)
