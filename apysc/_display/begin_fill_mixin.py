"""Class implementation for begin_fill method-related mix-in.
"""

from typing import Dict
from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._color.color import Color
from apysc._color.colorless import COLORLESS
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos


class BeginFillMixIn(VariableNameSuffixAttrOrVarMixIn, RevertMixIn):
    _fill_color: Color
    _fill_alpha: Number

    @final
    @arg_validation_decos.is_color(arg_position_index=1, optional=False)
    @arg_validation_decos.is_num(arg_position_index=2, optional=False)
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def begin_fill(self, *, color: Color, alpha: Union[float, Number] = 1.0) -> None:
        """
        Set single color value for fill.

        Parameters
        ----------
        color : Color
            A color setting.
        alpha : float or Number, default 1.0
            Color opacity (0.0 to 1.0).

        References
        ----------
        - Graphics begin_fill interface
            - https://simon-ritchie.github.io/apysc/en/graphics_begin_fill.html  # noqa

        Examples
        --------
        >>> import apysc as ap

        >>> _ = ap.Stage(
        ...     stage_width=150,
        ...     stage_height=150,
        ...     background_color=ap.Color("#333"),
        ...     stage_elem_id="stage",
        ... )
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(
        ...     color=ap.Color("#0af"),
        ...     alpha=0.5,
        ... )
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle.fill_color
        Color("#00aaff")
        >>> rectangle.fill_alpha
        Number(0.5)
        """
        from apysc._converter import cast

        self._initialize_fill_color_if_not_initialized()
        self._initialize_fill_alpha_if_not_initialized()
        self._fill_color = color
        if not isinstance(alpha, Number):
            alpha = cast.to_float_from_int(int_or_float=alpha)
        if isinstance(alpha, Number):
            self._fill_alpha.value = alpha.value
        else:
            self._fill_alpha.value = alpha

    @property
    @add_debug_info_setting(module_name=__name__)
    def fill_color(self) -> Color:
        """
        Get a current fill color.

        Returns
        -------
        fill_color : Color
            Current fill-color.
            If not be set, this interface returns a `COLORLESS` constant.

        Examples
        --------
        >>> import apysc as ap

        >>> _ = ap.Stage(
        ...     stage_width=150,
        ...     stage_height=150,
        ...     background_color=ap.Color("#333"),
        ...     stage_elem_id="stage",
        ... )
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(
        ...     color=ap.Color("#0af"),
        ...     alpha=0.5,
        ... )
        >>> sprite.graphics.fill_color
        Color("#00aaff")
        """

        self._initialize_fill_color_if_not_initialized()
        fill_color: Color = self._fill_color._copy()
        return fill_color

    @final
    def _initialize_fill_color_if_not_initialized(self) -> None:
        """
        Initialize the fill_color attribute if this interface
        does not initialize it yet.
        """
        if hasattr(self, "_fill_color"):
            return
        self._fill_color = COLORLESS

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
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"), alpha=0.5)
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle.fill_alpha
        Number(0.5)
        """
        from apysc._type import value_util

        self._initialize_fill_alpha_if_not_initialized()
        fill_alpha: Number = value_util.get_copy(value=self._fill_alpha)
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

    _fill_color_snapshots: Optional[Dict[str, str]] = None
    _fill_alpha_snapshots: Optional[Dict[str, float]] = None

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
            value=self._fill_color._value._value,
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
        self._fill_color._value._value = self._get_snapshot_val_if_exists(
            current_value=self._fill_color._value._value,
            snapshot_dict=self._fill_color_snapshots,
            snapshot_name=snapshot_name,
        )
        self._fill_alpha._value = self._get_snapshot_val_if_exists(
            current_value=self._fill_alpha._value,
            snapshot_dict=self._fill_alpha_snapshots,
            snapshot_name=snapshot_name,
        )
