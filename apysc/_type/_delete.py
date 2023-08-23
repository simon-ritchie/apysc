"""This module is for the `delete` function's expression
implementation.
"""

from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos


@arg_validation_decos.is_variable_name_interface_type(arg_position_index=0)
def delete(value: VariableNameMixIn) -> None:
    """
    Delete a specified value and make it undefined.

    Parameters
    ----------
    value : VariableNameMixIn
        A target value to delete.
    """
    _remove_from_parent(value=value)
    value._is_deleted_object = True
    _append_delete_expression(value=value)


def _remove_from_parent(*, value: VariableNameMixIn) -> None:
    """
    Remove a specified value from a parent if it is the `ParentMixIn`
    instance.

    Parameters
    ----------
    value : VariableNameMixIn
        _description_
    """
    from apysc._display.parent_mixin import ParentMixIn

    if not isinstance(value, ParentMixIn):
        return
    value.remove_from_parent()


def _append_delete_expression(*, value: VariableNameMixIn) -> None:
    """
    Append a delete expression.

    Parameters
    ----------
    value : VariableNameMixIn
        A target value to delete.
    """
    from apysc._expression import expression_data_util

    expression: str = (
        f"delete {value.variable_name};" f"\n{value.variable_name} = undefined;"
    )
    expression_data_util.append_js_expression(expression=expression)
