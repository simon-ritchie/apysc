"""Class implementation for radius value interface.
"""

from typing import Dict
from typing import Union

from apysc import Int
from apysc.type.revert_interface import RevertInterface
from apysc.type.variable_name_interface import VariableNameInterface


class RadiusInterface(VariableNameInterface, RevertInterface):

    _radius: Int

    def _initialize_radius_if_not_initialized(self) -> None:
        """
        Initialize _radius attribute if it is not initialized yet.
        """
        if hasattr(self, '_radius'):
            return
        self._radius = Int(0)

    @property
    def radius(self) -> Int:
        """
        Get radius value.

        Returns
        -------
        radius : Int
            Radius value.
        """
        from apysc.type import value_util
        self._initialize_radius_if_not_initialized()
        return value_util.get_copy(value=self._radius)

    @radius.setter
    def radius(self, value: Int) -> None:
        """
        Update radius value.

        Parameters
        ----------
        value : int or Int
            Radius value.
        """
        from apysc.validation import number_validation
        number_validation.validate_integer(integer=value)
        value = self._get_converted_radius_int(radius=value)
        self._radius = value
        self._append_radius_update_expression()

    def _get_converted_radius_int(self, radius: Union[int, Int]) -> Int:
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
        if not isinstance(radius, Int):
            return Int(radius)
        return radius

    def _append_radius_update_expression(self) -> None:
        """
        Append radius value updating expression.
        """
        from apysc.expression import expression_file_util
        from apysc.type import value_util
        self._initialize_radius_if_not_initialized()
        value_str: str = value_util.get_value_str_for_expression(
            value=self._radius)
        expression: str = (
            f'{self.variable_name}.radius({value_str});'
        )
        expression_file_util.append_js_expression(expression=expression)

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
