from apysc._material_design.icon.material_live_help_outlined_icon import (
    MaterialLiveHelpOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialLiveHelpOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialLiveHelpOutlinedIcon = MaterialLiveHelpOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
