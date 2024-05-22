"""The class implementation for the outlined `queue_music` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialQueueMusicOutlinedIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the outlined `queue_music` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><g><rect fill="none" height="24" width="24"/><rect fill="none" height="24" width="24"/><rect fill="none" height="24" width="24"/></g><g><g/><g><g transform="matrix(1 0 0 1 144 120)"><path d="M-122-114h-5v8.18c-0.31-0.11-0.65-0.18-1-0.18c-1.66,0-3,1.34-3,3s1.34,3,3,3s3-1.34,3-3v-9h3V-114 L-122-114z M-129-114h-12v2h12V-114L-129-114z M-129-110h-12v2h12V-110L-129-110z M-133-106h-8v2h8V-106L-133-106z M-129-103 c0-0.55,0.45-1,1-1c0.55,0,1,0.45,1,1s-0.45,1-1,1C-128.55-102-129-102.45-129-103z"/></g></g></g></svg>'  # noqa
