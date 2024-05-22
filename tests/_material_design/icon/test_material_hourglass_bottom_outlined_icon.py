from apysc._material_design.icon.material_hourglass_bottom_outlined_icon import (
    MaterialHourglassBottomOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHourglassBottomOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHourglassBottomOutlinedIcon = (
            MaterialHourglassBottomOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
