from apysc._material_design.icon.material_explore_icon import MaterialexploreIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialexploreIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialexploreIcon = MaterialexploreIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
