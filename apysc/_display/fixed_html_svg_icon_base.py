"""The class implementation for the fixed HTML SVG icon's base class.
"""

from abc import abstractmethod
from typing import Optional
from typing import Union

from apysc._color.color import Color
from apysc._color.colors import Colors
from apysc._display.child_mixin import ChildMixIn
from apysc._display.svg_icon import SvgIcon
from apysc._type.int import Int
from apysc._type.number import Number


class FixedHtmlSvgIconBase(SvgIcon):
    @abstractmethod
    def _get_fixed_svg_icon_html(self) -> str:
        """
        Get a fixed SVG icon HTML string.

        Returns
        -------
        fixed_svg_icon_html : str
            Fixed SVG icon HTML string.
        """
        return ""

    def __init__(
        self,
        x: Union[float, Number] = 0.0,
        y: Union[float, Number] = 0.0,
        size: Union[int, Int] = 24,
        fill_color: Color = Colors.GRAY_666666,
        fill_alpha: Union[float, Number] = 1.0,
        parent: Optional[ChildMixIn] = None,
        variable_name_suffix: str = "",
    ) -> None:
        """
        The class implementation for the SVG icon's class.

        Parameters
        ----------
        x : Union[float, Number], optional
            X-coordinate of the icon.
        y : Union[float, Number], optional
            Y-coordinate of the icon.
        size : Union[int, Int], optional
            Size of the icon.
        fill_color : Color, optional
            Fill-color of the icon.
        fill_alpha : Union[float, Number], optional
            Fill-alpha of the icon.
        parent : Optional[ChildMixIn], optional
            A parent instance to add this instance.
            If the specified value is None, this interface uses
            a stage instance.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        super(FixedHtmlSvgIconBase, self).__init__(
            svg_icon_html=self._get_fixed_svg_icon_html(),
            x=x,
            y=y,
            size=size,
            fill_color=fill_color,
            fill_alpha=fill_alpha,
            parent=parent,
            variable_name_suffix=variable_name_suffix,
        )
