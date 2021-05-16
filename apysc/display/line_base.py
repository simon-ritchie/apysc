"""Base class implementation for each lines.
"""

from typing import Any
from typing import Union
from abc import ABC, abstractmethod

from apysc import Array
from apysc import Int
from apysc.display.fill_alpha_interface import FillAlphaInterface
from apysc.display.fill_color_interface import FillColorInterface
from apysc.display.graphic_base import GraphicBase
from apysc.display.line_alpha_interface import LineAlphaInterface
from apysc.display.line_color_interface import LineColorInterface
from apysc.display.line_dash_dot_setting_interface import \
    LineDashDotSettingInterface
from apysc.display.line_dash_setting_interface import LineDashSettingInterface
from apysc.display.line_dot_setting_interface import LineDotSettingInterface
from apysc.display.line_joints_interface import LineJointsInterface
from apysc.display.line_round_dot_setting_interface import \
    LineRoundDotSettingInterface
from apysc.display.x_interface import XInterface
from apysc.display.y_interface import YInterface


class LineBase(
        GraphicBase, FillColorInterface, FillAlphaInterface,
        LineColorInterface, LineAlphaInterface,
        XInterface, YInterface,
        LineJointsInterface, LineDotSettingInterface,
        LineDashSettingInterface, LineRoundDotSettingInterface,
        LineDashDotSettingInterface, ABC):

    @abstractmethod
    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            Type name and variable name will be set.
        """

    def _set_line_setting_if_not_none_value_exists(
            self, parent_graphics: Any) -> None:
        """
        If a line setting (dot, dash, or something else) with a value
        other than None exists, set that value to the attribute.

        Parameters
        ----------
        parent_graphics : Graphics
            Parent Graphics instance.
        """
        from apysc.display.graphics import Graphics
        parent_graphics_: Graphics = parent_graphics
        if parent_graphics_.line_dot_setting is not None:
            self.line_dot_setting = parent_graphics_.line_dot_setting
            return
        if parent_graphics_.line_dash_setting is not None:
            self.line_dash_setting = parent_graphics_.line_dash_setting
            return
        if parent_graphics_.line_round_dot_setting is not None:
            self.line_round_dot_setting = \
                parent_graphics_.line_round_dot_setting
            return
        if parent_graphics_.line_dash_dot_setting is not None:
            self.line_dash_dot_setting = \
                parent_graphics_.line_dash_dot_setting
            return
