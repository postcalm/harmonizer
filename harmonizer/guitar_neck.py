import flet as ft

from harmonizer.tuning import Standard
from harmonizer.notes import Notes


class GuitarNeck(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/"

        self.open_strings = ft.Column([
            ft.Container(
                ft.Text(n, size=24),
                alignment=ft.alignment.center,
                width=35,
                height=35,
                bgcolor=ft.colors.GREY_300,
                shape=ft.BoxShape.CIRCLE,
            ) for n in Standard.E
        ])

        self.controls.append(
            ft.Container(
                ft.Row([
                    self.open_strings,
                    ft.VerticalDivider(width=15, color=ft.colors.BLACK),
                    ft.Column(self.strings(), spacing=10)
                ],
                    height=270
                )
            )
        )

    def strings(self) -> list[ft.Row]:
        strings = []
        for n in Standard.E:
            strings.append(ft.Row(
                [
                    ft.Container(
                        ft.Text(n, size=24),
                        alignment=ft.alignment.center,
                        width=35,
                        height=35,
                        bgcolor=ft.colors.GREY_300,
                        shape=ft.BoxShape.CIRCLE,
                    )
                    for n in Notes.get(n)[1:]
                ],
                spacing=20,
            ))
        return strings
