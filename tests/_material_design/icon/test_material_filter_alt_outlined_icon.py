from apysc._material_design.icon.material_filter_alt_outlined_icon import (
    MaterialFilterAltOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFilterAltOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFilterAltOutlinedIcon = MaterialFilterAltOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
