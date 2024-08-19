import flet as ft

from harmonizer.win_size import WindowSize


class BaseMenu(ft.Row):

    def __init__(self, size: WindowSize, page: ft.Page = None):
        super().__init__()
        self.page = page
        self.spacing = 0
        self.height = 40
        self.width = size.width
        # ширина каждой строки равна половине ширины окна - 5 пикселей для погрешности
        self.menu_items = ft.Row(
            [],
            width=size.width // 2 - 5,
            spacing=0,
            alignment=ft.MainAxisAlignment.START
        )
        self.buttons = ft.Row(
            [
                self.btn_close,
            ],
            width=size.width // 2 - 5,
            spacing=0,
            alignment=ft.MainAxisAlignment.END
        )
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
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    )
                ]
            ),
            expand=True,
            maximizable=False,
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
