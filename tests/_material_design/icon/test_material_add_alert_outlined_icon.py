from apysc._material_design.icon.material_add_alert_outlined_icon import MaterialaddAlertOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaddAlertOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaddAlertOutlinedIcon = MaterialaddAlertOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
