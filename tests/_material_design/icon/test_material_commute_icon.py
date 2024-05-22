from apysc._material_design.icon.material_commute_icon import MaterialCommuteIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCommuteIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCommuteIcon = MaterialCommuteIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
