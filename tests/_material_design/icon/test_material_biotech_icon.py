from apysc._material_design.icon.material_biotech_icon import MaterialbiotechIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialbiotechIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialbiotechIcon = MaterialbiotechIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
