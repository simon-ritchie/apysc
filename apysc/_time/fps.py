"""Definition of the FPS enum.
"""

from enum import Enum
from typing import Union


class _FPSDefinition:

    _fps: int
    _milisecond_interval: Union[int, float]

    def __init__(
            self, fps: int,
            milisecond_intervals: Union[int, float]) -> None:
        """
        FPS definition class.

        Parameters
        ----------
        fps : int
            FPS value, such as 30, 60.
        milisecond_intervals : int or float
            FPS value in milisecond intervals, such as 33, 16.
        """
        self._fps = fps
        self._milisecond_interval = milisecond_intervals


class FPS(Enum):
    pass
