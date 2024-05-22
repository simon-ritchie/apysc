from apysc._material_design.icon.material_slow_motion_video_outlined_icon import (
    MaterialSlowMotionVideoOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSlowMotionVideoOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSlowMotionVideoOutlinedIcon = (
            MaterialSlowMotionVideoOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
