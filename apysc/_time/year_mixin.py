"""Class implementations for the year-related mix-in.
"""

from typing import Union

from typing_extensions import final

from apysc._type.int import Int
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn


class YearMixIn(VariableNameSuffixAttrMixIn):

    _initial_year: Union[int, Int]
    _year: Int

    def _set_init_year_value(self, *, year: Union[int, Int]) -> None:
        """
        Set an initial year value.

        Parameters
        ----------
        year : Union[int, Int]
            An year's value to set.
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_int_from_builtin_val
        )
        self._initial_year = year
        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="year")
        self._year = get_copied_int_from_builtin_val(
            integer=year, variable_name_suffix=suffix
        )
