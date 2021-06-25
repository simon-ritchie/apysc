"""Class implementation for child related interface.
"""

from typing import Any
from typing import Dict
from typing import List
from typing import Union

from apysc import Array
from apysc import Boolean
from apysc import Int
from apysc._display.display_object import DisplayObject
from apysc._type.revert_interface import RevertInterface


class ChildInterface(RevertInterface):

    _children: Array[DisplayObject]
    _variable_name: str
    stage: Any

    def add_child(self, child: DisplayObject) -> None:
        """
        Add display object child to this instance.

        Parameters
        ----------
        child : DisplayObject
            Child instance to add.
        """
        from apysc._validation import display_validation
        self._initialize_children_if_not_initialized()
        display_validation.validate_display_object(display_object=child)
        if child.parent is not None:
            child.remove_from_parent()
        self._children.append(child)
        child.parent = self
        append_expression_of_add_child(child=child)

    def _initialize_children_if_not_initialized(self) -> None:
        """
        Initialize _children attribute if it is not initialized yet.
        """
        if hasattr(self, '_children'):
            return
        self._children = Array([])

    def remove_child(self, child: DisplayObject) -> None:
        """
        Remove display object child from this instance.

        Parameters
        ----------
        child : DisplayObject
            Child instance to remove.
        """
        self._initialize_children_if_not_initialized()
        append_expression_of_remove_child(child=child)
        for child_ in self._children.value:
            if child_ != child:
                continue
            self._children.remove(child)
            child.parent = None
            return

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
        self._initialize_children_if_not_initialized()
        index: Int = self._children.index_of(value=child)
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
        from apysc import append_js_expression
        expression: str = (
            f'{result.variable_name} = '
            f'{self._variable_name}.has({child.variable_name});'
        )
        append_js_expression(expression=expression)

    @property
    def num_children(self) -> Int:
        """
        Get a current children number.

        Returns
        -------
        num_children : int
            Current children number.
        """
        self._initialize_children_if_not_initialized()
        num_children: Int = Int(value=self._children.length)
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
        from apysc import append_js_expression
        expression: str = (
            f'{num_children.variable_name} = '
            f'{self._variable_name}.children().length;'
        )
        append_js_expression(expression=expression)

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
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        self._initialize_children_if_not_initialized()
        if self.num_children > index:
            child: DisplayObject = self._children[index]
        else:
            variable_name: str = expression_variables_util.\
                get_next_variable_name(type_name=var_names.DISPLAY_OBJECT)
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
        from apysc import append_js_expression
        from apysc._type import value_util
        index_str: str = value_util.get_value_str_for_expression(value=index)
        expression: str = (
            f'var {child.variable_name} = '
            f'{self._variable_name}.children()'
            f'[{index_str}];'
        )
        print(expression)
        append_js_expression(expression=expression)

    _children_snapshots: Dict[str, List[Any]]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values' snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_children_snapshots'):
            self._children_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_children_if_not_initialized()

        for child in self._children.value:
            if not isinstance(child, RevertInterface):
                continue
            child._run_all_make_snapshot_methods(snapshot_name=snapshot_name)

        self._children_snapshots[snapshot_name] = [*self._children._value]

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._children._value = [*self._children_snapshots[snapshot_name]]

        for child in self._children.value:
            if not isinstance(child, RevertInterface):
                continue
            child._run_all_revert_methods(snapshot_name=snapshot_name)


def append_expression_of_add_child(child: DisplayObject) -> None:
    """
    Append expression of add_child (add) to file.

    Parameters
    ----------
    child : DisplayObject
        Child object to add.
    """
    from apysc import append_js_expression
    parent_name: str = child.parent.variable_name  # type: ignore
    child_name: str = child.variable_name
    expression: str = (
        f'{parent_name}.add({child_name});'
    )
    append_js_expression(expression=expression)


def append_expression_of_remove_child(child: DisplayObject) -> None:
    """
    Append expression of remove_child (removeElement) to file.

    Parameters
    ----------
    child : DisplayObject
        Child object to remove.
    """
    from apysc import append_js_expression
    from apysc._expression import expression_variables_util
    from apysc._expression import var_names
    parent_name: str = expression_variables_util.get_next_variable_name(
        type_name=var_names.PARENT)
    child_name: str = child.variable_name
    expression: str = (
        f'var {parent_name} = {child_name}.parent();'
        f'\nif ({parent_name}) {{'
        f'\n  {parent_name}.removeElement({child_name});'
        '\n}'
    )
    append_js_expression(expression=expression)
