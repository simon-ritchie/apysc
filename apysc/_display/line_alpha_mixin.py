"""Class implementation for line alpha mix-in.
"""

from typing import Dict
from typing import Union

from typing_extensions import final

from apysc._animation.animation_line_alpha_mixin import AnimationLineAlphaMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.number import Number
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos


class LineAlphaMixIn(
    VariableNameSuffixAttrMixIn,
    AnimationLineAlphaMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
):

    _line_alpha: Number

    @final
    def _initialize_line_alpha_if_not_initialized(self) -> None:
        """
        Initialize _line_alpha attribute if this interface does not
        initialize it yet.
        """
        if hasattr(self, "_line_alpha"):
            return
        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="line_alpha")
        self._line_alpha = Number(
            1.0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_line_alpha_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_line_alpha_attr_linking_setting(self) -> None:
        """
        Append a line alpha attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._line_alpha, attr_name="line_alpha"
        )
        self._append_attr_to_linking_stack(
            attr=self._line_alpha, attr_name="line_alpha"
        )

    @property
    @add_debug_info_setting(module_name=__name__)
    def line_alpha(self) -> Number:
        """
        Get this instance's line alpha (opacity).

        Returns
        -------
        line_alpha : Number
            Current line alpha (opacity. 0.0 to 1.0).

        References
        ----------
        - GraphicsBase line_alpha interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_line_alpha.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color="#fff", thickness=5, alpha=1.0)
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle.line_alpha = ap.Number(0.5)
        >>> rectangle.line_alpha
        Number(0.5)
        """
        from apysc._type import value_util

        self._initialize_line_alpha_if_not_initialized()
        return value_util.get_copy(value=self._line_alpha)

    @line_alpha.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def line_alpha(self, value: Number) -> None:
        """
        Update this instance's line alpha (opacity).

        Parameters
        ----------
        value : Number
            Line alpha (opacity) to set.

        References
        ----------
        - GraphicsBase line_alpha interface
            - https://simon-ritchie.github.io/apysc/en/graphics_base_line_alpha.html  # noqa
        """
        self._initialize_line_alpha_if_not_initialized()
        self._update_line_alpha_and_skip_appending_exp(value=value)
        self._line_alpha._append_incremental_calc_substitution_expression()
        self._append_line_alpha_update_expression()

        self._append_line_alpha_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_line_alpha_update_expression(self) -> None:
        """
        Append line alpha updating expression.
        """
        import apysc as ap
        from apysc._type import value_util

        line_alpha_str: str = value_util.get_value_str_for_expression(
            value=self._line_alpha
        )
        expression: str = f"{self.variable_name}.stroke({{opacity: {line_alpha_str}}});"
        ap.append_js_expression(expression=expression)

    @final
    def _update_line_alpha_and_skip_appending_exp(
        self, *, value: Union[float, Number]
    ) -> None:
        """
        Update line alpha and skip appending expression.

        Parameters
        ----------
        value : float or Number
            Line alpha (opacity) to set.
        """
        import apysc as ap

        if isinstance(value, ap.Number):
            value_: ap.Number = value
        else:
            suffix: str = self._get_attr_variable_name_suffix(
                attr_identifier="line_alpha"
            )
            value_ = Number(value, variable_name_suffix=suffix)
        self._line_alpha = value_

    _line_alpha_snapshots: Dict[str, float]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_line_alpha_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_line_alpha_snapshots",
            value=self._line_alpha._value,
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
        self._line_alpha._value = self._line_alpha_snapshots[snapshot_name]
