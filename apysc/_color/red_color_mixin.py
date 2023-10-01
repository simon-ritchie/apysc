"""The mix-in class implementation for the `red_color` property.
"""

from apysc._type.int import Int
from apysc._html.debug_mode import add_debug_info_setting


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
        """
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix
        )
        from apysc._validation import variable_name_validation
        from apysc._expression import expression_data_util
        from apysc._color.color import Color

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
