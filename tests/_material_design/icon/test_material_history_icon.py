from apysc._material_design.icon.material_history_icon import MaterialhistoryIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialhistoryIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialhistoryIcon = MaterialhistoryIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
