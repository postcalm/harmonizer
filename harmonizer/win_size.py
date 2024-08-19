from dataclasses import dataclass


@dataclass(frozen=True)
class WindowSize:
    width: int
    height: int
