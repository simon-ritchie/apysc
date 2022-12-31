"""Class implementation for the rotation_around_center_interface
interface.
"""

from typing import Dict

from typing_extensions import final

from apysc._animation.animation_rotation_around_center_mixin import (
    AnimationRotationAroundCenterMixIn,
)
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.int import Int
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos


class RotationAroundCenterMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    AnimationRotationAroundCenterMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
):

    _rotation_around_center: Int

    @final
    def _initialize_rotation_around_center_if_not_initialized(self) -> None:
        """
        Initialize the `_rotation_around_center` attribute if this interface
        does not initialize it yet.
        """
        if hasattr(self, "_rotation_around_center"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="rotation_around_center"
        )
        self._rotation_around_center = Int(
            0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_rotation_around_center_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_rotation_around_center_attr_linking_setting(self) -> None:
        """
        Append a rotation around a center attribute linking setting.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._rotation_around_center, attr_name="rotation_around_center"
        )
        self._append_attr_to_linking_stack(
            attr=self._rotation_around_center, attr_name="rotation_around_center"
        )

    @property
    @add_debug_info_setting(module_name=__name__)
    def rotation_around_center(self) -> Int:
        """
        Get a rotation value around the center of this instance.

        Returns
        -------
        rotation_around_center : Int
            Rotation value around the center of this instance.

        References
        ----------
        - GraphicsBase rotation_around_center interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_rotation_around_center.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle.rotation_around_center = ap.Int(45)
        >>> rectangle.rotation_around_center
        Int(45)
        """
        from apysc._type import value_util

        self._initialize_rotation_around_center_if_not_initialized()
        return value_util.get_copy(value=self._rotation_around_center)

    @rotation_around_center.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def rotation_around_center(self, value: Int) -> None:
        """
        Update a rotation value around the center of this instance.

        Parameters
        ----------
        value : Int
            Rotation value around the center of this instance.

        References
        ----------
        - GraphicsBase rotation_around_center interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_rotation_around_center.html  # noqa
        """
        import apysc as ap

        self._initialize_rotation_around_center_if_not_initialized()
        before_value: ap.Int = self._rotation_around_center
        self._rotation_around_center = value
        self._append_rotation_around_center_update_expression(before_value=before_value)

        self._append_rotation_around_center_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_rotation_around_center_update_expression(
        self, *, before_value: Int
    ) -> None:
        """
        Append the rotation around the center of this instance
        updating expression.

        Parameters
        ----------
        before_value : ap.Int
            Before updating value.
        """
        import apysc as ap
        from apysc._type import value_util

        before_value_str: str = value_util.get_value_str_for_expression(
            value=before_value
        )
        after_value_str: str = value_util.get_value_str_for_expression(
            value=self._rotation_around_center
        )
        expression: str = (
            f"{self.variable_name}.rotate(-{before_value_str});"
            f"\n{self.variable_name}.rotate({after_value_str});"
            f"\n{before_value_str} = {after_value_str};"
        )
        ap.append_js_expression(expression=expression)

    _rotation_around_center_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_rotation_around_center_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_rotation_around_center_snapshots",
            value=int(self._rotation_around_center._value),
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
        self._rotation_around_center._value = self._rotation_around_center_snapshots[
            snapshot_name
        ]
