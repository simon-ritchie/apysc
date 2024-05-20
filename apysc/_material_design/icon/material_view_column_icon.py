"""The class implementation for the `view_column` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialviewColumnIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the `view_column` material icon.
    """

    def _get_fixed_svg_icon_html(self) -> str:
        """
        Get a fixed SVG icon HTML string.

        Returns
        -------
        fixed_svg_icon_html : str
            Fixed SVG icon HTML string.

        References
        ----------
        - Material Symbols & Icons, APACHE LICENSE, VERSION 2.0
            - https://fonts.google.com/icons?icon.size=24&icon.color=%23e8eaed
            - https://www.apache.org/licenses/LICENSE-2.0.html
        """
        return '<svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0z" fill="none"/><path d="M10 18h5V5h-5v13zm-6 0h5V5H4v13zM16 5v13h5V5h-5z"/></svg>'  # noqa
