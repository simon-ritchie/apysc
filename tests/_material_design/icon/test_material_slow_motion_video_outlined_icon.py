from apysc._material_design.icon.material_slow_motion_video_outlined_icon import (
    MaterialslowMotionVideoOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialslowMotionVideoOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialslowMotionVideoOutlinedIcon = (
            MaterialslowMotionVideoOutlinedIcon()
        )
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
