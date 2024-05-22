from apysc._material_design.icon.material_alarm_off_icon import MaterialAlarmOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAlarmOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAlarmOffIcon = MaterialAlarmOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
