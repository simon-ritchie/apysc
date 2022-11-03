"""Class implementation for the graphics clear method-related mix-in.
"""


from typing import Optional

from typing_extensions import final

from apysc._display.line_dash_dot_setting import LineDashDotSetting
from apysc._display.line_dash_setting import LineDashSetting
from apysc._display.line_dot_setting import LineDotSetting
from apysc._display.line_round_dot_setting import LineRoundDotSetting
from apysc._display.polyline import Polyline
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String


class GraphicsClearMixIn:

    _fill_color: String
    _fill_alpha: Number
    _line_color: String
    _line_thickness: Int
    _line_alpha: Number
    _current_line: Optional[Polyline]
    _line_cap: String
    _line_joints: String
    _line_dot_setting: Optional[LineDotSetting]
    _line_dash_setting: Optional[LineDashSetting]
    _line_round_dot_setting: Optional[LineRoundDotSetting]
    _line_dash_dot_setting: Optional[LineDashDotSetting]

    @final
    @add_debug_info_setting(module_name=__name__)
    def clear(self) -> None:
        """
        Clear all graphics and reset fill and line settings.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> _ = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
        >>> _ = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)
        >>> sprite.graphics.num_children
        Int(2)

        >>> sprite.graphics.fill_color
        String('#00aaff')

        >>> sprite.graphics.clear()
        >>> sprite.graphics.num_children
        Int(0)

        >>> sprite.graphics.fill_color
        String('')

        References
        ----------
        - Graphics clear interface
            - https://simon-ritchie.github.io/apysc/en/graphics_clear.html
        """
        import apysc as ap
        from apysc._display.begin_fill_mixin import BeginFillMixIn
        from apysc._display.child_mixin import ChildMixIn
        from apysc._display.fill_alpha_mixin import FillAlphaMixIn
        from apysc._display.fill_color_mixin import FillColorMixIn
        from apysc._display.line_alpha_mixin import LineAlphaMixIn
        from apysc._display.line_color_mixin import LineColorMixIn
        from apysc._display.line_style_mixin import LineStyleMixIn
        from apysc._display.line_thickness_mixin import LineThicknessMixIn

        if isinstance(self, (FillColorMixIn, BeginFillMixIn)):
            self._initialize_fill_color_if_not_initialized()
        self._fill_color.value = ""
        if isinstance(self, (FillAlphaMixIn, BeginFillMixIn)):
            self._initialize_fill_alpha_if_not_initialized()
        self._fill_alpha.value = 1.0
        if isinstance(self, (LineColorMixIn, LineStyleMixIn)):
            self._initialize_line_color_if_not_initialized()
        self._line_color.value = ""
        if isinstance(self, (LineThicknessMixIn, LineStyleMixIn)):
            self._initialize_line_thickness_if_not_initialized()
        self._line_thickness.value = 1
        if isinstance(self, (LineAlphaMixIn, LineStyleMixIn)):
            self._initialize_line_alpha_if_not_initialized()
        self._line_alpha.value = 1.0
        if isinstance(self, ChildMixIn):
            self._initialize_children_if_not_initialized()
            self.remove_children()
        if hasattr(self, "_current_line"):
            self._current_line = None
        if hasattr(self, "_line_cap"):
            self._line_cap = ap.String(ap.LineCaps.BUTT.value)
        if hasattr(self, "_line_joints"):
            self._line_joints = ap.String(ap.LineJoints.MITER.value)
        self._line_dot_setting = None
        self._line_dash_setting = None
        self._line_round_dot_setting = None
        self._line_dash_dot_setting = None
