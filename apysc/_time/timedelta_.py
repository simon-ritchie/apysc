"""Class implementations for timedelta-related interfaces.
"""

from datetime import timedelta
from typing import TYPE_CHECKING

from typing_extensions import final

from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.initial_substitution_exp_mixin import InitialSubstitutionExpMixIn

if TYPE_CHECKING:
    from apysc._time.datetime_ import DateTime


class TimeDelta(
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    InitialSubstitutionExpMixIn,
):
    """
    Class implementations for timedelta-related interfaces.
    """

    _left_datetime: "DateTime"
    _right_datetime: "DateTime"

    @arg_validation_decos.is_apysc_datetime(arg_position_index=1)
    @arg_validation_decos.is_apysc_datetime(arg_position_index=2)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        left_datetime: "DateTime",
        right_datetime: "DateTime",
        *,
        skip_init_substitution_expression_appending: bool = False,
    ) -> None:
        """
        Class implementations for timedelta-related interfaces.

        Parameters
        ----------
        left_datetime : DateTime
            Left-side datetime to compare.
        right_datetime : DateTime
            Right-side datetime to compare.
        skip_init_substitution_expression_appending : bool, default False
            A boolean indicates whether to skip an initial substitution
            expression or not. The `DateTime` class uses this option internally.
        """
        from apysc._expression import var_names
        from apysc._expression import expression_variables_util
        from apysc._expression.event_handler_scope import TemporaryNotHandlerScope

        with TemporaryNotHandlerScope():
            self._left_datetime = left_datetime
            self._right_datetime = right_datetime
            self._variable_name_suffix = _get_variable_name_suffix_from_datetimes(
                left_datetime=left_datetime,
                right_datetime=right_datetime,
            )
            self.variable_name = expression_variables_util.get_next_variable_name(
                type_name=var_names.TIME_DELTA,
            )

            self._append_constructor_expression()

        self._append_initial_substitution_expression_if_in_handler_scope(
            skip_appending=skip_init_substitution_expression_appending,
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression.
        """
        import apysc as ap

        expression: str = self._create_initial_substitution_expression()
        pass

    @final
    @add_debug_info_setting(module_name=__name__)
    def _create_initial_substitution_expression(self) -> str:
        """
        Create an initial value's substitution expression string.

        Returns
        -------
        expression : str
            Created expression string.
        """
        expression: str = (
            f"{self.variable_name} = {self._left_datetime.variable_name}.getTime()"
            f" - {self._right_datetime.variable_name}.getTime();"
        )
        return expression


def _get_variable_name_suffix_from_datetimes(
    *,
    left_datetime: "DateTime",
    right_datetime: "DateTime",
) -> str:
    """
    Get a variable name suffix from specified datetimes instances.

    Parameters
    ----------
    left_datetime : DateTime
        Left-side datetime to compare.
    right_datetime : DateTime
        Right-side datetime to compare.

    Returns
    -------
    variable_name_suffix : str
        A created variable name suffix string.
    """
    if (
        left_datetime._variable_name_suffix == ""
        and right_datetime._variable_name_suffix == ""
    ):
        return ""
    if left_datetime._variable_name_suffix == "":
        return right_datetime._variable_name_suffix
    if right_datetime._variable_name_suffix == "":
        return left_datetime._variable_name_suffix
    variable_name_suffix: str = (
        f"{left_datetime._variable_name_suffix}_"
        f"{right_datetime._variable_name_suffix}"
    )
    return variable_name_suffix