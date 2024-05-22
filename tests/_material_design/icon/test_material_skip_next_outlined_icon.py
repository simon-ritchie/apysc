from apysc._material_design.icon.material_skip_next_outlined_icon import (
    MaterialSkipNextOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSkipNextOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSkipNextOutlinedIcon = MaterialSkipNextOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
