from apysc._material_design.icon.material_arrow_circle_up_outlined_icon import (
    MaterialArrowCircleUpOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialArrowCircleUpOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialArrowCircleUpOutlinedIcon = MaterialArrowCircleUpOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
