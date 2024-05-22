from apysc._material_design.icon.material_verified_icon import MaterialVerifiedIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialVerifiedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialVerifiedIcon = MaterialVerifiedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
