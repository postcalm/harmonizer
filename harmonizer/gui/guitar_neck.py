import flet as ft

from harmonizer.types.dataclasses.tonality import Tonality
from harmonizer.types.dataclasses.tuning import Tuning
from harmonizer.types.enums.notes import Notes


class UIGuitarNeck(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.padding = ft.padding.all(20)

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
            nn = Notes.get_value(n)
            notes = Notes.get(nn)[1:] + [Notes.get(nn)[0]]
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

    def draw_tune(self):
        self.open_strings.controls.clear()
        self.open_strings.controls.append(self._draw_open_string())
        self.neck.controls.clear()
        self.neck.controls.append(self._draw_tune_string())
        self.open_strings.update()
        self.neck.update()

    def paint_note(self, note: ft.Container):
        tune = self.page.client_storage.get("tune") or Tuning.aslist()[0]
        tonality = self.page.client_storage.get("tonality") or Tonality.aslist()[0]
        tonica = self.page.client_storage.get("tonica") or Notes.get_value(Tuning.asdict().get(tune)[-1])
        tonality, tier = Tonality.asdict().get(tonality)
        notes = Notes.get(tonica)
        notes = [notes[t] for t in tonality]
        notes = dict(zip(notes, tier))
        if note.content.value in notes.keys():
            note.bgcolor = notes.get(note.content.value)

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

    def _draw_open_string(self):
        tune = self.page.client_storage.get("tune") or Tuning.aslist()[0]
        return ft.Column([
            self._note(Notes.get_value(n)) for n in Tuning.asdict().get(tune)
        ])

    def _draw_tune_string(self):
        return ft.Column(self.strings(), spacing=10)
