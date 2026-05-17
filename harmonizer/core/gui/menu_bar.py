import os
from typing import Callable

import flet as ft

from harmonizer.core import Session
from harmonizer.core.controllers.control import ControlController
from harmonizer.core.gui.menu import BaseMenu
from harmonizer.utils.app import get_app_path, use_so_lib


class Menu(BaseMenu):

    files_submenu: ft.SubmenuButton
    instrument_submenu: ft.SubmenuButton
    tools_submenu: ft.SubmenuButton

    def init(self):
        self.files_submenu = ft.SubmenuButton(ft.Text("File"), width=40)
        self.instrument_submenu = ft.SubmenuButton(ft.Text("Instrument"), width=80)
        self.tools_submenu = ft.SubmenuButton(ft.Text("Tools"), width=50)

        self.add_submenu_item(self.files_submenu, "Add new tuning", self._add_new_tune)
        self.add_submenu_item(self.instrument_submenu, "6-string", self._swap_6_string)
        self.add_submenu_item(self.instrument_submenu, "7-string", self._swap_7_string)
        self.add_submenu_item(self.tools_submenu, "Circle of fifths", self._open_qqc)

        self.add_menu_items([
            self.files_submenu,
            self.instrument_submenu,
            self.tools_submenu,
        ])

    def _open_qqc(self, _):
        use_so_lib("qqc")
        os.system(f"start {get_app_path() / 'qqc.exe'}")

    def _add_new_tune(self, _):
        use_so_lib("tune")
        os.system(f"start {get_app_path() / 'tune.exe'}")

    def _swap_6_string(self, _):
        Session().instrument = "six_string"
        ControlController().get("tune").run()
        ControlController().get("instrument").run()

    def _swap_7_string(self, _):
        Session().instrument = "seven_string"
        ControlController().get("tune").run()
        ControlController().get("instrument").run()
