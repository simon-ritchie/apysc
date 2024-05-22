"""The class implementation for the `block_flipped` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialBlockFlippedIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the `block_flipped` material icon.
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
        - Material icon document
            - https://simon-ritchie.github.io/apysc/en/material_icon.html
        - Material Symbols & Icons, APACHE LICENSE, VERSION 2.0
            - https://fonts.google.com/icons?icon.size=24&icon.color=%23e8eaed
            - https://www.apache.org/licenses/LICENSE-2.0.html
        """
        return '<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><g><rect fill="none" height="24" width="24"/></g><g><path d="M22,12c0-5.5-4.5-10-10-10S2,6.5,2,12s4.5,10,10,10S22,17.5,22,12z M5.7,7.1l11.2,11.2c-1.3,1.1-3,1.7-4.9,1.7 c-4.4,0-8-3.6-8-8C4,10.1,4.6,8.4,5.7,7.1z M20,12c0,1.9-0.6,3.6-1.7,4.9L7.1,5.7C8.4,4.6,10.1,4,12,4C16.4,4,20,7.6,20,12z"/></g></svg>'  # noqa
