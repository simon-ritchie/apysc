from apysc._material_design.icon.material_pets_icon import MaterialPetsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialPetsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialPetsIcon = MaterialPetsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
