from apysc._material_design.icon.material_settings_remote_outlined_icon import (
    MaterialSettingsRemoteOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsRemoteOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSettingsRemoteOutlinedIcon = MaterialSettingsRemoteOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
