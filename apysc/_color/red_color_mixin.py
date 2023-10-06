"""The mix-in class implementation for the `red_color` property.
"""

from typing import cast

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class RedColorMixIn:
    @property
    @add_debug_info_setting(module_name=__name__)
    def red_color(self) -> Int:
        """
        Get a red color integer value (0 to 255).

        Returns
        -------
        red_color : Int
            Red color integer value (0 to 255).

        References
        ----------
        - Color class red_color property
            - https://simon-ritchie.github.io/apysc/en/red_color.html

        Examples
        --------
        >>> import apysc as ap
        >>> color: ap.Color = ap.Color("#00aaff")
        >>> red_color: ap.Int = color.red_color
        >>> red_color
        Int(0)

        >>> color = ap.Color("#ff00aa")
        >>> red_color = color.red_color
        >>> red_color
        Int(255)

        >>> color.red_color = ap.Int(0)
        >>> red_color = color.red_color
        >>> red_color
        Int(0)
        """
        from apysc._color.color import Color
        from apysc._expression import expression_data_util
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )
        from apysc._validation import variable_name_validation

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self, value_identifier="red_color"
        )
        red_color: Int = Int(0, variable_name_suffix=suffix)
        color_py_str: str = "#000000"
        if isinstance(self, Color):
            color_py_str = self._value._value
        red_color._value = int(color_py_str[1:3], 16)
        variable_name: str = variable_name_validation.validate_variable_name_mixin_type(
            instance=self,
        ).variable_name

        expression: str = (
            f"{red_color.variable_name} = "
            f"parseInt({variable_name}.substring(1, 3), 16);"
        )
        expression_data_util.append_js_expression(expression=expression)
        return red_color

    @red_color.setter
    @arg_validation_decos.is_color(arg_position_index=0, optional=False)
    @arg_validation_decos.is_apysc_integer(arg_position_index=1)
    @arg_validation_decos.is_uint8_range(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def red_color(self, red_color: Int) -> None:
        """
        Set a red color integer value (0 to 255).

        Parameters
        ----------
        red_color : Int
            Red color integer value (0 to 255).

        References
        ----------
        - Color class red_color property
            - https://simon-ritchie.github.io/apysc/en/red_color.html

        Examples
        --------
        >>> import apysc as ap
        >>> color: ap.Color = ap.Color("#00aaff")
        >>> red_color: ap.Int = color.red_color
        >>> red_color
        Int(0)

        >>> color = ap.Color("#ff00aa")
        >>> red_color = color.red_color
        >>> red_color
        Int(255)

        >>> color.red_color = ap.Int(0)
        >>> red_color = color.red_color
        >>> red_color
        Int(0)
        """
        from apysc._color import color_util
        from apysc._color.color import Color
        from apysc._expression import expression_data_util
        from apysc._type.string import String

        self_color: Color = cast(Color, self)
        red_py_str: str = color_util.get_hex_str_from_int(color_int=red_color)
        self_color._value._value = f"#{red_py_str}{self_color._value._value[3:]}"
        tail_color_str: String = self_color._value.slice(start=3)
        red_color_str: String = color_util.get_hex_apysc_string_from_int(
            color_int=red_color, variable_name_suffix=red_color._variable_name_suffix
        )
        expression: str = (
            f'{self_color.variable_name} = "#" + {red_color_str.variable_name}'
            f" + {tail_color_str.variable_name};"
        )
        expression_data_util.append_js_expression(expression=expression)
