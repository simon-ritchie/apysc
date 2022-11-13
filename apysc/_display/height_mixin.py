"""Class implementation for height mix-in.
"""

from typing import Dict
from typing import Union

from typing_extensions import final

from apysc._animation.animation_height_mixin import AnimationHeightMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.int import Int
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos


class HeightMixIn(
    VariableNameSuffixAttrMixIn,
    AnimationHeightMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
):

    _height: Int

    @final
    def _initialize_height_if_not_initialized(self) -> None:
        """
        Initialize _height attribute if this interface does not
        initialize it yet.
        """
        if hasattr(self, "_height"):
            return
        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="height")
        self._height = Int(
            0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_height_attr_linking_setting()

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
    def height(self) -> Int:
        """
        Get this instance's height.

        Returns
        -------
        height : Int
            This instance's height.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle.height = ap.Int(100)
        >>> rectangle.height
        Int(100)
        """
        import apysc as ap
        from apysc._type import value_util

        self._initialize_height_if_not_initialized()
        height: ap.Int = value_util.get_copy(value=self._height)
        return height

    @height.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def height(self, value: Int) -> None:
        """
        Update this instance's height.

        Parameters
        ----------
        value : int
            Height value to set.
        """
        self._update_height_and_skip_appending_exp(value=value)
        self._height._append_incremental_calc_substitution_expression()
        self._append_height_update_expression()

        self._append_height_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_height_update_expression(self) -> None:
        """
        Append height updating expression.
        """
        import apysc as ap
        from apysc._type import value_util

        height_str: str = value_util.get_value_str_for_expression(value=self._height)
        expression: str = f"{self.variable_name}.height({height_str});"
        ap.append_js_expression(expression=expression)

    @final
    def _update_height_and_skip_appending_exp(self, *, value: Union[int, Int]) -> None:
        """
        Update height value and skip appending expression.

        Parameters
        ----------
        value : int or Int
            Height value to set.
        """
        import apysc as ap
        from apysc._converter import cast

        self._initialize_height_if_not_initialized()
        value = cast.to_int_from_float(int_or_float=value)
        if isinstance(value, ap.Int):
            value_: ap.Int = value
        else:
            suffix: str = self._get_attr_variable_name_suffix(attr_identifier="height")
            value_ = Int(value, variable_name_suffix=suffix)
        self._height = value_

    _height_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_height_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_height_snapshots",
            value=int(self._height._value),
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
        self._height._value = self._height_snapshots[snapshot_name]
