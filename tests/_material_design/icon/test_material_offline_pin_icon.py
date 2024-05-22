from apysc._material_design.icon.material_offline_pin_icon import MaterialOfflinePinIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialOfflinePinIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialOfflinePinIcon = MaterialOfflinePinIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
