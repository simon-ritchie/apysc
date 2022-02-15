"""Class implementation for graphic's base class.
"""

from typing import Union

from apysc._display import graphics
from apysc._display.display_object import DisplayObject
from apysc._display.flip_x_interface import FlipXInterface
from apysc._display.flip_y_interface import FlipYInterface
from apysc._display.rotation_around_center_interface import \
    RotationAroundCenterInterface
from apysc._display.rotation_around_point_interface import \
    RotationAroundPointInterface
from apysc._display.scale_x_from_center_interface import \
    ScaleXFromCenterInterface
from apysc._display.scale_x_from_point_interface import \
    ScaleXFromPointInterface
from apysc._display.scale_y_from_center_interface import \
    ScaleYFromCenterInterface
from apysc._display.scale_y_from_point_interface import \
    ScaleYFromPointInterface
from apysc._display.skew_x_interface import SkewXInterface
from apysc._display.skew_y_interface import SkewYInterface
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int


class GraphicsBase(
        DisplayObject, RotationAroundCenterInterface,
        RotationAroundPointInterface, ScaleXFromCenterInterface,
        ScaleYFromCenterInterface, ScaleXFromPointInterface,
        ScaleYFromPointInterface, FlipXInterface, FlipYInterface,
        SkewXInterface, SkewYInterface):

    _variable_name: str

    @add_debug_info_setting(  # type: ignore[misc]
        module_name=__name__, class_name='GraphicsBase')
    def __init__(
            self,
            *,
            parent: 'graphics.Graphics',
            x: Union[int, Int],
            y: Union[int, Int],
            variable_name: str) -> None:
        """
        Vector graphic base class.

        Parameters
        ----------
        parent : Graphics
            Parent `Graphics` instance.
        x : int or Int
            X position.
        y : int or Int
            Y position.
        variable_name : str
            Variable name of this instance. This will be used to
            js expression.
        """
        import apysc as ap
        from apysc._display.graphics import Graphics
        from apysc._validation import display_validation
        from apysc._validation import number_validation
        from apysc._validation import string_validation

        display_validation.validate_graphics(graphics=parent)
        self.parent_graphics: Graphics = parent
        number_validation.validate_integer(integer=x)
        number_validation.validate_integer(integer=y)
        if isinstance(x, ap.Int):
            x_: ap.Int = x
        else:
            x_ = ap.Int(x)
        self._x = x_
        if isinstance(y, ap.Int):
            y_: ap.Int = y
        else:
            y_ = ap.Int(y)
        self._y = y_
        string_validation.validate_not_empty_string(string=variable_name)
        super(GraphicsBase, self).__init__(
            variable_name=variable_name)
