"""Class implementation for graphics clear method related interface.
"""


from apyscript.type import Array
from apyscript.type import Int
from apyscript.type import Number
from apyscript.type import String


class GraphicsClearInterface:

    _fill_color: String
    _fill_alpha: Number
    _line_color: String
    _line_thickness: Int
    _line_alpha: Number
    _childs: Array

    def clear(self) -> None:
        """
        Clear all graphics and reset fill and line settings.
        """
        from apyscript.display.begin_fill_interface import BeginFillInterface
        from apyscript.display.child_interface import ChildInterface
        from apyscript.display.fill_alpha_interface import FillAlphaInterface
        from apyscript.display.fill_color_interface import FillColorInterface
        from apyscript.display.line_alpha_interface import LineAlphaInterface
        from apyscript.display.line_color_interface import LineColorInterface
        from apyscript.display.line_style_interface import LineStyleInterface
        from apyscript.display.line_thickness_interface import \
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
            self._initialize_childs_if_not_initialized()
        while self._childs:
            self._childs[0].remove_from_parent()
