from apysc._material_design.icon.material_no_sim_icon import MaterialnoSimIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnoSimIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnoSimIcon = MaterialnoSimIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
