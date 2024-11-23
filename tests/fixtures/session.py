import pytest

from harmonizer.core.models.harmony import Harmony
from harmonizer.core.session import Session


@pytest.fixture
def major_session():
    Session().tune = "standard_e"
    Session().tonality = "major"
    Session().tonica = "E"
    Session().harmony = Harmony()


@pytest.fixture
def minor_session():
    Session().tune = "standard_e"
    Session().tonality = "minor"
    Session().tonica = "E"
    Session().harmony = Harmony()
