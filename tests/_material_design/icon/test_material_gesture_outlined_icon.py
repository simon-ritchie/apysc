from apysc._material_design.icon.material_gesture_outlined_icon import (
    MaterialGestureOutlinedIcon,
)
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialGestureOutlinedIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialGestureOutlinedIcon = MaterialGestureOutlinedIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
