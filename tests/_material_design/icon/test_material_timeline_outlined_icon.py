from apysc._material_design.icon.material_timeline_outlined_icon import (
    MaterialtimelineOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialtimelineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialtimelineOutlinedIcon = MaterialtimelineOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
