from apysc._material_design.icon.material_polymer_icon import MaterialpolymerIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpolymerIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpolymerIcon = MaterialpolymerIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
