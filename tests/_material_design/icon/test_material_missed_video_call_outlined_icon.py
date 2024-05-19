from apysc._material_design.icon.material_missed_video_call_outlined_icon import (
    MaterialmissedVideoCallOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialmissedVideoCallOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialmissedVideoCallOutlinedIcon = (
            MaterialmissedVideoCallOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
