from apysc._material_design.icon.material_gavel_icon import MaterialgavelIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialgavelIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialgavelIcon = MaterialgavelIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
