"""Class implementation for line color interface.
"""

from typing import Dict
from typing import Optional

from typing_extensions import final

from apysc._animation.animation_line_color_mixin import AnimationLineColorMixIn
from apysc._color.color import Color
from apysc._color.colorless import COLORLESS
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.revert_mixin import RevertMixIn
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
    _line_color: Color

    @property
    @add_debug_info_setting(module_name=__name__)
    def line_color(self) -> Color:
        """
        Get this instance's line color.

        Returns
        -------
        line_color : Color
            Current line color (hexadecimal string, e.g., '#00aaff').
            If it is not set, it returns the `COLORLESS` constant.

        References
        ----------
        - GraphicsBase line_color interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_line_color.html  # noqa

        Examples
        --------
        >>> import apysc as ap

        >>> _ = ap.Stage(
        ...     stage_width=150,
        ...     stage_height=150,
        ...     background_color=ap.Color("#333"),
        ...     stage_elem_id="stage",
        ... )
        >>> rectangle: ap.Rectangle = ap.Rectangle(
        ...     x=50,
        ...     y=50,
        ...     width=50,
        ...     height=50,
        ...     line_color=ap.Color("#0af"),
        ...     line_thickness=2,
        ... )
        >>> rectangle.line_color
        Color("#00aaff")
        >>> rectangle.line_color = ap.Color("#ff00aa")
        >>> rectangle.line_color
        Color("#ff00aa")
        """
        from apysc._color.color import Color
        from apysc._type import value_util

        self._initialize_line_color_if_not_initialized()
        line_color: Color = value_util.get_copy(value=self._line_color)
        return line_color

    @line_color.setter
    @arg_validation_decos.is_color(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def line_color(self, value: Color) -> None:
        """
        Update this instance's line color.

        Parameters
        ----------
        value : Color
            Line color to set.

        References
        ----------
        - GraphicsBase line_color interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_line_color.html  # noqa

        Examples
        --------
        >>> import apysc as ap

        >>> _ = ap.Stage(
        ...     stage_width=150,
        ...     stage_height=150,
        ...     background_color=ap.Color("#333"),
        ...     stage_elem_id="stage",
        ... )
        >>> rectangle: ap.Rectangle = ap.Rectangle(
        ...     x=50,
        ...     y=50,
        ...     width=50,
        ...     height=50,
        ...     line_color=ap.Color("#0af"),
        ...     line_thickness=2,
        ... )
        >>> rectangle.line_color
        Color("#00aaff")
        >>> rectangle.line_color = ap.Color("#ff00aa")
        >>> rectangle.line_color
        Color("#ff00aa")
        """
        value = value._copy()
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
        from apysc._expression import expression_data_util

        expression: str = (
            f"{self.variable_name}.stroke({self._line_color._value.variable_name});"
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    def _set_initial_line_color_if_not_colorless(self, *, line_color: Color) -> None:
        """
        Set initial line color value if a specified value is
        not the `COLORLESS` constant.

        Parameters
        ----------
        line_color : Color
            A line color.
        """

        self._initialize_line_color_if_not_initialized()
        if line_color == COLORLESS:
            return
        self._update_line_color_and_skip_appending_exp(value=line_color)

    @final
    def _update_line_color_and_skip_appending_exp(self, *, value: Color) -> None:
        """
        Update line color and skip appending expression.

        Parameters
        ----------
        value : Color
            Line color to set.
        """
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
        self._line_color = COLORLESS

    _line_color_snapshots: Optional[Dict[str, str]] = None

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
            value=self._line_color._value._value,
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
        self._initialize_line_color_if_not_initialized()
        self._line_color._value._value = self._get_snapshot_val_if_exists(
            current_value=self._line_color._value._value,
            snapshot_dict=self._line_color_snapshots,
            snapshot_name=snapshot_name,
        )
