"""The class implementation for the `rtt` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialRttIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the `rtt` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0z" fill="none"/><title>ic_dialer_rtt_revised_24px</title><path d="M9.03 3l-1.11 7.07h2.62l.7-4.5h2.58L11.8 18.43H9.47L9.06 21h7.27l.4-2.57h-2.35l2-12.86h2.58l-.71 4.5h2.65L22 3H9.03zM8 5H4l-.31 2h4L8 5zm-.61 4h-4l-.31 2h4l.31-2zm.92 8h-6L2 19h6l.31-2zm.62-4h-6l-.31 2h6.01l.3-2z"/></svg>'  # noqa
