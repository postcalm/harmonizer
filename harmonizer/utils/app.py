"""
Функции для подмены so-библиотеки.
Т.к. на момент разработки многооконного приложения
flet не умел в данный функционал было решено реализовать
многооконность через подкладку so-библиотеки, являющейся
точкой входа для запуска приложения.
Также для корректного запуска приложения требуется пропатченный
шаблон flet - https://github.com/postcalm/flet-build-template/tree/0.23.2.
"""
import shutil
from pathlib import Path

from harmonizer.utils.pid import get_exe_by_pid, get_pid
from harmonizer.consts import PROJECT_NAME


def get_app_path() -> Path:
    """Возвращает путь до приложения"""
    exec_path = get_exe_by_pid(get_pid(PROJECT_NAME))
    return Path(exec_path).parent


def use_so_lib(name: str) -> None:
    """Использовать so-библиотеку указанного приложения"""
    shutil.copy(
        get_app_path() / "data" / f"{name}.so",
        get_app_path() / "data" / "app.so"
    )
