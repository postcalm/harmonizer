import pytest

from harmonizer.core.chords.model import Chord
from tests.testdata.chords import MINOR_CHORDS_DATA, MAJOR_CHORDS_DATA


@pytest.mark.usefixtures("minor_session")
@pytest.mark.parametrize("actual, expected", MINOR_CHORDS_DATA)
def test_minor_chords(actual, expected):
    assert getattr(Chord(), actual) == expected


@pytest.mark.usefixtures("major_session")
@pytest.mark.parametrize("actual, expected", MAJOR_CHORDS_DATA)
def test_major_chords(actual, expected):
    assert getattr(Chord(), actual) == expected
