"""The class implementation for the `outgoing_mail` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialOutgoingMailIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the `outgoing_mail` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><g><rect fill="none" height="24" width="24"/></g><g><g><path d="M18.5,11c0.17,0,0.34,0.01,0.5,0.03V6.87C19,5.84,18.16,5,17.13,5H3.87C2.84,5,2,5.84,2,6.87v10.26 C2,18.16,2.84,19,3.87,19h9.73C13.22,18.25,13,17.4,13,16.5C13,13.46,15.46,11,18.5,11z M10.4,13L4,9.19V7h0.23l6.18,3.68L16.74,7 H17v2.16L10.4,13z"/><polygon points="19,13 17.59,14.41 19.17,16 15,16 15,18 19.17,18 17.59,19.59 19,21 23,17"/></g></g></svg>'  # noqa
