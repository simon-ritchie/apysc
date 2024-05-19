from apysc._material_design.icon.material_list_alt_outlined_icon import (
    MateriallistAltOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMateriallistAltOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MateriallistAltOutlinedIcon = MateriallistAltOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
