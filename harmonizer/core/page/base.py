import flet as ft


class PageWizard(ft.Container):

    def __init__(self, root: ft.Page):
        super().__init__()
        self.root = root
