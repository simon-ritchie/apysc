from apysc._material_design.icon.material_visibility_icon import MaterialVisibilityIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVisibilityIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVisibilityIcon = MaterialVisibilityIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
