from apysc._material_design.icon.material_hourglass_disabled_outlined_icon import (
    MaterialHourglassDisabledOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHourglassDisabledOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHourglassDisabledOutlinedIcon = (
            MaterialHourglassDisabledOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
