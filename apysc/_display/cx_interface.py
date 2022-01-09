"""Class implementation for the center x-coordinate interface.
"""

from typing import Dict

from apysc._animation.animation_cx_interface import AnimationCxInterface
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface


class CxInterface(
        AnimationCxInterface, RevertInterface, AttrLinkingInterface):

    _cx: Int

    def _initialize_cx_if_not_initialized(self) -> None:
        """
        Initialize _cx attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_cx'):
            return
        self._cx = Int(0)

        self._append_cx_attr_linking_setting()

    def _append_cx_attr_linking_setting(self) -> None:
        """
        Append a cx attribute linking setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_cx_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=CxInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._cx, attr_name='cx')
            self._append_attr_to_linking_stack(attr=self._cx, attr_name='cx')

    @property
    def x(self) -> Int:
        """
        Get a center x-coordinate.

        Returns
        -------
        x : Int
            Center x-coordinate.

        References
        ----------
        - Display object x and y interfaces document
            - https://bit.ly/3q7GFQM

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
        >>> circle: ap.Circle = sprite.graphics.draw_circle(
        ...     x=100, y=100, radius=50)
        >>> circle.x = ap.Int(120)
        >>> circle.x
        Int(120)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='x', locals_=locals(),
                module_name=__name__, class_=CxInterface):
            from apysc._type import value_util
            self._initialize_cx_if_not_initialized()
            x: ap.Int = value_util.get_copy(value=self._cx)
            return x

    @x.setter
    def x(self, value: Int) -> None:
        """
        Update a center x-coordinate.

        Parameters
        ----------
        value : int or Int
            Center x-coordinate value.

        References
        ----------
        - Display object x and y interfaces document
            - https://bit.ly/3q7GFQM
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='x', locals_=locals(),
                module_name=__name__, class_=CxInterface):
            from apysc._validation import number_validation
            number_validation.validate_integer(integer=value)
            if not isinstance(value, ap.Int):
                value = ap.Int(value)
            self._cx = value
            self._cx._append_incremental_calc_substitution_expression()
            self._append_cx_update_expression()

            self._append_cx_attr_linking_setting()

    def _append_cx_update_expression(self) -> None:
        """
        Append cx position updating expression.
        """
        import apysc as ap
        from apysc._type import value_util
        self._initialize_cx_if_not_initialized()
        value_str: str = value_util.get_value_str_for_expression(
            value=self._cx)
        expression: str = (
            f'{self.variable_name}.cx({value_str});'
        )
        ap.append_js_expression(expression=expression)

    _cx_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_cx_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_cx_snapshots',
            value=int(self._cx._value), snapshot_name=snapshot_name)

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
        self._cx._value = self._cx_snapshots[snapshot_name]
