from apysc._material_design.icon.material_arrow_right_alt_icon import (
    MaterialArrowRightAltIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialArrowRightAltIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialArrowRightAltIcon = MaterialArrowRightAltIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
