from apysc._material_design.icon.material_tab_unselected_icon import (
    MaterialTabUnselectedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTabUnselectedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTabUnselectedIcon = MaterialTabUnselectedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
