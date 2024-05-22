from apysc._material_design.icon.material_explicit_icon import MaterialExplicitIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialExplicitIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialExplicitIcon = MaterialExplicitIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
