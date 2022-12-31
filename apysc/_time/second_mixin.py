"""Class implementations for the second-related mix-in.
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


class SecondMixIn(VariableNameMixIn, VariableNameSuffixAttrOrVarMixIn, RevertMixIn):

    _initial_second: Union[int, Int]
    _second: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_second_int(arg_position_index=1)
    def _set_init_second_value(self, *, second: Union[int, Int]) -> None:
        """
        Set an initial second value.

        Parameters
        ----------
        second : Union[int, Int]
            A second value to set.
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_int_from_builtin_val,
        )

        self._initial_second = second
        suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="second")
        self._second = get_copied_int_from_builtin_val(
            integer=second, variable_name_suffix=suffix
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_init_second_argument_expression(self) -> str:
        """
        Get an initial second argument expression string.

        Returns
        -------
        expression : str
            A created expression string.
        """
        if isinstance(self._initial_second, Int):
            return f", {self._initial_second.variable_name}"
        return f", {self._second._value}"

    @property
    @add_debug_info_setting(module_name=__name__)
    def second(self) -> Int:
        """
        Get a current second's value.

        Returns
        -------
        second : Int
            A current second value.

        References
        ----------
        - DateTime class second property
            - https://simon-ritchie.github.io/apysc/en/datetime_second.html

        Examples
        --------
        >>> import apysc as ap
        >>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1, second=30)
        >>> datetime_.second
        Int(30)
        >>> datetime_.second = ap.Int(50)
        >>> datetime_.second
        Int(50)
        """
        copied_second_val: Int = self._second._copy()
        self._append_second_getter_expression(second_val=copied_second_val)
        return copied_second_val

    @second.setter
    @arg_validation_decos.is_second_int(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def second(self, value: Int) -> None:
        """
        Set a second value.

        Parameters
        ----------
        value : Int
            A second value to set.

        References
        ----------
        - DateTime class second property
            - https://simon-ritchie.github.io/apysc/en/datetime_second.html

        Examples
        --------
        >>> import apysc as ap
        >>> datetime_: ap.DateTime = ap.DateTime(year=2022, month=12, day=1, second=30)
        >>> datetime_.second
        Int(30)
        >>> datetime_.second = ap.Int(50)
        >>> datetime_.second
        Int(50)
        """
        self._second = value._copy()
        self._append_second_setter_expression(second_val=value)

    @final
    @arg_validation_decos.is_second_int(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def _append_second_getter_expression(self, *, second_val: Int) -> None:
        """
        Append a second's getter expression string.

        Parameters
        ----------
        second_val : Int
            A second value to use in an expression.
        """
        import apysc as ap

        expression: str = (
            f"{second_val.variable_name} = {self.variable_name}.getSeconds();"
        )
        ap.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_second_int(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def _append_second_setter_expression(self, *, second_val: Int) -> None:
        """
        Append a second's setter expression string.

        Parameters
        ----------
        second_val : Int
            A second value to use in an expression.
        """
        import apysc as ap

        expression: str = (
            f"{self.variable_name}.setSeconds({second_val.variable_name});"
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
        self._second._run_all_make_snapshot_methods(snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._second._run_all_revert_methods(snapshot_name=snapshot_name)
