"""The class implementation for the outlined `supervised_user_circle` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialSupervisedUserCircleOutlinedIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the outlined `supervised_user_circle` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M0 0h24v24H0V0z" fill="none"/><path d="M12.5 10c0-1.65-1.35-3-3-3s-3 1.35-3 3 1.35 3 3 3 3-1.35 3-3zm-3 1c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm6.5 2c1.11 0 2-.89 2-2 0-1.11-.89-2-2-2-1.11 0-2.01.89-2 2 0 1.11.89 2 2 2zM11.99 2.01c-5.52 0-10 4.48-10 10s4.48 10 10 10 10-4.48 10-10-4.48-10-10-10zM5.84 17.12c.68-.54 2.27-1.11 3.66-1.11.07 0 .15.01.23.01.24-.64.67-1.29 1.3-1.86-.56-.1-1.09-.16-1.53-.16-1.3 0-3.39.45-4.73 1.43-.5-1.04-.78-2.2-.78-3.43 0-4.41 3.59-8 8-8s8 3.59 8 8c0 1.2-.27 2.34-.75 3.37-1-.59-2.36-.87-3.24-.87-1.52 0-4.5.81-4.5 2.7v2.78c-2.27-.13-4.29-1.21-5.66-2.86z"/></svg>'  # noqa
