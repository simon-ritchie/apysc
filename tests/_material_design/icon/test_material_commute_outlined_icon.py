from apysc._material_design.icon.material_commute_outlined_icon import (
    MaterialCommuteOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCommuteOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCommuteOutlinedIcon = MaterialCommuteOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
