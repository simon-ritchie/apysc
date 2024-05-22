from apysc._material_design.icon.material_add_alert_icon import MaterialAddAlertIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialAddAlertIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialAddAlertIcon = MaterialAddAlertIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
