"""Class implementation for line cap interface.
"""

from typing import Dict
from typing import Union

from apysc._display.line_caps import LineCaps
from apysc._type.revert_interface import RevertInterface
from apysc._type.string import String
from apysc._type.variable_name_interface import VariableNameInterface


class LineCapInterface(VariableNameInterface, RevertInterface):

    _line_cap: String

    def _initialize_line_cap_if_not_initialized(self) -> None:
        """
        Inilialize _line_cap attribute if it is not
        initialized yet.
        """
        if hasattr(self, '_line_cap'):
            return
        self._line_cap = String(LineCaps.BUTT.value)

    @property
    def line_cap(self) -> Union[String, LineCaps]:
        """
        Get this instance's line cap style setting.

        Returns
        -------
        line_cap : String
            Line cap style setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_cap = ap.LineCaps.ROUND
        >>> line.line_cap
        String('round')
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_cap', locals_=locals(),
                module_name=__name__, class_=LineCapInterface):
            self._initialize_line_cap_if_not_initialized()
            return self._line_cap._copy()

    @line_cap.setter
    def line_cap(self, value: Union[String, LineCaps]) -> None:
        """
        Set line cap style setting.

        Parameters
        ----------
        value : String or LineCaps
            Line cap style setting to set.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_cap', locals_=locals(),
                module_name=__name__, class_=LineCapInterface):
            self._update_line_cap_and_skip_appending_exp(value=value)
            self._append_line_cap_update_expression()

    def _append_line_cap_update_expression(self) -> None:
        """
        Append line cap updating expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_line_cap_update_expression,
                locals_=locals(),
                module_name=__name__, class_=LineCapInterface):
            from apysc._type import value_util
            cap_name: str = value_util.get_value_str_for_expression(
                value=self._line_cap)
            expression: str = (
                f'{self.variable_name}.attr({{"stroke-linecap": {cap_name}}});'
            )
            ap.append_js_expression(expression=expression)

    def _update_line_cap_and_skip_appending_exp(
            self, *, value: Union[String, LineCaps]) -> None:
        """
        Update line cap and skip appending expression.

        Parameters
        ----------
        value : String or LineCaps
            Line cap style setting to set.
        """
        from apysc._validation.display_validation import validate_line_cap
        if not isinstance(value, (String, LineCaps)):
            raise TypeError(
                'Not supported line_cap type specified: '
                f'{type(value)}'
                '\nAcceptable ones are: String or LineCaps.')
        validate_line_cap(cap=value)
        if isinstance(value, String):
            self._line_cap = value._copy()
        else:
            self._line_cap = String(value.value)

    _line_cap_snapshots: Dict[str, str]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_line_cap_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_line_cap_snapshots',
            value=self._line_cap._value, snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._line_cap._value = self._line_cap_snapshots[snapshot_name]
