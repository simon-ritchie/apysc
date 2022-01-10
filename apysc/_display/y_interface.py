"""Class implementation for the y-coordinate interface.
"""

from typing import Dict

from apysc._animation.animation_move_interface import AnimationMoveInterface
from apysc._animation.animation_y_interface import AnimationYInterface
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface


class YInterface(
        AnimationYInterface, AnimationMoveInterface, RevertInterface,
        AttrLinkingInterface):

    _y: Int

    def _initialize_y_if_not_initialized(self) -> None:
        """
        Initialize the _y attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_y'):
            return
        self._y = Int(0)

        self._append_y_attr_linking_setting()

    def _append_y_attr_linking_setting(self) -> None:
        """
        Append a y attribute linking setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_y_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=YInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._y, attr_name='y')
            self._append_attr_to_linking_stack(
                attr=self._y, attr_name='y')

    @property
    def y(self) -> Int:
        """
        Get a y-coordinate.

        Returns
        -------
        y : Int
            Y-coordinate.

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
        >>> rectangle.y = ap.Int(100)
        >>> rectangle.y
        Int(100)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='y', locals_=locals(),
                module_name=__name__, class_=YInterface):
            from apysc._type import value_util
            self._initialize_y_if_not_initialized()
            y: ap.Int = value_util.get_copy(value=self._y)
            return y

    @y.setter
    def y(self, value: Int) -> None:
        """
        Update y-coordinate.

        Parameters
        ----------
        value : int or Int
            Y-coordinate value.

        References
        ----------
        - Display object x and y interfaces document
            - https://bit.ly/2ToA5ba
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='y', locals_=locals(),
                module_name=__name__, class_=YInterface):
            from apysc._type.number_value_interface import NumberValueInterface
            from apysc._validation import number_validation
            if not isinstance(value, NumberValueInterface):
                number_validation.validate_integer(integer=value)
                value = ap.Int(value=value)
            self._y = value
            self._y._append_incremental_calc_substitution_expression()
            self._append_y_update_expression()

            self._append_y_attr_linking_setting()

    def _append_y_update_expression(self) -> None:
        """
        Append y position updating expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_y_update_expression, locals_=locals(),
                module_name=__name__, class_=YInterface):
            from apysc._type import value_util
            self._initialize_y_if_not_initialized()
            value_str: str = value_util.get_value_str_for_expression(
                value=self._y)
            expression: str = (
                f'{self.variable_name}.y({value_str});'
            )
            ap.append_js_expression(expression=expression)

    _y_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_y_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_y_snapshots',
            value=int(self._y._value), snapshot_name=snapshot_name)

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
        self._y._value = self._y_snapshots[snapshot_name]
