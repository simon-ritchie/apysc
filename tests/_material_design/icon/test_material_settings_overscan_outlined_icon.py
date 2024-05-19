from apysc._material_design.icon.material_settings_overscan_outlined_icon import (
    MaterialsettingsOverscanOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsOverscanOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsOverscanOutlinedIcon = (
            MaterialsettingsOverscanOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
