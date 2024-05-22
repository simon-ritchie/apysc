from apysc._material_design.icon.material_missed_video_call_icon import (
    MaterialMissedVideoCallIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMissedVideoCallIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMissedVideoCallIcon = MaterialMissedVideoCallIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
