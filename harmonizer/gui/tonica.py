import flet as ft

from harmonizer.types.enums.notes import Notes
from harmonizer.gui.guitar_neck import UIGuitarNeck
from harmonizer.utils.gui import get_flet_control


class UITonica(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.width = 150

        self.notes = ft.Dropdown(
            label="Tonica",
            options=self._notes_list(),
            value=Notes["E"],  # noqa
            on_change=self._chosen_type
        )

        self.content = self.notes

    def _chosen_type(self, e: ft.ControlEvent):
        self.page.client_storage.set("tonica", e.data)
        neck: UIGuitarNeck = get_flet_control(self, "UIGuitarNeck")
        neck.draw_tune()

    def _notes_list(self):
        return [
            ft.dropdown.Option(note) for note in Notes.get("A")
        ]
