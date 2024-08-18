import os
from pathlib import Path

import flet as ft

from harmonizer.core.gui.menu import BaseMenu


class Menu(BaseMenu):

    def init(self):
        self.add_menu_items([
            self.files_part,
            self.tools_part,
        ])

    @property
    def files_part(self):
        return ft.SubmenuButton(
            ft.Text("File"),
            [
                ft.MenuItemButton(
                    ft.Text("Will be later...")
                )
            ],
            width=40
        )

    @property
    def tools_part(self):
        return ft.SubmenuButton(
            ft.Text("Tools"),
            [
                ft.MenuItemButton(
                    ft.Text("Circle of fifths"),
                    on_click=self.open_qqc
                )
            ],
            width=50
        )

    def open_qqc(self, _):
        here = Path.cwd() / "qqc.exe"
        os.system(here)
