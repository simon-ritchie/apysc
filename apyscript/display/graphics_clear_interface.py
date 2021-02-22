"""Class implementation for graphics clear method related interface.
"""


from typing import List, Optional
from apyscript.display.graphic_base import GraphicBase


class GraphicsClearInterface:

    _fill_color: Optional[str] = None
    _fill_alpha: Optional[float] = None
    _line_color: Optional[str] = None
    _line_thickness: Optional[int] = None
    _line_alpha: Optional[float] = None
    _graphics: List[GraphicBase]


    def clear(self) -> None:
        """
        Clear all graphics and reset fill and line settings.
        """
        self._fill_color = None
        self._fill_alpha = None
        self._line_color = None
        self._line_thickness = None
        self._line_alpha = None
        self._graphics = []
