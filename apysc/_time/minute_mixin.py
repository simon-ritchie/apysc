"""Class implementations for the minute-related mix-in.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos


class MinuteMixIn(VariableNameMixIn, VariableNameSuffixAttrMixIn, RevertMixIn):

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
        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="minute")
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
        Get a current minute value.

        Returns
        -------
        minute : Int
            A current minute value.
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
        import apysc as ap

        expression: str = (
            f"{minute_val.variable_name} = {self.variable_name}.getMinutes();"
        )
        ap.append_js_expression(expression=expression)

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
        import apysc as ap

        expression: str = (
            f"{self.variable_name}.setMinutes({minute_val.variable_name});"
        )
        ap.append_js_expression(expression=expression)

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
