from apysc._material_design.icon.material_touch_app_icon import MaterialTouchAppIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialTouchAppIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: MaterialTouchAppIcon = MaterialTouchAppIcon()
        assert icon._svg_icon_html == icon._get_fixed_svg_icon_html()
