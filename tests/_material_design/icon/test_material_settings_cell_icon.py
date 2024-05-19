from apysc._material_design.icon.material_settings_cell_icon import (
    MaterialsettingsCellIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsettingsCellIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsettingsCellIcon = MaterialsettingsCellIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
