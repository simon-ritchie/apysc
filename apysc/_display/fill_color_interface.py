"""Class implementation for fill color interface.
"""

from typing import Dict
from typing import Union

from apysc._animation.animation_fill_color_interface import \
    AnimationFillColorInterface
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.revert_interface import RevertInterface
from apysc._type.string import String


class FillColorInterface(
        AnimationFillColorInterface, RevertInterface, AttrLinkingInterface):

    _fill_color: String

    @property  # type: ignore[misc]
    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='FillColorInterface')
    def fill_color(self) -> String:
        """
        Get this instance's fill color.

        Returns
        -------
        fill_color : String
            Current fill color (hexadecimal string, e.g., '#00aaff').
            If not be set, this interface returns a blank string.

        References
        ----------
        - Graphics fill_color interface document
            - https://simon-ritchie.github.io/apysc/graphics_fill_color.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> rectangle.fill_color = ap.String('#f0a')
        >>> rectangle.fill_color
        String('#ff00aa')
        """
        import apysc as ap
        from apysc._type import value_util
        self._initialize_fill_color_if_not_initialized()
        fill_color: ap.String = value_util.get_copy(value=self._fill_color)
        return fill_color

    @fill_color.setter
    def fill_color(self, value: String) -> None:
        """
        Update this instance's fill color.

        Parameters
        ----------
        value : String
            Fill color to set.

        References
        ----------
        - Graphics fill_color interface document
            - https://simon-ritchie.github.io/apysc/graphics_fill_color.html
        """
        from apysc._html.debug_mode import DebugInfo
        with DebugInfo(
                callable_='fill_color', args=[value], kwargs={},
                module_name=__name__,
                class_name=FillColorInterface.__name__):
            self._update_fill_color_and_skip_appending_exp(value=value)
            self._append_fill_color_update_expression()

            self._append_applying_new_attr_val_exp(
                new_attr=self._fill_color, attr_name='fill_color')
            self._append_attr_to_linking_stack(
                attr=self._fill_color, attr_name='fill_color')

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='FillColorInterface')
    def _append_fill_color_update_expression(self) -> None:
        """
        Append the fill color updating expression.
        """
        import apysc as ap
        expression: str = (
            f'{self.variable_name}.fill("{self.fill_color}");'
        )
        ap.append_js_expression(expression=expression)

    def _set_initial_fill_color_if_not_blank(
            self, *, fill_color: Union[str, String]) -> None:
        """
        Set the initial fill color if a specified value
        is not a blank string.

        Parameters
        ----------
        fill_color : str or String
            Fill color (hexadecimal string, e.g., '#00aaff').
        """
        import apysc as ap
        self._initialize_fill_color_if_not_initialized()
        if fill_color == '':
            return
        if isinstance(fill_color, ap.String):
            fill_color_: ap.String = fill_color
        else:
            fill_color_ = String(fill_color)
        self._update_fill_color_and_skip_appending_exp(
            value=fill_color_)

    def _update_fill_color_and_skip_appending_exp(
            self, *, value: String) -> None:
        """
        Update fill color and skip appending expression.

        Parameters
        ----------
        value : String
            Fill color to set.
        """
        from apysc._color import color_util
        value = color_util.complement_hex_color(
            hex_color_code=value)
        self._initialize_fill_color_if_not_initialized()
        self._fill_color.value = value

    def _initialize_fill_color_if_not_initialized(self) -> None:
        """
        Initialize the fill_color attribute if this interface
        does not initialize it yet.
        """
        if hasattr(self, '_fill_color'):
            return
        self._fill_color = String('')

    _fill_color_snapshots: Dict[str, str]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_fill_color_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_fill_color_snapshots',
            value=self._fill_color._value, snapshot_name=snapshot_name)

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
        self._fill_color._value = self._fill_color_snapshots[snapshot_name]
