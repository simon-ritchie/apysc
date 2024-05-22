from apysc._material_design.icon.material_settings_applications_outlined_icon import (
    MaterialSettingsApplicationsOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsApplicationsOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSettingsApplicationsOutlinedIcon = (
            MaterialSettingsApplicationsOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
