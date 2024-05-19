from apysc._material_design.icon.material_alarm_on_icon import MaterialalarmOnIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialalarmOnIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialalarmOnIcon = MaterialalarmOnIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
