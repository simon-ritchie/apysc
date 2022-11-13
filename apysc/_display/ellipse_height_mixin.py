"""Class implementation for the ellipse height mix-in.
"""

from typing import Dict

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.int import Int
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos


class EllipseHeightMixIn(
    VariableNameSuffixAttrMixIn,
    VariableNameMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
):

    _ellipse_height: Int

    @final
    def _initialize_ellipse_height_if_not_initialized(self) -> None:
        """
        Initialize _ellipse_height attribute if this interface does not
        initialize it yet.
        """
        if hasattr(self, "_ellipse_height"):
            return
        suffix: str = self._get_attr_variable_name_suffix(
            attr_identifier="ellipse_height"
        )
        self._ellipse_height = Int(
            0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_ellipse_height_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_ellipse_height_attr_linking_setting(self) -> None:
        """
        Append ellipse-height attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._ellipse_height, attr_name="ellipse_height"
        )
        self._append_attr_to_linking_stack(
            attr=self._ellipse_height, attr_name="ellipse_height"
        )

    @property
    @add_debug_info_setting(module_name=__name__)
    def ellipse_height(self) -> Int:
        """
        Get ellipse height value.

        Returns
        -------
        ellipse_height : Int
            Ellipse height value.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle.ellipse_width = ap.Int(10)
        >>> rectangle.ellipse_height = ap.Int(15)
        >>> rectangle.ellipse_height
        Int(15)
        """
        from apysc._type import value_util

        self._initialize_ellipse_height_if_not_initialized()
        return value_util.get_copy(value=self._ellipse_height)

    @ellipse_height.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def ellipse_height(self, value: Int) -> None:
        """
        Update ellipse height value.

        Parameters
        ----------
        value : Int
            Ellipse height value.
        """
        self._ellipse_height = value
        self._ellipse_height._append_incremental_calc_substitution_expression()
        self._append_ellipse_height_update_expression()

        self._append_ellipse_height_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_ellipse_height_update_expression(self) -> None:
        """
        Append ellipse height updating expression.
        """
        import apysc as ap
        from apysc._type import value_util

        self._initialize_ellipse_height_if_not_initialized()
        if hasattr(self, "_ellipse_width"):
            width_value_str: str = value_util.get_value_str_for_expression(
                value=getattr(self, "_ellipse_width")
            )
        else:
            width_value_str = value_util.get_value_str_for_expression(value=0)
        height_value_str: str = value_util.get_value_str_for_expression(
            value=self._ellipse_height
        )
        expression: str = (
            f"{self.variable_name}.radius({width_value_str}, " f"{height_value_str});"
        )
        ap.append_js_expression(expression=expression)

    _ellipse_height_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make the value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_ellipse_height_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_ellipse_height_snapshots",
            value=int(self._ellipse_height._value),
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert the value if the snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._ellipse_height._value = self._ellipse_height_snapshots[snapshot_name]
