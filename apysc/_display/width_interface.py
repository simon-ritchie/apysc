"""Class implementation for witdth interface.
"""

from typing import Dict
from typing import Union

from apysc._animation.animation_width_interface import AnimationWidthInterface
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface


class WidthInterface(
        AnimationWidthInterface, RevertInterface, AttrLinkingInterface):

    _width: Int

    def _initialize_width_if_not_initialized(self) -> None:
        """
        Initialize _width attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_width'):
            return
        self._width = Int(0)

        self._append_width_attr_linking_setting()

    def _append_width_attr_linking_setting(self) -> None:
        """
        Append a width attribute linking setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_width_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=WidthInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._width, attr_name='width')
            self._append_attr_to_linking_stack(
                attr=self._width, attr_name='width')

    @property
    def width(self) -> Int:
        """
        Get this instance's width.

        Returns
        -------
        width : Int
            This instance's width.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> rectangle.width = ap.Int(100)
        >>> rectangle.width
        Int(100)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='width', locals_=locals(),
                module_name=__name__, class_=WidthInterface):
            from apysc._type import value_util
            self._initialize_width_if_not_initialized()
            width: ap.Int = value_util.get_copy(value=self._width)
            return width

    @width.setter
    def width(self, value: Int) -> None:
        """
        Update this instance's width.

        Parameters
        ----------
        value : Int
            Width value to set.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='width', locals_=locals(),
                module_name=__name__, class_=WidthInterface):
            self._update_width_and_skip_appending_exp(value=value)
            self._width._append_incremental_calc_substitution_expression()
            self._append_width_update_expression()

            self._append_width_attr_linking_setting()

    def _append_width_update_expression(self) -> None:
        """
        Append width updating expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_width_update_expression,
                locals_=locals(),
                module_name=__name__, class_=WidthInterface):
            from apysc._type import value_util
            width_str: str = value_util.get_value_str_for_expression(
                value=self._width)
            expression: str = (
                f'{self.variable_name}.width({width_str});'
            )
            ap.append_js_expression(expression=expression)

    def _update_width_and_skip_appending_exp(
            self, *, value: Union[int, Int]) -> None:
        """
        Update width value and skip appending expression.

        Parameters
        ----------
        value : int or Int
            Width value to set.
        """
        from apysc._converter import cast
        from apysc._validation import size_validation
        self._initialize_width_if_not_initialized()
        value = cast.to_int_from_float(int_or_float=value)
        size_validation.validate_size_is_int(size=value)
        size_validation.validate_size_is_gte_zero(size=value)
        if isinstance(value, int):
            value = Int(value)
        self._width = value

    _width_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_width_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_width_snapshots',
            value=int(self._width._value), snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._width._value = self._width_snapshots[snapshot_name]
