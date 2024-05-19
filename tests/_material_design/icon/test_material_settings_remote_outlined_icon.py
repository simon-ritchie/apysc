from apysc._material_design.icon.material_settings_remote_outlined_icon import MaterialsettingsRemoteOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsRemoteOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsRemoteOutlinedIcon = MaterialsettingsRemoteOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
