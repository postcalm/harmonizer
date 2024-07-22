import flet as ft

from harmonizer.tuning import ALL_TUNE, Standard


class UITuning(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.title = ft.Text("Guitar tune")
        self.width = 400
        self.group = ft.RadioGroup(
            ft.Row(self._type_list()),
            value=Standard.name().lower(),
            on_change=self._chosen_type,
        )

        self.tune = ft.Dropdown(
            options=self._tune_list(self._get_tune_type()),
            # on_change=self._chosen,
        )

        self.content = ft.Column([
            # self.title,
            self.group,
            self.tune,
        ])

    def _chosen_type(self, e: ft.ControlEvent):
        self.page.client_storage.set("tune", e.data)
        self.tune.options = self._tune_list(self._get_tune_type())
        self.tune.update()

    def _get_tune_type(self):
        tune = self.page.client_storage.get("tune") or Standard.name()
        return tune.title()

    def _type_list(self):
        return [
            ft.Radio(k, value=k.lower()) for k in ALL_TUNE
        ]

    def _tune_list(self, type_):
        return [
            ft.dropdown.Option(tune) for tune in ALL_TUNE.get(type_).aslist()
        ]
