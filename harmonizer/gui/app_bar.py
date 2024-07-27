import flet as ft


class Menu(ft.Row):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.controls = [
            ft.WindowDragArea(
                ft.Container(
                    ft.Row([
                        ft.Text(""),
                        ft.IconButton(ft.icons.CLOSE, on_click=lambda _: page.window.close()),
                    ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    bgcolor=ft.colors.LIGHT_BLUE_100,
                    padding=ft.Padding(20, 0, 20, 0),
                ),
                expand=True
            ),
        ]
