"""Class implementation of the width and height mix-in
for the ellipse.

Notes
-----
A Subclass that inherits the normal WidthMixIn and
HeightMixIn can't use this interface.
"""

from typing import Dict

from typing_extensions import final

from apysc._animation.animation_height_for_ellipse_mixin import (
    AnimationHeightForEllipseMixIn,
)
from apysc._animation.animation_width_for_ellipse_mixin import (
    AnimationWidthForEllipseMixIn,
)
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.int import Int
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos


class WidthAndHeightMixInForEllipse(
    VariableNameSuffixAttrMixIn,
    AnimationWidthForEllipseMixIn,
    AnimationHeightForEllipseMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
):

    _width: Int
    _height: Int

    @final
    def _initialize_width_and_height_if_not_initialized(self) -> None:
        """
        Initialize _width and _height attributes if this interface
        does not initialize these yet.
        """
        if not hasattr(self, "_width"):
            suffix: str = self._get_attr_variable_name_suffix(attr_identifier="width")
            self._width = Int(
                0,
                variable_name_suffix=suffix,
                skip_init_substitution_expression_appending=True,
            )
            self._append_width_attr_linking_setting()
        if not hasattr(self, "_height"):
            suffix = self._get_attr_variable_name_suffix(attr_identifier="height")
            self._height = Int(
                0,
                variable_name_suffix=suffix,
                skip_init_substitution_expression_appending=True,
            )
            self._append_height_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_width_attr_linking_setting(self) -> None:
        """
        Append a width attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(new_attr=self._width, attr_name="width")
        self._append_attr_to_linking_stack(attr=self._width, attr_name="width")

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_height_attr_linking_setting(self) -> None:
        """
        Append a height attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._height, attr_name="height"
        )
        self._append_attr_to_linking_stack(attr=self._height, attr_name="height")

    @property
    @add_debug_info_setting(module_name=__name__)
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
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
        ...     x=100, y=100, width=50, height=50
        ... )
        >>> ellipse.width = ap.Int(100)
        >>> ellipse.width
        Int(100)
        """
        from apysc._type import value_util

        self._initialize_width_and_height_if_not_initialized()
        return value_util.get_copy(value=self._width)

    @width.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def width(self, value: Int) -> None:
        """
        Update a ellipse width value.

        Parameters
        ----------
        value : Int
            Ellipse width value.
        """
        self._width = value
        self._width._append_incremental_calc_substitution_expression()
        self._append_ellipse_width_and_height_update_expression()

        self._append_width_attr_linking_setting()

    @property
    @add_debug_info_setting(module_name=__name__)
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
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
        ...     x=100, y=100, width=50, height=50
        ... )
        >>> ellipse.height = ap.Int(100)
        >>> ellipse.height
        Int(100)
        """
        from apysc._type import value_util

        self._initialize_width_and_height_if_not_initialized()
        return value_util.get_copy(value=self._height)

    @height.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def height(self, value: Int) -> None:
        """
        Update a ellipse height value.

        Parameters
        ----------
        value : int or Int
            Ellipse height value.
        """
        self._height = value
        self._height._append_incremental_calc_substitution_expression()
        self._append_ellipse_width_and_height_update_expression()

        self._append_height_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_ellipse_width_and_height_update_expression(self) -> None:
        """
        Append an ellipse width and height updating expression.
        """
        import apysc as ap
        from apysc._type import value_util

        self._initialize_width_and_height_if_not_initialized()
        width_value_str: str = value_util.get_value_str_for_expression(
            value=self._width
        )
        height_value_str: str = value_util.get_value_str_for_expression(
            value=self._height
        )
        expression: str = (
            f"{self.variable_name}.radius("
            f"Math.trunc({width_value_str} / 2), "
            f"Math.trunc({height_value_str}) / 2);"
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
            dict_name="_width_snapshots",
            value=int(self._width._value),
            snapshot_name=snapshot_name,
        )
        self._set_single_snapshot_val_to_dict(
            dict_name="_height_snapshots",
            value=int(self._height._value),
            snapshot_name=snapshot_name,
        )

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
