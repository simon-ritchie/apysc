from apysc._material_design.icon.material_fit_screen_icon import MaterialfitScreenIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialfitScreenIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialfitScreenIcon = MaterialfitScreenIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
