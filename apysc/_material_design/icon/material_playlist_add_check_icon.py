"""The class implementation for the `playlist_add_check` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialPlaylistAddCheckIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the `playlist_add_check` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><g><rect fill="none" height="24" width="24"/></g><g><g><g><path d="M14,10H2v2h12V10z M14,6H2v2h12V6z M2,16h8v-2H2V16z M21.5,11.5L23,13l-6.99,7l-4.51-4.5L13,14l3.01,3L21.5,11.5z"/></g></g></g></svg>'  # noqa
