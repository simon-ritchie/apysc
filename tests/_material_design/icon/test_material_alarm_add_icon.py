from apysc._material_design.icon.material_alarm_add_icon import MaterialalarmAddIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialalarmAddIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialalarmAddIcon = MaterialalarmAddIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
