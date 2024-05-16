"""Class implementation for fill color mix-in.
"""

from typing import Dict
from typing import Optional

from typing_extensions import final

from apysc._animation.animation_fill_color_mixin import AnimationFillColorMixIn
from apysc._color.color import Color
from apysc._color.colorless import COLORLESS
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos


class FillColorMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    AnimationFillColorMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
):
    _fill_color: Color

    @property
    @add_debug_info_setting(module_name=__name__)
    def fill_color(self) -> Color:
        """
        Get this instance's fill color.

        Returns
        -------
        fill_color : Color
            Current fill color.
            If it is not set, it returns the `COLORLESS` constant.

        References
        ----------
        - GraphicsBase fill_color property
            - https://simon-ritchie.github.io/apysc/en/graphics_base_fill_color.html  # noqa

        Examples
        --------
        >>> import apysc as ap

        >>> _ = ap.Stage(
        ...     stage_width=150,
        ...     stage_height=150,
        ...     background_color=ap.Color("#333"),
        ...     stage_elem_id="stage",
        ... )
        >>> circle: ap.Circle = ap.Circle(
        ...     x=75,
        ...     y=75,
        ...     radius=50,
        ...     fill_color=ap.Color("#0af"),
        ... )
        >>> circle.fill_color
        Color("#00aaff")

        >>> circle.fill_color = ap.Color("#ff00aa")
        >>> circle.fill_color
        Color("#ff00aa")
        """
        from apysc._type import value_util

        self._initialize_fill_color_if_not_initialized()
        fill_color: Color = value_util.get_copy(value=self._fill_color)
        return fill_color

    @fill_color.setter
    @arg_validation_decos.is_color(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def fill_color(self, value: Color) -> None:
        """
        Update this instance's fill color.

        Parameters
        ----------
        value : Color
            Fill color to set.

        References
        ----------
        - GraphicsBase fill_color property
            - https://simon-ritchie.github.io/apysc/en/graphics_base_fill_color.html  # noqa

        Examples
        --------
        >>> import apysc as ap

        >>> _ = ap.Stage(
        ...     stage_width=150,
        ...     stage_height=150,
        ...     background_color=ap.Color("#333"),
        ...     stage_elem_id="stage",
        ... )
        >>> circle: ap.Circle = ap.Circle(
        ...     x=75,
        ...     y=75,
        ...     radius=50,
        ...     fill_color=ap.Color("#0af"),
        ... )
        >>> circle.fill_color
        Color("#00aaff")

        >>> circle.fill_color = ap.Color("#ff00aa")
        >>> circle.fill_color
        Color("#ff00aa")
        """
        value = value._copy()
        self._update_fill_color_and_skip_appending_exp(value=value)
        self._append_fill_color_update_expression()

        self._append_applying_new_attr_val_exp(
            new_attr=self._fill_color, attr_name="fill_color"
        )
        self._append_attr_to_linking_stack(
            attr=self._fill_color, attr_name="fill_color"
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_fill_color_update_expression(self) -> None:
        """
        Append the fill color updating expression.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"{self.variable_name}.fill({self.fill_color._value.variable_name});"
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_fill_color_if_not_colorless(self, *, fill_color: Color) -> None:
        """
        Set the initial fill color if a specified value
        is not the `COLORLESS` constant.

        Parameters
        ----------
        fill_color : Color
            A fill color.
        """

        self._initialize_fill_color_if_not_initialized()
        if fill_color == COLORLESS:
            return
        self._update_fill_color_and_skip_appending_exp(value=fill_color)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _update_fill_color_and_skip_appending_exp(self, *, value: Color) -> None:
        """
        Update fill color and skip appending expression.

        Parameters
        ----------
        value : Color
            Fill color to set.
        """
        self._initialize_fill_color_if_not_initialized()
        self._fill_color = value

    @final
    @add_debug_info_setting(module_name=__name__)
    def _initialize_fill_color_if_not_initialized(self) -> None:
        """
        Initialize the fill_color attribute if this interface
        does not initialize it yet.
        """
        if hasattr(self, "_fill_color"):
            return
        self._fill_color = COLORLESS

    _fill_color_snapshots: Optional[Dict[str, str]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_fill_color_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_fill_color_snapshots",
            value=self._fill_color._value._value,
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
        self._fill_color._value._value = self._get_snapshot_val_if_exists(
            current_value=self._fill_color._value._value,
            snapshot_dict=self._fill_color_snapshots,
            snapshot_name=snapshot_name,
        )
