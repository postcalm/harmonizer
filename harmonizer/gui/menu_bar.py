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
                                self.files_part,
                                self.tools_part,
                            ]),
                            ft.Row([
                                self.btn_close,
                            ]),
                        ],
                            width=780,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        )
                    ]
                ),
                expand=True
            ),
        ]

    @property
    def files_part(self):
        return ft.SubmenuButton(
            ft.Text("File"),
            [
                ft.MenuItemButton(
                    ft.Text("Will be later...")
                )
            ],
            width=40
        )

    @property
    def tools_part(self):
        return ft.SubmenuButton(
            ft.Text("Tools"),
            [
                ft.MenuItemButton(
                    ft.Text("Circle of fifths"),
                )
            ],
            width=50
        )

    @property
    def btn_close(self):
        return ft.IconButton(ft.icons.CLOSE, on_click=lambda _: self.page.window.close())
