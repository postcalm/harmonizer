import flet as ft

from harmonizer.core.controllers.control import ControlController
from harmonizer.core.session import Session
from harmonizer.core.size import FrameSize
from harmonizer.core.types.dataclasses.tonality import Tonality
from harmonizer.core.views import SettingsViewer


class TonalityViewer(SettingsViewer):
    """Класс для отрисовки тональности"""

    size = FrameSize(width=250)

    def init(self) -> None:
        self.set_content(
            ft.Dropdown,
            self._ton_list(),
            label="Tonality",
            value=Tonality.aslist()[0],
            on_change=self._chosen_type,
        )

    def _chosen_type(self, e: ft.ControlEvent):
        Session().tonality = e.data
        ControlController().get("instrument").run()

    def _ton_list(self):
        return [
            ft.dropdown.Option(ton, ton.replace("_", " ")) for ton in Tonality.aslist()
        ]
