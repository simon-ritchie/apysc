"""Definition of the FPS enum.
"""

from enum import Enum
from typing import Union

from typing_extensions import final


class FPSDefinition:

    _fps: int
    _millisecond_intervals: Union[int, float]

    @final
    def __init__(self, *, fps: int, millisecond_intervals: Union[int, float]) -> None:
        """
        FPS definition class.

        Parameters
        ----------
        fps : int
            FPS values, such as 30 and 60.
        millisecond_intervals : int or float
            FPS value in millisecond intervals, such as 33.333...
        """
        self._fps = fps
        self._millisecond_intervals = millisecond_intervals

    @property
    def millisecond_intervals(self) -> float:
        """
        Get a FPS value in milisecond intervals.

        Returns
        -------
        milisecond_interval : float
            FPS value in milisecond intervals, such as 33.333...
        """
        return self._millisecond_intervals


class FPS(Enum):
    """
    Definition of the FPS enum.

    References
    ----------
    - FPS enum
        - https://simon-ritchie.github.io/apysc/en/fps.html

    Examples
    --------
    >>> import apysc as ap
    >>> def on_timer(e: ap.TimerEvent, options: dict) -> None:
    ...     pass
    >>> ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
    """

    FPS_5 = FPSDefinition(fps=5, millisecond_intervals=200)
    FPS_10 = FPSDefinition(fps=10, millisecond_intervals=100)
    FPS_15 = FPSDefinition(fps=15, millisecond_intervals=66.6666667)
    FPS_20 = FPSDefinition(fps=20, millisecond_intervals=50)
    FPS_25 = FPSDefinition(fps=25, millisecond_intervals=40)
    FPS_30 = FPSDefinition(fps=30, millisecond_intervals=33.3333333)
    FPS_35 = FPSDefinition(fps=35, millisecond_intervals=28.5714286)
    FPS_40 = FPSDefinition(fps=40, millisecond_intervals=25)
    FPS_45 = FPSDefinition(fps=45, millisecond_intervals=22.2222222)
    FPS_50 = FPSDefinition(fps=50, millisecond_intervals=20)
    FPS_55 = FPSDefinition(fps=55, millisecond_intervals=18.1818182)
    FPS_60 = FPSDefinition(fps=60, millisecond_intervals=16.6666667)
