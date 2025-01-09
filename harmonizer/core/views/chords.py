import flet as ft

from harmonizer.core.controllers.st_chord import StageController, ChordController
from harmonizer.core.controllers.control import ControlController
from harmonizer.core.size import FrameSize
from harmonizer.core.views import BaseView


class ChordsViewer(BaseView):
    """"""

    size = FrameSize()
    pad = ft.Padding(20, 0, 0, 20)

    stage: StageController
    chord: ChordController

    def init(self) -> None:
        self.stage = StageController(self.page)
        self.chord = ChordController(self.page)

        ControlController().add("stage", self.stage)
        ControlController().add("chord", self.chord)
        self.set_content(
            ft.Row,
            [
                self.stage.viewer,
                self.chord.viewer,
            ],
        )
