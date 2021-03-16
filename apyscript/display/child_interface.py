"""Class implementation for child related interface.
"""

from typing import Any
from typing import Union

from apyscript.display.display_object import DisplayObject
from apyscript.expression import expression_file_util
from apyscript.expression import expression_variables_util
from apyscript.html import html_util
from apyscript.type import Array
from apyscript.type import Boolean
from apyscript.type import Int
from apyscript.type import value_util
from apyscript.validation import display_validation


class ChildInterface:

    _childs: Array
    _variable_name: str
    _js_child_adjust_num: int = 0
    stage: Any

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
        self._append_num_children_expression(num_children=num_children)
        return num_children

    def _append_num_children_expression(
            self, num_children: Int) -> None:
        """
        Append num_children method expression to file.

        Parameters
        ----------
        num_children : Int
            Current children number.
        """
        expression: str = (
            f'{num_children.variable_name} = '
            f'{self._variable_name}.children().length'
            f' - {self._js_child_adjust_num};'
        )
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)

    def get_child_at(self, index: Union[int, Int]) -> DisplayObject:
        """
        Get child at specified index.

        Parameters
        ----------
        index : int or Int
            Child's index (start from 0).

        Returns
        -------
        child : DisplayObject
            Target index child instance.
        """
        if self.num_children > index:
            child: DisplayObject = self._childs[index]
        else:
            variable_name: str = expression_variables_util.\
                get_next_variable_name(type_name='display_object')
            child = DisplayObject(
                stage=self.stage, variable_name=variable_name)
        self._append_get_child_at_expression(child=child, index=index)
        return child

    def _append_get_child_at_expression(
            self, child: DisplayObject, index: Union[int, Int]) -> None:
        """
        Append get_child_at method expression to file.

        Parameters
        ----------
        child : DisplayObject
            Target index child instance.
        index : int or Int
            Child's index (start from 0).
        """
        index_str: str = value_util.get_value_str_for_expression(value=index)
        expression: str = (
            f'{child.variable_name} = '
            f'{self._variable_name}.children()'
            f'[{index_str} + {self._js_child_adjust_num}];'
        )
        print(expression)
        expression_file_util.wrap_by_script_tag_and_append_expression(
            expression=expression)
