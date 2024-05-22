from apysc._material_design.icon.material_alarm_add_icon import MaterialAlarmAddIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAlarmAddIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAlarmAddIcon = MaterialAlarmAddIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
