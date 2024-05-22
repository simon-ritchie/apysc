"""The class implementation for the outlined `change_history` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialChangeHistoryOutlinedIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the outlined `change_history` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M12 7.77L18.39 18H5.61L12 7.77M12 4L2 20h20L12 4z"/></svg>'  # noqa
