"""The class implementation for the outlined `dynamic_form` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialDynamicFormOutlinedIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the outlined `dynamic_form` material icon.
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
        return '<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><g><rect fill="none" height="24" width="24"/><path d="M13,11H4c-1.1,0-2-0.9-2-2V6c0-1.1,0.9-2,2-2h9V11z M4,9h7V6H4V9z M15,20H4c-1.1,0-2-0.9-2-2v-3c0-1.1,0.9-2,2-2h11V20z M4,18h9v-3H4V18z M22,9h-2l2-5h-7v7h2v9L22,9z M4.75,17.25h1.5v-1.5h-1.5V17.25z M4.75,8.25h1.5v-1.5h-1.5V8.25z"/></g></svg>'  # noqa
