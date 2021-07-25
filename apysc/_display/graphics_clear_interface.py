"""Class implementation for graphics clear method related interface.
"""


from typing import Optional

import apysc as ap
from apysc._display.line_dash_dot_setting import LineDashDotSetting
from apysc._display.line_dash_setting import LineDashSetting
from apysc._display.line_dot_setting import LineDotSetting
from apysc._display.line_round_dot_setting import LineRoundDotSetting
from apysc._display.polyline import Polyline


class GraphicsClearInterface:

    _fill_color: ap.String
    _fill_alpha: ap.Number
    _line_color: ap.String
    _line_thickness: ap.Int
    _line_alpha: ap.Number
    _children: ap.Array
    _current_line: Optional[Polyline]
    _line_cap: ap.String
    _line_joints: ap.String
    _line_dot_setting: Optional[LineDotSetting]
    _line_dash_setting: Optional[LineDashSetting]
    _line_round_dot_setting: Optional[LineRoundDotSetting]
    _line_dash_dot_setting: Optional[LineDashDotSetting]

    def clear(self) -> None:
        """
        Clear all graphics and reset fill and line settings.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.clear, locals_=locals(),
                module_name=__name__, class_=GraphicsClearInterface):
            from apysc._display.begin_fill_interface import BeginFillInterface
            from apysc._display.child_interface import ChildInterface
            from apysc._display.fill_alpha_interface import FillAlphaInterface
            from apysc._display.fill_color_interface import FillColorInterface
            from apysc._display.line_alpha_interface import LineAlphaInterface
            from apysc._display.line_color_interface import LineColorInterface
            from apysc._display.line_style_interface import LineStyleInterface
            from apysc._display.line_thickness_interface import \
                LineThicknessInterface
            if isinstance(self, (FillColorInterface, BeginFillInterface)):
                self._initialize_fill_color_if_not_initialized()
            self._fill_color.value = ''
            if isinstance(self, (FillAlphaInterface, BeginFillInterface)):
                self._initialize_fill_alpha_if_not_initialized()
            self._fill_alpha.value = 1.0
            if isinstance(self, (LineColorInterface, LineStyleInterface)):
                self._initialize_line_color_if_not_initialized()
            self._line_color.value = ''
            if isinstance(self, (LineThicknessInterface, LineStyleInterface)):
                self._initialize_line_thickness_if_not_initialized()
            self._line_thickness.value = 1
            if isinstance(self, (LineAlphaInterface, LineStyleInterface)):
                self._initialize_line_alpha_if_not_initialized()
            self._line_alpha.value = 1.0
            if isinstance(self, ChildInterface):
                self._initialize_children_if_not_initialized()
            while self._children:
                self._children[0].remove_from_parent()
            if hasattr(self, '_current_line'):
                self._current_line = None
            if hasattr(self, '_line_cap'):
                self._line_cap = ap.String(ap.LineCaps.BUTT.value)
            if hasattr(self, '_line_joints'):
                self._line_joints = ap.String(ap.LineJoints.MITER.value)
            self._line_dot_setting = None
            self._line_dash_setting = None
            self._line_round_dot_setting = None
            self._line_dash_dot_setting = None
