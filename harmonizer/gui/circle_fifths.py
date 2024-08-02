import flet as ft


class CircleFifths:
    def __init__(self, page: ft.Page):
        self.page = page
        page.title = "Circle of Fifths"
        self._resize(None)

        ext = ft.Column([
            ft.ResponsiveRow([
                ft.Text("F"),
                ft.Text("C"),
                ft.Text("G"),
            ],

            ),
        ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        content = ft.Container(
            ext,
            alignment=ft.alignment.center,
            shape=ft.BoxShape.CIRCLE,
            border=ft.border.all(1),
            expand=True,
            expand_loose=True
        )
        page.add(content)

        page.window.on_event = self._resize

    def _resize(self, _):
        self.page.window.width = \
            self.page.window.min_width = \
            self.page.window.max_width = 600
        self.page.window.height = \
            self.page.window.min_height = \
            self.page.window.max_height = 600


def main(page: ft.Page):
    page.window.width = 600
    page.window.height = 600
    page.window.resizable = True
    normal_radius = 70
    hover_radius = 60
    normal_title_style = ft.TextStyle(
        size=16, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD
    )
    hover_title_style = ft.TextStyle(
        size=22,
        color=ft.colors.WHITE,
        weight=ft.FontWeight.BOLD,
        shadow=ft.BoxShadow(blur_radius=2, color=ft.colors.BLACK54),
    )

    def on_chart_event(e: ft.PieChartEvent, chart):
        for idx, section in enumerate(chart.sections):
            if idx == e.section_index:
                # section.radius = hover_radius
                section.title_style = hover_title_style
            else:
                # section.radius = normal_radius
                section.title_style = normal_title_style
        chart.update()

    outer = ft.PieChart(
        [
            ft.PieChartSection(
                12,
                title=note,
                title_style=normal_title_style,
                radius=normal_radius,
            )
            for note in ["F", "C", "G", "D", "A", "E", "B",
                         "F#", "C#", "G#", "Eb", "Bb"]
        ],
        sections_space=1,
        center_space_radius=150,
        start_degree_offset=-135,
        on_chart_event=lambda e: on_chart_event(e, outer),
    )
    inner = ft.PieChart(
        [
            ft.PieChartSection(
                12,
                title=note,
                title_style=normal_title_style,
                radius=normal_radius,
            )
            for note in ["Dm", "Am", "Em", "Bm", "F#m", "C#m", "G#m",
                         "Ebm", "Bbm", "Fm", "Cm", "Gm"]
        ],
        sections_space=1,
        center_space_radius=75,
        start_degree_offset=-135,
        on_chart_event=lambda e: on_chart_event(e, inner)
    )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def outer_circle(e: ft.ControlEvent):
        print(e.control)
        new = e.control
        current = stack.controls[-1]
        if current.key == new.key:
            return
        new = stack.controls.index(e.control)
        new = stack.controls.pop(new)
        stack.controls.insert(0, new)
        stack.update()

    cinner = ft.Container(
        inner, on_hover=outer_circle, border=ft.border.all(1), key="inner",
        height=250, width=250
    )
    couter = ft.Container(
        outer, on_hover=outer_circle, border=ft.border.all(1), key="outer")

    stack = ft.Stack([couter, cinner], expand=True,
                     alignment=ft.alignment.center)

    page.add(stack)


ft.app(main)
