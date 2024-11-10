from dataclasses import dataclass


@dataclass(frozen=True)
class FrameSize:
    width: int = None
    height: int = None
