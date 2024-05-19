from apysc._material_design.icon.material_sd_icon import MaterialsdIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsdIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsdIcon = MaterialsdIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
