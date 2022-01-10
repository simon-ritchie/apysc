"""Class implementation for the x-coordinate interface.
"""

from typing import Dict

from apysc._animation.animation_move_interface import AnimationMoveInterface
from apysc._animation.animation_x_interface import AnimationXInterface
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface


class XInterface(
        AnimationXInterface, AnimationMoveInterface, RevertInterface,
        AttrLinkingInterface):

    _x: Int

    def _initialize_x_if_not_initialized(self) -> None:
        """
        Initialize the _x attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_x'):
            return
        self._x = Int(0)

        self._append_x_attr_linking_setting()

    def _append_x_attr_linking_setting(self) -> None:
        """
        Append a x attribute linking setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_x_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=XInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._x, attr_name='x')
            self._append_attr_to_linking_stack(
                attr=self._x, attr_name='x')

    @property
    def x(self) -> Int:
        """
        Get a x-coordinate.

        Returns
        -------
        x : Int
            X-coordinate.

        References
        ----------
        - Display object x and y interfaces document
            - https://bit.ly/2ToA5ba

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> rectangle.x = ap.Int(100)
        >>> rectangle.x
        Int(100)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='x', locals_=locals(),
                module_name=__name__, class_=XInterface):
            from apysc._type import value_util
            self._initialize_x_if_not_initialized()
            x: ap.Int = value_util.get_copy(value=self._x)
            return x

    @x.setter
    def x(self, value: Int) -> None:
        """
        Update x-coordinate.

        Parameters
        ----------
        value : int or Int
            X-coordinate value.

        References
        ----------
        - Display object x and y interfaces document
            - https://bit.ly/2ToA5ba
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='x', locals_=locals(),
                module_name=__name__, class_=XInterface):
            from apysc._type.number_value_interface import NumberValueInterface
            from apysc._validation import number_validation
            if not isinstance(value, NumberValueInterface):
                number_validation.validate_integer(integer=value)
                value = ap.Int(value=value)
            self._x = value
            self._x._append_incremental_calc_substitution_expression()
            self._append_x_update_expression()

            self._append_x_attr_linking_setting()

    def _append_x_update_expression(self) -> None:
        """
        Append the x position updating expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_x_update_expression, locals_=locals(),
                module_name=__name__, class_=XInterface):
            from apysc._type import value_util
            self._initialize_x_if_not_initialized()
            value_str: str = value_util.get_value_str_for_expression(
                value=self._x)
            expression: str = (
                f'{self.variable_name}.x({value_str});'
            )
            ap.append_js_expression(expression=expression)

    _x_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_x_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_x_snapshots',
            value=int(self._x._value), snapshot_name=snapshot_name)

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
        self._x._value = self._x_snapshots[snapshot_name]
