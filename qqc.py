import flet as ft

from harmonizer.core.app import BaseApp
from harmonizer.consts import QQC_WINDOW_SIZE
from harmonizer.gui.qqc import UIQQC


class CircleFifths(BaseApp):
    window_size = QQC_WINDOW_SIZE

    qqc: UIQQC

    def init(self):
        self.qqc = UIQQC(self.page)
        self.page.add(self.qqc)
        self.page.update()


if __name__ == "__main__":
    ft.app(CircleFifths)
