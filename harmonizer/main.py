import flet as ft

from harmonizer.gui.homepage import UIHomepage


class Harmonizer:

    def __init__(self, page: ft.Page):
        self.page = page
        # page.window.center()
        page.title = "Harmonizer"
        page.window.width = 750
        page.window.height = 470

        self.homepage = UIHomepage(page)

        page.on_route_change = self.route_change
        page.on_view_pop = self.view_pop
        page.go(page.route)

    def route_change(self, _):
        self.page.views.clear()
        self.page.views.append(self.homepage)
        self.page.update()

    def view_pop(self, _):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)


if __name__ == "__main__":
    ft.app(Harmonizer)
