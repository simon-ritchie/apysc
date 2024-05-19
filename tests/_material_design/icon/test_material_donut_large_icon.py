from apysc._material_design.icon.material_donut_large_icon import MaterialdonutLargeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialdonutLargeIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialdonutLargeIcon = MaterialdonutLargeIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
