from typing import Optional


class Range:
    """
    This class is used to define a range of values, such as temperature or voltage, with optional
    minimum and maximum bounds and a fixed ratio.

    Args:
        min (Optional[float]): The optional minimum value of the range.
        max (Optional[float]): The optional maximum value of the range.
        ratio (int): The fixed ratio associated with the range.

    """

    min: Optional[float] = None
    max: Optional[float] = None
    ratio: int

    def __init__(self, min: Optional[float], max: Optional[float], ratio: int):
        self.min = min
        self.max = max
        self.ratio = ratio
