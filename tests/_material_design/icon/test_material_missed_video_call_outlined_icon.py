from apysc._material_design.icon.material_missed_video_call_outlined_icon import (
    MaterialMissedVideoCallOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialMissedVideoCallOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialMissedVideoCallOutlinedIcon = (
            MaterialMissedVideoCallOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
