from apysc._material_design.icon.material_no_sim_outlined_icon import (
    MaterialNoSimOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialNoSimOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialNoSimOutlinedIcon = MaterialNoSimOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
