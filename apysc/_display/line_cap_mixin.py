"""Class implementation for line cap mix-in.
"""

from typing import Dict
from typing import Union

from typing_extensions import final

from apysc._display.line_caps import LineCaps
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.string import String
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos


class LineCapMixIn(VariableNameSuffixAttrMixIn, VariableNameMixIn, RevertMixIn):

    _line_cap: String

    @final
    def _initialize_line_cap_if_not_initialized(self) -> None:
        """
        Initialize the _line_cap attribute if this
        interface does not initialize it yet.
        """
        if hasattr(self, "_line_cap"):
            return
        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="line_cap")
        self._line_cap = String(
            LineCaps.BUTT.value,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

    @property
    @add_debug_info_setting(module_name=__name__)
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
        >>> sprite.graphics.line_style(color="#fff", thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50
        ... )
        >>> line.line_cap = ap.LineCaps.ROUND
        >>> line.line_cap
        String('round')
        """
        self._initialize_line_cap_if_not_initialized()
        return self._line_cap._copy()

    @line_cap.setter
    @arg_validation_decos.is_line_cap(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def line_cap(self, value: Union[String, LineCaps]) -> None:
        """
        Set line cap style setting.

        Parameters
        ----------
        value : String or LineCaps
            Line cap style setting to set.
        """
        self._update_line_cap_and_skip_appending_exp(value=value)
        self._append_line_cap_update_expression()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_line_cap_update_expression(self) -> None:
        """
        Append line cap updating expression.
        """
        import apysc as ap
        from apysc._type import value_util

        cap_name: str = value_util.get_value_str_for_expression(value=self._line_cap)
        expression: str = (
            f'{self.variable_name}.attr({{"stroke-linecap": {cap_name}}});'
        )
        ap.append_js_expression(expression=expression)

    @final
    def _update_line_cap_and_skip_appending_exp(
        self, *, value: Union[String, LineCaps]
    ) -> None:
        """
        Update line cap and skip appending expression.

        Parameters
        ----------
        value : String or LineCaps
            Line cap style setting to set.
        """
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
            dict_name="_line_cap_snapshots",
            value=self._line_cap._value,
            snapshot_name=snapshot_name,
        )

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
