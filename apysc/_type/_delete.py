"""This module is for the `delete` function's expression
implementation.
"""

from apysc._type.variable_name_interface import VariableNameInterface
from apysc._validation import arg_validation_decos


@arg_validation_decos.is_variable_name_interface_type(arg_position_index=0)
def delete(value: VariableNameInterface) -> None:
    """
    Delete a specified value and make it undefined.

    Parameters
    ----------
    value : VariableNameInterface
        A target value to delete.
    """
    _remove_from_parent(value=value)
    value._is_deleted_object = True
    _append_delete_expression(value=value)


def _remove_from_parent(*, value: VariableNameInterface) -> None:
    """
    Remove a specified value from a parent if it is the `ParentInterface`
    instance.

    Parameters
    ----------
    value : VariableNameInterface
        _description_
    """
    from apysc._display.parent_interface import ParentInterface

    if not isinstance(value, ParentInterface):
        return
    value.remove_from_parent()


def _append_delete_expression(*, value: VariableNameInterface) -> None:
    """
    Append a delete expression.

    Parameters
    ----------
    value : VariableNameInterface
        A target value to delete.
    """
    import apysc as ap

    expression: str = (
        f"delete {value.variable_name};" f"\n{value.variable_name} = undefined;"
    )
    ap.append_js_expression(expression=expression)
