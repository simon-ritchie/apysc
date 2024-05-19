"""The class implementation for the outlined `addchart` material icon.
"""

from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase


class MaterialaddchartOutlinedIcon(FixedHtmlSvgIconBase):
    """
    The class implementation for the outlined `addchart` material icon.
    """

    def _get_fixed_svg_icon_html(self) -> str:
        """
        Get a fixed SVG icon HTML string.

        Returns
        -------
        fixed_svg_icon_html : str
            Fixed SVG icon HTML string.
        """
        return '<svg xmlns="http://www.w3.org/2000/svg" enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24" width="24"><g><rect fill="none" height="24" width="24"/><path d="M22,5v2h-3v3h-2V7h-3V5h3V2h2v3H22z M19,19H5V5h6V3H5C3.9,3,3,3.9,3,5v14c0,1.1,0.9,2,2,2h14c1.1,0,2-0.9,2-2v-6h-2V19z M15,13v4h2v-4H15z M11,17h2V9h-2V17z M9,17v-6H7v6H9z"/></g></svg>'  # noqa
