"""Class implementation for height interface.
"""

from typing import Dict
from typing import Union

from apysc._animation.animation_height_interface import \
    AnimationHeightInterface
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface


class HeightInterface(
        AnimationHeightInterface, RevertInterface, AttrLinkingInterface):

    _height: Int

    def _initialize_height_if_not_initialized(self) -> None:
        """
        Initialize _height attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_height'):
            return
        self._height = Int(0)

        self._append_height_attr_linking_setting()

    def _append_height_attr_linking_setting(self) -> None:
        """
        Append a height attribute linking setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_height_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=HeightInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._height, attr_name='height')
            self._append_attr_to_linking_stack(
                attr=self._height, attr_name='height')

    @property
    def height(self) -> Int:
        """
        Get this instance's height.

        Returns
        -------
        height : Int
            This instance's height.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> rectangle.height = ap.Int(100)
        >>> rectangle.height
        Int(100)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='height', locals_=locals(),
                module_name=__name__, class_=HeightInterface):
            from apysc._type import value_util
            self._initialize_height_if_not_initialized()
            height: ap.Int = value_util.get_copy(value=self._height)
            return height

    @height.setter
    def height(self, value: Int) -> None:
        """
        Update this instance's height.

        Parameters
        ----------
        value : int
            Height value to set.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='height', locals_=locals(),
                module_name=__name__, class_=HeightInterface):
            self._update_height_and_skip_appending_exp(value=value)
            self._height._append_incremental_calc_substitution_expression()
            self._append_height_update_expression()

            self._append_height_attr_linking_setting()

    def _append_height_update_expression(self) -> None:
        """
        Append height updating expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_height_update_expression,
                locals_=locals(),
                module_name=__name__, class_=HeightInterface):
            from apysc._type import value_util
            height_str: str = value_util.get_value_str_for_expression(
                value=self._height)
            expression: str = (
                f'{self.variable_name}.height({height_str});'
            )
            ap.append_js_expression(expression=expression)

    def _update_height_and_skip_appending_exp(
            self, *, value: Union[int, Int]) -> None:
        """
        Update height value and skip appending expression.

        Parameters
        ----------
        value : int or Int
            Height value to set.
        """
        from apysc._converter import cast
        from apysc._validation import size_validation
        self._initialize_height_if_not_initialized()
        value = cast.to_int_from_float(int_or_float=value)
        size_validation.validate_size_is_int(size=value)
        size_validation.validate_size_is_gte_zero(size=value)
        if isinstance(value, int):
            value = Int(value)
        self._height = value

    _height_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_height_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_height_snapshots',
            value=int(self._height._value), snapshot_name=snapshot_name)

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
        self._height._value = self._height_snapshots[snapshot_name]
