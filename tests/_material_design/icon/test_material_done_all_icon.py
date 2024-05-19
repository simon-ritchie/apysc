from apysc._material_design.icon.material_done_all_icon import MaterialdoneAllIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdoneAllIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdoneAllIcon = MaterialdoneAllIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
