from apysc._material_design.icon.material_eco_icon import MaterialEcoIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialEcoIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialEcoIcon = MaterialEcoIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
