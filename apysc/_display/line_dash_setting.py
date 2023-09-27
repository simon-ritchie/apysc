"""Dash setting class implementation for a line.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_to_apysc_val_from_builtin_mixin import (
    AttrToApyscValFromBuiltinMixIn,
)
from apysc._type.dictionary import Dictionary
from apysc._type.int import Int
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos


class LineDashSetting(
    Dictionary[str, Int],
    VariableNameSuffixAttrOrVarMixIn,
    AttrToApyscValFromBuiltinMixIn,
):
    """
    Dash setting class for a line.

    References
    ----------
    - Graphics line_style interface
        - https://simon-ritchie.github.io/apysc/en/graphics_line_style.html  # noqa

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=10)
    >>> line: ap.Line = sprite.graphics.draw_line(
    ...     x_start=50, y_start=50, x_end=150, y_end=50
    ... )
    >>> line.line_dash_setting = ap.LineDashSetting(dash_size=5, space_size=2)
    >>> line.line_dash_setting.dash_size
    Int(5)

    >>> line.line_dash_setting.space_size
    Int(2)
    """

    @final
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=1, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=2, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=2, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=3, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        *,
        dash_size: Union[int, Int],
        space_size: Union[int, Int],
        variable_name_suffix: str = ""
    ) -> None:
        """
        Dash setting class for a line.

        Parameters
        ----------
        dash_size : int or Int
            Dash size.
        space_size : int or Int
            Blank space size between dashes.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        References
        ----------
        - Graphics line_style interface
            - https://simon-ritchie.github.io/apysc/en/graphics_line_style.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50
        ... )
        >>> line.line_dash_setting = ap.LineDashSetting(dash_size=5, space_size=2)
        >>> line.line_dash_setting.dash_size
        Int(5)

        >>> line.line_dash_setting.space_size
        Int(2)
        """
        self._variable_name_suffix = variable_name_suffix
        dash_size_: Int = self._get_copied_int_from_builtin_val(
            integer=dash_size, attr_identifier="dash_size"
        )
        space_size_: Int = self._get_copied_int_from_builtin_val(
            integer=space_size, attr_identifier="space_size"
        )
        super(LineDashSetting, self).__init__(
            {
                "dash_size": dash_size_,
                "space_size": space_size_,
            },
            variable_name_suffix=self._variable_name_suffix,
        )

    @property
    @add_debug_info_setting(module_name=__name__)
    def dash_size(self) -> Int:
        """
        Get a dash size setting.

        Returns
        -------
        dash_size : Int
            Dash size setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50
        ... )
        >>> line.line_dash_setting = ap.LineDashSetting(dash_size=5, space_size=2)
        >>> line.line_dash_setting.dash_size
        Int(5)
        """
        return self["dash_size"]

    @property
    @add_debug_info_setting(module_name=__name__)
    def space_size(self) -> Int:
        """
        Get a space size setting.

        Returns
        -------
        space_size : Int
            Space size setting.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=10)
        >>> line: ap.Line = sprite.graphics.draw_line(
        ...     x_start=50, y_start=50, x_end=150, y_end=50
        ... )
        >>> line.line_dash_setting = ap.LineDashSetting(dash_size=5, space_size=2)
        >>> line.line_dash_setting.space_size
        Int(2)
        """
        return self["space_size"]
