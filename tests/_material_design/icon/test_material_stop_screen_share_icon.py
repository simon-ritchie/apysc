from apysc._material_design.icon.material_stop_screen_share_icon import (
    MaterialStopScreenShareIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialStopScreenShareIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialStopScreenShareIcon = MaterialStopScreenShareIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
