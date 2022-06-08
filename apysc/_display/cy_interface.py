"""Class implementation for the center y-coordinate interface.
"""

from typing import Dict

from apysc._animation.animation_cy_interface import AnimationCyInterface
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.int import Int
from apysc._type.revert_interface import RevertInterface
from apysc._validation import arg_validation_decos


class CyInterface(
        AnimationCyInterface, RevertInterface, AttrLinkingInterface):

    _cy: Int

    def _initialize_cy_if_not_initialized(self) -> None:
        """
        Initialize _cy attribute if this interface does not
        initialize it yet.
        """
        if hasattr(self, '_cy'):
            return
        self._cy = Int(0)

        self._append_cy_attr_linking_setting()

    @add_debug_info_setting(
        module_name=__name__, class_name='CyInterface')
    def _append_cy_attr_linking_setting(self) -> None:
        """
        Append cy attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._cy, attr_name='cy')
        self._append_attr_to_linking_stack(attr=self._cy, attr_name='cy')

    @property
    @add_debug_info_setting(
        module_name=__name__, class_name='CyInterface')
    def y(self) -> Int:
        """
        Get a center y-coordinate.

        Returns
        -------
        y : Int
            Center y-coordinate.

        References
        ----------
        - Display object x and y interfaces document
            - https://simon-ritchie.github.io/apysc/display_object_x_and_y.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
        >>> circle: ap.Circle = sprite.graphics.draw_circle(
        ...     x=100, y=100, radius=50)
        >>> circle.y = ap.Int(120)
        >>> circle.y
        Int(120)
        """
        import apysc as ap
        from apysc._type import value_util
        self._initialize_cy_if_not_initialized()
        y: ap.Int = value_util.get_copy(value=self._cy)
        return y

    @y.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(
        module_name=__name__, class_name='CyInterface')
    def y(self, value: Int) -> None:
        """
        Update a center y-coordinate.

        Parameters
        ----------
        value : Int
            Center y-coordinate value.

        References
        ----------
        - Display object x and y interfaces document
            - https://simon-ritchie.github.io/apysc/display_object_x_and_y.html  # noqa
        """
        self._cy = value
        self._cy._append_incremental_calc_substitution_expression()
        self._append_cy_update_expression()

        self._append_cy_attr_linking_setting()

    @add_debug_info_setting(
        module_name=__name__, class_name='CyInterface')
    def _append_cy_update_expression(self) -> None:
        """
        Append cy position updating expression.
        """
        import apysc as ap
        from apysc._type import value_util
        self._initialize_cy_if_not_initialized()
        value_str: str = value_util.get_value_str_for_expression(
            value=self._cy)
        expression: str = (
            f'{self.variable_name}.cy({value_str});'
        )
        ap.append_js_expression(expression=expression)

    _cy_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_cy_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name='_cy_snapshots',
            value=int(self._cy._value), snapshot_name=snapshot_name)

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
        self._cy._value = self._cy_snapshots[snapshot_name]
