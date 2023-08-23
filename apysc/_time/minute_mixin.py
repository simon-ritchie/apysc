"""Class implementations for the minute-related mix-in.
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


class MinuteMixIn(VariableNameMixIn, VariableNameSuffixAttrOrVarMixIn, RevertMixIn):
    _initial_minute: Union[int, Int]
    _minute: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_minute_int(arg_position_index=1)
    def _set_init_minute_value(self, *, minute: Union[int, Int]) -> None:
        """
        Set an initial minute value.

        Parameters
        ----------
        minute : Union[int, Int]
            A minute value to set.
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_int_from_builtin_val,
        )

        self._initial_minute = minute
        suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="minute")
        self._minute = get_copied_int_from_builtin_val(
            integer=minute, variable_name_suffix=suffix
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_init_minute_argument_expression(self) -> str:
        """
        Get an initial minute's argument expression string.

        Returns
        -------
        expression : str
            A created expression string.
        """
        if isinstance(self._initial_minute, Int):
            return f", {self._initial_minute.variable_name}"
        return f", {self._minute._value}"

    @property
    @add_debug_info_setting(module_name=__name__)
    def minute(self) -> Int:
        """
        Get a current minute's value.

        Returns
        -------
        minute : Int
            A current minute value.

        References
        ----------
        - DateTime class minute property
            - https://simon-ritchie.github.io/apysc/en/datetime_minute.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1, minute=30)
        >>> datetime_.minute
        Int(30)
        >>> datetime_.minute = ap.Int(50)
        >>> datetime_.minute
        Int(50)
        """
        copied_minute_val: Int = self._minute._copy()
        self._append_minute_getter_expression(minute_val=copied_minute_val)
        return copied_minute_val

    @minute.setter
    @arg_validation_decos.is_minute_int(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def minute(self, value: Int) -> None:
        """
        Set a minute value.

        Parameters
        ----------
        value : Int
            A minute value to set.

        References
        ----------
        - DateTime class minute property
            - https://simon-ritchie.github.io/apysc/en/datetime_minute.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1, minute=30)
        >>> datetime_.minute
        Int(30)
        >>> datetime_.minute = ap.Int(50)
        >>> datetime_.minute
        Int(50)
        """
        self._minute = value._copy()
        self._append_minute_setter_expression(minute_val=value)

    @final
    @arg_validation_decos.is_minute_int(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def _append_minute_getter_expression(self, *, minute_val: Int) -> None:
        """
        Append a minute's getter expression string.

        Parameters
        ----------
        minute_val : Int
            A month value to use in an expression.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"{minute_val.variable_name} = {self.variable_name}.getMinutes();"
        )
        expression_data_util.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_minute_int(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def _append_minute_setter_expression(self, *, minute_val: Int) -> None:
        """
        Append a minute's setter expression string.

        Parameters
        ----------
        minute_val : Int
            A minute value to use in an expression.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"{self.variable_name}.setMinutes({minute_val.variable_name});"
        )
        expression_data_util.append_js_expression(expression=expression)

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._minute._run_all_make_snapshot_methods(snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._minute._run_all_revert_methods(snapshot_name=snapshot_name)
