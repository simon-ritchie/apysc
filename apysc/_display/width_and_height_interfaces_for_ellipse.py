"""Class implementation of the width and height Interfaces
for the ellipse.

Notes
-----
Subclass that inherit the normal WidthInterface and HeightInterface
can't use this interface.
"""

from typing import Dict

from apysc._animation.animation_height_for_ellipse_interface import \
    AnimationHeightForEllipseInterface
from apysc._animation.animation_width_for_ellipse_interface import \
    AnimationWidthForEllipseInterface
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface


class WidthAndHeightInterfacesForEllipse(
        AnimationWidthForEllipseInterface,
        AnimationHeightForEllipseInterface,
        RevertInterface, AttrLinkingInterface):

    _width: Int
    _height: Int

    def _initialize_width_and_height_if_not_initialized(self) -> None:
        """
        Initialize _width and _height attributes if these are not
        initialized yet.
        """
        if not hasattr(self, '_width'):
            self._width = Int(0)
            self._append_width_attr_linking_setting()
        if not hasattr(self, '_height'):
            self._height = Int(0)
            self._append_height_attr_linking_setting()

    def _append_width_attr_linking_setting(self) -> None:
        """
        Append a width attricute linking setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_width_attr_linking_setting,
                locals_=locals(),
                module_name=__name__,
                class_=WidthAndHeightInterfacesForEllipse):
            self._append_applying_new_attr_val_exp(
                new_attr=self._width, attr_name='width')
            self._append_attr_to_linking_stack(
                attr=self._width, attr_name='width')

    def _append_height_attr_linking_setting(self) -> None:
        """
        Append a height attribute linking setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_height_attr_linking_setting,
                locals_=locals(),
                module_name=__name__,
                class_=WidthAndHeightInterfacesForEllipse):
            self._append_applying_new_attr_val_exp(
                new_attr=self._height, attr_name='height')
            self._append_attr_to_linking_stack(
                attr=self._height, attr_name='height')

    @property
    def width(self) -> Int:
        """
        Get a ellipse width value.

        Returns
        -------
        width : Int
            Ellipse width.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
        ...     x=100, y=100, width=50, height=50)
        >>> ellipse.width = ap.Int(100)
        >>> ellipse.width
        Int(100)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='width', locals_=locals(),
                module_name=__name__,
                class_=WidthAndHeightInterfacesForEllipse):
            from apysc._type import value_util
            self._initialize_width_and_height_if_not_initialized()
            return value_util.get_copy(value=self._width)

    @width.setter
    def width(self, value: Int) -> None:
        """
        Update a ellipse width value.

        Parameters
        ----------
        value : int or Int
            Ellipse width value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='width', locals_=locals(),
                module_name=__name__,
                class_=WidthAndHeightInterfacesForEllipse):
            from apysc._validation import number_validation
            if not isinstance(value, ap.Int):
                number_validation.validate_integer(integer=value)
                value = ap.Int(value)
            self._width = value
            self._width._append_incremental_calc_substitution_expression()
            self._append_ellipse_width_and_height_update_expression()

            self._append_width_attr_linking_setting()

    @property
    def height(self) -> Int:
        """
        Get a ellipse height value.

        Returns
        -------
        height : Int
            Ellipse height.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
        ...     x=100, y=100, width=50, height=50)
        >>> ellipse.height = ap.Int(100)
        >>> ellipse.height
        Int(100)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='height', locals_=locals(),
                module_name=__name__,
                class_=WidthAndHeightInterfacesForEllipse):
            from apysc._type import value_util
            self._initialize_width_and_height_if_not_initialized()
            return value_util.get_copy(value=self._height)

    @height.setter
    def height(self, value: Int) -> None:
        """
        Update a ellipse height value.

        Parameters
        ----------
        value : int or Int
            Ellipse height value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='height', locals_=locals(),
                module_name=__name__,
                class_=WidthAndHeightInterfacesForEllipse):
            from apysc._validation import number_validation
            if not isinstance(value, ap.Int):
                number_validation.validate_integer(integer=value)
                value = ap.Int(value)
            self._height = value
            self._height._append_incremental_calc_substitution_expression()
            self._append_ellipse_width_and_height_update_expression()

            self._append_height_attr_linking_setting()

    def _append_ellipse_width_and_height_update_expression(self) -> None:
        """
        Append an ellipse width and height updating expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_ellipse_width_and_height_update_expression,  # noqa
                locals_=locals(),
                module_name=__name__,
                class_=WidthAndHeightInterfacesForEllipse):
            from apysc._type import value_util
            self._initialize_width_and_height_if_not_initialized()
            width_value_str: str = value_util.get_value_str_for_expression(
                value=self._width)
            height_value_str: str = value_util.get_value_str_for_expression(
                value=self._height)
            expression: str = (
                f'{self.variable_name}.radius('
                f'parseInt({width_value_str} / 2), '
                f'parseInt({height_value_str}) / 2);'
            )
            ap.append_js_expression(expression=expression)

    _width_snapshots: Dict[str, int]
    _height_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make the values' snapshots.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_width_and_height_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_width_snapshots',
            value=int(self._width._value), snapshot_name=snapshot_name)
        self._set_single_snapshot_val_to_dict(
            dict_name='_height_snapshots',
            value=int(self._height._value), snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert the values if the snapshots exist.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._width._value = self._width_snapshots[snapshot_name]
        self._height._value = self._height_snapshots[snapshot_name]
