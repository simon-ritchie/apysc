"""Class implementation for the rotation_around_point interface.
"""

from typing import Any
from typing import Dict

import apysc as ap
from apysc._animation.animation_rotation_around_point_interface import \
    AnimationRotationAroundPointInterface
from apysc._type.revert_interface import RevertInterface


class RotationAroundPointInterface(
        AnimationRotationAroundPointInterface, RevertInterface):

    _rotation_around_point: ap.Dictionary[str, ap.Int]

    def _initialize_rotation_around_point_if_not_initialized(self) -> None:
        """
        Initialize the `_rotation_around_point` attribute if it hasn't
        been initialized yet.
        """
        if hasattr(self, '_rotation_around_point'):
            return
        self._rotation_around_point = ap.Dictionary({})

    def get_rotation_around_point(self, x: ap.Int, y: ap.Int) -> ap.Int:
        """
        Get a rotation value around the given coordinates.

        Parameters
        ----------
        x : Int
            X-coordinate.
        y : Int
            Y-coordinate.

        Returns
        -------
        rotation : Int
            Rotation value around the given coordinates.

        References
        ----------
        - GraphicsBase rotate_around_point interfaces document
            - https://bit.ly/37TDwKs
        """
        with ap.DebugInfo(
                callable_=self.get_rotation_around_point, locals_=locals(),
                module_name=__name__, class_=RotationAroundPointInterface):
            from apysc._display import rotation_interface_helper
            from apysc._type.expression_string import ExpressionString
            from apysc._validation import number_validation
            number_validation.validate_integer(integer=x)
            number_validation.validate_integer(integer=y)
            self._initialize_rotation_around_point_if_not_initialized()
            default_val: ap.Int = ap.Int(0)
            key_exp_str: ExpressionString = rotation_interface_helper.\
                get_coordinates_key_for_expression(
                    x=int(x._value), y=int(y._value))
            rotation: ap.Int = self._rotation_around_point.get(
                key=key_exp_str, default=default_val)
            return rotation

    def set_rotation_around_point(
            self, rotation: ap.Int, x: ap.Int, y: ap.Int) -> None:
        """
        Update a rotation value around the given coordinates.

        Parameters
        ----------
        rotation : Int
            Rotation value to set.
        x : Int
            X-coordinate.
        y : Int
            Y-coordinate.

        References
        ----------
        - GraphicsBase rotate_around_point interfaces document
            - https://bit.ly/37TDwKs
        """
        with ap.DebugInfo(
                callable_=self.set_rotation_around_point, locals_=locals(),
                module_name=__name__, class_=RotationAroundPointInterface):
            from apysc._display import rotation_interface_helper
            from apysc._type.expression_string import ExpressionString
            from apysc._validation import number_validation
            number_validation.validate_integer(integer=rotation)
            number_validation.validate_integer(integer=x)
            number_validation.validate_integer(integer=y)
            self._initialize_rotation_around_point_if_not_initialized()
            key_exp_str: ExpressionString = rotation_interface_helper.\
                get_coordinates_key_for_expression(
                    x=int(x._value), y=int(y._value))
            self._rotation_around_point._value[key_exp_str.value] = rotation
            self._append_rotation_around_point_update_expression(
                rotation=rotation, x=x, y=y)

    def _append_rotation_around_point_update_expression(
            self, rotation: ap.Int, x: ap.Int, y: ap.Int) -> None:
        """
        Append a rotation value around the given coordinates
        updating expression.

        Parameters
        ----------
        rotation : Int
            Rotation value to set.
        x : Int
            X-coordinate.
        y : Int
            Y-coordinate.
        """
        with ap.DebugInfo(
                callable_=self._append_rotation_around_point_update_expression,  # noqa
                locals_=locals(),
                module_name=__name__, class_=RotationAroundPointInterface):
            expression: str = \
                self._get_rotation_around_point_updating_expression(
                    rotation=rotation, x=x, y=y)
            ap.append_js_expression(expression=expression)

    def _get_rotation_around_point_updating_expression(
            self, rotation: ap.Int, x: ap.Int, y: ap.Int) -> str:
        """
        Get a rotation value around the given coordinates updating
        expression string.

        Parameters
        ----------
        rotation : Int
            Rotation value to set.
        x : Int
            X-coordinate.
        y : Int
            Y-coordinate.

        Returns
        -------
        expression : str
            A rotation value around the given coordinates updating
            expression string.
        """
        from apysc._display import rotation_interface_helper
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._type import value_util
        from apysc._type.expression_string import ExpressionString
        self._initialize_rotation_around_point_if_not_initialized()
        before_value_str: str = expression_variables_util.\
            get_next_variable_name(type_name=var_names.INT)
        key_exp_str: ExpressionString = rotation_interface_helper.\
            get_coordinates_key_for_expression(x=x, y=y)
        after_value_str: str = value_util.get_value_str_for_expression(
            value=rotation)
        x_value_str: str = value_util.get_value_str_for_expression(
            value=x)
        y_value_str: str = value_util.get_value_str_for_expression(
            value=y)
        rotation_around_point_value_str: str = value_util.\
            get_value_str_for_expression(
                value=self._rotation_around_point)
        expression: str = (
            f'if ({key_exp_str.value} in '
            f'{rotation_around_point_value_str}) {{'
            f'\n  var {before_value_str} = '
            f'{rotation_around_point_value_str}[{key_exp_str.value}];'
            '\n}else {'
            f'\n  {before_value_str} = 0;'
            '\n}'
            f'\n{self.variable_name}.rotate('
            f'-{before_value_str}, {x_value_str}, {y_value_str});'
            f'\n{self.variable_name}.rotate('
            f'{after_value_str}, {x_value_str}, {y_value_str});'
            f'\n{rotation_around_point_value_str}[{key_exp_str.value}] = '
            f'{after_value_str};'
        )
        return expression

    _rotation_around_point_snapshots: Dict[str, Dict[str, Any]]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_rotation_around_point_snapshots'):
            self._rotation_around_point_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_rotation_around_point_if_not_initialized()
        self._rotation_around_point_snapshots[snapshot_name] = {
            **self._rotation_around_point._value}

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert a value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._rotation_around_point._value = \
            self._rotation_around_point_snapshots[snapshot_name]
