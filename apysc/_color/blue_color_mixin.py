"""The mix-in class implementation for the `blue_color` property.
"""

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int


class BlueColorMixIn:
    @property
    @add_debug_info_setting(module_name=__name__)
    def blue_color(self) -> Int:
        """
        Get a blue color integer value (0 to 255).

        Returns
        -------
        blue_color : Int
            Blue color integer value (0 to 255).

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage(
        ...     background_color=ap.Color("#333"),
        ...     stage_elem_id="stage",
        ... )
        >>> color: ap.Color = ap.Color("#aaff00")
        >>> blue_color: ap.Int = color.blue_color
        >>> blue_color
        Int(0)

        >>> color = ap.Color("#00aaff")
        >>> blue_color = color.blue_color
        >>> blue_color
        Int(255)
        """
        from apysc._color.color import Color
        from apysc._expression import expression_data_util
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )
        from apysc._validation import variable_name_validation

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self, value_identifier="blue_color"
        )
        blue_color: Int = Int(0, variable_name_suffix=suffix)
        color_py_str: str = "#000000"
        if isinstance(self, Color):
            color_py_str = self._value._value
        blue_color._value = int(color_py_str[5:7], 16)
        variable_name: str = variable_name_validation.validate_variable_name_mixin_type(
            instance=self,
        ).variable_name

        expression: str = (
            f"{blue_color.variable_name} = "
            f"parseInt({variable_name}.substring(5, 7), 16);"
        )
        expression_data_util.append_js_expression(expression=expression)
        return blue_color
