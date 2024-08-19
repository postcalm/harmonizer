import flet as ft

from harmonizer.types.dataclasses.tuning import Tuning
from harmonizer.gui.guitar_neck import UIGuitarNeck
from harmonizer.utils.gui import get_flet_control


class UITuning(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.width = 250

        self.tune = ft.Dropdown(
            label="Guitar tune",
            options=self._tune_list(),
            value=Tuning.aslist()[0],
            on_change=self._chosen_type,
            on_click=self._update_tune
        )

        self.content = self.tune

    def _chosen_type(self, e: ft.ControlEvent):
        self.page.client_storage.set("tune", e.data)
        neck: UIGuitarNeck = get_flet_control(self, "UIGuitarNeck")
        neck.draw_tune()

    def _tune_list(self):
        return [
            ft.dropdown.Option(tune, tune.replace("_", " ")) for tune in Tuning.aslist()
        ]

    def _update_tune(self, _):
        Tuning.update()
        self.tune.options = self._tune_list()
        self.tune.update()
