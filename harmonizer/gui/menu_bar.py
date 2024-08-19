import os

import flet as ft

from harmonizer.core.gui.menu import BaseMenu
from harmonizer.utils.app import get_app_path, use_so_lib


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
                    ft.Text("Add new tuning"),
                    on_click=self.add_new_tune
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
        use_so_lib("qqc")
        os.system(f"start {get_app_path() / 'qqc.exe'}")

    def add_new_tune(self, _):
        use_so_lib("tune")
        os.system(f"start {get_app_path() / 'tune.exe'}")

