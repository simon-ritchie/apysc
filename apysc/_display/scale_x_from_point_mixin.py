"""Class implementation for the scale_x_from_point mix-in.
"""

from typing import Any
from typing import Dict

from typing_extensions import final

from apysc._animation.animation_scale_x_from_point_mixin import (
    AnimationScaleXFromPointMixIn,
)
from apysc._display.set_lower_scale_limit_mixin import SetLowerScaleLimitMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.dictionary import Dictionary
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos


class ScaleXFromPointMixIn(
    VariableNameSuffixAttrMixIn,
    AnimationScaleXFromPointMixIn,
    SetLowerScaleLimitMixIn,
    RevertMixIn,
):

    _scale_x_from_point: Dictionary[str, Number]

    @final
    def _initialize_scale_x_from_point_if_not_initialized(self) -> None:
        """
        Initialize the `_scale_x_from_point` attribute if
        this instance does not initialize it yet.
        """
        if hasattr(self, "_scale_x_from_point"):
            return
        suffix: str = self._get_attr_variable_name_suffix(
            attr_identifier="scale_x_from_point"
        )
        self._scale_x_from_point = Dictionary(
            {},
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

    @final
    @arg_validation_decos.is_apysc_integer(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def get_scale_x_from_point(self, *, x: Int) -> Number:
        """
        Get a scale-x value from the given x-coordinate.

        Parameters
        ----------
        x : Int
            X-coordinate.

        Returns
        -------
        scale_x : Number
            Scale-x value from the given x-coordinate.

        Notes
        -----
        The scale's minimum value is almost zero, and it does not become negative.

        References
        ----------
        - GraphicsBase scale_from_point interfaces
            - https://simon-ritchie.github.io/apysc/en/graphics_base_scale_from_point.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> x: ap.Int = ap.Int(100)
        >>> rectangle.set_scale_x_from_point(scale_x=ap.Number(1.5), x=x)
        >>> rectangle.get_scale_x_from_point(x=x)
        Number(1.5)
        """
        import apysc as ap
        from apysc._display import scale_interface_helper
        from apysc._type.expression_string import ExpressionString

        self._initialize_scale_x_from_point_if_not_initialized()
        default_val: ap.Number = ap.Number(1.0)
        key_exp_str: ExpressionString = (
            scale_interface_helper.get_coordinate_key_for_expression(
                coordinate=int(x._value)
            )
        )
        scale_x: ap.Number = self._scale_x_from_point.get(
            key=key_exp_str, default=default_val
        )
        return scale_x

    @final
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @arg_validation_decos.is_apysc_integer(arg_position_index=2)
    @add_debug_info_setting(module_name=__name__)
    def set_scale_x_from_point(self, *, scale_x: Number, x: Int) -> None:
        """
        Update a scale-x value from the given x-coordinate.

        Parameters
        ----------
        scale_x : Number
            Scale-x value to set.
        x : Int
            X-coordinate.

        Notes
        -----
        The scale's minimum value is almost zero, and it does not become negative.

        References
        ----------
        - GraphicsBase scale_from_point interfaces
            - https://simon-ritchie.github.io/apysc/en/graphics_base_scale_from_point.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> x: ap.Int = ap.Int(100)
        >>> rectangle.set_scale_x_from_point(scale_x=ap.Number(1.5), x=x)
        >>> rectangle.get_scale_x_from_point(x=x)
        Number(1.5)
        """
        from apysc._display import scale_interface_helper
        from apysc._type.expression_string import ExpressionString

        self._initialize_scale_x_from_point_if_not_initialized()
        key_exp_str: ExpressionString = (
            scale_interface_helper.get_coordinate_key_for_expression(
                coordinate=int(x._value)
            )
        )
        self._set_lower_scale_limit(value=scale_x)
        self._scale_x_from_point._value[key_exp_str.value] = scale_x
        self._append_scale_x_from_point_update_expression(x=x)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_scale_x_from_point_update_expression(self, *, x: Int) -> None:
        """
        Append the scale-x from the specified x-coordinate updating
        expression.

        Parameters
        ----------
        x : Int
            X-coordinate.
        """
        import apysc as ap
        from apysc._display import scale_interface_helper

        expression: str
        expression = scale_interface_helper.get_scale_updating_expression(
            coordinate=x,
            scale_dict=self._scale_x_from_point,
            interface_variable_name=self.variable_name,
            coordinate_type=scale_interface_helper.CoordinateType.X,
        )
        ap.append_js_expression(expression=expression)

    _scale_x_from_point_snapshots: Dict[str, Dict[str, Any]]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_scale_x_from_point_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_scale_x_from_point_snapshots",
            value={**self._scale_x_from_point._value},
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._scale_x_from_point._value = self._scale_x_from_point_snapshots[
            snapshot_name
        ]
