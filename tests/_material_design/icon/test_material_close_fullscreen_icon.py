from apysc._material_design.icon.material_close_fullscreen_icon import (
    MaterialcloseFullscreenIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialcloseFullscreenIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialcloseFullscreenIcon = MaterialcloseFullscreenIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
