import json

import flet as ft

from harmonizer.core.gui.menu import BaseMenu
from harmonizer.core.gui.alert import OkAlert
from harmonizer.consts import NEW_TUNE_WINDOW_SIZE, USER_TUNE_FILE, STORAGE_DIR
from harmonizer.core.types.enums.notes import Notes


class UINewTune(ft.Container):
    number_strings = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth"
    ]

    def __init__(self, page: ft.Page):
        super().__init__()
        STORAGE_DIR.mkdir(exist_ok=True)
        page.padding = 0
        self.expand = True
        self.error_alert = OkAlert("Oops...", "Please, fill in all fields.")
        self.success_alert = OkAlert("Yeah", "Tuning added successfully!")

        page.overlay.extend([self.error_alert, self.success_alert])

        self.menu = BaseMenu(NEW_TUNE_WINDOW_SIZE)
        self.tune = ft.TextField(
            label="New guitar tuning",
            hint_text="Please enter your guitar tuning here"
        )
        self.strings = ft.Container(
            ft.ResponsiveRow(
                controls=[self._string(num) for num in self.number_strings],
                vertical_alignment=ft.CrossAxisAlignment.STRETCH
            ),
            expand=True,
        )
        self.footer = ft.Row(
            [
                self.btn_save,
                self.btn_cancel,
            ],
            alignment=ft.MainAxisAlignment.END,
        )

        self.content = ft.Column(
            [
                self.menu,
                ft.Container(ft.Column(
                    [
                        self.tune,
                        ft.Divider(),
                        self.strings,
                        ft.Divider(),
                        self.footer,
                    ]
                ),
                    padding=ft.padding.all(10),
                    expand=True
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

    def _notes_list(self):
        return [
            ft.dropdown.Option(note) for note in Notes.get("A")
        ]

    def _string(self, number: str):
        return ft.Dropdown(
            label=f"{number} string".capitalize(),
            hint_text="Choose note",
            options=self._notes_list(),
            col=6,
        )

    @property
    def btn_save(self):
        return ft.ElevatedButton(
            "Save",
            on_click=self.save
        )

    @property
    def btn_cancel(self):
        return ft.ElevatedButton(
            "Cancel",
            on_click=lambda _: self.page.window.close()
        )

    def save(self, e: ft.ControlEvent):
        strings = self.strings.content.controls
        notes = [string.value for string in strings]
        tune = self.tune.value.replace(" ", "_")
        if not tune or not all(notes):
            self.error_alert.open = True
            e.control.page.update()
            return
        data = {}
        if USER_TUNE_FILE.exists():
            data = json.load(USER_TUNE_FILE.open())
        data.update({tune: notes})
        json.dump(data, USER_TUNE_FILE.open("w"), indent=2)
        self.success_alert.open = True
        e.control.page.update()
