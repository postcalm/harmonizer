from harmonizer.core.chords.types import ChordTypes
from harmonizer.core.models.harmony import Harmony
from harmonizer.core.session import Session
from harmonizer.core.types.enums.notes import Notes
from harmonizer.core.types.enums.tier import Tone


class Chord:
    """
    Модель аккорда
    """

    stage: int
    harmony: Harmony

    def __init__(self, stage: int = 1):
        assert 1 <= stage <= 7
        self.stage = stage - 1
        self.harmony = Session().harmony
        self.notes = Session().harmony.notes
        self.tone = self.harmony.get_tone(self.notes[self.stage])

    @property
    def triad(self) -> list[str]:
        if self.tone == Tone.MAJOR:
            return self._get_chord(ChordTypes.MAJ_TRIAD)
        if self.tone == Tone.MINOR:
            return self._get_chord(ChordTypes.MIN_TRIAD)

    @property
    def sus2(self) -> list[str]:
        return self._get_chord(ChordTypes.SUS2)

    @property
    def sus4(self) -> list[str]:
        return self._get_chord(ChordTypes.SUS4)

    @property
    def power(self) -> list[str]:
        return self._get_chord(ChordTypes.POWER)

    @property
    def septacord(self) -> list[str]:
        if self.tone == Tone.MAJOR:
            return self._get_chord(ChordTypes.MAJ_SEPT)
        if self.tone == Tone.MINOR:
            return self._get_chord(ChordTypes.MIN_SEPT)

    def _get_chord(self, chord_type: ChordTypes) -> list[str]:
        harmony = Notes.get(self.notes[self.stage])
        notes = []
        intervals = chord_type.value
        sum_ = 0
        for n in intervals:
            sum_ += n
            notes.append(harmony[sum_])
        return notes
