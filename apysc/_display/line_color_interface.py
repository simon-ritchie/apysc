"""Class implementation for line color interface.
"""

from typing import Dict
from typing import Union

from apysc._animation.animation_line_color_interface import \
    AnimationLineColorInterface
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.revert_interface import RevertInterface
from apysc._type.string import String


class LineColorInterface(
        AnimationLineColorInterface, RevertInterface, AttrLinkingInterface):

    _line_color: String

    @property
    def line_color(self) -> String:
        """
        Get this instance's line color.

        Returns
        -------
        line_color : String
            Current line color (hexadecimal string, e.g., '#00aaff').
            If not be set, blank string will be returned.

        References
        ----------
        - Graphics line_color interface document
            - https://simon-ritchie.github.io/apysc/graphics_line_color.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50)
        >>> line.line_color = ap.String('#0af')
        >>> line.line_color
        String('#00aaff')
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_color', locals_=locals(),
                module_name=__name__, class_=LineColorInterface):
            from apysc._type import value_util
            self._initialize_line_color_if_not_initialized()
            line_color: ap.String = value_util.get_copy(
                value=self._line_color)
            return line_color

    @line_color.setter
    def line_color(self, value: String) -> None:
        """
        Update this instance's line color.

        Parameters
        ----------
        value : str
            Line color to set.

        References
        ----------
        - Graphics line_color interface document
            - https://simon-ritchie.github.io/apysc/graphics_line_color.html
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='line_color', locals_=locals(),
                module_name=__name__, class_=LineColorInterface):
            self._initialize_line_color_if_not_initialized()
            self._update_line_color_and_skip_appending_exp(value=value)
            self._append_line_color_update_expression()

            self._append_applying_new_attr_val_exp(
                new_attr=self._line_color, attr_name='line_color')
            self._append_attr_to_linking_stack(
                attr=self._line_color, attr_name='line_color')

    def _append_line_color_update_expression(self) -> None:
        """
        Append line color updating expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_line_color_update_expression,
                locals_=locals(),
                module_name=__name__, class_=LineColorInterface):
            from apysc._type import value_util
            line_color_str: str = value_util.get_value_str_for_expression(
                value=self._line_color)
            expression: str = (
                f'{self.variable_name}.stroke({line_color_str});'
            )
            ap.append_js_expression(expression=expression)

    def _set_initial_line_color_if_not_blank(
            self, *, line_color: Union[str, String]) -> None:
        """
        Set initial line color value if specified value is not
        blank string.

        Parameters
        ----------
        line_color : str or String
            Line color (hexadecimal string, e.g., '#00aaff').
        """
        self._initialize_line_color_if_not_initialized()
        if line_color == '':
            return
        if isinstance(line_color, str):
            line_color = String(line_color)
        self._update_line_color_and_skip_appending_exp(value=line_color)

    def _update_line_color_and_skip_appending_exp(
            self, *, value: String) -> None:
        """
        Update line color and skip appending expression.

        Parameters
        ----------
        value : String
            Line color to set.
        """
        from apysc._color import color_util
        self._initialize_line_color_if_not_initialized()
        value = color_util.complement_hex_color(
            hex_color_code=value)
        self._initialize_line_color_if_not_initialized()
        self._line_color = value

    def _initialize_line_color_if_not_initialized(self) -> None:
        """
        Initialize line_color attribute if that value is not
        initialized yet.
        """
        if hasattr(self, '_line_color'):
            return
        self._line_color = String('')

    _line_color_snapshots: Dict[str, str]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_line_color_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_line_color_snapshots',
            value=self._line_color._value, snapshot_name=snapshot_name)

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
        self._line_color._value = self._line_color_snapshots[snapshot_name]
