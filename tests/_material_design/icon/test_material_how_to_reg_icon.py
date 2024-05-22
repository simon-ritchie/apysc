from apysc._material_design.icon.material_how_to_reg_icon import MaterialHowToRegIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHowToRegIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHowToRegIcon = MaterialHowToRegIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
