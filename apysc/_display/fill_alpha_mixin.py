"""Class implementation for fill alpha mix-in.
"""

from typing import Dict
from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._animation.animation_fill_alpha_mixin import AnimationFillAlphaMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.number import Number
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos


class FillAlphaMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    AnimationFillAlphaMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
):
    _fill_alpha: Number

    @final
    def _initialize_fill_alpha_if_not_initialized(self) -> None:
        """
        Initialize _fill_alpha attribute if this interface does not
        initialize it yet.
        """
        if hasattr(self, "_fill_alpha"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="fill_alpha"
        )
        self._fill_alpha = Number(
            1.0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_fill_alpha_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_fill_alpha_attr_linking_setting(self) -> None:
        """
        Append a scale-y attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._fill_alpha, attr_name="fill_alpha"
        )
        self._append_attr_to_linking_stack(
            attr=self._fill_alpha, attr_name="fill_alpha"
        )

    @property
    @add_debug_info_setting(module_name=__name__)
    def fill_alpha(self) -> Number:
        """
        Get this instance's fill opacity.

        Returns
        -------
        fill_alpha : Number
            Current fill opacity (0.0 to 1.0).

        References
        ----------
        - GraphicsBase fill_alpha interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_fill_alpha.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle.fill_alpha = ap.Number(0.5)
        >>> rectangle.fill_alpha
        Number(0.5)
        """
        from apysc._type import value_util

        self._initialize_fill_alpha_if_not_initialized()
        fill_alpha: Number = value_util.get_copy(value=self._fill_alpha)
        return fill_alpha

    @fill_alpha.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def fill_alpha(self, value: Number) -> None:
        """
        Update this instance's fill opacity.

        Parameters
        ----------
        value : Number
            Fill opacity to set.

        References
        ----------
        - GraphicsBase fill_alpha interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_fill_alpha.html  # noqa
        """
        self._update_fill_alpha_and_skip_appending_exp(value=value)
        self._fill_alpha._append_incremental_calc_substitution_expression()
        self._append_fill_alpha_update_expression()

        self._append_fill_alpha_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_fill_alpha_update_expression(self) -> None:
        """
        Append the fill alpha updating expression.
        """
        from apysc._expression import expression_data_util
        from apysc._type import value_util

        value_str: str = value_util.get_value_str_for_expression(value=self._fill_alpha)
        expression: str = f"{self.variable_name}.fill({{opacity: {value_str}}});"
        expression_data_util.append_js_expression(expression=expression)

    @final
    def _update_fill_alpha_and_skip_appending_exp(
        self, *, value: Union[float, Number]
    ) -> None:
        """
        Update the fill opacity and skip appending expression.

        Parameters
        ----------
        value : float or Number
            Fill opacity to set.
        """
        from apysc._converter import cast

        self._initialize_fill_alpha_if_not_initialized()
        if not isinstance(value, Number):
            suffix: str = self._get_attr_or_variable_name_suffix(
                value_identifier="fill_alpha"
            )
            value = cast.to_float_from_int(int_or_float=value)
            value_: Number = Number(value=value, variable_name_suffix=suffix)
        else:
            value_ = value
        self._fill_alpha = value_

    _fill_alpha_snapshots: Optional[Dict[str, float]] = None

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
            dict_name="_fill_alpha_snapshots",
            value=self._fill_alpha._value,
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
        self._fill_alpha._value = self._get_snapshot_val_if_exists(
            current_value=self._fill_alpha._value,
            snapshot_dict=self._fill_alpha_snapshots,
            snapshot_name=snapshot_name,
        )
