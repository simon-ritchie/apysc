from apysc._material_design.icon.material_highlight_alt_outlined_icon import (
    MaterialHighlightAltOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHighlightAltOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHighlightAltOutlinedIcon = MaterialHighlightAltOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
