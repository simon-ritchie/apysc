from apysc._material_design.icon.material_open_in_full_outlined_icon import (
    MaterialOpenInFullOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialOpenInFullOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialOpenInFullOutlinedIcon = MaterialOpenInFullOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
