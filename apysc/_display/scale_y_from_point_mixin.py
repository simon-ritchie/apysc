"""Class implementation for the scale_y_from_point mix-in.
"""

from typing import Any
from typing import Dict
from typing import Optional

from typing_extensions import final

from apysc._animation.animation_scale_y_from_point_mixin import (
    AnimationScaleYFromPointMixIn,
)
from apysc._display.set_lower_scale_limit_mixin import SetLowerScaleLimitMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.dictionary import Dictionary
from apysc._type.expression_string import ExpressionString
from apysc._type.number import Number
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos


class ScaleYFromPointMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    AnimationScaleYFromPointMixIn,
    SetLowerScaleLimitMixIn,
    RevertMixIn,
):
    _scale_y_from_point: Dictionary[str, Number]

    @final
    def _initialize_scale_y_from_point_if_not_initialized(self) -> None:
        """
        Initialize the `_scale_y_from_point` attribute if this
        instance does not initialize it yet.
        """
        if hasattr(self, "_scale_y_from_point"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="scale_y_from_point"
        )
        self._scale_y_from_point = Dictionary(
            {},
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

    @final
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def get_scale_y_from_point(self, *, y: Number) -> Number:
        """
        Get a scale-y value from the given y-coordinate.

        Parameters
        ----------
        y : Number
            Y-coordinate.

        Returns
        -------
        scale_y : ap.Number
            Scale-y value from the given y-coordinate.

        References
        ----------
        - GraphicsBase scale_from_point interfaces
            - https://simon-ritchie.github.io/apysc/en/graphics_base_scale_from_point.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> y: ap.Number = ap.Number(100)
        >>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)
        >>> rectangle.get_scale_y_from_point(y=y)
        Number(1.5)
        """
        from apysc._display import scale_interface_helper

        self._initialize_scale_y_from_point_if_not_initialized()
        default_val: Number = Number(1.0)
        key_exp_str: ExpressionString = (
            scale_interface_helper.get_coordinate_key_for_expression(
                coordinate=float(y._value)
            )
        )
        scale_y: Number = self._scale_y_from_point.get(
            key=key_exp_str, default=default_val
        )
        return scale_y

    @final
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @arg_validation_decos.is_apysc_num(arg_position_index=2)
    @add_debug_info_setting(module_name=__name__)
    def set_scale_y_from_point(self, *, scale_y: Number, y: Number) -> None:
        """
        Update a scale-y value from the given y-coordinate.

        Parameters
        ----------
        scale_y : Number
            Scale-y value to set.
        y : Number
            Y-coordinate.

        References
        ----------
        - GraphicsBase scale_from_point interfaces
            - https://simon-ritchie.github.io/apysc/en/graphics_base_scale_from_point.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> y: ap.Number = ap.Number(100)
        >>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)
        >>> rectangle.get_scale_y_from_point(y=y)
        Number(1.5)
        """
        from apysc._display import scale_interface_helper

        self._initialize_scale_y_from_point_if_not_initialized()
        key_exp_str: ExpressionString = (
            scale_interface_helper.get_coordinate_key_for_expression(
                coordinate=float(y._value)
            )
        )
        self._set_lower_scale_limit(value=scale_y)
        self._scale_y_from_point._value[key_exp_str.value] = scale_y
        self._append_scale_y_from_point_update_expression(y=y)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_scale_y_from_point_update_expression(self, *, y: Number) -> None:
        """
        Append the scale-y from the specified y-coordinate updating
        expression.

        Parameters
        ----------
        y : Number
            Y-coordinate.
        """
        from apysc._display import scale_interface_helper
        from apysc._expression import expression_data_util

        expression: str
        expression = scale_interface_helper.get_scale_updating_expression(
            coordinate=y,
            scale_dict=self._scale_y_from_point,
            interface_variable_name=self.variable_name,
            coordinate_type=scale_interface_helper.CoordinateType.Y,
        )
        expression_data_util.append_js_expression(expression=expression)

    _scale_y_from_point_snapshots: Optional[Dict[str, Dict[str, Any]]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_scale_y_from_point_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_scale_y_from_point_snapshots",
            value={**self._scale_y_from_point._value},
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
        self._scale_y_from_point._value = self._get_snapshot_val_if_exists(
            current_value=self._scale_y_from_point._value,
            snapshot_dict=self._scale_y_from_point_snapshots,
            snapshot_name=snapshot_name,
        )
