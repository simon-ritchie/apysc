"""The class implementation for the outlined `report_off` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialReportOffOutlinedIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the outlined `report_off` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M9.1 5h5.8L19 9.1v5.8l-.22.22 1.42 1.41.8-.8V8.27L15.73 3H8.27l-.8.8 1.41 1.42z"/><circle cx="12" cy="16" r="1"/><path d="M13 9.33V7h-2v.33zM2.41 1.58L1 2.99l3.64 3.64L3 8.27v7.46L8.27 21h7.46l1.64-1.64L21.01 23l1.41-1.41L2.41 1.58zM14.9 19H9.1L5 14.9V9.1l1.05-1.05 9.9 9.9L14.9 19z"/></svg>'  # noqa
