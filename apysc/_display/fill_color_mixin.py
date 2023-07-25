"""Class implementation for fill color mix-in.
"""

from typing import Dict
from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._animation.animation_fill_color_mixin import AnimationFillColorMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.string import String
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos
from apysc._color.color import Color
from apysc._color.colorless import COLORLESS


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
            Current fill color (hexadecimal string, e.g., '#00aaff').
            If it is not set, it returns the `COLORLESS` constant.

        References
        ----------
        - GraphicsBase fill_color interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_fill_color.html  # noqa
        """
        import apysc as ap
        from apysc._type import value_util

        self._initialize_fill_color_if_not_initialized()
        fill_color: ap.String = value_util.get_copy(value=self._fill_color)
        return fill_color

    @fill_color.setter
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def fill_color(self, value: String) -> None:
        """
        Update this instance's fill color.

        Parameters
        ----------
        value : String
            Fill color to set.

        References
        ----------
        - GraphicsBase fill_color interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_fill_color.html  # noqa
        """
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
        import apysc as ap

        expression: str = f'{self.variable_name}.fill("{self.fill_color}");'
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_fill_color_if_not_blank(
        self, *, fill_color: Color
    ) -> None:
        """
        Set the initial fill color if a specified value
        is not a blank string.

        Parameters
        ----------
        fill_color : Color
            Fill color (hexadecimal string, e.g., '#00aaff').
        """
        import apysc as ap

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
        from apysc._color import color_util

        self._initialize_fill_color_if_not_initialized()
        self._fill_color.value = value

    @final
    @add_debug_info_setting(module_name=__name__)
    def _initialize_fill_color_if_not_initialized(self) -> None:
        """
        Initialize the fill_color attribute if this interface
        does not initialize it yet.
        """
        if hasattr(self, "_fill_color"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="fill_color"
        )
        self._fill_color = String(
            "",
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

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
            value=self._fill_color._value,
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
        self._fill_color._value = self._get_snapshot_val_if_exists(
            current_value=self._fill_color._value,
            snapshot_dict=self._fill_color_snapshots,
            snapshot_name=snapshot_name,
        )
