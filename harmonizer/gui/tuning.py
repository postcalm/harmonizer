import flet as ft

from harmonizer.tuning import Tuning
from harmonizer.gui.guitar_neck import UIGuitarNeck


class UITuning(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.homepage = self.page.views[0]
        self.width = 400

        self.tune = ft.Dropdown(
            label="Guitar tune",
            options=self._tune_list(),
            value=Tuning.aslist()[0],
            on_change=self._chosen_type,
        )

        self.content = ft.Column([
            self.tune,
        ])

    def _chosen_type(self, e: ft.ControlEvent):
        self.page.client_storage.set("tune", e.data)
        neck: UIGuitarNeck = self.parent.controls[1]
        neck.draw_tune()

    def _tune_list(self):
        return [
            ft.dropdown.Option(tune, tune.replace("_", " ")) for tune in Tuning.aslist()
        ]
