"""The class implementation for the `donut_large` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialDonutLargeIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the `donut_large` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><g><rect fill="none" height="24" width="24"/></g><g><g><g><path d="M11,5.08V2C6,2.5,2,6.81,2,12s4,9.5,9,10v-3.08c-3-0.48-6-3.4-6-6.92S8,5.56,11,5.08z M18.97,11H22c-0.47-5-4-8.53-9-9 v3.08C16,5.51,18.54,8,18.97,11z M13,18.92V22c5-0.47,8.53-4,9-9h-3.03C18.54,16,16,18.49,13,18.92z"/></g></g></g></svg>'  # noqa
