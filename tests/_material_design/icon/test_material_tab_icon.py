from apysc._material_design.icon.material_tab_icon import MaterialTabIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTabIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTabIcon = MaterialTabIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
