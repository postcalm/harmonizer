import flet as ft


class Alert(ft.AlertDialog):
    def __init__(self, title: str, content: str):
        super().__init__()
        self.modal = True
        self.title = ft.Text(title)
        self.content = ft.Text(content)
        self.actions_alignment = ft.MainAxisAlignment.END
        self.init_actions()

    def init_actions(self):
        pass


class OkAlert(Alert):

    def init_actions(self):
        self.actions = [
            ft.TextButton("Ok", on_click=self.close)
        ]

    def close(self, e: ft.ControlEvent):
        self.open = False
        e.control.page.update()
