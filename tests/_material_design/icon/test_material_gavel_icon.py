from apysc._material_design.icon.material_gavel_icon import MaterialGavelIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialGavelIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialGavelIcon = MaterialGavelIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
