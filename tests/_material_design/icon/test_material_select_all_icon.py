from apysc._material_design.icon.material_select_all_icon import MaterialselectAllIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialselectAllIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialselectAllIcon = MaterialselectAllIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
