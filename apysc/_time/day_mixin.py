"""Class implementations for the day-related mix-in.
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


class DayMixIn(VariableNameMixIn, VariableNameSuffixAttrOrVarMixIn, RevertMixIn):

    _initial_day: Union[int, Int]
    _day: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_day_int(arg_position_index=1)
    def _set_init_day_value(self, *, day: Union[int, Int]) -> None:
        """
        Set an initial day value.

        Parameters
        ----------
        day : Union[int, Int]
            A day value to set.
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_int_from_builtin_val,
        )

        self._initial_day = day
        suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="day")
        self._day = get_copied_int_from_builtin_val(
            integer=day, variable_name_suffix=suffix
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_init_day_argument_expression(self) -> str:
        """
        Get an initial day's argument expression string.

        Returns
        -------
        expression : str
            A created expression string.
        """
        if isinstance(self._initial_day, Int):
            return f", {self._initial_day.variable_name}"
        return f", {self._day._value}"

    @property
    @add_debug_info_setting(module_name=__name__)
    def day(self) -> Int:
        """
        Get a current day's value.

        Returns
        -------
        day : Int
            A current-day value.

        References
        ----------
        - DateTime class day property
            - https://simon-ritchie.github.io/apysc/en/datetime_day.html

        Examples
        --------
        >>> import apysc as ap
        >>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
        >>> datetime_.day
        Int(1)
        >>> datetime_.day = ap.Int(2)
        >>> datetime_.day
        Int(2)
        """
        copied_day_val: Int = self._day._copy()
        self._append_day_getter_expression(day_val=copied_day_val)
        return copied_day_val

    @day.setter
    @arg_validation_decos.is_day_int(arg_position_index=1)
    def day(self, value: Int) -> None:
        """
        Set a day value.

        Parameters
        ----------
        value : Int
            A day value to set.

        References
        ----------
        - DateTime class day property
            - https://simon-ritchie.github.io/apysc/en/datetime_day.html

        Examples
        --------
        >>> import apysc as ap
        >>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1)
        >>> datetime_.day
        Int(1)
        >>> datetime_.day = ap.Int(2)
        >>> datetime_.day
        Int(2)
        """
        self._day = value._copy()
        self._append_day_setter_expression(day_val=value)

    @final
    @arg_validation_decos.is_day_int(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def _append_day_getter_expression(self, *, day_val: Int) -> None:
        """
        Append a day's getter expression string.

        Parameters
        ----------
        day_val : Int
            A day value to use in an expression.
        """
        import apysc as ap

        expression: str = f"{day_val.variable_name} = {self.variable_name}.getDate();"
        ap.append_js_expression(expression=expression)

    def _append_day_setter_expression(self, *, day_val: Int) -> None:
        """
        Append a day's setter expression string.

        Parameters
        ----------
        day_val : Int
            A day value to use in an expression.
        """
        import apysc as ap

        expression: str = f"{self.variable_name}.setDate({day_val.variable_name});"
        ap.append_js_expression(expression=expression)

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._day._run_all_make_snapshot_methods(snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._day._run_all_revert_methods(snapshot_name=snapshot_name)
