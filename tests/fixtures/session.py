import pytest

from harmonizer.core.session import Session
from harmonizer.core.views.guitar import set_harmony


@pytest.fixture
def major_session():
    Session().tune = "standard_e"
    Session().tonality = "major"
    Session().tonica = "E"
    Session().harmony = set_harmony()


@pytest.fixture
def minor_session():
    Session().tune = "standard_e"
    Session().tonality = "minor"
    Session().tonica = "E"
    Session().harmony = set_harmony()
