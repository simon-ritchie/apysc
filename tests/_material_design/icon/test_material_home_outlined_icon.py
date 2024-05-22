from apysc._material_design.icon.material_home_outlined_icon import (
    MaterialHomeOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHomeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHomeOutlinedIcon = MaterialHomeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
