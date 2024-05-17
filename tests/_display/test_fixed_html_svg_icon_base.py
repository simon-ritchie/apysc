from apysc._testing.testing_helper import apply_test_settings
from apysc._display.fixed_html_svg_icon_base import FixedHtmlSvgIconBase
import apysc as ap


class _TestIcon(FixedHtmlSvgIconBase):

    def get_fixed_svg_icon_html(self) -> str:
        """
        Get a fixed SVG icon HTML string.

        Returns
        -------
        fixed_svg_icon_html : str
            Fixed SVG icon HTML string.
        """
        return '<svg></svg>'


class TestFixedHtmlSvgIconBase:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: _TestIcon = _TestIcon(
            x=50,
            y=100,
            size=48,
            fill_color=ap.Colors.GRAY_777777,
            fill_alpha=0.5,
            variable_name_suffix='test_suffix',
        )
        assert icon._svg_icon_html == '<svg></svg>'
        assert icon.x == ap.Number(50)
        assert icon.y == ap.Number(100)
        assert icon.width == ap.Int(48)
        assert icon.height == ap.Int(48)
        assert icon.fill_color == ap.Colors.GRAY_777777
        assert icon.fill_alpha == ap.Number(0.5)
        assert icon._variable_name_suffix == "test_suffix"
