"""The class implementation for the outlined `view_stream` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialviewStreamOutlinedIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the outlined `view_stream` material icon.
    """

    def _get_fixed_svg_icon_html(self) -> str:
        """
        Get a fixed SVG icon HTML string.

        Returns
        -------
        fixed_svg_icon_html : str
            Fixed SVG icon HTML string.
        """
        return '<svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M4 6v12h17V6H4zm15 10H6v-3h13v3zM6 11V8h13v3H6z"/></svg>'  # noqa
