import flet as ft

from harmonizer.core.app import BaseApp
from harmonizer.gui.tune import UINewTune
from harmonizer.consts import NEW_TUNE_WINDOW_SIZE


class NewTune(BaseApp):
    window_size = NEW_TUNE_WINDOW_SIZE

    newtune: UINewTune

    def init(self):
        self.newtune = UINewTune(self.page)
        self.page.add(self.newtune)
        self.page.update()


if __name__ == "__main__":
    ft.app(NewTune)
