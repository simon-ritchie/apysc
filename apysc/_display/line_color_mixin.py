"""Class implementation for line color interface.
"""

from typing import Dict
from typing import Union

from typing_extensions import final

from apysc._animation.animation_line_color_mixin import AnimationLineColorMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.string import String
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos


class LineColorMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    AnimationLineColorMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
):

    _line_color: String

    @property
    @add_debug_info_setting(module_name=__name__)
    def line_color(self) -> String:
        """
        Get this instance's line color.

        Returns
        -------
        line_color : String
            Current line color (hexadecimal string, e.g., '#00aaff').
            If not be set, this interface returns a blank string.

        References
        ----------
        - GraphicsBase line_color interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_line_color.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color="#fff", thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50
        ... )
        >>> line.line_color = ap.String("#0af")
        >>> line.line_color
        String('#00aaff')
        """
        import apysc as ap
        from apysc._type import value_util

        self._initialize_line_color_if_not_initialized()
        line_color: ap.String = value_util.get_copy(value=self._line_color)
        return line_color

    @line_color.setter
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def line_color(self, value: String) -> None:
        """
        Update this instance's line color.

        Parameters
        ----------
        value : str
            Line color to set.

        References
        ----------
        - GraphicsBase line_color interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_line_color.html  # noqa
        """
        self._initialize_line_color_if_not_initialized()
        self._update_line_color_and_skip_appending_exp(value=value)
        self._append_line_color_update_expression()

        self._append_applying_new_attr_val_exp(
            new_attr=self._line_color, attr_name="line_color"
        )
        self._append_attr_to_linking_stack(
            attr=self._line_color, attr_name="line_color"
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_line_color_update_expression(self) -> None:
        """
        Append line color updating expression.
        """
        import apysc as ap
        from apysc._type import value_util

        line_color_str: str = value_util.get_value_str_for_expression(
            value=self._line_color
        )
        expression: str = f"{self.variable_name}.stroke({line_color_str});"
        ap.append_js_expression(expression=expression)

    @final
    def _set_initial_line_color_if_not_blank(
        self, *, line_color: Union[str, String]
    ) -> None:
        """
        Set initial line color value if a specified value is
        not a blank string.

        Parameters
        ----------
        line_color : str or String
            Line color (hexadecimal string, e.g., '#00aaff').
        """
        import apysc as ap

        self._initialize_line_color_if_not_initialized()
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="line_color"
        )
        if line_color == "":
            return
        if isinstance(line_color, ap.String):
            line_color_: ap.String = line_color
        else:
            line_color_ = String(line_color, variable_name_suffix=suffix)
        self._update_line_color_and_skip_appending_exp(value=line_color_)

    @final
    def _update_line_color_and_skip_appending_exp(self, *, value: String) -> None:
        """
        Update line color and skip appending expression.

        Parameters
        ----------
        value : String
            Line color to set.
        """
        from apysc._color import color_util

        self._initialize_line_color_if_not_initialized()
        value = color_util.complement_hex_color(hex_color_code=value)
        self._initialize_line_color_if_not_initialized()
        self._line_color = value

    @final
    def _initialize_line_color_if_not_initialized(self) -> None:
        """
        Initialize the line_color attribute if this
        interface does not initialize it yet.
        """
        if hasattr(self, "_line_color"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="line_color"
        )
        self._line_color = String(
            "",
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

    _line_color_snapshots: Dict[str, str]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_line_color_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_line_color_snapshots",
            value=self._line_color._value,
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
        self._line_color._value = self._line_color_snapshots[snapshot_name]
