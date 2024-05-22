from apysc._material_design.icon.material_slow_motion_video_icon import (
    MaterialSlowMotionVideoIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSlowMotionVideoIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialSlowMotionVideoIcon = MaterialSlowMotionVideoIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
