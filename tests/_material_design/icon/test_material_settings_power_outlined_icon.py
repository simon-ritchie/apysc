from apysc._material_design.icon.material_settings_power_outlined_icon import (
    MaterialsettingsPowerOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsPowerOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsPowerOutlinedIcon = MaterialsettingsPowerOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
