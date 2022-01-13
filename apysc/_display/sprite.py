"""Implementations for Sprite class.
"""

from typing import Optional

from apysc._display import graphics
from apysc._display.child_interface import ChildInterface
from apysc._display.display_object import DisplayObject
from apysc._type.revert_interface import RevertInterface


class Sprite(DisplayObject, ChildInterface, RevertInterface):
    """
    Basic display object that can be parent.

    References
    ----------
    - Sprite document
        - https://simon-ritchie.github.io/apysc/sprite.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite_1: ap.Sprite = ap.Sprite()
    >>> # Create the sprite child rectangle
    >>> sprite_1.graphics.begin_fill(color='#0af')
    >>> rect: ap.Rectangle = sprite_1.graphics.draw_rect(
    ...     x=50, y=50, width=50, height=50)
    >>> sprite_1.graphics.contains(rect)
    Boolean(True)

    >>> # Move the created rectangle to the other sprite
    >>> sprite_2: ap.Sprite = ap.Sprite()
    >>> sprite_2.add_child(rect)
    >>> sprite_1.graphics.contains(rect)
    Boolean(False)
    >>> sprite_2.contains(rect)
    Boolean(True)

    >>> # Move the sprite container
    >>> sprite_2.x = ap.Int(50)
    >>> sprite_2.x
    Int(50)
    """

    graphics: 'graphics.Graphics'

    def __init__(
            self, *,
            variable_name: Optional[str] = None) -> None:
        """
        Basic display object that can be parent.

        Parameters
        ----------
        variable_name : str or None, default None
            Variable name of this instance. This will be used to
            js expression. It is not necessary to specify any
            string except when Sprite subclass will be instantiated.

        References
        ----------
        - Sprite document
            - https://simon-ritchie.github.io/apysc/sprite.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite_1: ap.Sprite = ap.Sprite()
        >>> # Create the sprite child rectangle
        >>> sprite_1.graphics.begin_fill(color='#0af')
        >>> rect: ap.Rectangle = sprite_1.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> sprite_1.graphics.contains(rect)
        Boolean(True)

        >>> # Move the created rectangle to the other sprite
        >>> sprite_2: ap.Sprite = ap.Sprite()
        >>> sprite_2.add_child(rect)
        >>> sprite_1.graphics.contains(rect)
        Boolean(False)
        >>> sprite_2.contains(rect)
        Boolean(True)

        >>> # Move the sprite container
        >>> sprite_2.x = ap.Int(50)
        >>> sprite_2.x
        Int(50)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=Sprite):
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            stage: ap.Stage = ap.get_stage()
            if variable_name is None:
                variable_name = expression_variables_util.\
                    get_next_variable_name(type_name=var_names.SPRITE)
            self._children = ap.Array([])
            super(Sprite, self).__init__(variable_name=variable_name)
            self._append_constructor_expression()
            self.graphics = graphics.Graphics(parent=self)
            stage.add_child(child=self)
            self._set_overflow_visible_setting()

    def _append_constructor_expression(self) -> bool:
        """
        Append Sprite constructor expression.

        Notes
        -----
        Expression not to be added if instance is Sprite subclass.

        Returns
        -------
        appended : bool
            If expression appended, then True will be set.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_constructor_expression,
                locals_=locals(),
                module_name=__name__, class_=Sprite):
            from apysc._display.stage import get_stage_variable_name
            from apysc._type import type_util
            is_same_class_instance: bool = type_util.is_same_class_instance(
                class_=Sprite, instance=self)
            if not is_same_class_instance:
                return False
            stage_variable_name: str = get_stage_variable_name()
            expression: str = (
                f'\nvar {self.variable_name} = {stage_variable_name}.nested();'
            )
            ap.append_js_expression(expression=expression)
            return True

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make values' snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self.graphics._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert values if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self.graphics._run_all_revert_methods(snapshot_name=snapshot_name)

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            Type name and variable name will be set
            (e.g., `Sprite('<variable_name>')`).
        """
        repr_str: str = f"Sprite('{self.variable_name}')"
        return repr_str
