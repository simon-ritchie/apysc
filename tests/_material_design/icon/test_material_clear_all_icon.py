from apysc._material_design.icon.material_clear_all_icon import MaterialClearAllIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialClearAllIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialClearAllIcon = MaterialClearAllIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
