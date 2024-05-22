from apysc._material_design.icon.material_speed_icon import MaterialSpeedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSpeedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSpeedIcon = MaterialSpeedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
