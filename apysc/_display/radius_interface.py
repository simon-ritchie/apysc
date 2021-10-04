"""Class implementation for radius value interface.
"""

from typing import Dict
from typing import Union

import apysc as ap
from apysc._animation.animation_radius_interface import \
    AnimationRadiusInterface
from apysc._type.attr_linking_interface import AttrLinkingInterface
from apysc._type.revert_interface import RevertInterface


class RadiusInterface(
        AnimationRadiusInterface, RevertInterface, AttrLinkingInterface):

    _radius: ap.Int

    def _initialize_radius_if_not_initialized(self) -> None:
        """
        Initialize _radius attribute if it hasn't been initialized yet.
        """
        if hasattr(self, '_radius'):
            return
        self._radius = ap.Int(0)

        self._append_raidus_attr_linking_setting()

    def _append_raidus_attr_linking_setting(self) -> None:
        """
        Append a radius attribute linking setting.
        """
        with ap.DebugInfo(
                callable_=self._append_raidus_attr_linking_setting,
                locals_=locals(),
                module_name=__name__, class_=RadiusInterface):
            self._append_applying_new_attr_val_exp(
                new_attr=self._radius, attr_name='radius')
            self._append_attr_to_linking_stack(
                attr=self._radius, attr_name='radius')

    @property
    def radius(self) -> ap.Int:
        """
        Get radius value.

        Returns
        -------
        radius : Int
            Radius value.
        """
        with ap.DebugInfo(
                callable_='radius', locals_=locals(),
                module_name=__name__, class_=RadiusInterface):
            from apysc._type import value_util
            self._initialize_radius_if_not_initialized()
            return value_util.get_copy(value=self._radius)

    @radius.setter
    def radius(self, value: ap.Int) -> None:
        """
        Update radius value.

        Parameters
        ----------
        value : int or Int
            Radius value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='radius', locals_=locals(),
                module_name=__name__, class_=RadiusInterface):
            from apysc._validation import number_validation
            number_validation.validate_integer(integer=value)
            value = self._get_converted_radius_int(radius=value)
            self._radius = value
            self._radius._append_incremental_calc_substitution_expression()
            self._append_radius_update_expression()

            self._append_raidus_attr_linking_setting()

    def _get_converted_radius_int(self, radius: Union[int, ap.Int]) -> ap.Int:
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
        with ap.DebugInfo(
                callable_=self._get_converted_radius_int, locals_=locals(),
                module_name=__name__, class_=RadiusInterface):
            if not isinstance(radius, ap.Int):
                return ap.Int(radius)
            return radius

    def _append_radius_update_expression(self) -> None:
        """
        Append radius value updating expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_radius_update_expression,
                locals_=locals(),
                module_name=__name__, class_=RadiusInterface):
            from apysc._type import value_util
            self._initialize_radius_if_not_initialized()
            value_str: str = value_util.get_value_str_for_expression(
                value=self._radius)
            expression: str = (
                f'{self.variable_name}.radius({value_str});'
            )
            ap.append_js_expression(expression=expression)

    _radius_snapshots: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_radius_snapshots'):
            self._radius_snapshots = {}
        if self._snapshot_exists(snapshot_name=snapshot_name):
            return
        self._initialize_radius_if_not_initialized()
        self._radius_snapshots[snapshot_name] = int(self._radius._value)

    def _revert(self, snapshot_name: str) -> None:
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
