from apysc._material_design.icon.material_settings_power_icon import (
    MaterialSettingsPowerIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsPowerIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSettingsPowerIcon = MaterialSettingsPowerIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
