import flet as ft

from harmonizer.tuning import Standard
from harmonizer.notes import Notes


class UIGuitarNeck(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.padding = ft.Padding(0, 20, 0, 0)

        # TODO: select through ui
        self.open_strings = ft.Column([
            self._note(n) for n in Standard.E
        ])

        self.content = ft.Row([
            self.open_strings,
            ft.VerticalDivider(width=15, color=ft.colors.BLACK),
            ft.Column(self.strings(), spacing=10)
        ],
            height=270,
        )

    def strings(self) -> list:
        strings = []
        # TODO: select through ui
        for n in Standard.E:
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
