from apysc._material_design.icon.material_explore_off_outlined_icon import (
    MaterialexploreOffOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialexploreOffOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialexploreOffOutlinedIcon = MaterialexploreOffOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
