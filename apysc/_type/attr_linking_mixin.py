"""Class implementation for the attribute linking mix-in.

This mix-in updates an old property value to achieve
consistency in the handler functions.
"""

from typing import Dict
from typing import List
from typing import Union

from typing_extensions import final

from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String

_AttrName = str
_Attr = Union[Int, Number, String, Boolean]


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
        for in_stack_value in self._attr_linking_stack[attr_name]:
            if in_stack_value.variable_name == attr.variable_name:
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
        import apysc as ap

        self._initialize_attr_linking_stack(attr_name=attr_name)
        if not self._attr_linking_stack:
            return
        new_attr_name: str = new_attr.variable_name
        expression: str = ""
        for stacked_value in self._attr_linking_stack[attr_name]:
            if stacked_value.variable_name == new_attr_name:
                continue
            if expression != "":
                expression += "\n"
            expression += f"{stacked_value.variable_name} = {new_attr_name};"
        ap.append_js_expression(expression=expression)
