from apysc._material_design.icon.material_close_fullscreen_icon import (
    MaterialCloseFullscreenIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialCloseFullscreenIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialCloseFullscreenIcon = MaterialCloseFullscreenIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
