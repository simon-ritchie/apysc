from apysc._material_design.icon.material_highlight_alt_icon import (
    MaterialHighlightAltIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHighlightAltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHighlightAltIcon = MaterialHighlightAltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
