"""Base class implementation for the animation.
"""

from typing import Optional, Union

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class AnimationBase(VariableNameInterface, RevertInterface):

    _duration: ap.Int
    _delay: ap.Int
    _easing: Optional[ap.Easing]

    def __init__(
            self,
            duration: Union[int, ap.Int],
            delay: Union[int, ap.Int] = 0,
            easing: Optional[ap.Easing] = None) -> None:
        """
        Base class for the animation.

        Parameters
        ----------
        duration : int or Int
            Milliseconds before the animation ends.
        delay : int or Int, default 0
            Milliseconds before the animation starts.
        easing : Easing or None, default None
            Easing setting. If None, Linear calculation is used.
        """
        from apysc._converter import to_apysc_val_from_builtin
        self._duration = to_apysc_val_from_builtin.\
            get_copied_int_from_builtin_val(integer=duration)
        self._delay = to_apysc_val_from_builtin.\
            get_copied_int_from_builtin_val(integer=delay)
        self._easing = easing

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values' snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
