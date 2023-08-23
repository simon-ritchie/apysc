"""Class implementations for the millisecond-related mix-in.
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


class MillisecondMixIn(
    VariableNameMixIn, VariableNameSuffixAttrOrVarMixIn, RevertMixIn
):
    _initial_millisecond: Union[int, Int]
    _millisecond: Int

    @final
    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_millisecond_int(arg_position_index=1)
    def _set_init_millisecond_value(self, *, millisecond: Union[int, Int]) -> None:
        """
        Set an initial millisecond value.

        Parameters
        ----------
        millisecond : Union[int, Int]
            A millisecond value to set.
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_int_from_builtin_val,
        )

        self._initial_millisecond = millisecond
        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="millisecond"
        )
        self._millisecond = get_copied_int_from_builtin_val(
            integer=millisecond,
            variable_name_suffix=suffix,
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_init_millisecond_argument_expression(self) -> str:
        """
        Get an initial millisecond argument expression string.

        Returns
        -------
        expression : str
            A created expression string.
        """
        if isinstance(self._initial_millisecond, Int):
            return f", {self._initial_millisecond.variable_name}"
        return f", {self._millisecond._value}"

    @property
    @add_debug_info_setting(module_name=__name__)
    def millisecond(self) -> Int:
        """
        Get a current millisecond value.

        Returns
        -------
        millisecond : Int
            A current millisecond value.

        References
        ----------
        - DateTime class millisecond property
            - https://simon-ritchie.github.io/apysc/en/datetime_millisecond.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> datetime_: ap.DateTime = ap.DateTime(
        ...     year=2022, month=12, day=1, millisecond=500
        ... )
        >>> datetime_.millisecond
        Int(500)
        >>> datetime_.millisecond = ap.Int(300)
        >>> datetime_.millisecond
        Int(300)
        """
        copied_millisecond_val: Int = self._millisecond._copy()
        self._append_millisecond_getter_expression(
            millisecond_val=copied_millisecond_val
        )
        return copied_millisecond_val

    @millisecond.setter
    @arg_validation_decos.is_millisecond_int(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def millisecond(self, value: Int) -> None:
        """
        Set a millisecond value.

        Parameters
        ----------
        value : Int
            A millisecond value to set.

        References
        ----------
        - DateTime class millisecond property
            - https://simon-ritchie.github.io/apysc/en/datetime_millisecond.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> datetime_: ap.DateTime = ap.DateTime(
        ...     year=2022, month=12, day=1, millisecond=500
        ... )
        >>> datetime_.millisecond
        Int(500)
        >>> datetime_.millisecond = ap.Int(300)
        >>> datetime_.millisecond
        Int(300)
        """
        self._millisecond = value._copy()
        self._append_millisecond_setter_expression(millisecond_val=value)

    @final
    @arg_validation_decos.is_millisecond_int(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def _append_millisecond_getter_expression(self, *, millisecond_val: Int) -> None:
        """
        Append a millisecond's getter expression string.

        Parameters
        ----------
        millisecond_val : Int
            A millisecond value to use in an expression.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"{millisecond_val.variable_name} = {self.variable_name}.getMilliseconds();"
        )
        expression_data_util.append_js_expression(expression)

    def _append_millisecond_setter_expression(self, *, millisecond_val: Int) -> None:
        """
        Append a millisecond's setter expression string.

        Parameters
        ----------
        millisecond_val : Int
            A millisecond value to use in an expression.
        """
        from apysc._expression import expression_data_util

        expression: str = (
            f"{self.variable_name}.setMilliseconds({millisecond_val.variable_name});"
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
        self._millisecond._run_all_make_snapshot_methods(snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._millisecond._run_all_revert_methods(snapshot_name=snapshot_name)
