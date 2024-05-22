from apysc._material_design.icon.material_settings_applications_icon import (
    MaterialSettingsApplicationsIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsApplicationsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSettingsApplicationsIcon = MaterialSettingsApplicationsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
