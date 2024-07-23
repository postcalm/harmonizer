import flet as ft


def get_flet_control(obj: ft.Control, name: str):
    for c in obj.parent.controls:
        if c.__class__.__name__ == name:
            return c
    else:
        return get_flet_control(obj.parent, name)
