from apysc._material_design.icon.material_perm_data_setting_icon import (
    MaterialPermDataSettingIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPermDataSettingIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPermDataSettingIcon = MaterialPermDataSettingIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
