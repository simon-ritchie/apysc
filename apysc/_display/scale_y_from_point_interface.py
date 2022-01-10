"""Class implementation for the scale_y_from_point interfaces.
"""

from typing import Any
from typing import Dict

from apysc._animation.animation_scale_y_from_point_interface import \
    AnimationScaleYFromPointInterface
from apysc._type.dictionary import Dictionary
from apysc._type.expression_string import ExpressionString
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.revert_interface import RevertInterface


class ScaleYFromPointInterface(
        AnimationScaleYFromPointInterface, RevertInterface):

    _scale_y_from_point: Dictionary[str, Number]

    def _initialize_scale_y_from_point_if_not_initialized(self) -> None:
        """
        Initialize the `_scale_y_from_point` attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_scale_y_from_point'):
            return
        self._scale_y_from_point = Dictionary({})

    def get_scale_y_from_point(self, y: Int) -> Number:
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

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> y: ap.Int = ap.Int(100)
        >>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)
        >>> rectangle.get_scale_y_from_point(y=y)
        Number(1.5)
        """
        import apysc as ap
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

    def set_scale_y_from_point(self, scale_y: Number, y: Int) -> None:
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

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> y: ap.Int = ap.Int(100)
        >>> rectangle.set_scale_y_from_point(scale_y=ap.Number(1.5), y=y)
        >>> rectangle.get_scale_y_from_point(y=y)
        Number(1.5)
        """
        import apysc as ap
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
            self, *, y: Int) -> None:
        """
        Append the scale-y from the specified y-coordinate updating
        expression.

        Parameters
        ----------
        y : Int
            Y-coordinate.
        """
        import apysc as ap
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

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_scale_y_from_point_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_scale_y_from_point_snapshots',
            value={**self._scale_y_from_point._value},
            snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
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
