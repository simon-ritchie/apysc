from apysc._material_design.icon.material_support_icon import MaterialSupportIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSupportIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSupportIcon = MaterialSupportIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
