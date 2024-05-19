from apysc._material_design.icon.material_donut_small_icon import MaterialdonutSmallIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdonutSmallIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdonutSmallIcon = MaterialdonutSmallIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
