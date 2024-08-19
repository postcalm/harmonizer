import flet as ft

from harmonizer.core.app import BaseApp
from harmonizer.gui.homepage import UIHomepage
from harmonizer.consts import MAIN_WINDOW_SIZE, USER_DIR


class Harmonizer(BaseApp):
    window_size = MAIN_WINDOW_SIZE

    homepage: UIHomepage

    def init(self):
        USER_DIR.mkdir(exist_ok=True)

        self.homepage = UIHomepage(self.page)

        self.page.on_route_change = self.route_change
        self.page.go(self.page.route)

    def route_change(self, _):
        self.page.views.clear()
        self.page.views.append(self.homepage)
        self.page.update()


if __name__ == "__main__":
    ft.app(Harmonizer)
