"""Class implementation for the scale_x_from_point interfaces.
"""

from typing import Any
from typing import Dict

import apysc as ap
from apysc._animation.animation_scale_x_from_point_interface import \
    AnimationScaleXFromPointInterface
from apysc._type.revert_interface import RevertInterface


class ScaleXFromPointInterface(
        AnimationScaleXFromPointInterface, RevertInterface):

    _scale_x_from_point: ap.Dictionary[str, ap.Number]

    def _initialize_scale_x_from_point_if_not_initialized(self) -> None:
        """
        Initialize the `_scale_x_from_point` attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_scale_x_from_point'):
            return
        self._scale_x_from_point = ap.Dictionary({})

    def get_scale_x_from_point(self, x: ap.Int) -> ap.Number:
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

        References
        ----------
        - GraphicsBase scale_from_point interfaces document
            - https://bit.ly/3xRBhlw
        """
        with ap.DebugInfo(
                callable_=self.get_scale_x_from_point, locals_=locals(),
                module_name=__name__, class_=ScaleXFromPointInterface):
            from apysc._display import scale_interface_helper
            from apysc._type.expression_string import ExpressionString
            from apysc._validation import number_validation
            number_validation.validate_integer(integer=x)
            self._initialize_scale_x_from_point_if_not_initialized()
            default_val: ap.Number = ap.Number(1.0)
            key_exp_str: ExpressionString = scale_interface_helper.\
                get_coordinate_key_for_expression(coordinate=int(x._value))
            scale_x: ap.Number = self._scale_x_from_point.get(
                key=key_exp_str, default=default_val)
            return scale_x

    def set_scale_x_from_point(self, scale_x: ap.Number, x: ap.Int) -> None:
        """
        Update a scale-x value from the given x-coordinate.

        Parameters
        ----------
        scale_x : Number
            Scale-x value to set.
        x : Int
            X-coordinate.

        References
        ----------
        - GraphicsBase scale_from_point interfaces document
            - https://bit.ly/3xRBhlw
        """
        with ap.DebugInfo(
                callable_=self.set_scale_x_from_point, locals_=locals(),
                module_name=__name__, class_=ScaleXFromPointInterface):
            from apysc._display import scale_interface_helper
            from apysc._type.expression_string import ExpressionString
            from apysc._validation import number_validation
            number_validation.validate_num(num=scale_x)
            number_validation.validate_integer(integer=x)
            self._initialize_scale_x_from_point_if_not_initialized()
            key_exp_str: ExpressionString = scale_interface_helper.\
                get_coordinate_key_for_expression(coordinate=int(x._value))
            self._scale_x_from_point._value[key_exp_str.value] = scale_x
            self._append_scale_x_from_point_update_expression(x=x)

    def _append_scale_x_from_point_update_expression(
            self, x: ap.Int) -> None:
        """
        Append the scale-x from the specified x-coordinate updating
        expression.

        Parameters
        ----------
        x : Int
            X-coordinate.
        """
        with ap.DebugInfo(
                callable_=self._append_scale_x_from_point_update_expression,
                locals_=locals(),
                module_name=__name__, class_=ScaleXFromPointInterface):
            from apysc._display import scale_interface_helper
            expression: str
            expression = scale_interface_helper.get_scale_updating_expression(
                coordinate=x,
                scale_dict=self._scale_x_from_point,
                interface_variable_name=self.variable_name,
                coordinate_type=scale_interface_helper.CoordinateType.X)
            ap.append_js_expression(expression=expression)

    _scale_x_from_point_snapshots: Dict[str, Dict[str, Any]]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_scale_x_from_point_snapshots'):
            self._scale_x_from_point_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_scale_x_from_point_if_not_initialized()
        self._scale_x_from_point_snapshots[snapshot_name] = {
            **self._scale_x_from_point._value}

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
        self._scale_x_from_point._value = self._scale_x_from_point_snapshots[
            snapshot_name]
