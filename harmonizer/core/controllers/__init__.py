from harmonizer.core.session import Session
from harmonizer.core.views import BaseView


class BaseController:
    """Базовый контроллер"""

    model: Session = Session()
    viewer: BaseView = None

    def run(self):
        self.viewer.draw()
