"""The mix-in class implementation for the `green_color` property.
"""

from typing import cast

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class GreenColorMixIn:
    @property
    @add_debug_info_setting(module_name=__name__)
    def green_color(self) -> Int:
        """
        Get a green color integer value (0 to 255).

        Returns
        -------
        green_color : Int
            Green color integer value (0 to 255).

        References
        ----------
        - Color class green_color property
            - https://simon-ritchie.github.io/apysc/en/green_color.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage(
        ...     background_color=ap.Color("#333"),
        ...     stage_elem_id="stage",
        ... )

        >>> color: ap.Color = ap.Color("#aa00ff")
        >>> green_color: ap.Int = color.green_color
        >>> green_color
        Int(0)

        >>> color = ap.Color("#00ffaa")
        >>> green_color = color.green_color
        >>> green_color
        Int(255)

        >>> color.green_color = ap.Int(0)
        >>> green_color = color.green_color
        >>> green_color
        Int(0)

        >>> color.green_color = ap.Int(255)
        >>> green_color = color.green_color
        >>> green_color
        Int(255)
        """
        from apysc._color.color import Color
        from apysc._expression import expression_data_util
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )
        from apysc._validation import variable_name_validation

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self, value_identifier="green_color"
        )
        green_color: Int = Int(0, variable_name_suffix=suffix)
        color_py_str: str = "#000000"
        if isinstance(self, Color):
            color_py_str = self._value._value
        green_color._value = int(color_py_str[3:5], 16)
        variable_name: str = variable_name_validation.validate_variable_name_mixin_type(
            instance=self,
        ).variable_name

        expression: str = (
            f"{green_color.variable_name} = "
            f"parseInt({variable_name}.substring(3, 5), 16);"
        )
        expression_data_util.append_js_expression(expression=expression)
        return green_color

    @green_color.setter
    @arg_validation_decos.is_color(arg_position_index=0, optional=False)
    @arg_validation_decos.is_apysc_integer(arg_position_index=1)
    @arg_validation_decos.is_uint8_range(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def green_color(self, green_color: Int) -> None:
        """
        Set a green color integer value (0 to 255).

        Parameters
        ----------
        green_color : Int
            Green color integer value (0 to 255).

        References
        ----------
        - Color class green_color property
            - https://simon-ritchie.github.io/apysc/en/green_color.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage(
        ...     background_color=ap.Color("#333"),
        ...     stage_elem_id="stage",
        ... )

        >>> color: ap.Color = ap.Color("#aa00ff")
        >>> green_color: ap.Int = color.green_color
        >>> green_color
        Int(0)

        >>> color = ap.Color("#00ffaa")
        >>> green_color = color.green_color
        >>> green_color
        Int(255)

        >>> color.green_color = ap.Int(0)
        >>> green_color = color.green_color
        >>> green_color
        Int(0)

        >>> color.green_color = ap.Int(255)
        >>> green_color = color.green_color
        >>> green_color
        Int(255)
        """
        from apysc._color import color_util
        from apysc._color.color import Color
        from apysc._expression import expression_data_util
        from apysc._type.string import String

        self_color: Color = cast(Color, self)
        original_py_color_str: str = self_color._value._value
        green_py_str: str = color_util.get_hex_str_from_int(color_int=green_color)
        self_color._value._value = (
            f"{original_py_color_str[:3]}{green_py_str}{original_py_color_str[5:]}"
        )
        green_color_str: String = color_util.get_hex_apysc_string_from_int(
            color_int=green_color,
            variable_name_suffix=green_color._variable_name_suffix,
        )
        head_color_str: String = self_color._value.slice(start=0, end=3)
        tail_color_str: String = self_color._value.slice(start=5)
        expression: str = (
            f"{self_color.variable_name} = {head_color_str.variable_name} "
            f"+ {green_color_str.variable_name} + {tail_color_str.variable_name};"
        )
        expression_data_util.append_js_expression(expression=expression)
