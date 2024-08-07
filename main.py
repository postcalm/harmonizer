import sys
import multiprocessing

import flet as ft

from harmonizer.gui.homepage import UIHomepage


class Harmonizer:

    def __init__(self, page: ft.Page):
        self.page = page
        page.window.center()
        page.title = "Harmonizer"
        page.window.frameless = True
        page.window.shadow = True
        page.window.resizable = False

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
        self.page.window.width = \
            self.page.window.min_width = \
            self.page.window.max_width = 800
        self.page.window.height = \
            self.page.window.min_height = \
            self.page.window.max_height = 470


if __name__ == "__main__":
    # print(getattr(sys, "frozen", False))
    # https://stackforgeeks.com/blog/pyinstallerbuilt-windows-exe-fails-with-multiprocessing-duplicate
    # https://stackoverflow.com/questions/7067787/python-multiprocessing-processes-become-copies-of-the-main-process-when-run-fr
    # https://pyinstaller.org/en/stable/runtime-information.html
    print(sys.executable)
    multiprocessing.set_executable(sys.executable)
    setattr(sys, "frozen", True)
    multiprocessing.freeze_support()
    ft.app(Harmonizer)
