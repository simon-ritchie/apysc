from apysc._material_design.icon.material_alarm_on_icon import MaterialAlarmOnIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAlarmOnIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAlarmOnIcon = MaterialAlarmOnIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
