from apysc._material_design.icon.material_close_fullscreen_outlined_icon import (
    MaterialCloseFullscreenOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCloseFullscreenOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCloseFullscreenOutlinedIcon = (
            MaterialCloseFullscreenOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
