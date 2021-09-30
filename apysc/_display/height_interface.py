"""Class implementation for height interface.
"""

from typing import Dict
from typing import Union

import apysc as ap
from apysc._animation.animation_height_interface import \
    AnimationHeightInterface
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.revert_interface import RevertInterface


class HeightInterface(
        AnimationHeightInterface, RevertInterface, AttrLinkingInterface):

    _height: ap.Int

    def _initialize_height_if_not_initialized(self) -> None:
        """
        Initialize _height attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_height'):
            return
        self._height = ap.Int(0)

        self._append_height_attr_linking_setting()

    def _append_height_attr_linking_setting(self) -> None:
        """
        Append a height attribute linking setting.
        """
        with ap.DebugInfo(
                callable_=self._append_height_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=HeightInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._height, attr_name='height')
            self._append_attr_to_linking_stack(
                attr=self._height, attr_name='height')

    @property
    def height(self) -> ap.Int:
        """
        Get this instance's height.

        Returns
        -------
        height : Int
            This instance's height.
        """
        with ap.DebugInfo(
                callable_='height', locals_=locals(),
                module_name=__name__, class_=HeightInterface):
            from apysc._type import value_util
            self._initialize_height_if_not_initialized()
            height: ap.Int = value_util.get_copy(value=self._height)
            return height

    @height.setter
    def height(self, value: ap.Int) -> None:
        """
        Update this instance's height.

        Parameters
        ----------
        value : int
            Height value to set.
        """
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
            self, value: Union[int, ap.Int]) -> None:
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
            value = ap.Int(value)
        self._height = value

    _height_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_height_snapshots'):
            self._height_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_height_if_not_initialized()
        self._height_snapshots[snapshot_name] = int(self._height._value)

    def _revert(self, snapshot_name: str) -> None:
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
