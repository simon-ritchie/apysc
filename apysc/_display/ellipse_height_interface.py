"""Class implementation for the ellipse height interface.
"""

from typing import Dict

from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class EllipseHeightInterface(
        VariableNameInterface, RevertInterface, AttrLinkingInterface):

    _ellipse_height: Int

    def _initialize_ellipse_height_if_not_initialized(self) -> None:
        """
        Initialize _ellipse_height attribute if it hasn't
        been initialized yet.
        """
        if hasattr(self, '_ellipse_height'):
            return
        self._ellipse_height = Int(0)

        self._append_ellipse_height_attr_linking_setting()

    def _append_ellipse_height_attr_linking_setting(self) -> None:
        """
        Append a ellipse-height attribute linking setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_ellipse_height_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=EllipseHeightInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._ellipse_height, attr_name='ellipse_height')
            self._append_attr_to_linking_stack(
                attr=self._ellipse_height, attr_name='ellipse_height')

    @property
    def ellipse_height(self) -> Int:
        """
        Get ellipse height value.

        Returns
        -------
        ellipse_height : Int
            Ellipse height value.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> rectangle.ellipse_width = ap.Int(10)
        >>> rectangle.ellipse_height = ap.Int(15)
        >>> rectangle.ellipse_height
        Int(15)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='ellipse_height', locals_=locals(),
                module_name=__name__, class_=EllipseHeightInterface):
            from apysc._type import value_util
            self._initialize_ellipse_height_if_not_initialized()
            return value_util.get_copy(value=self._ellipse_height)

    @ellipse_height.setter
    def ellipse_height(self, value: Int) -> None:
        """
        Update ellipse height value.

        Parameters
        ----------
        value : int or Int
            Ellipse height value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='ellipse_height', locals_=locals(),
                module_name=__name__, class_=EllipseHeightInterface):
            from apysc._validation import number_validation
            number_validation.validate_integer(integer=value)
            if isinstance(value, int):
                value = ap.Int(value)
            self._ellipse_height = value
            self._ellipse_height.\
                _append_incremental_calc_substitution_expression()
            self._append_ellipse_height_update_expression()

            self._append_ellipse_height_attr_linking_setting()

    def _append_ellipse_height_update_expression(self) -> None:
        """
        Append ellipse height updating expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_ellipse_height_update_expression,
                locals_=locals(),
                module_name=__name__, class_=EllipseHeightInterface):
            from apysc._type import value_util
            self._initialize_ellipse_height_if_not_initialized()
            if hasattr(self, '_ellipse_width'):
                width_value_str: str = value_util.get_value_str_for_expression(
                    value=getattr(self, '_ellipse_width'))
            else:
                width_value_str = value_util.get_value_str_for_expression(
                    value=0)
            height_value_str: str = value_util.get_value_str_for_expression(
                value=self._ellipse_height)
            expression: str = (
                f'{self.variable_name}.radius({width_value_str}, '
                f'{height_value_str});'
            )
            ap.append_js_expression(expression=expression)

    _ellipse_height_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make the value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_ellipse_height_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_ellipse_height_snapshots',
            value=int(self._ellipse_height._value),
            snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert the value if the snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._ellipse_height._value = self._ellipse_height_snapshots[
            snapshot_name]
