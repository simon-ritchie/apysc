"""Class implementation for child related interface.
"""

from typing import List

from apyscript.display.display_object import DisplayObject
from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.type.int import Int
from apyscript.validation import display_validation


class ChildInterface:

    _childs: List[DisplayObject]

    def add_child(self, child: DisplayObject) -> None:
        """
        Add display object child to this instance.

        Parameters
        ----------
        child : DisplayObject
            Child instance to add.
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
        parent_name: str = child.parent.variable_name  # type: ignore
        child_name: str = child.variable_name
        expression: str = (
            f'{parent_name}.add({child_name});'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression(expression=expression)

    def remove_child(self, child: DisplayObject) -> None:
        """
        Remove display object child from this instance.

        Parameters
        ----------
        child : DisplayObject
            Child instance to remove.

        Raises
        ------
        ValueError
            If specified child not found in this instance's child list.
        """
        for child_ in self._childs:
            if child_ != child:
                continue
            self._childs.remove(child)
            self._append_expression_of_remove_child(child=child)
            child.parent = None
            return
        raise ValueError(
            'Specified child not found in this instance\'s child list.'
            f'\nChild type: {type(child)}'
            f'\nChild variable name: {child.variable_name}')

    def _append_expression_of_remove_child(self, child: DisplayObject) -> None:
        """
        Append expression of remove_child (removeElement) to file.

        Parameters
        ----------
        child : DisplayObject
            Child object to remove.
        """
        parent_name: str = child.parent.variable_name  # type: ignore
        child_name: str = child.variable_name
        expression: str = (
            f'{parent_name}.removeElement({child_name});'
        )
        expression = html_util.wrap_expression_by_script_tag(
            expression=expression)
        expression_file_util.append_expression(expression=expression)

    def contains(self, child: DisplayObject) -> bool:
        """
        Get a boolean whether this instance contains specified child.

        Parameters
        ----------
        child : DisplayObject
            Child instance to check.

        Returns
        -------
        result : bool
            If this instance contains specified child, True will
            be set.
        """
        try:
            self._childs.index(child)
        except ValueError:
            return False
        return True

    @property
    def num_children(self) -> Int:
        """
        Get a current children number.

        Returns
        -------
        num_children : int
            Current children number.
        """
        num_children: Int = Int(value=len(self._childs))
        return num_children

    def get_child_at(self, index: int) -> DisplayObject:
        """
        Get child at specified index.

        Parameters
        ----------
        index : int
            Child's index (start from 0).

        Returns
        -------
        child : DisplayObject
            Target index child instance.

        Raises
        ------
        ValueError
            If specified index is out of range.
        """
        if index >= self.num_children:
            raise ValueError(
                'Specified child index is out of range.'
                f'\nCurrent Child number: {self.num_children}'
                f'\nSpecified index: {index}')
        child: DisplayObject = self._childs[index]
        return child
