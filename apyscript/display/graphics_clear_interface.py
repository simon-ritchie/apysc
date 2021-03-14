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
        self._fill_color.value = ''
        self._fill_alpha = Number(1.0)
        self._line_color.value = ''
        self._line_thickness = Int(1)
        self._line_alpha = Number(1.0)
        while self._childs:
            self._childs[0].remove_from_parent()
