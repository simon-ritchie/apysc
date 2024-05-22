from apysc._material_design.icon.material_biotech_icon import MaterialBiotechIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialBiotechIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialBiotechIcon = MaterialBiotechIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
