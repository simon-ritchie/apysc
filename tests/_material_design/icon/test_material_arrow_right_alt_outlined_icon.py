from apysc._material_design.icon.material_arrow_right_alt_outlined_icon import (
    MaterialArrowRightAltOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialArrowRightAltOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialArrowRightAltOutlinedIcon = MaterialArrowRightAltOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
