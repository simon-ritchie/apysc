from apysc._material_design.icon.material_more_time_outlined_icon import (
    MaterialMoreTimeOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMoreTimeOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMoreTimeOutlinedIcon = MaterialMoreTimeOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
