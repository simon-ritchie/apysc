from apysc._material_design.icon.material_perm_data_setting_outlined_icon import MaterialpermDataSettingOutlinedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpermDataSettingOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpermDataSettingOutlinedIcon = MaterialpermDataSettingOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
