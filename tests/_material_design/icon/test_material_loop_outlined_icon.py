from apysc._material_design.icon.material_loop_outlined_icon import (
    MaterialloopOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialloopOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialloopOutlinedIcon = MaterialloopOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
