from apysc._material_design.icon.material_tab_unselected_icon import (
    MaterialtabUnselectedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtabUnselectedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtabUnselectedIcon = MaterialtabUnselectedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
