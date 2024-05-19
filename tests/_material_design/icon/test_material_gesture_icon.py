from apysc._material_design.icon.material_gesture_icon import MaterialgestureIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialgestureIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialgestureIcon = MaterialgestureIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
