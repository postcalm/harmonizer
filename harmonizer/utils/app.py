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
