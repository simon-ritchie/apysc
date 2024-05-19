from apysc._material_design.icon.material_nat_icon import MaterialnatIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialnatIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialnatIcon = MaterialnatIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
