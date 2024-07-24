import flet as ft

from harmonizer.types.dataclasses.tonality import Tonality
from harmonizer.types.dataclasses.tuning import Tuning
from harmonizer.types.enums.notes import Notes
from harmonizer.types.enums.chords import Functions


class UIGuitarNeck(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.padding = ft.Padding(0, 20, 0, 0)

        self.open_strings = self._draw_open_string()
        self.neck = self._draw_tune_string()

        self.content = ft.Row([
            self.open_strings,
            ft.VerticalDivider(width=15, color=ft.colors.BLACK),
            self.neck,
        ],
            height=270,
        )

    def strings(self) -> list:
        strings = []
        tune = self.page.client_storage.get("tune") or Tuning.aslist()[0]
        for n in Tuning.asdict().get(tune):
            notes = Notes.get(n)[1:] + [Notes.get(n)[0]]
            stack = ft.Stack([
                ft.Divider(height=37, color=ft.colors.BLACK),
                ft.Row(
                    [self._note(n) for n in notes],
                    spacing=20,
                ),
            ],
                width=660,
            )
            strings.append(stack)
        return strings

    def _note(self, n):
        note = ft.Container(
            ft.Text(n, size=24),
            alignment=ft.alignment.center,
            width=37,
            height=37,
            bgcolor=ft.colors.GREY_300,
            shape=ft.BoxShape.CIRCLE,
            shadow=ft.BoxShadow(
                blur_radius=5,
                color=ft.colors.BLACK,
                offset=ft.Offset(4, -3),
                blur_style=ft.ShadowBlurStyle.NORMAL,
            )
        )
        self.paint_note(note)
        return note

    def draw_tune(self):
        self.open_strings.controls.clear()
        self.open_strings.controls.append(self._draw_open_string())
        self.neck.controls.clear()
        self.neck.controls.append(self._draw_tune_string())
        self.open_strings.update()
        self.neck.update()

    def _draw_open_string(self):
        tune = self.page.client_storage.get("tune") or Tuning.aslist()[0]
        return ft.Column([
            self._note(n) for n in Tuning.asdict().get(tune)
        ])

    def _draw_tune_string(self):
        return ft.Column(self.strings(), spacing=10)

    def paint_note(self, note: ft.Container):
        tune = self.page.client_storage.get("tune") or Tuning.aslist()[0]
        tonality = self.page.client_storage.get("tonality") or Tonality.aslist()[0]
        tonica = self.page.client_storage.get("tonica") or Tuning.asdict().get(tune)[-1]
        tonality = Tonality.asdict().get(tonality)
        notes = Notes.get(tonica)
        notes = [notes[t] for t in tonality]
        if note.content.value in notes:
            note.bgcolor = Functions.TONIC
