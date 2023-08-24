"""Class implementation for line thickness mix-in.
"""

from typing import Dict
from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._animation.animation_line_thickness_mixin import AnimationLineThicknessMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.int import Int
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos


class LineThicknessMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    AnimationLineThicknessMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
):
    _line_thickness: Int

    @final
    def _initialize_line_thickness_if_not_initialized(self) -> None:
        """
        Initialize _line_thickness attribute if this interface
        does not initialize it yet.
        """
        if hasattr(self, "_line_thickness"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="line_thickness"
        )
        self._line_thickness = Int(
            1,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_line_thickness_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_line_thickness_attr_linking_setting(self) -> None:
        """
        Append a line thickness attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._line_thickness, attr_name="line_thickness"
        )
        self._append_attr_to_linking_stack(
            attr=self._line_thickness, attr_name="line_thickness"
        )

    @property
    @add_debug_info_setting(module_name=__name__)
    def line_thickness(self) -> Int:
        """
        Get this instance's line thickness.

        Returns
        -------
        line_thickness : Int
            Current line thickness.

        References
        ----------
        - GraphicsBase line_thickness interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_line_thickness.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=5)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50
        ... )
        >>> line.line_thickness
        Int(5)
        """
        from apysc._type import value_util

        return value_util.get_copy(value=self._line_thickness)

    @line_thickness.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def line_thickness(self, value: Int) -> None:
        """
        Update this instance's line thickness.

        Parameters
        ----------
        value : Int
            Line thickness to set.

        References
        ----------
        - GraphicsBase line_thickness interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_line_thickness.html  # noqa
        """
        self._update_line_thickness_and_skip_appending_exp(value=value)
        self._line_thickness._append_incremental_calc_substitution_expression()
        self._append_line_thickness_update_expression()

        self._append_line_thickness_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_line_thickness_update_expression(self) -> None:
        """
        Append line thickness update expression.
        """
        from apysc._expression import expression_data_util
        from apysc._type import value_util

        line_thickness_str: str = value_util.get_value_str_for_expression(
            value=self.line_thickness
        )
        expression: str = (
            f'{self.variable_name}.attr({{"stroke-width": ' f"{line_thickness_str}}});"
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    def _update_line_thickness_and_skip_appending_exp(
        self, *, value: Union[int, Int]
    ) -> None:
        """
        Update line thickness and skip appending expression.

        Parameters
        ----------
        value : Int or int
            Line thickness to set.
        """

        if isinstance(value, Int):
            value_: Int = value
        else:
            suffix: str = self._get_attr_or_variable_name_suffix(
                value_identifier="line_thickness"
            )
            value_ = Int(value, variable_name_suffix=suffix)
        self._line_thickness = value_

    _line_thickness_snapshots: Optional[Dict[str, int]] = None

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_line_thickness_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_line_thickness_snapshots",
            value=self._line_thickness._value,
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
        self._initialize_line_thickness_if_not_initialized()
        self._line_thickness._value = self._get_snapshot_val_if_exists(
            current_value=self._line_thickness._value,
            snapshot_dict=self._line_thickness_snapshots,
            snapshot_name=snapshot_name,
        )
