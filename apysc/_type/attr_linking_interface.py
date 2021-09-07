"""Class implementation for the attribute linking interface.

This interface is used for updating an old property value to
achieve consistency in the handler functions.
"""

from typing import Generic, TypeVar
from typing import List

import apysc as ap

_T = TypeVar('_T', ap.Int, ap.Number, ap.String)


class AttrLinkingInterface(Generic[_T]):

    _attr_linking_stack: List[_T]

    def _initialize_attr_linking_stack(self) -> None:
        """
        Initialize the _attr_linking_stack attribute if it hasn't been
        initialized yet.
        """
        if hasattr(self, '_attr_linking_stack'):
            return
        self._attr_linking_stack = []

    def _append_attr_to_linking_stack(self, attr: _T) -> None:
        """
        Append an attribute to the linking attribute stack.

        Parameters
        ----------
        attr : Int or Number or String
            Target attribute to be appended.
        """
        self._initialize_attr_linking_stack()
        self._attr_linking_stack.append(attr)

    def _append_applying_new_attr_val_exp(self, new_attr: _T) -> None:
        """
        Append the expression of applying new attribute value to each
        stacked value.

        Parameters
        ----------
        new_attr : Int or Number or String
            New attribute value.
        """
        self._initialize_attr_linking_stack()
        if not self._attr_linking_stack:
            return
        new_attr_name: str = new_attr.variable_name
        expression: str = ''
        for stacked_value in self._attr_linking_stack:
            if stacked_value.variable_name == new_attr_name:
                continue
            if expression != '':
                expression += '\n'
            expression += (
                f'{stacked_value.variable_name} = {new_attr_name};'
            )
        ap.append_js_expression(expression=expression)
