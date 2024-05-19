from apysc._material_design.icon.material_no_sim_outlined_icon import MaterialnoSimOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnoSimOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnoSimOutlinedIcon = MaterialnoSimOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
