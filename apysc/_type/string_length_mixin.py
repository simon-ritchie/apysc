"""The mix-in class implementation for the `String`'s `length` method.
"""

from typing import TYPE_CHECKING

from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos

if TYPE_CHECKING:
    from apysc._type.int import Int


class StringLengthMixIn:
    @property
    @arg_validation_decos.is_apysc_string(arg_position_index=0)
    @add_debug_info_setting(module_name=__name__)
    def length(self) -> "Int":
        """
        Get a character length (number).

        Returns
        -------
        characters_length : Int
            A character length (number).

        References
        ----------
        - String class length property
            - https://simon-ritchie.github.io/apysc/en/string_length.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> string: ap.String = ap.String("Hello")
        >>> string.length
        Int(5)
        """
        import apysc as ap
        from apysc._validation.variable_name_validation import (
            validate_variable_name_mixin_type,
        )

        self_variable_name: str = validate_variable_name_mixin_type(
            instance=self,
        ).variable_name
        characters_length: ap.Int = ap.Int(0)
        if isinstance(self, ap.String):
            characters_length._value = len(self._value)
        expression: str = (
            f"{characters_length.variable_name} = [...{self_variable_name}].length;"
        )
        ap.append_js_expression(expression=expression)
        return characters_length
