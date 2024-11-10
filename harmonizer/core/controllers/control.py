from harmonizer.core import Singleton
from harmonizer.core.controllers import BaseController


class ControlController(metaclass=Singleton):
    """Управляющий контроллер"""

    _controllers: dict[str, BaseController] = {}

    def add(self, name: str, controller: BaseController) -> None:
        """
        Добавляет контроллер

        :param name: Название контролера
        :param controller: Контроллер
        :return: None
        """
        self._controllers[name] = controller

    def get(self, name: str) -> BaseController:
        """
        Получить контроллер по названию

        :param name: Название контроллера
        :return: Контроллер
        """
        return self._controllers.get(name)
