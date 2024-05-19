from apysc._material_design.icon.material_clear_all_icon import MaterialclearAllIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialclearAllIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialclearAllIcon = MaterialclearAllIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
