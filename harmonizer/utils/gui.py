from typing import Any

import flet as ft


def get_flet_control(obj: ft.Control, name: str) -> Any:
    """Возвращает элемент управления flet, существующий в приложении"""
    content = getattr(obj.parent, "content", None)
    if not content:
        control = getattr(obj.parent, "controls", None)
    else:
        control = content.controls
    for c in control:
        if c.__class__.__name__ == name:
            return c
    else:
        return get_flet_control(obj.parent, name)
