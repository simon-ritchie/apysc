from apysc._material_design.icon.material_pets_icon import MaterialpetsIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialpetsIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialpetsIcon = MaterialpetsIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
