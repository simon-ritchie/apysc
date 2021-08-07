"""Class implementation for child related interface.
"""

from typing import Any
from typing import Dict
from typing import List
from typing import Union

import apysc as ap
from apysc._display.display_object import DisplayObject
from apysc._type.revert_interface import RevertInterface


class ChildInterface(RevertInterface):

    _children: ap.Array[DisplayObject]
    _variable_name: str
    stage: Any

    def add_child(self, child: DisplayObject) -> None:
        """
        Add display object child to this instance.

        Parameters
        ----------
        child : DisplayObject
            Child instance to add.

        References
        ----------
        - Sprite class add_child and remove_child interfaces document
            - https://bit.ly/2Ugk47G
        """
        with ap.DebugInfo(
                callable_=self.add_child, locals_=locals(),
                module_name=__name__, class_=ChildInterface):
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
        Initialize _children attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_children'):
            return
        self._children = ap.Array([])

    def remove_child(self, child: DisplayObject) -> None:
        """
        Remove display object child from this instance.

        Parameters
        ----------
        child : DisplayObject
            Child instance to remove.

        References
        ----------
        - Sprite class add_child and remove_child interfaces document
            - https://bit.ly/2Ugk47G
        """
        with ap.DebugInfo(
                callable_=self.remove_child, locals_=locals(),
                module_name=__name__, class_=ChildInterface):
            self._initialize_children_if_not_initialized()
            append_expression_of_remove_child(child=child)
            for child_ in self._children.value:
                if child_ != child:
                    continue
                self._children.remove(child)
                child.parent = None
                return

    def contains(self, child: DisplayObject) -> ap.Boolean:
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

        References
        ----------
        - Sprite class contains interface document
            - https://simon-ritchie.github.io/apysc/sprite_contains.html
        """
        with ap.DebugInfo(
                callable_=self.contains, locals_=locals(),
                module_name=__name__, class_=ChildInterface):
            self._initialize_children_if_not_initialized()
            index: ap.Int = self._children.index_of(value=child)
            if index == -1:
                result: ap.Boolean = ap.Boolean(False)
            else:
                result = ap.Boolean(True)
            self._append_contains_expression(result=result, child=child)
            return result

    def _append_contains_expression(
            self, result: ap.Boolean, child: DisplayObject) -> None:
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
        ap.append_js_expression(expression=expression)

    @property
    def num_children(self) -> ap.Int:
        """
        Get a current children number.

        Returns
        -------
        num_children : int
            Current children number.

        References
        ----------
        - Sprite class num_children interface document
            - https://simon-ritchie.github.io/apysc/sprite_num_children.html
        """
        with ap.DebugInfo(
                callable_='num_children', locals_=locals(),
                module_name=__name__, class_=ChildInterface):
            self._initialize_children_if_not_initialized()
            num_children: ap.Int = ap.Int(value=self._children.length)
            self._append_num_children_expression(num_children=num_children)
            return num_children

    def _append_num_children_expression(
            self, num_children: ap.Int) -> None:
        """
        Append num_children method expression to file.

        Parameters
        ----------
        num_children : Int
            Current children number.
        """
        expression: str = (
            f'{num_children.variable_name} = '
            f'{self._variable_name}.children().length;'
        )
        ap.append_js_expression(expression=expression)

    def get_child_at(self, index: Union[int, ap.Int]) -> DisplayObject:
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

        References
        ----------
        - Sprite class get_child_at interface document
            - https://bit.ly/3rggoi6
        """
        with ap.DebugInfo(
                callable_=self.get_child_at, locals_=locals(),
                module_name=__name__, class_=ChildInterface):
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
            self, child: DisplayObject, index: Union[int, ap.Int]) -> None:
        """
        Append get_child_at method expression to file.

        Parameters
        ----------
        child : DisplayObject
            Target index child instance.
        index : int or Int
            Child's index (start from 0).
        """
        from apysc._type import value_util
        index_str: str = value_util.get_value_str_for_expression(value=index)
        expression: str = (
            f'var {child.variable_name} = '
            f'{self._variable_name}.children()'
            f'[{index_str}];'
        )
        ap.append_js_expression(expression=expression)

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
    with ap.DebugInfo(
            callable_=append_expression_of_add_child, locals_=locals(),
            module_name=__name__):
        parent_name: str = child.parent.variable_name  # type: ignore
        child_name: str = child.variable_name
        expression: str = (
            f'{parent_name}.add({child_name});'
        )
        ap.append_js_expression(expression=expression)


def append_expression_of_remove_child(child: DisplayObject) -> None:
    """
    Append expression of remove_child (removeElement) to file.

    Parameters
    ----------
    child : DisplayObject
        Child object to remove.
    """
    with ap.DebugInfo(
            callable_=append_expression_of_remove_child, locals_=locals(),
            module_name=__name__):
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
        ap.append_js_expression(expression=expression)
