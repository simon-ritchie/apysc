from apysc._material_design.icon.material_accessible_forward_icon import MaterialaccessibleForwardIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialaccessibleForwardIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialaccessibleForwardIcon = MaterialaccessibleForwardIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
