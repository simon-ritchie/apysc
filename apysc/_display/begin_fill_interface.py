"""Class implementation for begin_fill method related interface.

See Also
--------
- graphics_clear_interface
"""


from typing import Dict
from typing import TypeVar
from typing import Union

import apysc as ap
from apysc._type.revert_interface import RevertInterface

StrOrString = TypeVar('StrOrString', str, ap.String)


class BeginFillInterface(RevertInterface):

    _fill_color: ap.String
    _fill_alpha: ap.Number

    def begin_fill(
            self, color: StrOrString,
            alpha: Union[float, ap.Number] = 1.0) -> None:
        """
        Set single color value for fill.

        Parameters
        ----------
        color : str or String
            Hexadecimal color string. e.g., '#00aaff'
        alpha : float or Number, default 1.0
            Color opacity (0.0 to 1.0).

        References
        ----------
        - Graphics begin_fill interface document
            - https://bit.ly/3ikhNAh
        """
        with ap.DebugInfo(
                callable_=self.begin_fill, locals_=locals(),
                module_name=__name__, class_=BeginFillInterface):
            from apysc._color import color_util
            from apysc._converter import cast
            from apysc._validation import color_validation
            from apysc._validation import number_validation
            self._initialize_fill_color_if_not_initialized()
            self._initialize_fill_alpha_if_not_initialized()
            if color != '':
                color = color_util.complement_hex_color(
                    hex_color_code=color)
            self._fill_color.value = color
            number_validation.validate_num(num=alpha)
            if not isinstance(alpha, ap.Number):
                alpha = cast.to_float_from_int(int_or_float=alpha)
            color_validation.validate_alpha_range(alpha=alpha)
            if isinstance(alpha, ap.Number):
                self._fill_alpha.value = alpha.value
            else:
                self._fill_alpha.value = alpha

    @property
    def fill_color(self) -> ap.String:
        """
        Get current fill color.

        Returns
        -------
        fill_color : String
            Current fill color (hexadecimal string, e.g., '#00aaff').
            If not be set, blank string will be returned.
        """
        with ap.DebugInfo(
                callable_='fill_color', locals_=locals(),
                module_name=__name__, class_=BeginFillInterface):
            from apysc._type import value_util
            self._initialize_fill_color_if_not_initialized()
            fill_color: ap.String = value_util.get_copy(value=self._fill_color)
            return fill_color

    def _initialize_fill_color_if_not_initialized(self) -> None:
        """
        Initialize fill_color attribute it hasn't been initialized yet.
        """
        if hasattr(self, '_fill_color'):
            return
        self._fill_color = ap.String('')

    @property
    def fill_alpha(self) -> ap.Number:
        """
        Get current fill color opacity.

        Returns
        -------
        fill_alpha : Number
            Current fill color opacity (0.0 to 1.0).
            If not be set, 1.0 will be returned.
        """
        with ap.DebugInfo(
                callable_='fill_alpha', locals_=locals(),
                module_name=__name__, class_=BeginFillInterface):
            from apysc._type import value_util
            self._initialize_fill_alpha_if_not_initialized()
            fill_alpha: ap.Number = value_util.get_copy(value=self._fill_alpha)
            return fill_alpha

    def _initialize_fill_alpha_if_not_initialized(self) -> None:
        """
        Initialize fill_alpha attribute it hasn't been initialized yet.
        """
        if hasattr(self, '_fill_alpha'):
            return
        self._fill_alpha = ap.Number(1.0)

    _fill_color_snapshots: Dict[str, str]
    _fill_alpha_snapshots: Dict[str, float]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values' snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_fill_color_snapshots'):
            self._fill_color_snapshots = {}
            self._fill_alpha_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_fill_color_if_not_initialized()
        self._initialize_fill_alpha_if_not_initialized()
        self._fill_color_snapshots[snapshot_name] = self._fill_color._value
        self._fill_alpha_snapshots[snapshot_name] = self._fill_alpha._value

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._fill_color._value = self._fill_color_snapshots[snapshot_name]
        self._fill_alpha._value = self._fill_alpha_snapshots[snapshot_name]
