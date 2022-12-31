"""Class implementation for radius value mix-in.
"""

from typing import Dict
from typing import Union

from typing_extensions import final

from apysc._animation.animation_radius_mixin import AnimationRadiusMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.int import Int
from apysc._type.revert_mixin import RevertMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._validation import arg_validation_decos


class RadiusMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    AnimationRadiusMixIn,
    RevertMixIn,
    AttrLinkingMixIn,
):

    _radius: Int

    @final
    def _initialize_radius_if_not_initialized(self) -> None:
        """
        Initialize _radius attribute if this interface does not
        initialize it yet.
        """
        if hasattr(self, "_radius"):
            return
        suffix: str = self._get_attr_or_variable_name_suffix(value_identifier="radius")
        self._radius = Int(
            0,
            variable_name_suffix=suffix,
            skip_init_substitution_expression_appending=True,
        )

        self._append_raidus_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_raidus_attr_linking_setting(self) -> None:
        """
        Append a radius attribute linking settings.
        """
        self._append_applying_new_attr_val_exp(
            new_attr=self._radius, attr_name="radius"
        )
        self._append_attr_to_linking_stack(attr=self._radius, attr_name="radius")

    @property
    @add_debug_info_setting(module_name=__name__)
    def radius(self) -> Int:
        """
        Get radius value.

        Returns
        -------
        radius : Int
            Radius value.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)
        >>> circle.radius = ap.Int(75)
        >>> circle.radius
        Int(75)
        """
        from apysc._type import value_util

        self._initialize_radius_if_not_initialized()
        return value_util.get_copy(value=self._radius)

    @radius.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def radius(self, value: Int) -> None:
        """
        Update radius value.

        Parameters
        ----------
        value : Int
            Radius value.
        """
        self._radius = value
        self._radius._append_incremental_calc_substitution_expression()
        self._append_radius_update_expression()

        self._append_raidus_attr_linking_setting()

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_converted_radius_int(self, *, radius: Union[int, Int]) -> Int:
        """
        Get a radius converted Int instance.

        Parameters
        ----------
        radius : int or Int
            Radius value.

        Returns
        -------
        radius : Int
            Type converted radius value.
        """
        import apysc as ap

        if not isinstance(radius, ap.Int):
            suffix: str = self._get_attr_or_variable_name_suffix(
                value_identifier="radius"
            )
            return ap.Int(radius, variable_name_suffix=suffix)
        return radius

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_radius_update_expression(self) -> None:
        """
        Append radius value updating expression.
        """
        import apysc as ap
        from apysc._type import value_util

        self._initialize_radius_if_not_initialized()
        value_str: str = value_util.get_value_str_for_expression(value=self._radius)
        expression: str = f"{self.variable_name}.radius({value_str});"
        ap.append_js_expression(expression=expression)

    _radius_snapshots: Dict[str, int]

    def _make_snapshot(self, *, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._initialize_radius_if_not_initialized()
        self._set_single_snapshot_val_to_dict(
            dict_name="_radius_snapshots",
            value=int(self._radius._value),
            snapshot_name=snapshot_name,
        )

    def _revert(self, *, snapshot_name: str) -> None:
        """
        Revert value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._radius._value = self._radius_snapshots[snapshot_name]
