"""Class implementations for the hour-related mix-in.
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


class HourMixIn(VariableNameMixIn, VariableNameSuffixAttrOrVarMixIn, RevertMixIn):
    _initial_hour: Union[int, Int]
    _hour: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_hour_int(arg_position_index=1)
    def _set_init_hour_value(self, *, hour: Union[int, Int]) -> None:
        """
        Set an initial hour value.

        Parameters
        ----------
        hour : Union[int, Int]
            An hour value to set.
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_int_from_builtin_val,
        )

        self._initial_hour = hour
        suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="hour")
        self._hour = get_copied_int_from_builtin_val(
            integer=hour, variable_name_suffix=suffix
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_init_hour_argument_expression(self) -> str:
        """
        Get an initial hour's argument expression string.

        Returns
        -------
        expression : str
            A created expression string.
        """
        if isinstance(self._initial_hour, Int):
            return f", {self._initial_hour.variable_name}"
        return f", {self._hour._value}"

    @property
    @add_debug_info_setting(module_name=__name__)
    def hour(self) -> Int:
        """
        Get a current hour's value.

        Returns
        -------
        hour : Int
            A current hour value.

        References
        ----------
        - DateTime class hour property
            - https://simon-ritchie.github.io/apysc/en/datetime_hour.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1, hour=5)
        >>> datetime_.hour
        Int(5)
        >>> datetime_.hour = ap.Int(10)
        >>> datetime_.hour
        Int(10)
        """
        copied_hour_val: Int = self._hour._copy()
        self._append_hour_getter_expression(hour_val=copied_hour_val)
        return copied_hour_val

    @hour.setter
    @arg_validation_decos.is_hour_int(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def hour(self, value: Int) -> None:
        """
        Set an hour value.

        Parameters
        ----------
        value : Int
            A hour value to set.

        References
        ----------
        - DateTime class hour property
            - https://simon-ritchie.github.io/apysc/en/datetime_hour.html

        Examples
        --------
        >>> import apysc as ap
        >>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1, hour=5)
        >>> datetime_.hour
        Int(5)
        >>> datetime_.hour = ap.Int(10)
        >>> datetime_.hour
        Int(10)
        """
        self._hour = value._copy()
        self._append_hour_setter_expression(hour_val=value)

    @final
    @arg_validation_decos.is_hour_int(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def _append_hour_getter_expression(self, *, hour_val: Int) -> None:
        """
        Append an hour's getter expression string.

        Parameters
        ----------
        hour_val : Int
            An hour value to use in an expression.
        """
        from apysc._expression import expression_data_util

        expression: str = f"{hour_val.variable_name} = {self.variable_name}.getHours();"
        expression_data_util.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_hour_int(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def _append_hour_setter_expression(self, *, hour_val: Int) -> None:
        """
        Append an hour's setter expression string.

        Parameters
        ----------
        hour_val : Int
            An hour value to use in an expression.
        """
        from apysc._expression import expression_data_util

        expression: str = f"{self.variable_name}.setHours({hour_val.variable_name});"
        expression_data_util.append_js_expression(expression=expression)

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._hour._run_all_make_snapshot_methods(snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._hour._run_all_revert_methods(snapshot_name=snapshot_name)
