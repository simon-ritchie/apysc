"""Class implementation for the scale_x_from_point interface.
"""


from typing import Union
import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class ScaleXFromPointInterface(VariableNameInterface, RevertInterface):

    _scale_x_from_point: ap.Dictionary

    def _initialize_scale_x_from_point_if_not_initialized(self) -> None:
        """
        Initialize the `_scale_x_from_points` attribute if it hasn't been
        initialized_yet.
        """
        if hasattr(self, '_scale_x_from_point'):
            return
        self._scale_x_from_point = ap.Dictionary({})

    def get_scale_x_from_point(
            self,
            x: ap.Int,
            y: ap.Int) -> ap.Number:
        """
        Get a scale-x value from the given point.

        Parameters
        ----------
        x : Int
            X-coordinate.
        y : Int
            Y-coordinate.

        Returns
        -------
        scale_x : ap.Number
            Scale-x value from the given point.
        """
        with ap.DebugInfo(
                callable_=self.get_scale_x_from_point, locals_=locals(),
                module_name=__name__, class_=ScaleXFromPointInterface):
            from apysc._display import scale_interface_helper
            from apysc._validation import number_validation
            from apysc._type.expression_string import ExpressionString
            number_validation.validate_integer(integer=x)
            number_validation.validate_integer(integer=y)
            self._initialize_scale_x_from_point_if_not_initialized()
            default_val: ap.Number = ap.Number(1.0)
            key_exp_str: ExpressionString = scale_interface_helper.\
                get_point_key_for_expression(x=x, y=y)
            scale_x: ap.Number = self._scale_x_from_point.get(
                key=key_exp_str, default=default_val)
            return scale_x

    def set_scale_x_from_point(
            self, scale_x: ap.Number,
            x: ap.Int,
            y: ap.Int) -> None:
        """
        Update a scale-x value from the given point.

        Parameters
        ----------
        scale_x : Number
            Scale-x value to set.
        x : Int
            X-coordinate.
        y : Int
            Y-coordinate.
        """
        with ap.DebugInfo(
                callable_=self.set_scale_x_from_point, locals_=locals(),
                module_name=__name__, class_=ScaleXFromPointInterface):
            from apysc._display import scale_interface_helper
            from apysc._validation import number_validation
            from apysc._type.expression_string import ExpressionString
            number_validation.validate_num(num=scale_x)
            number_validation.validate_integer(integer=x)
            number_validation.validate_integer(integer=y)
            self._initialize_scale_x_from_point_if_not_initialized()
            key_exp_str: ExpressionString = scale_interface_helper.\
                get_point_key_for_expression(x=x, y=y)
            before_value: ap.Number = self._scale_x_from_point[
                key_exp_str.value]
            self._scale_x_from_point._value[key_exp_str.value] = scale_x
            self._append_scale_x_from_point_update_expression(
                before_value=before_value, x=x, y=y)

    def _append_scale_x_from_point_update_expression(
            self, before_value: ap.Number, x: ap.Int, y: ap.Int) -> None:
        """
        Append the scale-x from the specified point updating expression.

        Parameters
        ----------
        before_value : ap.Number
            Before updating value.
        """
        with ap.DebugInfo(
                callable_=self._append_scale_x_from_point_update_expression,
                locals_=locals(),
                module_name=__name__, class_=ScaleXFromPointInterface):
            from apysc._type import value_util
            from apysc._display import scale_interface_helper
            from apysc._type.expression_string import ExpressionString
            before_value_str: str = value_util.get_value_str_for_expression(
                value=before_value)
            key_exp_str: ExpressionString = scale_interface_helper.\
                get_point_key_for_expression(x=x, y=y)
            after_value_str: str = value_util.get_value_str_for_expression(
                value=self._scale_x_from_point._value[key_exp_str.value])
            x_value_str: str = value_util.get_value_str_for_expression(
                value=x)
            y_value_str: str = value_util.get_value_str_for_expression(
                value=y)
            scale_x_from_point_value_str: str = value_util.\
                get_value_str_for_expression(value=self._scale_x_from_point)
            expression: str = (
                f'{self.variable_name}.scale(1 / {before_value_str}, '
                f'1, {x_value_str}, {y_value_str});'
                f'\n{self.variable_name}.scale({after_value_str}, '
                f'1, {x_value_str}, {y_value_str});'
                f'\n{scale_x_from_point_value_str}[{key_exp_str}] = '
                f'{after_value_str};'
            )
            ap.append_js_expression(expression=expression)

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert a value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
