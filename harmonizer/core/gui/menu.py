import flet as ft


class BaseMenu(ft.Row):

    def __init__(self, width: int, page: ft.Page = None):
        super().__init__()
        self.menu_items = ft.Row([])
        self.buttons = ft.Row([
            self.btn_close,
        ])
        drag_area = ft.WindowDragArea(
            ft.MenuBar(
                expand=True,
                style=ft.MenuStyle(
                    alignment=ft.alignment.top_left,
                    bgcolor=ft.colors.LIGHT_BLUE_100,
                ),
                controls=[
                    ft.Row([
                        self.menu_items,
                        self.buttons,
                    ],
                        expand=True,
                        width=width,
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    )
                ]
            ),
            expand=True
        )
        self.controls = [drag_area]

        self.init()

    def init(self) -> None:
        pass

    def add_menu_items(self, items: list[ft.Control]) -> None:
        self.menu_items.controls = items

    @property
    def btn_close(self):
        return ft.IconButton(
            ft.icons.CLOSE,
            on_click=lambda _: self.page.window.close()
        )
