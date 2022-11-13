"""Class implementation for the x-coordinate interface.
"""

from typing import Dict
from typing import Union

from typing_extensions import final

from apysc._animation.animation_move_mixin import AnimationMoveMixIn
from apysc._animation.animation_x_mixin import AnimationXMixIn
from apysc._display.x_mixin_base import XMixInBase
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.int import Int
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_mixin import VariableNameSuffixAttrMixIn
from apysc._validation import arg_validation_decos


class XMixIn(
    XMixInBase,
    VariableNameSuffixAttrMixIn,
    AnimationXMixIn,
    AnimationMoveMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
):
    @final
    @add_debug_info_setting(module_name=__name__)
    def _initialize_x_if_not_initialized(self) -> None:
        """
        Initialize the _x attribute if this instance does not
        initialize it yet.
        """
        if hasattr(self, "_x"):
            return
        suffix: str = self._get_attr_variable_name_suffix(attr_identifier="x")
        self._x = Int(
            0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_x_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_x_attr_linking_setting(self) -> None:
        """
        Append an x attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(new_attr=self._x, attr_name="x")
        self._append_attr_to_linking_stack(attr=self._x, attr_name="x")

    @property
    @add_debug_info_setting(module_name=__name__)
    def x(self) -> Int:
        """
        Get an x-coordinate.

        Returns
        -------
        x : Int
            X-coordinate.

        References
        ----------
        - Display object x and y interfaces
            - https://simon-ritchie.github.io/apysc/en/display_object_x_and_y.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> rectangle.x = ap.Int(100)
        >>> rectangle.x
        Int(100)
        """
        import apysc as ap
        from apysc._type import value_util

        self._initialize_x_if_not_initialized()
        x: ap.Int = value_util.get_copy(value=self._x)
        return x

    @x.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def x(self, value: Int) -> None:
        """
        Update x-coordinate.

        Parameters
        ----------
        value : Int
            X-coordinate value.

        References
        ----------
        - Display object x and y interfaces
            - https://simon-ritchie.github.io/apysc/en/display_object_x_and_y.html  # noqa
        """
        self._initialize_x_if_not_initialized()
        self._x = value
        self._x._append_incremental_calc_substitution_expression()
        self._append_x_update_expression()

        self._append_x_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_x_update_expression(self) -> None:
        """
        Append the x position updating expression.
        """
        import apysc as ap
        from apysc._type import value_util

        self._initialize_x_if_not_initialized()
        value_str: str = value_util.get_value_str_for_expression(value=self._x)
        expression: str = f"{self.variable_name}.x({value_str});"
        ap.append_js_expression(expression=expression)

    @final
    def _update_x_and_skip_appending_exp(self, *, x: Union[int, Int]) -> None:
        """
        Update x-coordinate and skip appending an expression.

        Parameters
        ----------
        x : int or Int
            X-coordinate value.
        """
        if isinstance(x, Int):
            x_: Int = x
        else:
            suffix: str = self._get_attr_variable_name_suffix(attr_identifier="x")
            x_ = Int(x, variable_name_suffix=suffix)
        self._x = x_

    _x_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_x_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_x_snapshots",
            value=int(self._x._value),
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert a value if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._x._value = self._x_snapshots[snapshot_name]
