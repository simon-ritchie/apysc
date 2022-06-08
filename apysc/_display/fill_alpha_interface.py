"""Class implementation for fill alpha interface.
"""

from typing import Dict

from apysc._animation.animation_fill_alpha_interface import \
    AnimationFillAlphaInterface
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.number import Number
from apysc._type.revert_interface import RevertInterface
from apysc._validation import arg_validation_decos


class FillAlphaInterface(
        AnimationFillAlphaInterface, RevertInterface, AttrLinkingInterface):

    _fill_alpha: Number

    def _initialize_fill_alpha_if_not_initialized(self) -> None:
        """
        Initialize _fill_alpha attribute if this interface does not
        initialize it yet.
        """
        if hasattr(self, '_fill_alpha'):
            return
        self._fill_alpha = Number(1.0)

        self._append_fill_alpha_attr_linking_setting()

    @add_debug_info_setting(
        module_name=__name__, class_name='FillAlphaInterface')
    def _append_fill_alpha_attr_linking_setting(self) -> None:
        """
        Append a scale-y attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._fill_alpha, attr_name='fill_alpha')
        self._append_attr_to_linking_stack(
            attr=self._fill_alpha, attr_name='fill_alpha')

    @property
    @add_debug_info_setting(
        module_name=__name__, class_name='FillAlphaInterface')
    def fill_alpha(self) -> Number:
        """
        Get this instance's fill opacity.

        Returns
        -------
        fill_alpha : Number
            Current fill opacity (0.0 to 1.0).

        References
        ----------
        - Graphics fill_alpha interface document
            - https://simon-ritchie.github.io/apysc/graphics_fill_alpha.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> rectangle.fill_alpha = ap.Number(0.5)
        >>> rectangle.fill_alpha
        Number(0.5)
        """
        import apysc as ap
        from apysc._type import value_util
        self._initialize_fill_alpha_if_not_initialized()
        fill_alpha: ap.Number = value_util.get_copy(
            value=self._fill_alpha)
        return fill_alpha

    @fill_alpha.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=1)
    @add_debug_info_setting(
        module_name=__name__, class_name='FillAlphaInterface')
    def fill_alpha(
            self, value: Number) -> None:
        """
        Update this instance's fill opacity.

        Parameters
        ----------
        value : Number
            Fill opacity to set.

        References
        ----------
        - Graphics fill_alpha interface document
            - https://simon-ritchie.github.io/apysc/graphics_fill_alpha.html
        """
        self._update_fill_alpha_and_skip_appending_exp(value=value)
        self._fill_alpha._append_incremental_calc_substitution_expression()
        self._append_fill_alpha_update_expression()

        self._append_fill_alpha_attr_linking_setting()

    @add_debug_info_setting(
        module_name=__name__, class_name='FillAlphaInterface')
    def _append_fill_alpha_update_expression(self) -> None:
        """
        Append the fill alpha updating expression.
        """
        import apysc as ap
        from apysc._type import value_util
        value_str: str = value_util.get_value_str_for_expression(
            value=self._fill_alpha)
        expression: str = (
            f'{self.variable_name}.fill({{opacity: {value_str}}});'
        )
        ap.append_js_expression(expression=expression)

    def _update_fill_alpha_and_skip_appending_exp(
            self, *, value: Number) -> None:
        """
        Update the fill opacity and skip appending expression.

        Parameters
        ----------
        value : Number
            Fill opacity to set.
        """
        from apysc._converter import cast
        self._initialize_fill_alpha_if_not_initialized()
        if not isinstance(value, Number):
            value = cast.to_float_from_int(int_or_float=value)
            value = Number(value=value)
        self._fill_alpha = value

    _fill_alpha_snapshots: Dict[str, float]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_fill_alpha_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_fill_alpha_snapshots',
            value=self._fill_alpha._value, snapshot_name=snapshot_name)

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
        self._fill_alpha._value = self._fill_alpha_snapshots[snapshot_name]
