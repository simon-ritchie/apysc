"""The class implementation for the outlined `invert_colors_off` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialInvertColorsOffOutlinedIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the outlined `invert_colors_off` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M12 5.1v4.05l7.4 7.4c1.15-2.88.59-6.28-1.75-8.61L12 2.27 8.56 5.71l1.41 1.41L12 5.1zm-7.6-.73L2.99 5.78l2.78 2.78c-2.54 3.14-2.35 7.75.57 10.68C7.9 20.8 9.95 21.58 12 21.58c1.78 0 3.56-.59 5.02-1.77l2.7 2.7 1.41-1.41L4.4 4.37zM12 19.59c-1.6 0-3.11-.62-4.24-1.76C6.62 16.69 6 15.19 6 13.59c0-1.32.43-2.56 1.21-3.59L12 14.79v4.8z"/></svg>'  # noqa
