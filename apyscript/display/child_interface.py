"""Class implementation for child related interface.
"""

from apyscript.display.display_object import DisplayObject
from apyscript.expression import expression_file_util
from apyscript.html import html_util
from apyscript.type import Array
from apyscript.type import Boolean
from apyscript.type import Int
from apyscript.validation import display_validation


class ChildInterface:

    _childs: Array
    _variable_name: str

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
        """
        self._append_expression_of_remove_child(child=child)
        for child_ in self._childs.value:
            if child_ != child:
                continue
            self._childs.remove(child)
            child.parent = None
            return

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

    def contains(self, child: DisplayObject) -> Boolean:
        """
        Get a boolean whether this instance contains specified child.

        Parameters
        ----------
        child : DisplayObject
            Child instance to check.

        Returns
        -------
        result : Boolean
            If this instance contains specified child, True will
            be set.
        """
        index: Int = self._childs.index_of(value=child)
        if index == -1:
            result: Boolean = Boolean(False)
        else:
            result = Boolean(True)
        self._append_contains_expression(result=result, child=child)
        return result

    def _append_contains_expression(
            self, result: Boolean, child: DisplayObject) -> None:
        """
        Append contains method expression to file.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        child : DisplayObject
            Child instance to check.
        """
        expression: str = (
            f'{result.variable_name} = '
            f'{self._variable_name}.has({child.variable_name});'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    @property
    def num_children(self) -> Int:
        """
        Get a current children number.

        Returns
        -------
        num_children : int
            Current children number.
        """
        num_children: Int = Int(value=self._childs.length)
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
