from apysc._material_design.icon.material_explore_outlined_icon import (
    MaterialExploreOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialExploreOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialExploreOutlinedIcon = MaterialExploreOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
