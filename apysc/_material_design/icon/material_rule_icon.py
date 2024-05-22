"""The class implementation for the `rule` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialRuleIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the `rule` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><g><rect fill="none" height="24" width="24"/><path d="M16.54,11L13,7.46l1.41-1.41l2.12,2.12l4.24-4.24l1.41,1.41L16.54,11z M11,7H2v2h9V7z M21,13.41L19.59,12L17,14.59 L14.41,12L13,13.41L15.59,16L13,18.59L14.41,20L17,17.41L19.59,20L21,18.59L18.41,16L21,13.41z M11,15H2v2h9V15z"/></g></svg>'  # noqa
