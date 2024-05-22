from apysc._material_design.icon.material_gesture_icon import MaterialGestureIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialGestureIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialGestureIcon = MaterialGestureIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
