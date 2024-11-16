import flet as ft

from harmonizer.core.controllers.control import ControlController
from harmonizer.core.session import Session
from harmonizer.core.size import FrameSize
from harmonizer.core.models.tuning import Tuning
from harmonizer.core.views import SettingsViewer


class TuneViewer(SettingsViewer):
    """Класс для отрисовки гитарного строя/дропа"""

    size = FrameSize(width=250)

    def init(self) -> None:
        self.set_content(
            ft.Dropdown,
            self._tune_list(),
            value=Tuning().first(),
            label="Guitar tune",
            on_change=self._chosen_type,
            on_click=self._update_tune,
        )

    def _chosen_type(self, e: ft.ControlEvent):
        Session().tune = e.data
        Session().tonica = Tuning().get(e.data).last()
        ControlController().get("instrument").run()
        ControlController().get("tonica").run()

    def _tune_list(self):
        tuning = Tuning().all()
        tuning.sort(key=lambda tune: tune.name)
        return [
            ft.dropdown.Option(tune.id, tune.name) for tune in tuning
        ]

    def _update_tune(self, _) -> None:
        Tuning().update()
        self.content.options = self._tune_list()
        self.content.update()
