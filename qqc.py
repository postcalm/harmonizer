import flet as ft

from harmonizer.core.gui.menu import BaseMenu

qqc = {
    "C": "Am",
    "G": "Em",
    "D": "Bm",
    "A": "F#m",
    "E": "C#m",
    "B": "G#m",
    "F#": "Ebm",
    "C#": "Bbm",
    "G#": "Fm",
    "Eb": "Cm",
    "Bb": "Gm",
    "F": "Dm",
}
invert_qqc = {v: k for k, v in qqc.items()}


class QQCSection(ft.PieChart):
    normal_radius = 70
    hover_radius = 80

    def __init__(self, space_radius: int, tonality: list):
        super().__init__()
        self.sections_space = 1
        self.start_degree_offset = -135
        self.center_space_radius = space_radius

        self.normal_title_style = ft.TextStyle(
            size=16, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD
        )
        self.hover_title_style = ft.TextStyle(
            size=22,
            color=ft.colors.WHITE,
            weight=ft.FontWeight.BOLD,
            shadow=ft.BoxShadow(blur_radius=2, color=ft.colors.BLACK54),
        )

        self.sections = [
            self._part_section(t) for t in tonality
        ]

        self.on_chart_event = self._on_chart_event

    def _part_section(self, tonal: str):
        return ft.PieChartSection(
            12,
            title=tonal,
            title_style=self.normal_title_style,
            radius=self.normal_radius,
        )

    def _on_chart_event(self, e: ft.PieChartEvent):
        for idx, section in enumerate(self.sections):
            if idx == e.section_index:
                # section.radius = hover_radius
                section.title_style = self.hover_title_style
            else:
                # section.radius = normal_radius
                section.title_style = self.normal_title_style
        self.update()


class CircleFifths(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/"
        self.page = page
        self.padding = 0
        page.window.center()
        page.window.width = 600
        page.window.height = 600
        page.window.resizable = False
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.window.title_bar_hidden = True
        page.window.title_bar_buttons_hidden = True

        self.outer = QQCSection(150, list(qqc.keys()))
        self.inner = QQCSection(75, list(qqc.values()))

        cinner = ft.Container(self.inner, on_hover=self._swap_qq, key="inner", height=250, width=250)
        couter = ft.Container(self.outer, on_hover=self._swap_qq, key="outer")

        self.menu = BaseMenu(575)
        self.stack = ft.Stack([couter, cinner], expand=True, alignment=ft.alignment.center)
        self.controls = [
            self.menu,
            self.stack
        ]
        page.on_route_change = self.route_change
        page.go(self.route)

        page.window.on_resized = self._resize

    def _swap_qq(self, e: ft.ControlEvent):
        new = e.control
        current = self.stack.controls[-1]
        if current.key == new.key:
            return
        new = self.stack.controls.index(e.control)
        new = self.stack.controls.pop(new)
        self.stack.controls.insert(0, new)
        self.stack.update()

    def route_change(self, _):
        self.page.views.clear()
        self.page.views.append(self)
        self.page.update()

    def _resize(self, _):
        self.page.window.width = \
            self.page.window.min_width = \
            self.page.window.max_width = 600
        self.page.window.height = \
            self.page.window.min_height = \
            self.page.window.max_height = 600


if __name__ == "__main__":
    ft.app(CircleFifths)
