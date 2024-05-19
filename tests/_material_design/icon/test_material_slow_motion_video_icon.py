from apysc._material_design.icon.material_slow_motion_video_icon import (
    MaterialslowMotionVideoIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialslowMotionVideoIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialslowMotionVideoIcon = MaterialslowMotionVideoIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
