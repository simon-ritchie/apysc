"""Class implementation for the scale_y_from_point interfaces.
"""

from typing import Any
from typing import Dict

import apysc as ap
from apysc._animation.animation_scale_y_from_point_interface import \
    AnimationScaleYFromPointInterface
from apysc._type.expression_string import ExpressionString
from apysc._type.revert_interface import RevertInterface


class ScaleYFromPointInterface(
        AnimationScaleYFromPointInterface, RevertInterface):

    _scale_y_from_point: ap.Dictionary[str, ap.Number]

    def _initialize_scale_y_from_point_if_not_initialized(self) -> None:
        """
        Initialize the `_scale_y_from_point` attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_scale_y_from_point'):
            return
        self._scale_y_from_point = ap.Dictionary({})

    def get_scale_y_from_point(self, y: ap.Int) -> ap.Number:
        """
        Get a scale-y value from the given y-coordinate.

        Parameters
        ----------
        y : Int
            Y-coordinate.

        Returns
        -------
        scale_y : ap.Number
            Scale-y value from the given y-coordinate.

        References
        ----------
        - GraphicsBase scale_from_point interfaces document
            - https://bit.ly/3xRBhlw
        """
        with ap.DebugInfo(
                callable_=self.get_scale_y_from_point, locals_=locals(),
                module_name=__name__, class_=ScaleYFromPointInterface):
            from apysc._display import scale_interface_helper
            from apysc._validation import number_validation
            number_validation.validate_integer(integer=y)
            self._initialize_scale_y_from_point_if_not_initialized()
            default_val: ap.Number = ap.Number(1.0)
            key_exp_str: ExpressionString = scale_interface_helper.\
                get_coordinate_key_for_expression(coordinate=int(y._value))
            scale_y: ap.Number = self._scale_y_from_point.get(
                key=key_exp_str, default=default_val)
            return scale_y

    def set_scale_y_from_point(self, scale_y: ap.Number, y: ap. Int) -> None:
        """
        Update a scale-y value from the given y-coordinate.

        Parameters
        ----------
        scale_y : Number
            Scale-y value to set.
        y : Int
            Y-coordinate.

        References
        ----------
        - GraphicsBase scale_from_point interfaces document
            - https://bit.ly/3xRBhlw
        """
        with ap.DebugInfo(
                callable_=self.set_scale_y_from_point, locals_=locals(),
                module_name=__name__, class_=ScaleYFromPointInterface):
            from apysc._display import scale_interface_helper
            from apysc._validation import number_validation
            number_validation.validate_num(num=scale_y)
            number_validation.validate_integer(integer=y)
            self._initialize_scale_y_from_point_if_not_initialized()
            key_exp_str: ExpressionString = scale_interface_helper.\
                get_coordinate_key_for_expression(coordinate=int(y._value))
            self._scale_y_from_point._value[key_exp_str.value] = scale_y
            self._append_scale_y_from_point_update_expression(y=y)

    def _append_scale_y_from_point_update_expression(
            self, y: ap.Int) -> None:
        """
        Append the scale-y from the specified y-coordinate updating
        expression.

        Parameters
        ----------
        y : Int
            Y-coordinate.
        """
        with ap.DebugInfo(
                callable_=self.set_scale_y_from_point, locals_=locals(),
                module_name=__name__, class_=ScaleYFromPointInterface):
            from apysc._display import scale_interface_helper
            expression: str
            expression = scale_interface_helper.get_scale_updating_expression(
                coordinate=y,
                scale_dict=self._scale_y_from_point,
                interface_variable_name=self.variable_name,
                coordinate_type=scale_interface_helper.CoordinateType.Y)
            ap.append_js_expression(expression=expression)

    _scale_y_from_point_snapshots: Dict[str, Dict[str, Any]]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_scale_y_from_point_snapshots'):
            self._scale_y_from_point_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_scale_y_from_point_if_not_initialized()
        self._scale_y_from_point_snapshots[snapshot_name] = {
            **self._scale_y_from_point._value}

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
        self._scale_y_from_point._value = self._scale_y_from_point_snapshots[
            snapshot_name]
