import flet as ft

from harmonizer.core.gui.note import Note
from harmonizer.core.session import Session
from harmonizer.core.size import FrameSize
from harmonizer.core.models.tuning import Tuning
from harmonizer.core.types.enums.notes import Notes
from harmonizer.core.views import InstrumentViewer


class GuitarViewer(InstrumentViewer):
    """Класс для отрисовки гитарного грифа"""

    pad = ft.padding.all(20)

    note_size: FrameSize = FrameSize(37, 37)

    open_strings: ft.Column
    neck: ft.Column

    def init(self) -> None:
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
        self.open_strings.controls.clear()
        self.open_strings.controls.append(self._open_strings())
        self.neck.controls.clear()
        self.neck.controls.append(self._tune_string())
        self.open_strings.update()
        self.neck.update()

    def _strings(self):
        strings = []
        tune = Session().tune or Tuning().first()
        for n in Tuning().get(tune).notes:
            nn = Notes.get_pretty(n)
            notes = Notes.get(nn)[1:] + [Notes.get(nn)[0]]
            stack = ft.Stack([
                ft.Divider(height=self.note_size.height, color=ft.colors.BLACK),
                ft.Row(
                    [Note(n, self.note_size) for n in notes],
                    spacing=20,
                ),
            ],
                width=660,
            )
            strings.append(stack)
        return strings

    def _open_strings(self) -> ft.Column:
        tune = Session().tune or Tuning().first()
        return ft.Column([
            Note(Notes.get_pretty(n), self.note_size) for n in Tuning().get(tune).notes
        ])

    def _tune_string(self) -> ft.Column:
        return ft.Column(self._strings(), spacing=10)
