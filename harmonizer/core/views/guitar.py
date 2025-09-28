import flet as ft

from harmonizer.core.gui.note import Note
from harmonizer.core.models.matrix import StringMatrix
from harmonizer.core.session import Session
from harmonizer.core.size import FrameSize
from harmonizer.core.models.harmony import Harmony
from harmonizer.core.models.tuning import Tuning
from harmonizer.core.types.enums.notes import Notes
from harmonizer.core.views import InstrumentViewer


class GuitarViewer(InstrumentViewer):
    """Класс для отрисовки гитарного грифа"""

    pad = ft.padding.all(20)

    note_size: FrameSize = FrameSize(37, 37)

    open_strings: ft.Column
    neck: ft.Column

    _matrix: StringMatrix

    def init(self) -> None:
        Session().harmony = Harmony()
        tune = Session().tune or Tuning().first()
        self._matrix = StringMatrix(tune)
        self.open_strings = self._open_strings()
        self.neck = self._tune_string()

        self.set_content(
            ft.Row,
            [
                self.open_strings,
                ft.VerticalDivider(width=15, color=ft.colors.BLACK),
                self.neck,
            ],
            height=270,
        )

    def draw(self) -> None:
        Session().harmony = Harmony()
        self._matrix = StringMatrix(Session().tune or Tuning().first())
        self.open_strings.controls.clear()
        self.open_strings.controls.append(self._open_strings())
        self.neck.controls.clear()
        self.neck.controls.append(self._tune_string())
        self.open_strings.update()
        self.neck.update()

    def _strings(self):
        strings = []
        for line in self._matrix:
            stack = ft.Stack([
                ft.Divider(height=self.note_size.height, color=ft.colors.BLACK),
                ft.Row(
                    [Note(n, self.note_size) for n in line[1:]],
                    spacing=20,
                ),
            ],
                width=660,
            )
            strings.append(stack)
        return strings

    def _open_strings(self) -> ft.Column:
        open_string = self._matrix.get_transposed()[0]
        return ft.Column([
            Note(n, self.note_size) for n in open_string
        ])

    def _tune_string(self) -> ft.Column:
        return ft.Column(self._strings(), spacing=10)
