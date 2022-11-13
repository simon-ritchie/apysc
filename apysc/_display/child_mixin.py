"""Class implementation for the child-related mix-in.
"""

from typing import TYPE_CHECKING
from typing import Any
from typing import Dict
from typing import List
from typing import Union

from typing_extensions import final

from apysc._display.display_object import DisplayObject
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.array import Array
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos

if TYPE_CHECKING:
    from apysc._display.stage import Stage


class ChildMixIn(
    VariableNameSuffixAttrMixIn,
    VariableNameMixIn,
    RevertMixIn,
    VariableNameSuffixMixIn,
):

    _children: Array[DisplayObject]
    stage: "Stage"

    @final
    @arg_validation_decos.is_display_object(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def add_child(self, child: DisplayObject) -> None:
        """
        Add display object child to this instance.

        Parameters
        ----------
        child : DisplayObject
            Child instance to add.

        References
        ----------
        - add_child and remove_child interfaces
            - https://simon-ritchie.github.io/apysc/en/add_child_and_remove_child.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite_1: ap.Sprite = ap.Sprite()
        >>> sprite_1.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> sprite_2: ap.Sprite = ap.Sprite()
        >>> sprite_2.add_child(rectangle)
        """
        self._initialize_children_if_not_initialized()
        if child.parent is not None:
            child.remove_from_parent()
        self._children.append(child)
        child.parent = self
        append_expression_of_add_child(child=child)

    @final
    def _initialize_children_if_not_initialized(self) -> None:
        """
        Initialize _children attribute if this interface does not
        initialize it yet.
        """
        if hasattr(self, "_children"):
            return
        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="children")
        self._children = Array(
            [],
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

    @final
    @arg_validation_decos.is_display_object(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def remove_child(self, child: DisplayObject) -> None:
        """
        Remove display object child from this instance.

        Parameters
        ----------
        child : DisplayObject
            Child instance to remove.

        References
        ----------
        - add_child and remove_child interfaces
            - https://simon-ritchie.github.io/apysc/en/add_child_and_remove_child.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> sprite.graphics.remove_child(rectangle)
        >>> print(rectangle.parent)
        None
        """
        self._initialize_children_if_not_initialized()
        append_expression_of_remove_child(child=child)
        for child_ in self._children._value:
            if child_ != child:
                continue
            self._children.remove(child)
            child.parent = None
            return

    @final
    @arg_validation_decos.is_display_object(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def contains(self, child: DisplayObject) -> Boolean:
        """
        Get a boolean whether this instance contains a specified child.

        Parameters
        ----------
        child : DisplayObject
            Child instance to check.

        Returns
        -------
        result : Boolean
            If this instance contains a specified child, this
            method returns True.

        References
        ----------
        - contains interface
            - https://simon-ritchie.github.io/apysc/en/contains.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> sprite.graphics.contains(rectangle)
        Boolean(True)

        >>> rectangle.remove_from_parent()
        >>> sprite.graphics.contains(rectangle)
        Boolean(False)
        """
        import apysc as ap

        self._initialize_children_if_not_initialized()
        index: ap.Int = self._children.index_of(value=child)
        if index == -1:
            result: ap.Boolean = ap.Boolean(
                False, variable_name_suffix=self._variable_name_suffix
            )
        else:
            result = ap.Boolean(True, variable_name_suffix=self._variable_name_suffix)
        self._append_contains_expression(result=result, child=child)
        return result

    @final
    def _append_contains_expression(
        self, *, result: Boolean, child: DisplayObject
    ) -> None:
        """
        Append contains method expression.

        Parameters
        ----------
        result : Boolean
            Result boolean value.
        child : DisplayObject
            Child instance to check.
        """
        import apysc as ap

        expression: str = (
            f"{result.variable_name} = "
            f"{self.variable_name}.has({child.variable_name});"
        )
        ap.append_js_expression(expression=expression)

    @property
    @add_debug_info_setting(module_name=__name__)
    def num_children(self) -> Int:
        """
        Get a current children's number.

        Returns
        -------
        num_children : int
            Current children number.

        References
        ----------
        - num_children interface
            - https://simon-ritchie.github.io/apysc/en/num_children.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)
        >>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=150, y=50, width=50, height=50
        ... )
        >>> sprite.graphics.num_children
        Int(2)
        """
        import apysc as ap

        self._initialize_children_if_not_initialized()
        num_children: ap.Int = ap.Int(
            value=self._children.length, variable_name_suffix=self._variable_name_suffix
        )
        self._append_num_children_expression(num_children=num_children)
        return num_children

    @final
    def _append_num_children_expression(self, *, num_children: Int) -> None:
        """
        Append num_children method expression.

        Parameters
        ----------
        num_children : Int
            Current children number.
        """
        import apysc as ap

        expression: str = (
            f"{num_children.variable_name} = "
            f"{self.variable_name}.children().length;"
        )
        ap.append_js_expression(expression=expression)

    @final
    @arg_validation_decos.is_integer(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def get_child_at(self, index: Union[int, Int]) -> DisplayObject:
        """
        Get a child at a specified index.

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
        - get_child_at interface
            - https://simon-ritchie.github.io/apysc/en/get_child_at.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af", alpha=0.5)
        >>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=150, y=50, width=50, height=50
        ... )
        >>> child_at_index_1: ap.DisplayObject = sprite.graphics.get_child_at(1)
        >>> child_at_index_1 == rectangle_2
        True
        """
        from apysc._display.any_display_object import AnyDisplayObject
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names

        self._initialize_children_if_not_initialized()
        if self.num_children > index:
            child: DisplayObject = self._children[index]
        else:
            variable_name: str = expression_variables_util.get_next_variable_name(
                type_name=var_names.DISPLAY_OBJECT
            )
            child = AnyDisplayObject(variable_name=variable_name)
        self._append_get_child_at_expression(child=child, index=index)
        return child

    @final
    def _append_get_child_at_expression(
        self, *, child: DisplayObject, index: Union[int, Int]
    ) -> None:
        """
        Append a get_child_at method expression.

        Parameters
        ----------
        child : DisplayObject
            Target index child instance.
        index : int or Int
            Child's index (start from 0).
        """
        import apysc as ap
        from apysc._type import value_util

        index_str: str = value_util.get_value_str_for_expression(value=index)
        expression: str = (
            f"var {child.variable_name} = "
            f"{self.variable_name}.children()"
            f"[{index_str}];"
        )
        ap.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def remove_children(self) -> None:
        """
        Remove all children from this instance.

        References
        ----------
        - remove_children interface
            - https://simon-ritchie.github.io/apysc/en/remove_children.html
        """
        self._initialize_children_if_not_initialized()
        self._children.clear()
        self._append_expression_of_remove_children()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_expression_of_remove_children(self) -> None:
        """
        Append an expression of the `remove_children` interface.
        """
        import apysc as ap

        expression: str = (
            f"var children = {self.variable_name}.children();"
            "\nvar length = children.length;"
            "\nfor (var i = 0; i < length; i++) {"
            "\n  var child = children[i];"
            f"\n  {self.variable_name}.remove(child);"
            "\n}"
        )
        ap.append_js_expression(expression=expression)

    _children_snapshots: Dict[str, List[Any]]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make values' snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_children_if_not_initialized()
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return

        for child in self._children.value:  # type: ignore
            if not isinstance(child, RevertMixIn):
                continue
            child._run_all_make_snapshot_methods(snapshot_name=snapshot_name)

        self._set_single_snapshot_val_to_dict(
            dict_name="_children_snapshots",
            value=[*self._children._value],
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert values if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._children._value = [*self._children_snapshots[snapshot_name]]

        for child in self._children.value:  # type: ignore
            if not isinstance(child, RevertMixIn):
                continue
            child._run_all_revert_methods(snapshot_name=snapshot_name)


@add_debug_info_setting(module_name=__name__)
def append_expression_of_add_child(*, child: DisplayObject) -> None:
    """
    Append expression of add_child (add).

    Parameters
    ----------
    child : DisplayObject
        Child object to add.
    """
    import apysc as ap

    parent_name: str = child.parent.variable_name  # type: ignore
    child_name: str = child.variable_name
    expression: str = f"{parent_name}.add({child_name});"
    ap.append_js_expression(expression=expression)


@add_debug_info_setting(module_name=__name__)
def append_expression_of_remove_child(*, child: DisplayObject) -> None:
    """
    Append expression of remove_child interface.

    Parameters
    ----------
    child : DisplayObject
        Child object to remove.
    """
    import apysc as ap
    from apysc._expression import expression_variables_util
    from apysc._expression import var_names

    parent_name: str = expression_variables_util.get_next_variable_name(
        type_name=var_names.PARENT
    )
    child_name: str = child.variable_name
    expression: str = (
        f"var {parent_name} = {child_name}.parent();"
        f"\nif ({parent_name}) {{"
        f"\n  {parent_name}.removeElement({child_name});"
        "\n}"
    )
    ap.append_js_expression(expression=expression)
