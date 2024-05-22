from apysc._material_design.icon.material_list_icon import MaterialListIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialListIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialListIcon = MaterialListIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
