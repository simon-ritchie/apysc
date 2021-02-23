"""Class implementation for child related interface.
"""

from typing import List

from apyscript.display.display_object import DisplayObject
from apyscript.validation import display_validation
from apyscript.expression import expression_file_util
from apyscript.html import html_util


class ChildInterface:

    _childs: List[DisplayObject]

    def add_child(self, child: DisplayObject) -> None:
        """
        Add display object child to this object.

        Parameters
        ----------
        child : DisplayObject
            Child object to add.
        """
        display_validation.validate_display_object(display_object=child)
        self._childs.append(child)
        child.parent = self
        self._append_expression_of_add_child(child=child)

    def _append_expression_of_add_child(self, child: DisplayObject) -> None:
        """
        Append expression of add_child (add) to file.

        Parameters
        ----------
        child : DisplayObject
            Child object to add.
        """
        expression: str = (
            f'{child.parent.variable_name}.add({child.variable_name});'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression(expression=expression)
