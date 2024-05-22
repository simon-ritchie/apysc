from apysc._material_design.icon.material_timeline_outlined_icon import (
    MaterialTimelineOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTimelineOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTimelineOutlinedIcon = MaterialTimelineOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
