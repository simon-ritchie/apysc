from apysc._material_design.icon.material_settings_remote_icon import (
    MaterialsettingsRemoteIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsRemoteIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsRemoteIcon = MaterialsettingsRemoteIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
