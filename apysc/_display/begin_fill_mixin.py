"""Class implementation for begin_fill method-related mix-in.
"""


from typing import Dict
from typing import TypeVar
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.string import String
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos

StrOrString = TypeVar("StrOrString", str, String)


class BeginFillMixIn(VariableNameSuffixAttrOrVarMixIn, RevertMixIn):

    _fill_color: String
    _fill_alpha: Number

    @final
    @arg_validation_decos.is_hex_color_code_format(arg_position_index=1)
    @arg_validation_decos.is_num(arg_position_index=2)
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=2)
    @add_debug_info_setting(module_name=__name__)
    def begin_fill(
        self, *, color: StrOrString, alpha: Union[float, Number] = 1.0
    ) -> None:
        """
        Set single color value for fill.

        Parameters
        ----------
        color : str or String
            Hexadecimal color string. e.g., '#00aaff'
        alpha : float or Number, default 1.0
            Color opacity (0.0 to 1.0).

        References
        ----------
        - Graphics begin_fill interface
            - https://simon-ritchie.github.io/apysc/en/graphics_begin_fill.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle.fill_color
        String('#00aaff')
        """
        import apysc as ap
        from apysc._color import color_util
        from apysc._converter import cast

        self._initialize_fill_color_if_not_initialized()
        self._initialize_fill_alpha_if_not_initialized()
        if color != "":
            color = color_util.complement_hex_color(hex_color_code=color)
        self._fill_color.value = color
        if not isinstance(alpha, ap.Number):
            alpha = cast.to_float_from_int(int_or_float=alpha)
        if isinstance(alpha, ap.Number):
            self._fill_alpha.value = alpha.value
        else:
            self._fill_alpha.value = alpha

    @property
    @add_debug_info_setting(module_name=__name__)
    def fill_color(self) -> String:
        """
        Get current fill color.

        Returns
        -------
        fill_color : String
            Current fill color (hexadecimal string, e.g., '#00aaff').
            If not be set, this interface returns a blank string.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle.fill_color
        String('#00aaff')
        """
        import apysc as ap
        from apysc._type import value_util

        self._initialize_fill_color_if_not_initialized()
        fill_color: ap.String = value_util.get_copy(value=self._fill_color)
        return fill_color

    @final
    def _initialize_fill_color_if_not_initialized(self) -> None:
        """
        Initialize the fill_color attribute if this interface
        does not initialize it yet.
        """
        if hasattr(self, "_fill_color"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="fill_color"
        )
        self._fill_color = String(
            "",
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

    @property
    @add_debug_info_setting(module_name=__name__)
    def fill_alpha(self) -> Number:
        """
        Get current fill color opacity.

        Returns
        -------
        fill_alpha : Number
            Current fill color opacity (0.0 to 1.0).
            If not be set, 1.0 will be returned.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle.fill_alpha
        Number(0.5)
        """
        import apysc as ap
        from apysc._type import value_util

        self._initialize_fill_alpha_if_not_initialized()
        fill_alpha: ap.Number = value_util.get_copy(value=self._fill_alpha)
        return fill_alpha

    @final
    def _initialize_fill_alpha_if_not_initialized(self) -> None:
        """
        Initialize the fill_alpha attribute if this interface
        does not initialize it yet.
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

    _fill_color_snapshots: Dict[str, str]
    _fill_alpha_snapshots: Dict[str, float]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make values' snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_fill_color_if_not_initialized()
        self._initialize_fill_alpha_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_fill_color_snapshots",
            value=self._fill_color._value,
            snapshot_name=snapshot_name,
        )
        self._set_single_snapshot_val_to_dict(
            dict_name="_fill_alpha_snapshots",
            value=self._fill_alpha._value,
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert values if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._fill_color._value = self._fill_color_snapshots[snapshot_name]
        self._fill_alpha._value = self._fill_alpha_snapshots[snapshot_name]
