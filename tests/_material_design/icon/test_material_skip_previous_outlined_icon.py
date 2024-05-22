from apysc._material_design.icon.material_skip_previous_outlined_icon import (
    MaterialSkipPreviousOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSkipPreviousOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSkipPreviousOutlinedIcon = MaterialSkipPreviousOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
