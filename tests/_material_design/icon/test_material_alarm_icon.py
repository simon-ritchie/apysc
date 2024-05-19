from apysc._material_design.icon.material_alarm_icon import MaterialalarmIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialalarmIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialalarmIcon = MaterialalarmIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
