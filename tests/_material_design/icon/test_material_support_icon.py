from apysc._material_design.icon.material_support_icon import MaterialsupportIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialsupportIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialsupportIcon = MaterialsupportIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
