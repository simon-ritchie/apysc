"""Class implementation for the `String` class's `split` mix-in.
"""

from typing import TYPE_CHECKING

from apysc._type.variable_name_mixin import VariableNameMixIn

if TYPE_CHECKING:
    from apysc._type.array import Array
    from apysc._type.string import String


class StringSplitMixIn(VariableNameMixIn):
    def split(self, *, sep: "String") -> "Array[String]":
        """
        Split a current string with a separator string.

        Parameters
        ----------
        sep : String
            A separator string.

        Returns
        -------
        splitted_strs : Array[String]
            A splitted strings' array.

        References
        ----------
        - String class split interface
            - https://simon-ritchie.github.io/apysc/en/string_split.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> str_value: ap.String = ap.String("Lorem ipsum dolor sit")
        >>> splitted_strs: ap.Array[ap.String] = str_value.split(sep=ap.String(" "))
        >>> ap.assert_arrays_equal(splitted_strs, ["Lorem", "ipsum", "dolor", "sit"])
        """
        from apysc._type.array import Array
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        suffix: str = get_attr_or_variable_name_suffix(
            instance=self,
            value_identifier="splitted_strs",
        )
        splitted_strs: Array[String] = Array([], variable_name_suffix=suffix)
        self._append_split_expression(splitted_strs=splitted_strs, sep=sep)
        return splitted_strs

    def _append_split_expression(
        self,
        *,
        splitted_strs: "Array[String]",
        sep: "String",
    ) -> None:
        """
        Append a `split` method's expression string.

        Parameters
        ----------
        splitted_strs : Array[String]
            A splitted strings' array.
        sep : String
            A separator string.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"{splitted_strs.variable_name} = "
            f"{self.variable_name}.split({sep.variable_name});"
        )
        expression_data_util.append_js_expression(expression=expression)
