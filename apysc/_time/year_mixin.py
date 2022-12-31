"""Class implementations for the year-related mix-in.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos


class YearMixIn(VariableNameMixIn, VariableNameSuffixAttrOrVarMixIn, RevertMixIn):

    _initial_year: Union[int, Int]
    _year: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_four_digit_year(arg_position_index=1)
    def _set_init_year_value(self, *, year: Union[int, Int]) -> None:
        """
        Set an initial year value.

        Parameters
        ----------
        year : Union[int, Int]
            A year value to set.
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_int_from_builtin_val,
        )

        self._initial_year = year
        suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="year")
        self._year = get_copied_int_from_builtin_val(
            integer=year, variable_name_suffix=suffix
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_init_year_argument_expression(self) -> str:
        """
        Get an initial year's argument expression string.

        Returns
        -------
        expression : str
            A created expression string.
        """
        if isinstance(self._initial_year, Int):
            return f"{self._initial_year.variable_name}"
        return f"{self._year._value}"

    @property
    @add_debug_info_setting(module_name=__name__)
    def year(self) -> Int:
        """
        Get a current year's value.

        Returns
        -------
        year : Int
            A current year value.

        References
        ----------
        - DateTime class year property
            - https://simon-ritchie.github.io/apysc/en/datetime_year.html

        Examples
        --------
        >>> import apysc as ap
        >>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
        >>> datetime_.year
        Int(2022)
        >>> datetime_.year = ap.Int(2023)
        >>> datetime_.year
        Int(2023)
        """
        copied_year_val: Int = self._year._copy()
        self._append_year_getter_expression(year_val=copied_year_val)
        return copied_year_val

    @year.setter
    @arg_validation_decos.is_four_digit_year(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def year(self, value: Int) -> None:
        """
        Set a year value.

        Parameters
        ----------
        value : Int
            A year value to set.

        References
        ----------
        - DateTime class year property
            - https://simon-ritchie.github.io/apysc/en/datetime_year.html

        Examples
        --------
        >>> import apysc as ap
        >>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
        >>> datetime_.year
        Int(2022)
        >>> datetime_.year = ap.Int(2023)
        >>> datetime_.year
        Int(2023)
        """
        self._year = value._copy()
        self._append_year_setter_expression(year_val=value)

    @final
    @arg_validation_decos.is_four_digit_year(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def _append_year_getter_expression(self, *, year_val: Int) -> None:
        """
        Append a year's getter expression string.

        Parameters
        ----------
        year_val : Int
            A year value to use in an expression.
        """
        import apysc as ap

        expression: str = (
            f"{year_val.variable_name} = {self.variable_name}.getFullYear();"
        )
        ap.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_four_digit_year(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def _append_year_setter_expression(self, *, year_val: Int) -> None:
        """
        Append a year's setter expression string.

        Parameters
        ----------
        year_val : Int
            A year value to use in an expression.
        """
        import apysc as ap

        expression: str = f"{self.variable_name}.setFullYear({year_val.variable_name});"
        ap.append_js_expression(expression=expression)

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._year._run_all_make_snapshot_methods(snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._year._run_all_revert_methods(snapshot_name=snapshot_name)
