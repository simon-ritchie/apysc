from apysc._material_design.icon.material_filter_alt_outlined_icon import (
    MaterialfilterAltOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfilterAltOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfilterAltOutlinedIcon = MaterialfilterAltOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
