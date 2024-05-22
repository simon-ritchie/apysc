from apysc._material_design.icon.material_explore_off_icon import MaterialExploreOffIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialExploreOffIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialExploreOffIcon = MaterialExploreOffIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
