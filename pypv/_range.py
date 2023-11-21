from typing import Optional


class Range:
    min: Optional[float] = None
    max: Optional[float] = None
    ratio: int

    def __init__(self, min: Optional[float], max: Optional[float], ratio: int):
        self.min = min
        self.max = max
        self.ratio = ratio
