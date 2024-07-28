import flet as ft


class Menu(ft.Row):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.controls = [
            ft.WindowDragArea(
                ft.MenuBar(
                    expand=True,
                    style=ft.MenuStyle(
                        alignment=ft.alignment.top_left,
                        bgcolor=ft.colors.LIGHT_BLUE_100,
                    ),
                    controls=[
                        ft.Row([
                            ft.Row([
                                ft.SubmenuButton(
                                    ft.Text("File"),
                                    [
                                        ft.MenuItemButton(
                                            ft.Text("Will be later...")
                                        )
                                    ],
                                    width=40
                                ),
                                ft.SubmenuButton(
                                    ft.Text("Tools"),
                                    [
                                        ft.MenuItemButton(
                                            ft.Text("Quint circle")
                                        )
                                    ],
                                    width=50
                                )
                            ]),
                            ft.Row([
                                ft.IconButton(ft.icons.CLOSE, on_click=lambda _: page.window.close())
                            ]),
                        ],
                            width=780,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            expand=True,
                        )
                    ]
                ),
                expand=True
            ),
        ]
