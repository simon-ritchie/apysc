# pyright: reportGeneralTypeIssues=false

"""Implementations for Sprite class.
"""

from typing_extensions import final

from apysc._display import graphics
from apysc._display.child_mixin import ChildMixIn
from apysc._display.css_mixin import CssMixIn
from apysc._display.display_object import DisplayObject
from apysc._display.get_bounds_mixin import GetBoundsMixIn
from apysc._display.set_overflow_visible_setting_mixin import (
    SetOverflowVisibleSettingMixIn,
)
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn
from apysc._event.enter_frame_mixin import EnterFrameMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._loop.initialize_with_base_value_interface import (
    InitializeWithBaseValueInterface,
)
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._validation import arg_validation_decos

_Graphics = graphics.Graphics


class Sprite(
    XMixIn,
    YMixIn,
    EnterFrameMixIn,
    SetOverflowVisibleSettingMixIn,
    CssMixIn,
    GetBoundsMixIn,
    DisplayObject,
    ChildMixIn,
    RevertMixIn,
    VariableNameSuffixMixIn,
    InitializeWithBaseValueInterface,
):
    """
    This class is for the basic display object that
    can be a parent.

    References
    ----------
    - Sprite
        - https://simon-ritchie.github.io/apysc/en/sprite.html

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite_1: ap.Sprite = ap.Sprite()
    >>> # Create the sprite child rectangle
    >>> sprite_1.graphics.begin_fill(color=ap.Color("#0af"))
    >>> rect: ap.Rectangle = sprite_1.graphics.draw_rect(
    ...     x=50, y=50, width=50, height=50
    ... )
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
    >>> sprite_2.x = ap.Number(50)
    >>> sprite_2.x
    Number(50.0)
    """

    graphics: "_Graphics"

    @arg_validation_decos.is_builtin_string(arg_position_index=1, optional=True)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self, *, variable_name: str = "", variable_name_suffix: str = ""
    ) -> None:
        """
        Create a basic display object that can be a parent.

        Parameters
        ----------
        variable_name : str, default '
            Variable name of this instance. A js expression uses
            this setting. It is unnecessary to specify any
            string except when instantiating the `Sprite` subclass.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        References
        ----------
        - Sprite
            - https://simon-ritchie.github.io/apysc/en/sprite.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite_1: ap.Sprite = ap.Sprite()
        >>> # Create the sprite child rectangle
        >>> sprite_1.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rect: ap.Rectangle = sprite_1.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
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
        >>> sprite_2.x = ap.Number(50)
        >>> sprite_2.x
        Number(50.0)
        """
        from apysc._display.stage import Stage
        from apysc._display.stage import get_stage
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._type.array import Array

        self._variable_name_suffix = variable_name_suffix
        stage: Stage = get_stage()
        if variable_name == "":
            variable_name = expression_variables_util.get_next_variable_name(
                type_name=var_names.SPRITE
            )

        suffix: str = self._get_attr_or_variable_name_suffix(
            value_identifier="children"
        )
        self._children = Array([], variable_name_suffix=suffix)

        super(Sprite, self).__init__(variable_name=variable_name)
        self._append_constructor_expression()
        suffix = self._get_attr_or_variable_name_suffix(value_identifier="graphics")
        self.graphics = graphics.Graphics(parent=self, variable_name_suffix=suffix)
        stage.add_child(child=self)
        self._set_overflow_visible_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        """
        Append Sprite constructor expression.
        """
        from apysc._display.stage import Stage
        from apysc._display.stage import get_stage
        from apysc._expression import expression_data_util

        stage: Stage = get_stage()
        expression: str = (
            f"\nvar {self.variable_name} = {stage.variable_name}.nested();"
        )
        expression_data_util.append_js_expression(expression=expression)

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
        self.graphics._run_all_make_snapshot_methods(snapshot_name=snapshot_name)

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
        self.graphics._run_all_revert_methods(snapshot_name=snapshot_name)

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            Type name and variable name will be set
            (e.g., `Sprite("<variable_name>")`).
        """
        repr_str: str = f'{Sprite.__name__}("{self.variable_name}")'
        return repr_str

    @classmethod
    @final
    def _initialize_with_base_value(cls) -> "Sprite":
        """
        Initialize this class with a base value(s).

        Returns
        -------
        sprite : Sprite
            An initialized sprite instance.
        """
        from apysc._type.boolean import Boolean

        sprite: Sprite = Sprite()
        sprite.visible = Boolean(False)
        return sprite
