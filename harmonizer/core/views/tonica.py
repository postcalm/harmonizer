import flet as ft

from harmonizer.core.controllers.control import ControlController
from harmonizer.core.session import Session
from harmonizer.core.size import FrameSize
from harmonizer.core.types.enums.notes import Notes
from harmonizer.core.views import SettingsViewer


class TonicaViewer(SettingsViewer):
    """Класс для отрисовки тоники"""

    size = FrameSize(width=150)

    def init(self) -> None:
        self.set_content(
            ft.Dropdown,
            self._notes_list(),
            label="Tonica",
            value=Notes.get_name("E"),
            on_change=self._chosen_type,
        )

    def _chosen_type(self, e: ft.ControlEvent):
        Session().tonica = e.data
        ControlController().get("instrument").run()

    def _notes_list(self):
        return [
            ft.dropdown.Option(note) for note in Notes.get("A")
        ]
