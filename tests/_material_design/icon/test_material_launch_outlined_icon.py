from apysc._material_design.icon.material_launch_outlined_icon import (
    MaterialLaunchOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLaunchOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLaunchOutlinedIcon = MaterialLaunchOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
