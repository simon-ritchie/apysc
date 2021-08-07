"""Class implementation for the rotation_around_center_interface
interface.
"""

from typing import Union

import apysc as ap
from apysc._type.revert_interface import RevertInterface
from apysc._type.variable_name_interface import VariableNameInterface


class RotationAroundCenterInterface(VariableNameInterface, RevertInterface):

    _rotation_around_center: ap.Int

    def _initialize_rotation_around_center_if_not_initialized(self) -> None:
        """
        Initialize the `_rotation_around_center` attribute if if hasn't
        been initialized yet.
        """
        if hasattr(self, '_rotation_around_center'):
            return
        self._rotation_around_center = ap.Int(0)

    # def rotate_around_center(
    #         self, additional_rotation: Union[int, ap.Int]) -> None:
    #     """
    #     Add a rotation value around the center of this instance.

    #     Notes
    #     -----
    #     - This interface value is a relative value, not a absolute value,
    #         so if you call this value multiple times, total rotation will
    #         be cumulative.
    #     - This interface is not supported by the container instance, such
    #         as the `Sprite` class due to the HTML (SVG) specification.

    #     Parameters
    #     ----------
    #     additional_rotation : int or Int
    #         A value to add.

    #     References
    #     ----------
    #     - GraphicsBase rotate_around_center interface document
    #         - https://bit.ly/3hP6d12
    #     """
    #     import apysc as ap
    #     with ap.DebugInfo(
    #             callable_=self.rotate_around_center, locals_=locals(),
    #             module_name=__name__, class_=RotateAroundCenterInterface):
    #         from apysc._type import value_util
    #         from apysc._validation import number_validation
    #         number_validation.validate_integer(
    #             integer=additional_rotation)
    #         value_str: str = value_util.get_value_str_for_expression(
    #             value=additional_rotation)
    #         expression: str = (
    #             f'{self.variable_name}.rotate({value_str});'
    #         )
    #         ap.append_js_expression(expression=expression)

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make a value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert a value if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
