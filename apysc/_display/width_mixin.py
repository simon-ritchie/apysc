"""Class implementation for width mix-in.
"""

from typing import Dict
from typing import Union

from typing_extensions import final

from apysc._animation.animation_width_mixin import AnimationWidthMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.int import Int
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos


class WidthMixIn(
    VariableNameSuffixAttrMixIn,
    AnimationWidthMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
):

    _width: Int

    @final
    def _initialize_width_if_not_initialized(self) -> None:
        """
        Initialize _width attribute if this instance does not
        initialize it yet.
        """
        if hasattr(self, "_width"):
            return
        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="width")
        self._width = Int(
            0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_width_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_width_attr_linking_setting(self) -> None:
        """
        Append a width attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(new_attr=self._width, attr_name="width")
        self._append_attr_to_linking_stack(attr=self._width, attr_name="width")

    @property
    @add_debug_info_setting(module_name=__name__)
    def width(self) -> Int:
        """
        Get this instance's width.

        Returns
        -------
        width : Int
            This instance's width.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle.width = ap.Int(100)
        >>> rectangle.width
        Int(100)
        """
        import apysc as ap
        from apysc._type import value_util

        self._initialize_width_if_not_initialized()
        width: ap.Int = value_util.get_copy(value=self._width)
        return width

    @width.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def width(self, value: Int) -> None:
        """
        Update this instance's width.

        Parameters
        ----------
        value : Int
            Width value to set.
        """
        self._update_width_and_skip_appending_exp(value=value)
        self._width._append_incremental_calc_substitution_expression()
        self._append_width_update_expression()

        self._append_width_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_width_update_expression(self) -> None:
        """
        Append width updating expression.
        """
        import apysc as ap
        from apysc._type import value_util

        width_str: str = value_util.get_value_str_for_expression(value=self._width)
        expression: str = f"{self.variable_name}.width({width_str});"
        ap.append_js_expression(expression=expression)

    @final
    def _update_width_and_skip_appending_exp(self, *, value: Union[int, Int]) -> None:
        """
        Update width value and skip appending expression.

        Parameters
        ----------
        value : int or Int
            Width value to set.
        """
        import apysc as ap
        from apysc._converter import cast

        self._initialize_width_if_not_initialized()
        value = cast.to_int_from_float(int_or_float=value)
        if isinstance(value, ap.Int):
            value_: ap.Int = value
        else:
            suffix: str = self._get_attr_variable_name_suffix(attr_identifier="width")
            value_ = Int(value, variable_name_suffix=suffix)
        self._width = value_

    _width_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_width_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_width_snapshots",
            value=int(self._width._value),
            snapshot_name=snapshot_name,
        )

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
        self._width._value = self._width_snapshots[snapshot_name]
