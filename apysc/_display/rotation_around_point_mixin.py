"""Class implementation for the rotation_around_point mix-in.
"""

from typing import Any
from typing import Dict
from typing import Optional

from typing_extensions import final

from apysc._animation.animation_rotation_around_point_mixin import (
    AnimationRotationAroundPointMixIn,
)
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.dictionary import Dictionary
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos


class RotationAroundPointMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    AnimationRotationAroundPointMixIn,
    RevertMixIn,
):
    _rotation_around_point: Dictionary[str, Int]

    @final
    def _initialize_rotation_around_point_if_not_initialized(self) -> None:
        """
        Initialize the `_rotation_around_point` attribute
        if this interface does not initialize it yet.
        """
        if hasattr(self, "_rotation_around_point"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="rotation_around_point"
        )
        self._rotation_around_point = Dictionary(
            {},
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def get_rotation_around_point(self, *, x: Number, y: Number) -> Int:
        """
        Get a rotation value around the given coordinates.

        Parameters
        ----------
        x : Number
            X-coordinate.
        y : Number
            Y-coordinate.

        Returns
        -------
        rotation : Int
            Rotation value around the given coordinates.

        References
        ----------
        - GraphicsBase rotate_around_point interfaces
            - https://simon-ritchie.github.io/apysc/en/graphics_base_rotation_around_point.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> x: ap.Number = ap.Number(100)
        >>> y: ap.Number = ap.Number(100)
        >>> rectangle.set_rotation_around_point(rotation=ap.Int(45), x=x, y=y)
        >>> rectangle.get_rotation_around_point(x=x, y=y)
        Int(45)
        """
        from apysc._display import rotation_interface_helper
        from apysc._type.expression_string import ExpressionString

        self._initialize_rotation_around_point_if_not_initialized()
        default_val: Int = Int(0)
        key_exp_str: ExpressionString = (
            rotation_interface_helper.get_coordinates_key_for_expression(
                x=float(x._value), y=float(y._value)
            )
        )
        rotation: Int = self._rotation_around_point.get(
            key=key_exp_str, default=default_val
        )
        return rotation

    @final
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @arg_validation_decos.is_num(arg_position_index=3, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def set_rotation_around_point(self, *, rotation: Int, x: Number, y: Number) -> None:
        """
        Update a rotation value around the given coordinates.

        Parameters
        ----------
        rotation : Int
            Rotation value to set.
        x : Number
            X-coordinate.
        y : Number
            Y-coordinate.

        References
        ----------
        - GraphicsBase rotate_around_point interfaces
            - https://simon-ritchie.github.io/apysc/en/graphics_base_rotation_around_point.html  # noqa
        """
        from apysc._display import rotation_interface_helper
        from apysc._type.expression_string import ExpressionString

        self._initialize_rotation_around_point_if_not_initialized()
        key_exp_str: ExpressionString = (
            rotation_interface_helper.get_coordinates_key_for_expression(
                x=int(x._value), y=int(y._value)
            )
        )
        self._rotation_around_point._value[key_exp_str.value] = rotation
        self._append_rotation_around_point_update_expression(
            rotation=rotation, x=x, y=y
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_rotation_around_point_update_expression(
        self, *, rotation: Int, x: Number, y: Number
    ) -> None:
        """
        Append a rotation value around the given coordinates
        updating expression.

        Parameters
        ----------
        rotation : Int
            Rotation value to set.
        x : Number
            X-coordinate.
        y : Number
            Y-coordinate.
        """
        from apysc._expression import expression_data_util

        expression: str = self._get_rotation_around_point_updating_expression(
            rotation=rotation, x=x, y=y
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    def _get_rotation_around_point_updating_expression(
        self, *, rotation: Int, x: Number, y: Number
    ) -> str:
        """
        Get a rotation value around the given coordinates'
        updating expression string.

        Parameters
        ----------
        rotation : Int
            Rotation value to set.
        x : Number
            X-coordinate.
        y : Number
            Y-coordinate.

        Returns
        -------
        expression : str
            A rotation value around the given coordinates'
            updating expression string.
        """
        from apysc._display import rotation_interface_helper
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._type import value_util
        from apysc._type.expression_string import ExpressionString

        self._initialize_rotation_around_point_if_not_initialized()
        before_value_str: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.INT
        )
        key_exp_str: ExpressionString = (
            rotation_interface_helper.get_coordinates_key_for_expression(x=x, y=y)
        )
        after_value_str: str = value_util.get_value_str_for_expression(value=rotation)
        x_value_str: str = value_util.get_value_str_for_expression(value=x)
        y_value_str: str = value_util.get_value_str_for_expression(value=y)
        rotation_around_point_value_str: str = value_util.get_value_str_for_expression(
            value=self._rotation_around_point
        )
        expression: str = (
            f"if ({key_exp_str.value} in "
            f"{rotation_around_point_value_str}) {{"
            f"\n  var {before_value_str} = "
            f"{rotation_around_point_value_str}[{key_exp_str.value}];"
            "\n}else {"
            f"\n  {before_value_str} = 0;"
            "\n}"
            f"\n{self.variable_name}.rotate("
            f"-{before_value_str}, {x_value_str}, {y_value_str});"
            f"\n{self.variable_name}.rotate("
            f"{after_value_str}, {x_value_str}, {y_value_str});"
            f"\n{rotation_around_point_value_str}[{key_exp_str.value}] = "
            f"{after_value_str};"
        )
        return expression

    _rotation_around_point_snapshots: Optional[Dict[str, Dict[str, Any]]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_rotation_around_point_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_rotation_around_point_snapshots",
            value={**self._rotation_around_point._value},
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
        self._rotation_around_point._value = self._get_snapshot_val_if_exists(
            current_value=self._rotation_around_point._value,
            snapshot_dict=self._rotation_around_point_snapshots,
            snapshot_name=snapshot_name,
        )
