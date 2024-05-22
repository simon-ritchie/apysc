from apysc._material_design.icon.material_open_in_new_outlined_icon import (
    MaterialOpenInNewOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialOpenInNewOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialOpenInNewOutlinedIcon = MaterialOpenInNewOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
