"""Class implementation for the scale_x_from_center interface.
"""

from typing import Dict

from apysc._animation.animation_scale_x_from_center_interface import \
    AnimationScaleXFromCenterInterface
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.number import Number
from apysc._type.revert_interface import RevertInterface


class ScaleXFromCenterInterface(
        AnimationScaleXFromCenterInterface, RevertInterface,
        AttrLinkingInterface):

    _scale_x_from_center: Number

    def _initialize_scale_x_from_center_if_not_initialized(self) -> None:
        """
        Initialize the `_scale_x_from_center` attribute if it hasn't been
        initialized yet.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.
                _initialize_scale_x_from_center_if_not_initialized,
                locals_=locals(),
                module_name=__name__, class_=ScaleXFromCenterInterface):
            if hasattr(self, '_scale_x_from_center'):
                return
            self._scale_x_from_center = ap.Number(1.0)

            self._append_scale_x_from_center_attr_linking_setting()

    def _append_scale_x_from_center_attr_linking_setting(self) -> None:
        """
        Append a scale-x attribute linking setting.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.
                _append_scale_x_from_center_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=ScaleXFromCenterInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._scale_x_from_center,
                attr_name='scale_x_from_center')
            self._append_attr_to_linking_stack(
                attr=self._scale_x_from_center,
                attr_name='scale_x_from_center')

    @property
    def scale_x_from_center(self) -> Number:
        """
        Get a scale-x value from the center of this instance.

        Returns
        -------
        scale_x_from_center : ap.Number
            Scale-x value from the center of this instance.

        References
        ----------
        - GraphicsBase scale_x_from_center and scale_y_from_center interfaces
            - https://bit.ly/3ityoCX

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> rectangle.scale_x_from_center = ap.Number(1.5)
        >>> rectangle.scale_x_from_center
        Number(1.5)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='scale_x_from_center', locals_=locals(),
                module_name=__name__, class_=ScaleXFromCenterInterface):
            from apysc._type import value_util
            self._initialize_scale_x_from_center_if_not_initialized()
            return value_util.get_copy(value=self._scale_x_from_center)

    @scale_x_from_center.setter
    def scale_x_from_center(self, value: Number) -> None:
        """
        Update a scale-x value from the center of this instance.

        Parameters
        ----------
        value : ap.Number
            Scale-x value from the center of this instance.

        References
        ----------
        - GraphicsBase scale_x_from_center and scale_y_from_center interfaces
            - https://bit.ly/3ityoCX
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='scale_x_from_center', locals_=locals(),
                module_name=__name__, class_=ScaleXFromCenterInterface):
            from apysc._validation import number_validation
            self._initialize_scale_x_from_center_if_not_initialized()
            number_validation.validate_num(num=value)
            if not isinstance(value, ap.Number):
                value = ap.Number(value)
            before_value: ap.Number = self._scale_x_from_center
            self._scale_x_from_center = value
            self._append_scale_x_from_center_update_expression(
                before_value=before_value)

            self._append_scale_x_from_center_attr_linking_setting()

    def _append_scale_x_from_center_update_expression(
            self, *, before_value: Number) -> None:
        """
        Append the scale-x from the center of this instance
        updating expression.

        Parameters
        ----------
        before_value : ap.Number
            Before updating value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_scale_x_from_center_update_expression,
                locals_=locals(),
                module_name=__name__, class_=ScaleXFromCenterInterface):
            from apysc._type import value_util
            before_value_str: str = value_util.get_value_str_for_expression(
                value=before_value)
            after_value_str: str = value_util.get_value_str_for_expression(
                value=self._scale_x_from_center)
            expression: str = (
                f'{self.variable_name}.scale(1 / {before_value_str}, 1);'
                f'\n{self.variable_name}.scale({after_value_str}, 1);'
                f'\n{before_value_str} = {after_value_str};'
            )
            ap.append_js_expression(expression=expression)

    _scale_x_from_center_snapshots: Dict[str, float]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_scale_x_from_center_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_scale_x_from_center_snapshots',
            value=self._scale_x_from_center._value,
            snapshot_name=snapshot_name)

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
        self._scale_x_from_center._value = \
            self._scale_x_from_center_snapshots[snapshot_name]
