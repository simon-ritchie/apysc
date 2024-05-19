from apysc._material_design.icon.material_explicit_icon import MaterialexplicitIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialexplicitIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialexplicitIcon = MaterialexplicitIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
