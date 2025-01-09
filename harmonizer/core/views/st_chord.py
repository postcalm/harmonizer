import flet as ft

from harmonizer.core import Session
from harmonizer.core.chords.model import Chord
from harmonizer.core.controllers.control import ControlController
from harmonizer.core.size import FrameSize
from harmonizer.core.views import SettingsViewer


class StageViewer(SettingsViewer):
    """"""

    size = FrameSize(width=100)

    def init(self) -> None:
        self.set_content(
            ft.Dropdown,
            self._stage_list(),
            label="Stage",
            on_change=self._chosen_stage,
        )

    def _chosen_stage(self, e: ft.ControlEvent):
        Session().stage = int(e.data)
        ControlController().get("instrument").run()

    def _stage_list(self):
        return [
            ft.dropdown.Option(str(s), str(s)) for s in range(1, 8)
        ]


class ChordViewer(SettingsViewer):
    """Класс для отрисовки выбора аккорда"""

    size = FrameSize()

    def init(self) -> None:
        self.set_content(
            ft.Dropdown,
            self._chords_list(),
            label="Chords",
            on_change=self._chosen_chord,
        )

    def _chosen_chord(self, e: ft.ControlEvent):
        Session().chord = e.data
        ControlController().get("instrument").run()

    def _chords_list(self):
        return [
            ft.dropdown.Option(c, c.capitalize()) for c in Chord.all()
        ]
