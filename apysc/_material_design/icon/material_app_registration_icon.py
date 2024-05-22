"""The class implementation for the `app_registration` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialAppRegistrationIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the `app_registration` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><g><rect fill="none" height="24" width="24"/></g><g><g><rect height="4" width="4" x="10" y="4"/><rect height="4" width="4" x="4" y="16"/><rect height="4" width="4" x="4" y="10"/><rect height="4" width="4" x="4" y="4"/><polygon points="14,12.42 14,10 10,10 10,14 12.42,14"/><path d="M20.88,11.29l-1.17-1.17c-0.16-0.16-0.42-0.16-0.58,0L18.25,11L20,12.75l0.88-0.88C21.04,11.71,21.04,11.45,20.88,11.29z"/><polygon points="11,18.25 11,20 12.75,20 19.42,13.33 17.67,11.58"/><rect height="4" width="4" x="16" y="4"/></g></g></svg>'  # noqa
