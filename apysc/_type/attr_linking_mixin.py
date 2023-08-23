"""Class implementation for the attribute linking mix-in.

This mix-in updates an old property value to achieve
consistency in the handler functions.
"""

from typing import Dict
from typing import List
from typing import Union

from typing_extensions import final

from apysc._color.color import Color
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String

_AttrName = str
_Attr = Union[Int, Number, String, Boolean, Color]


class AttrLinkingMixIn:
    _attr_linking_stack: Dict[_AttrName, List[_Attr]]

    @final
    def _initialize_attr_linking_stack(self, *, attr_name: str) -> None:
        """
        Initialize the _attr_linking_stack attribute if
        this instance does not initialize it yet.

        Parameters
        ----------
        attr_name : str
            Target attribute name.
        """
        if not hasattr(self, "_attr_linking_stack"):
            self._attr_linking_stack = {}
        if attr_name in self._attr_linking_stack:
            return
        self._attr_linking_stack[attr_name] = []

    @final
    def _append_attr_to_linking_stack(self, *, attr: _Attr, attr_name: str) -> None:
        """
        Append an attribute to the linking attribute stack.

        Parameters
        ----------
        attr : Int or Number or String or Boolean
            Target attribute to be appended.
        attr_name : str
            Target attribute name.
        """
        self._initialize_attr_linking_stack(attr_name=attr_name)
        if self._is_target_attr_already_linked(attr=attr, attr_name=attr_name):
            return
        self._attr_linking_stack[attr_name].append(attr)

    @final
    def _is_target_attr_already_linked(self, *, attr: _Attr, attr_name: str) -> bool:
        """
        Get a boolean value whether this instance already
        appends a specified attribute to the linking
        attribute stack.

        Parameters
        ----------
        attr : Int or Number or String or Boolean
            Target attribute to be appended.
        attr_name : str
            Target attribute name.

        Returns
        -------
        result : bool
            If this instance already appends a specified
            attribute to the linking stack, this interface
            returns True.
        """

        self._initialize_attr_linking_stack(attr_name=attr_name)
        attr_variable_name: str = _get_variable_name_from_attr(attr=attr)
        for in_stack_value in self._attr_linking_stack[attr_name]:
            in_stack_value_variable_name: str = _get_variable_name_from_attr(
                attr=in_stack_value
            )
            if in_stack_value_variable_name == attr_variable_name:
                return True
        return False

    @final
    def _append_applying_new_attr_val_exp(
        self, *, new_attr: _Attr, attr_name: str
    ) -> None:
        """
        Append the expression of applying a new attribute
        value to each stacked value.

        Parameters
        ----------
        new_attr : Int or Number or String or Boolean
            New attribute value.

        attr_name : str
            Target attribute name.
        """
        from apysc._expression import expression_data_util

        self._initialize_attr_linking_stack(attr_name=attr_name)
        if not self._attr_linking_stack:
            return
        new_attr_name: str = _get_variable_name_from_attr(attr=new_attr)
        expression: str = ""
        for stacked_value in self._attr_linking_stack[attr_name]:
            stacked_value_variable_name: str = _get_variable_name_from_attr(
                attr=stacked_value
            )
            if stacked_value_variable_name == new_attr_name:
                continue
            if expression != "":
                expression += "\n"
            expression += f"{stacked_value_variable_name} = {new_attr_name};"
        expression_data_util.append_js_expression(expression=expression)


def _get_variable_name_from_attr(*, attr: _Attr) -> str:
    """
    Get a variable name from a specified attribute.

    Parameters
    ----------
    attr : _Attr
        An attribute.

    Returns
    -------
    variable_name : str
        A specified attribute's variable name.
    """
    from apysc._type.variable_name_mixin import VariableNameMixIn

    if isinstance(attr, Color):
        return attr._value.variable_name
    if isinstance(attr, VariableNameMixIn):
        return attr.variable_name
    return ""
