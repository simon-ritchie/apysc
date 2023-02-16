"""Class implementation for the `String` class's `split` mix-in.
"""

from typing import TYPE_CHECKING, List

from apysc._type.variable_name_mixin import VariableNameMixIn

if TYPE_CHECKING:
    from apysc._type.array import Array
    from apysc._type.string import String


class StringSplitMixIn(VariableNameMixIn):

    _value: str

    def split(self, *, sep: "String") -> "Array[String]":
        """
        Split a current string with a separator string.

        Parameters
        ----------
        sep : String
            A separator string.

        Returns
        -------
        splited_strs : Array[String]
            A splited strings' array.
        """
        from apysc._type.array import Array
        from apysc._type.variable_name_suffix_attr_or_var_mixin import (
            VariableNameSuffixAttrOrVarMixIn,
        )
        suffix: str = ""
        if isinstance(self, VariableNameSuffixAttrOrVarMixIn):
            suffix = self._get_attr_or_variable_name_suffix(
                value_identifier="splitted_strs"
            )
        splited_strs: Array[String] = Array([], variable_name_suffix=suffix)
        self._append_split_expression(splited_strs=splited_strs, sep=sep)
        return splited_strs


    def _append_split_expression(
        self,
        *,
        splited_strs: "Array[String]",
        sep: "String",
    ) -> None:
        """
        Append a `split` method's expression string.

        Parameters
        ----------
        splited_strs : Array[String]
            A splited strings' array.
        sep : String
            A separator string.
        """
        import apysc as ap

        expression: str = (
            f"{splited_strs.variable_name} = "
            f"{self.variable_name}.split({sep.variable_name});"
        )
        ap.append_js_expression(expression=expression)
