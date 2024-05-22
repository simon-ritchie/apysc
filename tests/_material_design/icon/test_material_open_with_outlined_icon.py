from apysc._material_design.icon.material_open_with_outlined_icon import (
    MaterialOpenWithOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialOpenWithOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialOpenWithOutlinedIcon = MaterialOpenWithOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
