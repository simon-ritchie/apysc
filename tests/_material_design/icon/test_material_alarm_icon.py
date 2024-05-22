from apysc._material_design.icon.material_alarm_icon import MaterialAlarmIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAlarmIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAlarmIcon = MaterialAlarmIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
