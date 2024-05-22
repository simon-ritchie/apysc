from apysc._material_design.icon.material_speed_outlined_icon import (
    MaterialSpeedOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSpeedOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSpeedOutlinedIcon = MaterialSpeedOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
