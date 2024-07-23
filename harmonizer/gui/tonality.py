import flet as ft

from harmonizer.gui.guitar_neck import UIGuitarNeck
from harmonizer.types.dataclasses.tonality import Tonality
from harmonizer.utils.gui import get_flet_control


class UITonality(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.width = 250

        self.tonality = ft.Dropdown(
            label="Tonality",
            options=self._ton_list(),
            value=Tonality.aslist()[0],
            on_change=self._chosen_type,
        )

        self.content = self.tonality

    def _chosen_type(self, e: ft.ControlEvent):
        self.page.client_storage.set("tonality", e.data)
        neck: UIGuitarNeck = get_flet_control(self, "UIGuitarNeck")
        # neck.draw_tune()

    def _ton_list(self):
        return [
            ft.dropdown.Option(ton, ton.replace("_", " ")) for ton in Tonality.aslist()
        ]
