from apysc._material_design.icon.material_hourglass_full_outlined_icon import (
    MaterialHourglassFullOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialHourglassFullOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialHourglassFullOutlinedIcon = MaterialHourglassFullOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
