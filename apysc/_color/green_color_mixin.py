"""The mix-in class implementation for the `green_color` property.
"""

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int


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
