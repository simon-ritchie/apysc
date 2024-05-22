from apysc._material_design.icon.material_fit_screen_icon import MaterialFitScreenIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialFitScreenIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialFitScreenIcon = MaterialFitScreenIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
