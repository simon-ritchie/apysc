"""Class implementation for the scale_y_from_center mix-in.
"""

from typing import Dict

from typing_extensions import final

from apysc._animation.animation_scale_y_from_center_mixin import (
    AnimationScaleYFromCenterMixIn,
)
from apysc._display.set_lower_scale_limit_mixin import SetLowerScaleLimitMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.number import Number
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos


class ScaleYFromCenterMixIn(
    VariableNameSuffixAttrMixIn,
    AnimationScaleYFromCenterMixIn,
    SetLowerScaleLimitMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
):

    _scale_y_from_center: Number

    @final
    @add_debug_info_setting(module_name=__name__)
    def _initialize_scale_y_from_center_if_not_initialized(self) -> None:
        """
        Initialize the `_scale_y_from_center` attribute if this
        instance does not initialize it yet.
        """
        import apysc as ap

        if hasattr(self, "_scale_y_from_center"):
            return
        suffix: str = self._get_attr_variable_name_suffix(
            attr_identifier="scale_y_from_center"
        )
        self._scale_y_from_center = ap.Number(
            1.0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_scale_y_from_center_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_scale_y_from_center_attr_linking_setting(self) -> None:
        """
        Append a scale-y attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._scale_y_from_center, attr_name="scale_y_from_center"
        )
        self._append_attr_to_linking_stack(
            attr=self._scale_y_from_center, attr_name="scale_y_from_center"
        )

    @property
    @add_debug_info_setting(module_name=__name__)
    def scale_y_from_center(self) -> Number:
        """
        Get a scale-y value from the center of this instance.

        Returns
        -------
        scale_y_from_center : ap.Number
            Scale-y value from the center of this instance.

        Notes
        -----
        The scale's minimum value is almost zero, and it does not become negative.

        References
        ----------
        - GraphicsBase scale_x_from_center and scale_y_from_center interfaces
            - https://simon-ritchie.github.io/apysc/en/graphics_base_scale_from_center.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle.scale_y_from_center = ap.Number(1.5)
        >>> rectangle.scale_y_from_center
        Number(1.5)
        """
        from apysc._type import value_util

        self._initialize_scale_y_from_center_if_not_initialized()
        return value_util.get_copy(value=self._scale_y_from_center)

    @scale_y_from_center.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def scale_y_from_center(self, value: Number) -> None:
        """
        Update a scale-y value from the center of this instance.

        Parameters
        ----------
        value : ap.Number
            Scale-y value from the center of this instance.

        Notes
        -----
        The scale's minimum value is almost zero, and it does not become negative.

        References
        ----------
        - GraphicsBase scale_x_from_center and scale_y_from_center interfaces
            - https://simon-ritchie.github.io/apysc/en/graphics_base_scale_from_center.html  # noqa
        """
        import apysc as ap

        self._initialize_scale_y_from_center_if_not_initialized()
        before_value: ap.Number = self._scale_y_from_center
        self._set_lower_scale_limit(value=value)
        self._scale_y_from_center = value
        self._append_scale_y_from_center_update_expression(before_value=before_value)

        self._append_scale_y_from_center_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_scale_y_from_center_update_expression(
        self, *, before_value: Number
    ) -> None:
        """
        Append the scale-y from the center of this instance
        updating expression.

        Parameters
        ----------
        before_value : ap.Number
            Before updating value.
        """
        import apysc as ap
        from apysc._type import value_util

        before_value_str: str = value_util.get_value_str_for_expression(
            value=before_value
        )
        after_value_str: str = value_util.get_value_str_for_expression(
            value=self._scale_y_from_center
        )
        expression: str = (
            f"{self.variable_name}.scale(1, 1 / {before_value_str});"
            f"\n{self.variable_name}.scale(1, {after_value_str});"
            f"\n{before_value_str} = {after_value_str};"
        )
        ap.append_js_expression(expression=expression)

    _scale_y_from_center_snapshots: Dict[str, float]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_scale_y_from_center_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_scale_y_from_center_snapshots",
            value=self._scale_y_from_center._value,
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._scale_y_from_center._value = self._scale_y_from_center_snapshots[
            snapshot_name
        ]
