import flet as ft

from harmonizer.tuning import Tuning
from harmonizer.notes import Notes


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
        # TODO: select through ui
        tune = self.page.client_storage.get("tune") or Tuning.aslist()[0]
        for n in Tuning.asdict().get(tune):
            stack = ft.Stack([
                ft.Divider(height=37, color=ft.colors.BLACK),
                ft.Row(
                    [self._note(n) for n in Notes.get(n)[1:]],
                    spacing=20,
                ),
            ],
                width=600,
            )
            strings.append(stack)
        return strings

    def _note(self, n):
        return ft.Container(
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
