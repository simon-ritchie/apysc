from apysc._material_design.icon.material_alarm_add_outlined_icon import MaterialalarmAddOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialalarmAddOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialalarmAddOutlinedIcon = MaterialalarmAddOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
