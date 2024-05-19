from apysc._material_design.icon.material_explore_off_icon import MaterialexploreOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialexploreOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialexploreOffIcon = MaterialexploreOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
