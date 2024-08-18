import os
import random
from multiprocessing import freeze_support

import flet
from flet_multi_page import subPage


def second_target(page: flet.Page):
    colors = ["blue", "pink", "black", "red", "green"]
    page.bgcolor = random.choice(colors)
    page.add(flet.Text("Hello new page!", color="white"))
    page.update()


def first_target(page: flet.Page):
    def start_new_page(e):
        os.environ["FLET_SERVER_PORT"] = "0"
        subPage(target=second_target).start()

    page.add(flet.ElevatedButton("start new page", on_click=start_new_page))
    page.update()


if __name__ == "__main__":
    freeze_support()
    flet.app(target=first_target)
