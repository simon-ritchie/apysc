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
        from apyscript.display.fill_color_interface import FillColorInterface
        from apyscript.display.fill_alpha_interface import FillAlphaInterface
        from apyscript.display.line_color_interface import LineColorInterface
        from apyscript.display.line_thickness_interface import \
            LineThicknessInterface
        if isinstance(self, FillColorInterface):
            self._initialize_fill_color_if_not_initialized()
        self._fill_color.value = ''
        if isinstance(self, FillAlphaInterface):
            self._initialize_fill_alpha_if_not_initialized()
        self._fill_alpha.value = 1.0
        if isinstance(self, LineColorInterface):
            self._initialize_line_color_if_not_initialized()
        self._line_color.value = ''
        if isinstance(self, LineThicknessInterface):
            self._initialize_line_thickness_if_not_initialized()
        self._line_thickness.value = 1
        self._line_alpha.value = 1.0
        while self._childs:
            self._childs[0].remove_from_parent()
