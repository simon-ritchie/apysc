"""Class implementation for the flip_x interface.
"""

from typing import Dict

from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.boolean import Boolean
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class FlipXInterface(
        VariableNameInterface, RevertInterface, AttrLinkingInterface):

    _flip_x: Boolean

    def _initialize_flip_x_if_not_initialized(self) -> None:
        """
        Initialize the _flip_x attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_flip_x'):
            return
        self._flip_x = Boolean(False)

        self._append_flip_x_attr_linking_setting()

    def _append_flip_x_attr_linking_setting(self) -> None:
        """
        Append a flip-x attribute linking setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_flip_x_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=FlipXInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._flip_x, attr_name='flip_x')
            self._append_attr_to_linking_stack(
                attr=self._flip_x, attr_name='flip_x')

    @property
    def flip_x(self) -> Boolean:
        """
        Get a boolean value whether the x-axis is flipped or not.

        Returns
        -------
        flip_x : Boolean
            A boolean value whether the x-axis is flipped or not.

        References
        ----------
        - GraphicsBase flip_x and flip_y interfaces document
            - https://bit.ly/31F9lHv

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
        ...     points=[
        ...         ap.Point2D(x=0, y=0),
        ...         ap.Point2D(x=0, y=50),
        ...         ap.Point2D(x=50, y=25),
        ...     ])
        >>> polygon.flip_x = ap.Boolean(True)
        >>> polygon.flip_x
        Boolean(True)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='flip_x', locals_=locals(),
                module_name=__name__, class_=FlipXInterface):
            from apysc._type import value_util
            self._initialize_flip_x_if_not_initialized()
            return value_util.get_copy(value=self._flip_x)

    @flip_x.setter
    def flip_x(self, value: Boolean) -> None:
        """
        Update a x-axis flipping value.

        Parameters
        ----------
        value : Boolean
            Flipping value. If True, a x-axis will be flipped,
            otherwise it will be reset.

        References
        ----------
        - GraphicsBase flip_x and flip_y interfaces document
            - https://bit.ly/31F9lHv
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='flip_x', locals_=locals(),
                module_name=__name__, class_=FlipXInterface):
            self._initialize_flip_x_if_not_initialized()
            before_value: ap.Boolean = self._flip_x
            self._flip_x = value
            self._append_flip_x_update_expression(before_value=before_value)

            self._append_flip_x_attr_linking_setting()

    def _append_flip_x_update_expression(
            self, *, before_value: Boolean) -> None:
        """
        Append a x-axis flipping value updating expression.

        Parameters
        ----------
        before_value : Boolean
            Before updating flipping value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_flip_x_update_expression,
                locals_=locals(),
                module_name=__name__, class_=FlipXInterface):
            from apysc._display import flip_interface_helper
            self._initialize_flip_x_if_not_initialized()
            expression: str = flip_interface_helper.\
                make_flip_update_expression(
                    before_value=before_value, after_value=self._flip_x,
                    axis=flip_interface_helper.Axis.X,
                    interface_variable_name=self.variable_name)
            ap.append_js_expression(expression=expression)

    _flip_x_snapshots: Dict[str, bool]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_flip_x_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_flip_x_snapshots',
            value=self._flip_x._value, snapshot_name=snapshot_name)

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
        self._flip_x._value = self._flip_x_snapshots[snapshot_name]
