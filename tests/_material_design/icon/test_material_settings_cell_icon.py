from apysc._material_design.icon.material_settings_cell_icon import (
    MaterialSettingsCellIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSettingsCellIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSettingsCellIcon = MaterialSettingsCellIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
