from apysc._material_design.icon.material_close_fullscreen_outlined_icon import (
    MaterialcloseFullscreenOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcloseFullscreenOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcloseFullscreenOutlinedIcon = (
            MaterialcloseFullscreenOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
