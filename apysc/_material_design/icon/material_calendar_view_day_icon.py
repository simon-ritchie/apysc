"""The class implementation for the `calendar_view_day` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialcalendarViewDayIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the `calendar_view_day` material icon.
    """

    def _get_fixed_svg_icon_html(self) -> str:
        """
        Get a fixed SVG icon HTML string.

        Returns
        -------
        fixed_svg_icon_html : str
            Fixed SVG icon HTML string.
        """
        return '<svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0z" fill="none"/><path d="M3 17h18v2H3zm0-7h18v5H3zm0-4h18v2H3z"/></svg>'  # noqa
